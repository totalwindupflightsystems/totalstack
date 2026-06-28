def handler(store, request: dict) -> dict:
    return store.start_conversation(
        botId=request["botId"],
        botAliasId=request["botAliasId"],
        localeId=request["localeId"],
        sessionId=request["sessionId"],
        conversationMode=request.get("conversationMode"))

