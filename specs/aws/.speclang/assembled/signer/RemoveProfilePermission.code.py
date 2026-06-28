def handler(store, request):
    profileName = request["profileName"]
    revisionId = request["revisionId"]
    statementId = request["statementId"]
    newRevId = store.remove_permission(profileName, statementId, revisionId)
    return {"revisionId": newRevId}
