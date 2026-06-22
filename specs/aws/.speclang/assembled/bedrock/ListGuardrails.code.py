def handler(store, request: dict) -> dict:
    return store.list_guardrails(
        guardrailIdentifier=request.get("guardrailIdentifier"),
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"))
