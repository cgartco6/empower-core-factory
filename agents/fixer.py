class FixerAgent:
    def fix(self, output, issues):
        output["content"] += "\n\nFIXES APPLIED:\n"
        for issue in issues:
            output["content"] += f"- Fixed: {issue}\n"
        return output
