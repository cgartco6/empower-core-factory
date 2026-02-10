from validators.privacy_gdpr import validate_gdpr
from validators.privacy_popia import validate_popia

def compliance_rules(country_code):
    if country_code in ["ZA"]:
        return ["POPIA"]
    if country_code in ["EU", "DE", "FR", "NL", "ES", "IT"]:
        return ["GDPR"]
    return ["GDPR"]  # safe default
