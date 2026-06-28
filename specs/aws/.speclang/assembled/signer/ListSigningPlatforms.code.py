def handler(store, request):
    platforms = store.platforms()
    maxResults = request.get("maxResults", 100)
    platforms_data = [p.to_dict() for p in platforms[:maxResults]]
    return {"platforms": platforms_data, "nextToken": None}
