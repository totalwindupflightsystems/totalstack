def handler(store, request):
    record = store.create_profile(
        name=request["name"],
        roleArns=request.get("roleArns"),
        sessionPolicy=request.get("sessionPolicy"),
        durationSeconds=request.get("durationSeconds"),
        managedPolicyArns=request.get("managedPolicyArns"),
        requireInstanceProperties=request.get("requireInstanceProperties"),
        tags=request.get("tags"),
        enabled=request.get("enabled", True),
    )
    return {"profile": record.to_dict()}
