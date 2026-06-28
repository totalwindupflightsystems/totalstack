def handler(store, request: dict) -> dict:
    return store.create_group_membership(request["identityStoreId"], request["groupId"], request["memberId"])
