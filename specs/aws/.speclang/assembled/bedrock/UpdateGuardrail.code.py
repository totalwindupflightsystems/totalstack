def handler(store, request: dict) -> dict:
    record = store.update_guardrail(request)
    return {"guardrailId": record.guardrailId, "guardrailArn": record.guardrailArn,
            "version": record.version, "updatedAt": record.updatedAt}
