# SYSTEM_STATE.md

## 1. OBJETIVO DEL PROYECTO
Proporcionar una plataforma de agentes (Solutions Agent Platform) modular, escalable y robusta para la ejecución de flujos de IA, manteniendo una separación clara entre infraestructura, servicios y la lógica de los agentes.

## 2. ARQUITECTURA ACTUAL (flujo Antigravity → GitHub → VM → Docker)
El flujo de desarrollo y despliegue sigue este camino:
1. **Desarrollo Local:** Se escribe código localmente en Windows usando Antigravity.
2. **Control de Versiones:** Los cambios se integran y suben a GitHub (rama `main`).
3. **Despliegue Automático:** Un Webhook en la VM detecta el evento de push.
4. **Ejecución en VM:** El webhook ejecuta un script local que descarga los cambios y redespliega los servicios usando Docker.

## 3. REPOSITORIO (URL y rama)
- **URL:** `https://github.com/patriciobecerraescalona-create/solutions-agent-platform.git`
- **Rama:** `main`

## 4. ENTORNO LOCAL (ruta Windows y herramienta Antigravity)
- **Ruta Windows:** `c:\dev\solutions-agent-platform`
- **Herramienta principal:** Antigravity

## 5. ENTORNO VM (DigitalOcean, IP, usuario, ruta)
- **Proveedor:** DigitalOcean
- **IP:** 159.223.113.80
- **Usuario:** patricio
- **Ruta:** `/home/patricio/workspace/solutions-agent-platform`

## 6. SERVICIOS ACTIVOS (API y webhook)
- **API Principal (`sap_api`):** Aplicación FastAPI estructurada de forma modular.
- **Webhook de Despliegue:** Servicio que escucha peticiones HTTP de GitHub y automatiza el redespliegue.

## 7. DOCKER (docker-compose, servicio sap_api)
- Orquestación gestionada a través de `infra/docker/docker-compose.yml`.
- El servicio principal `sap_api` se construye a partir de `services/api/Dockerfile`, el cual copia el código fuente desde `app` y ejecuta el servidor expuesto en el puerto 8000.

## 8. BACKEND ACTUAL (estructura modular en services/api/app)
El backend está estructurado modularmente bajo la carpeta `services/api/app/`:
- `main.py`: Punto de entrada de FastAPI que incluye e inicializa los routers.
- `routes/`: Contiene los endpoints separados (`health.py`, `execute.py`).
- `schemas/`: Contiene los modelos de Pydantic (`execute.py` con `ExecuteResponse`).
- `services/`: Contiene la lógica de negocio subyacente (`executor.py`).

## 9. ENDPOINTS VALIDADOS (/health y /api/v1/execute con ejemplos JSON)

**GET /health**
Respuesta:
```json
{
  "status": "ok",
  "service": "solutions-agent-platform-api"
}
```

**POST /api/v1/execute**
Payload (Ejemplo):
```json
{
  "test": 123
}
```
Respuesta:
```json
{
  "response": "Core execution received successfully.",
  "actions": [],
  "trace": {
    "received_payload": {
      "test": 123
    }
  }
}
```

## 10. DEPLOY AUTOMÁTICO (flujo completo y script deploy.sh)
El ciclo se completa al hacer `git push`. GitHub dispara un webhook que es recibido por la VM, la cual ejecuta localmente un script `deploy.sh`. Este script automatiza:
- Sincronización del repositorio mediante `git pull origin main`.
- Reconstrucción de la imagen y reinicio de contenedores usando `docker-compose up -d --build`.

## 11. WEBHOOK (FastAPI + systemd + estado sin autenticación)
- Servicio webhook construido en FastAPI.
- **Puerto:** 9000
- **Servicio systemd:** `deploy-webhook`
- **Endpoint:** `http://159.223.113.80:9000/deploy`
- Se mantiene corriendo en la VM en segundo plano mediante `systemd`.
- **Estado Actual:** Funcionando sin autenticación (los endpoints del webhook están abiertos a recibir cualquier POST para gatillar el script).

## 12. MECÁNICA DE TRABAJO (flujo correcto con commit/push manual)
1. Escribir y validar código localmente usando Antigravity.
2. Hacer `git add`, `git commit` y `git push origin main` de forma manual.
3. Esperar que el webhook reciba la notificación de GitHub y actualice la VM de manera automática.

## 13. REGLAS IMPORTANTES (NO trabajar directo en VM, etc.)
- **NUNCA modificar archivos directamente en la VM.** Todo cambio debe transitar a través del repositorio de GitHub.
- Evitar saltarse el flujo del webhook; si la VM falla, se depura desde local y se hace push.
- Mantener la separación de responsabilidades dentro del framework FastAPI (routers aislados de servicios).

## 14. COMANDOS CLAVE (git, curl)
**Comandos Git:**
```bash
git status
git add .
git commit -m "Descripción del cambio"
git push origin main
```

**Comandos Curl (Validación Local):**
```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/api/v1/execute -H "Content-Type: application/json" -d "{\"test\": 123}"
```

**Comandos Curl (Validación Pública VM):**
```bash
curl http://159.223.113.80:8000/health
```

## 15. PROBLEMAS CONOCIDOS
- Docker Desktop no se encuentra activo/disponible para pruebas locales en el entorno actual de Windows (requiere probar localmente mediante Virtual Environment en Python).
- El webhook de despliegue actualmente carece de autenticación/validación de firma (secretos de GitHub).

## 16. PRÓXIMOS PASOS
- Añadir validación de webhook (Signature o Secret token).
- Añadir componentes de Bases de Datos cuando el dominio lo requiera.
- Integrar la invocación de LLMs (Large Language Models) en el servicio ejecutor.

## 17. ÚLTIMO CHECKPOINT
- Refactorización completada: Migración de `services/api/main.py` monolítico a estructura modular de FastAPI bajo la carpeta `/app`.
- Endpoints de test validados de forma exitosa respondiendo `200 OK`.

## 18. PRINCIPIO BASE DEL PROYECTO
**Single Source of Truth (SSOT):** GitHub es la fuente única de la verdad. La VM y los despliegues son solamente una consecuencia automatizada del código que está persistido en la rama `main`.
