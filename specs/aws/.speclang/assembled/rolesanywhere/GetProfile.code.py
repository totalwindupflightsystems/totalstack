def handler(store, request):
    record = store.profiles(request["profileId"])
    if not record:
        raise ResourceNotFoundException(f"Profile {request['profileId']} not found")
    return {"profile": record.to_dict()}
