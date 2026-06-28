def handler(store, request):
    profileName = request["profileName"]
    perms, revId, nextToken = store.list_permissions(profileName)
    return {
        "revisionId": revId,
        "policySizeBytes": len(str(perms)),
        "permissions": [p.to_dict() for p in perms],
    }
