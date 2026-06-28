def handler(store, request: dict) -> dict:
    return store.reject_resource_share_invitation(
        request["resourceShareInvitationArn"],
        clientToken=request.get("clientToken"),
    )
