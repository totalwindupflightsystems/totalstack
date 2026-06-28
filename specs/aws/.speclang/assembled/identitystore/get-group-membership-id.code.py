def handler(store, request: dict) -> dict:
    return store.get_group_membership_id(request["identityStoreId"], request["groupId"], request["memberId"])
