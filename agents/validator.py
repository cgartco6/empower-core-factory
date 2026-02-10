from validators.legal import validate_legal
from validators.course import validate_course

class ValidatorAgent:
    def validate(self, output, task):
        errors = []

        if task["type"] == "legal":
            errors += validate_legal(output)

        if task["type"] == "course":
            errors += validate_course(output)

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }
