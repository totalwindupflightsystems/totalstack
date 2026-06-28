def handler(store, request: dict) -> dict:
    return store.accept_resource_share_invitation(
        request["resourceShareInvitationArn"],
        clientToken=request.get("clientToken"),
    )
