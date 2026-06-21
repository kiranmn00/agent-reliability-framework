import json

from agent import Agent
from verifier import verify_response
from evaluation import calculate_confidence

agent = Agent()

with open("test_cases.json") as file:

    test_cases = json.load(file)

for case in test_cases:

    task = case["task"]

    response = agent.generate_response(task)

    verification = verify_response(
        task,
        response
    )

    confidence = calculate_confidence(
        verification["verified"],
        response
    )

    print("\n")
    print("=" * 50)
    print(f"TASK: {task}")
    print("=" * 50)

    print("Agent Response:")
    print(response)

    print("\nVerification:")
    print(verification)

    print(
        f"\nConfidence Score: {confidence}%"
    )
