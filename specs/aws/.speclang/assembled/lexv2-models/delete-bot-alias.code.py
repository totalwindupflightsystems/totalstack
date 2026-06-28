def delete_bot_alias(store, request: dict) -> dict:
    store.delete_bot_alias(request["botId"], request["botAliasName"])
    return {}
