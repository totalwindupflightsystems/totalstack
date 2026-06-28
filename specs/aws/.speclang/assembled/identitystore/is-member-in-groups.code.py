def handler(store, request: dict) -> dict:
    return store.is_member_in_groups(request["identityStoreId"], request["memberId"], request["groupIds"])
