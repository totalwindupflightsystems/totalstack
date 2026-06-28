def handler(store, request):
    profileName = request["profileName"]
    store.cancel_profile(profileName)
    return {}
