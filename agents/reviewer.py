class ReviewerAgent:
    def review(self, output, task):
        issues = []
        if len(output["content"]) < 100:
            issues.append("Content too short")

        return {
            "approved": len(issues) == 0,
            "issues": issues
        }
