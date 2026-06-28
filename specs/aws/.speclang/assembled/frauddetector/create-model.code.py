def handler(store, r: dict) -> dict:
    store.create_model(r["modelId"], r["modelType"],
        eventTypeName=r.get("eventTypeName", ""),
        **{k: v for k, v in r.items() if k not in ("modelId", "modelType", "eventTypeName")})
    return {}
