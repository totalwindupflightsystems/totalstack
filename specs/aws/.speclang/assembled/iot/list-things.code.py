def list_things(store, request: dict) -> dict:
    things = store.list_things()
    return {"things": things}
