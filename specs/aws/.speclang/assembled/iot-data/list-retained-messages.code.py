def list_retained_messages(store, request: dict) -> dict:
    msgs = store.list_retained_messages()
    return {"retainedMessages": msgs}
