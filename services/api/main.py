from fastapi import FastAPI

app = FastAPI(title="Solutions Agent Platform API")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "solutions-agent-platform-api"
    }

@app.post("/api/v1/execute")
def execute(payload: dict):
    return {
        "response": "Core execution received successfully.",
        "actions": [],
        "trace": {
            "received_payload": payload
        }
    }
