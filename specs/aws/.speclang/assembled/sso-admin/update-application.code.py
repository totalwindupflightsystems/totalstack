def handler(store, request: dict) -> dict:
    return store.update_application(request["applicationArn"], name=request.get("name"), description=request.get("description"), status=request.get("status"), portalOptions=request.get("portalOptions"))
