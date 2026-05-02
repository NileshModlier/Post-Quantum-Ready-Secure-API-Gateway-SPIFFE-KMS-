
import json
from datetime import datetime


def audit_event(event: str, **details):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "details": details
    }
    print(json.dumps(record))
