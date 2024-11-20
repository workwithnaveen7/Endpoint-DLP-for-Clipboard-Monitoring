import re

def is_sensitive_data(data):

    return (detect_aadhaar(data) or
            detect_pan(data) or
            detect_phone_number(data) or
            detect_email(data) or
            detect_bank_account(data) or
            detect_driving_license(data))

def detect_aadhaar(data):
    pattern = r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"
    return bool(re.search(pattern, data))

def detect_pan(data):
    pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
    return bool(re.search(pattern, data))

def detect_phone_number(data):
    pattern = r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b"
    return bool(re.search(pattern, data))

def detect_email(data):

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return bool(re.search(pattern, data))

def detect_bank_account(data):
    pattern = r"\b\d{16}\b"
    return bool(re.search(pattern, data))

def detect_driving_license(data):

    pattern = r"\b[A-Z]{2}\d{2}[A-Z]{2}\d{4}\b"
    return bool(re.search(pattern, data))
