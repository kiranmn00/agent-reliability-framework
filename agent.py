class Agent:

    def generate_response(self, task):

        task = task.lower()

        if "sync issue" in task:
            return {
                "root_cause": "Inventory mismatch",
                "severity": "Medium"
            }

        if "los alarm" in task:
            return {
                "root_cause": "Loss of Signal",
                "severity": "High"
            }

        return {
            "root_cause": "Unknown",
            "severity": "Unknown"
        }
