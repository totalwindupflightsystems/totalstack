def handler(store, request: dict) -> dict:
    return store.get_table_auto_scaling_settings(**request)

