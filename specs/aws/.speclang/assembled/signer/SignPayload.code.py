def handler(store, request):
    profileName = request["profileName"]
    payload = request["payload"]
    payloadFormat = request["payloadFormat"]
    profileOwner = request.get("profileOwner")
    return store.sign_payload(profileName, payload, payloadFormat, profileOwner)
