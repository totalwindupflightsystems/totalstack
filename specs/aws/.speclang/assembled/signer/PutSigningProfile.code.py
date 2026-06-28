def handler(store, request):
    profileName = request["profileName"]
    platformId = request["platformId"]
    signingMaterial = request.get("signingMaterial")
    signatureValidityPeriod = request.get("signatureValidityPeriod")
    overrides = request.get("overrides")
    signingParameters = request.get("signingParameters")
    tags = request.get("tags")

    # Try create first — if exists, update
    existing = store.profiles(profileName)
    if existing:
        record = store.update_profile(profileName, signingMaterial, signatureValidityPeriod,
                                      overrides, signingParameters, tags)
    else:
        record = store.create_profile(profileName, platformId, signingMaterial,
                                      signatureValidityPeriod, overrides,
                                      signingParameters, tags)
    return {"arn": record.arn, "profileVersion": record.profileVersion,
            "profileVersionArn": record.profileVersionArn}
