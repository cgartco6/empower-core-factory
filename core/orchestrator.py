from agents.generator import GeneratorAgent
from agents.reviewer import ReviewerAgent
from agents.validator import ValidatorAgent
from agents.fixer import FixerAgent

class Orchestrator:
    def __init__(self):
        self.generator = GeneratorAgent()
        self.reviewer = ReviewerAgent()
        self.validator = ValidatorAgent()
        self.fixer = FixerAgent()

    def run(self, task):
        output = self.generator.create(task)

        for _ in range(3):  # bounded correction loop
            review = self.reviewer.review(output, task)
            validation = self.validator.validate(output, task)

            if review["approved"] and validation["valid"]:
                return output

            output = self.fixer.fix(
                output,
                issues=review["issues"] + validation["errors"]
            )

        raise Exception("Output failed validation after fixes")
if not check_regression(task, output):
    raise Exception("Regression detected – output changed unexpectedly")
