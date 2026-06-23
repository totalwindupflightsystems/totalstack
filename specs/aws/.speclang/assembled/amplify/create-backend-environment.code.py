def handler(store, request: dict) -> dict:
    record = store.create_backend_environment(request["appId"], request["environmentName"], **{k: v for k, v in request.items() if k not in ("appId", "environmentName")})
    return {"backendEnvironment": record.to_dict()}
