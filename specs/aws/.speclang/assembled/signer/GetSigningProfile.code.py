def handler(store, request):
    profileName = request["profileName"]
    profile = store.profiles(profileName)
    if not profile:
        raise ResourceNotFoundException(f"Signing profile {profileName} not found")
    return profile.to_dict()
