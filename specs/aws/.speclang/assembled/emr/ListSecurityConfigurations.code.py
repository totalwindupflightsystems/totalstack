def handler(store, request: dict) -> dict:
    configs = store.list_security_configurations()
    return {"SecurityConfigurations": [c.to_dict() for c in configs]}
