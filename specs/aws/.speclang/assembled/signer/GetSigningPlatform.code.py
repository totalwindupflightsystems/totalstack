def handler(store, request):
    platformId = request["platformId"]
    platform = store.platforms(platformId)
    if not platform:
        raise ResourceNotFoundException(f"Signing platform {platformId} not found")
    return platform.to_dict()
