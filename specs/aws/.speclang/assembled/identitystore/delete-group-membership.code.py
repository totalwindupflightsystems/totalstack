def handler(store, request: dict) -> dict:
    return store.delete_group_membership(request["identityStoreId"], request["membershipId"])
