class GeneratorAgent:
    def create(self, task):
        return {
            "type": task["type"],
            "content": f"Generated {task['type']} for {task['topic']}",
            "metadata": task
        }
