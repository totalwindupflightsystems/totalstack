def handler(store, request):
    signatureTimestamp = request["signatureTimestamp"]
    platformId = request["platformId"]
    profileVersionArn = request["profileVersionArn"]
    jobArn = request["jobArn"]
    certificateHashes = request["certificateHashes"]
    return store.get_revocation_status(signatureTimestamp, platformId, profileVersionArn, jobArn, certificateHashes)
