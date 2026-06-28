def handler(store, r: dict) -> dict:
    mt = r.get("modelType", "")
    store.update_model(r["modelId"], mt,
        **{k: v for k, v in r.items() if k not in ("modelId", "modelType")})
    return {}
