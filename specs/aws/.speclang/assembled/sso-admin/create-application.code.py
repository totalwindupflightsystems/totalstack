def handler(store, request: dict) -> dict:
    return store.create_application(request["instanceArn"], request["applicationProviderArn"], request["name"], description=request.get("description"), portalOptions=request.get("portalOptions"), tags=request.get("tags"))
