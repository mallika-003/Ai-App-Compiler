metrics = {
    "total_requests": 0,
    "validation_failures": 0,
    "repairs": 0
}

def track_request():
    metrics["total_requests"] += 1

def track_failure():
    metrics["validation_failures"] += 1

def track_repair():
    metrics["repairs"] += 1