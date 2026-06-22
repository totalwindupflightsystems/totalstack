def handler(store, request: dict) -> dict:
    return store.delete_guardrail(
        request["guardrailIdentifier"],
        guardrailVersion=request.get("guardrailVersion"))
