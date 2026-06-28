def handler(store, request):
    record = store.delete_profile(request["profileId"])
    return {"profile": record.to_dict()}
