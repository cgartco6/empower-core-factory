from validators.privacy_gdpr import validate_gdpr
from validators.privacy_popia import validate_popia

def validate_privacy(doc, country):
    errors = []

    if country == "ZA":
        errors += validate_popia(doc)
    else:
        errors += validate_gdpr(doc)

    return errors
