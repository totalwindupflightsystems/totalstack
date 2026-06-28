def handler(store, request):
    profileName = request["profileName"]
    action = request["action"]
    principal = request["principal"]
    statementId = request["statementId"]
    profileVersion = request.get("profileVersion")
    revisionId = request.get("revisionId")
    newRevisionId = store.add_permission(profileName, action, principal, statementId, profileVersion, revisionId)
    return {"revisionId": newRevisionId}
