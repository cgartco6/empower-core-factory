from core.orchestrator import Orchestrator

factory = Orchestrator()

task = {
    "type": "course",
    "topic": "Solar Installation Bootcamp",
    "country": "South Africa"
}

result = factory.run(task)
print(result)
