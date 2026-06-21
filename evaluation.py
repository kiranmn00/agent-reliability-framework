def calculate_confidence(
        verified,
        response):

    score = 50

    if verified:
        score += 40

    if response["severity"] != "Unknown":
        score += 10

    return score
