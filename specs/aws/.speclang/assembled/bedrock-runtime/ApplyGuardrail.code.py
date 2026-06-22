def handler(store, request: dict) -> dict:
    """Apply a guardrail to content."""
    return {
        "action": "NONE",
        "outputs": [],
        "assessments": [],
        "guardrailCoverage": {"textCharacters": {"guarded": 0, "total": 0}},
        "usage": {"topicPolicyUnits": 0, "contentPolicyUnits": 0, "wordPolicyUnits": 0,
                   "sensitiveInformationPolicyUnits": 0, "sensitiveInformationPolicyFreeUnits": 0,
                   "contextualGroundingPolicyUnits": 0},
    }

