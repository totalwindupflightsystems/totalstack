def handler(store, request: dict) -> dict:
    return store.describe_group_membership(request["identityStoreId"], request["membershipId"])
