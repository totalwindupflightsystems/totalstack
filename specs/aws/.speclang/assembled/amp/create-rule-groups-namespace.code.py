def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k not in ("clientToken",)}
    return store.create_rule_groups_namespace(**kwargs)

