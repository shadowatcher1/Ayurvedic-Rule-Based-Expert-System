# Ayurvedic Classification as a Rule-Based Expert System
# Educational IKS-CS Demonstration
# This is not a medical diagnostic system.


def classify_dosha(body_build, appetite, activity,
                   sleep, temperature, skin):
    """
    Classify the user's Dosha based on six characteristics.
    """

    # Initialize scores
    scores = {
        "Vata": 0,
        "Pitta": 0,
        "Kapha": 0
    }

    # -------------------------
    # VATA RULES
    # -------------------------
    if body_build == "lean":
        scores["Vata"] += 1
    if appetite == "irregular":
        scores["Vata"] += 1
    if activity == "high":
        scores["Vata"] += 1
    if sleep == "light":
        scores["Vata"] += 1
    if temperature == "cold":
        scores["Vata"] += 1
    if skin == "dry":
        scores["Vata"] += 1

    # -------------------------
    # PITTA RULES
    # -------------------------
    if body_build == "medium":
        scores["Pitta"] += 1
    if appetite == "strong":
        scores["Pitta"] += 1
    if activity == "moderate":
        scores["Pitta"] += 1
    if sleep == "moderate":
        scores["Pitta"] += 1
    if temperature == "cool":
        scores["Pitta"] += 1
    if skin == "sensitive":
        scores["Pitta"] += 1

    # -------------------------
    # KAPHA RULES
    # -------------------------
    if body_build == "large":
        scores["Kapha"] += 1
    if appetite == "steady":
        scores["Kapha"] += 1
    if activity == "low":
        scores["Kapha"] += 1
    if sleep == "deep":
        scores["Kapha"] += 1
    if temperature == "neutral":
        scores["Kapha"] += 1
    if skin == "oily":
        scores["Kapha"] += 1

    # Find maximum score
    max_score = max(scores.values())

    # Find categories having maximum score
    winners = [
        dosha for dosha, score in scores.items()
        if score == max_score
    ]

    # Handle tie
    if len(winners) > 1:
        classification = "Mixed / Equal Classification"
    else:
        classification = winners[0]

    return scores, classification


def main():
    print("==============================================")
    print(" AYURVEDIC RULE-BASED EXPERT SYSTEM")
    print("==============================================")

    body_build = input("Body build (lean/medium/large): ").lower()
    appetite = input("Appetite (irregular/strong/steady): ").lower()
    activity = input("Activity level (high/moderate/low): ").lower()
    sleep = input("Sleep (light/moderate/deep): ").lower()
    temperature = input("Temperature preference (cold/cool/neutral): ").lower()
    skin = input("Skin type (dry/sensitive/oily): ").lower()

    scores, result = classify_dosha(
        body_build, appetite, activity,
        sleep, temperature, skin
    )

    print("\n--------------- RESULT ---------------")
    print("Vata Score  :", scores["Vata"])
    print("Pitta Score :", scores["Pitta"])
    print("Kapha Score :", scores["Kapha"])
    print("Classification:", result)
    print("--------------------------------------")
    print("Educational model only; not a medical")
    print("diagnostic or treatment system.")


if __name__ == "__main__":
    main()