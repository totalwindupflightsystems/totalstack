def handler(store, request: dict) -> dict:
    record = store.create_guardrail_version(
        request["guardrailIdentifier"],
        description=request.get("description"),
        clientRequestToken=request.get("clientRequestToken"))
    return {"guardrailId": record.guardrailId,
            "version": str(record.numericalVersion - 1)}
