def handler(store, request: dict) -> dict:
    record = store.delete_backend_environment(request["appId"], request["environmentName"])
    return {"backendEnvironment": record.to_dict()}
