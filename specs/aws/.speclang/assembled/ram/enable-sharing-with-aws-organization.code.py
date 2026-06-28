def handler(store, request: dict) -> dict:
    return store.enable_sharing_with_aws_organization()
