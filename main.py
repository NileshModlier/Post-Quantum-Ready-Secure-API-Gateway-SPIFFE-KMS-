
from fastapi import FastAPI, Request
from gateway.crypto.strategy import negotiate_crypto
from gateway.security.identity import authenticate_client
from gateway.observability.audit import audit_event

app = FastAPI(title="Post‑Quantum‑Ready Secure API Gateway")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.api_route("/proxy/{path:path}", methods=["GET", "POST"])
async def proxy(request: Request, path: str):
    client_identity = authenticate_client(request)
    crypto_context = negotiate_crypto(request)

    audit_event(
        event="REQUEST_ACCEPTED",
        path=path,
        client_identity=client_identity,
        crypto=crypto_context
    )

    # Placeholder backend forwarding
    return {
        "path": path,
        "crypto": crypto_context,
        "client": client_identity,
        "result": "forwarded"
    }
