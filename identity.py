
from fastapi import Request


def authenticate_client(request: Request):
    cert = request.headers.get("X-Client-Cert")
    if cert:
        return {
            "auth_type": "mTLS",
            "client": "cert-subject-example",
            "trust_level": "HIGH"
        }
    return {"auth_type": "TLS", "client": "anonymous"}
