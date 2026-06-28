def handler(store, request):
    record = store.disable_profile(request["profileId"])
    return {"profile": record.to_dict()}
