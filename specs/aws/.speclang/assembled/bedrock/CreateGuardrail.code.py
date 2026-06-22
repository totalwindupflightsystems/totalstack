def handler(store, request: dict) -> dict:
    record = store.create_guardrail(request)
    return {"guardrailId": record.guardrailId, "guardrailArn": record.guardrailArn,
            "version": record.version, "createdAt": record.createdAt}
