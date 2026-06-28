def handler(store, request):
    record = store.update_profile(
        request["profileId"],
        name=request.get("name"),
        roleArns=request.get("roleArns"),
        sessionPolicy=request.get("sessionPolicy"),
        durationSeconds=request.get("durationSeconds"),
        managedPolicyArns=request.get("managedPolicyArns"),
        requireInstanceProperties=request.get("requireInstanceProperties"),
    )
    return {"profile": record.to_dict()}
