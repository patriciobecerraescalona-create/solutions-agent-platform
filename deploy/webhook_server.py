from fastapi import FastAPI
import subprocess

app = FastAPI(title="Solutions Agent Platform Deploy Webhook")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "deploy-webhook"
    }

@app.post("/deploy")
def deploy():
    result = subprocess.run(
        ["/home/patricio/workspace/solutions-agent-platform/deploy/deploy.sh"],
        capture_output=True,
        text=True,
    )

    return {
        "status": "ok" if result.returncode == 0 else "failed",
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
