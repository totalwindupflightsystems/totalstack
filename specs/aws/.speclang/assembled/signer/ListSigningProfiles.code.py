def handler(store, request):
    profiles = store.profiles()
    maxResults = request.get("maxResults", 100)
    profiles_data = [p.to_dict() for p in profiles[:maxResults]]
    return {"profiles": profiles_data, "nextToken": None}
