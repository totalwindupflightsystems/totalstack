def handler(store, r: dict) -> dict:
    store.create_eventtype(r["name"],
        eventVariables=r.get("eventVariables", []),
        entityTypes=r.get("entityTypes", []),
        **{k: v for k, v in r.items() if k not in ("name", "eventVariables", "entityTypes")})
    return {}
