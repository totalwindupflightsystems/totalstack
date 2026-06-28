def handler(store, r: dict) -> dict:
    store.update_variable(r["name"],
        **{k: v for k, v in r.items() if k not in ("name",)})
    return {}
