def verify_response(task, response):

    task = task.lower()

    verification_result = {
        "verified": False,
        "reason": ""
    }

    if "sync issue" in task:

        if response["root_cause"] == "Inventory mismatch":

            verification_result["verified"] = True
            verification_result["reason"] = (
                "Root cause matched known sync issue pattern"
            )

    elif "los alarm" in task:

        if response["root_cause"] == "Loss of Signal":

            verification_result["verified"] = True
            verification_result["reason"] = (
                "Alarm classification verified"
            )

    return verification_result
