def describe_bot_alias(store, request: dict) -> dict:
    return store.describe_bot_alias(request["botId"], request["botAliasName"])
