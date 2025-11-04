import re

def detect_sensitive_info(text):
    patterns = {
        'emails': re.findall(r'[\w\.-]+@[\w\.-]+', text),
        'passwords': re.findall(r'password\s*[:=]\s*\S+', text, re.IGNORECASE),
        'api_keys': re.findall(r'(?:api[_-]?key)\s*[:=]\s*\S+', text, re.IGNORECASE),
        'tokens': re.findall(r'(?:token)\s*[:=]\s*\S+', text, re.IGNORECASE),
    }
    return patterns
