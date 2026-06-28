def handler(store, request):
    record = store.enable_profile(request["profileId"])
    return {"profile": record.to_dict()}
