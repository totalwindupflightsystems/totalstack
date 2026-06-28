def handler(store, request):
    profileName = request["profileName"]
    profileVersion = request["profileVersion"]
    reason = request["reason"]
    effectiveTime = request["effectiveTime"]
    store.revoke_profile(profileName, profileVersion, reason, effectiveTime)
    return {}
