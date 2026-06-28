def handler(store, request: dict) -> dict:
    return store.get_resource_share_invitations(
        resourceShareInvitationArns=request.get("resourceShareInvitationArns"),
        resourceShareArns=request.get("resourceShareArns"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
