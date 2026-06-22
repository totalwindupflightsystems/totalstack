def handler(store, request: dict) -> dict:
    return store.get_account_configuration()
