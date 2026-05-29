def extract_intent(prompt):

    prompt = prompt.lower()

    features = []

    if "login" in prompt:
        features.append("authentication")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "payment" in prompt:
        features.append("payments")
        
    assumptions = []

    if "school" in prompt:
        assumptions.append(
        "Assuming student and teacher roles"
    )

    return {
    "app_type": "CRM",
    "features": features,
    "assumptions": assumptions
}