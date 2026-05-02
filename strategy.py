
def negotiate_crypto(request):
    pq_capable = request.headers.get("X-Client-PQ") == "true"

    if pq_capable:
        return {
            "tls_mode": "HYBRID",
            "key_exchange": ["X25519", "Kyber"],
            "signature": ["ECDSA", "Dilithium"]
        }

    return {
        "tls_mode": "TLS13",
        "key_exchange": ["X25519"],
        "signature": ["ECDSA"]
    }
