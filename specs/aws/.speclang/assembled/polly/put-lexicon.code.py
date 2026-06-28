def handler(store, request: dict) -> dict:
    return store.put_lexicon(
        Name=request["Name"],
        Content=request["Content"])

