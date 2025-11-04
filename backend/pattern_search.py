import re

def detect_sensitive_info(text):
    results = {
        "emails": len(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)),
        "passwords": len(re.findall(r"password\s*[:=]\s*\S+", text, re.IGNORECASE)),
        "api_keys": len(re.findall(r"api[_-]?key\s*[:=]\s*\S+", text, re.IGNORECASE)),
        "tokens": len(re.findall(r"token\s*[:=]\s*\S+", text, re.IGNORECASE)),
    }
    return results
