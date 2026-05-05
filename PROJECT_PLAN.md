# PROJECT_PLAN.md

# Proyecto: Contractual Assistance + Smart Payments
# Fecha: 2026-05-05

## 1. VISIÓN GENERAL
Construir un sistema que actúe como intermediario inteligente entre personas, empresas, contratos, pagos y decisiones operativas.

El sistema debe democratizar la relación cliente-empresa, reduciendo la asimetría de información y ayudando a las personas a entender lo que contrataron, cumplir sus pagos y tomar mejores decisiones.

Este proyecto **NO** es una plataforma genérica de agentes, ni una fábrica de agentes, ni un sistema multi-agente de propósito general. Es un **producto vertical específico** enfocado exclusivamente en resolver un problema concreto de contratos, pagos, comprensión y timing.

## 2. EL PROBLEMA REAL
Las personas no siempre entienden sus contratos, no recuerdan fechas de pago, pierden información relevante y terminan pagando intereses, multas o cargos evitables.

Las empresas, por su parte, enfrentan morosidad, reclamos, costos de cobranza y mala experiencia de cliente, muchas veces por problemas de comunicación, timing y comprensión.

## 3. INSIGHT CLAVE
El problema no es solo financiero. Es un problema de:
- Comprensión.
- Timing.
- Acceso a información.
- Orden documental.
- Comunicación clara entre empresa y cliente.

## 4. LA SOLUCIÓN
Un sistema vertical compuesto por los siguientes componentes clave:

### WhatsApp como Canal Principal
WhatsApp **no es opcional ni una fase posterior**: es el canal conversacional principal desde el primer módulo. El usuario puede preguntar, recibir alertas, enviar fotos de boletas, pedir resúmenes, solicitar ayuda y recibir instrucciones.

### App como Capa de Control y Visualización
La app **no reemplaza a WhatsApp** ni compite con él. Funciona como un **contenedor operativo**:
- Muestra contratos, pagos, historial, boletas y alertas.
- Ofrece botones de acción y herramientas de organización.
- Desde la app se abre WhatsApp con instrucciones claras o flujos guiados.
La app organiza, controla y visualiza; WhatsApp conversa.

### Base de Conocimiento por Empresa Contratante
Debe existir una base de conocimiento específica por cada empresa contratante que incluya:
- Políticas.
- Contratos tipo.
- Reportes.
- Reglas internas y condiciones comerciales.
- Procedimientos.

### Captura Automática de Información
El sistema debe ser capaz de capturar información automáticamente a través de múltiples vías: correo, fotos de boletas, documentos subidos, cargas manuales y WhatsApp.

### Control Completo del Ciclo de Pagos
El sistema **no solo recuerda pagos**, sino que debe controlar el ciclo completo del pago, desde la notificación hasta la resolución.

### Motor Central
El núcleo está compuesto por IA + reglas + base de conocimiento + trazabilidad.

## 5. ARQUITECTURA DEL PRODUCTO
```text
Usuario
→ App / WhatsApp
→ API
→ Motor de ejecución
→ Base de conocimiento de empresa
→ Analizador de contratos
→ Motor de pagos
→ Motor de alertas
→ Generador de respuesta
→ WhatsApp / App
```

## 6. ALCANCE DEL PROYECTO

**Este proyecto está estrictamente limitado a:**
- Contratos de servicios (ej: luz, telecomunicaciones, suscripciones).
- Gestión del ciclo completo de los pagos asociados.
- Interpretación simple de cláusulas y contratos.
- Asistencia directa al usuario en su toma de decisiones.

**Explícitamente NO incluye (Fuera de alcance):**
- Sistema multi-agente o de orquestación compleja.
- Marketplace de agentes o ecosistema abierto de bots.
- Framework, arquitectura o herramientas genéricas para la creación de agentes ajenos a este caso de uso.
