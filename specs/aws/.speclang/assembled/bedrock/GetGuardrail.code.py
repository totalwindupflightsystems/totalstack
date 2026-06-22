def handler(store, request: dict) -> dict:
    record = store.get_guardrail(
        request["guardrailIdentifier"],
        guardrailVersion=request.get("guardrailVersion"))
    return record.to_dict()
