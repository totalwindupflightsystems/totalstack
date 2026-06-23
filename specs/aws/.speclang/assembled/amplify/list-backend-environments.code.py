def handler(store, request: dict) -> dict:
    return store.list_backend_environments(request["appId"], request.get("nextToken"), request.get("maxResults"), request.get("environmentName"))
