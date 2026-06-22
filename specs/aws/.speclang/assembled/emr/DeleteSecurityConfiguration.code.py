def handler(store, request: dict) -> dict:
    store.delete_security_configuration(request["Name"])
    return {}
