import hashlib

def generate_license(customer_id, domain):
    raw = f"{customer_id}:{domain}"
    return hashlib.sha256(raw.encode()).hexdigest()

def validate_license(license_key, customer_id, domain):
    return license_key == generate_license(customer_id, domain)
