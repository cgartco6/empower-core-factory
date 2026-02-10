import json
import hashlib

REGRESSION_DB = "regressions.json"

def hash_output(output):
    return hashlib.sha256(
        json.dumps(output, sort_keys=True).encode()
    ).hexdigest()

def store_baseline(task, output):
    with open(REGRESSION_DB, "a+") as f:
        f.write(json.dumps({
            "task": task,
            "hash": hash_output(output)
        }) + "\n")

def check_regression(task, output):
    current = hash_output(output)
    with open(REGRESSION_DB, "r") as f:
        for line in f:
            if task == json.loads(line)["task"]:
                if current != json.loads(line)["hash"]:
                    return False
    return True
