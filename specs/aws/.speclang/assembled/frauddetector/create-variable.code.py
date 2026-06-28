def handler(store, r: dict) -> dict:
    store.create_variable(r["name"], dataType=r.get("dataType", ""),
        dataSource=r.get("dataSource", ""), defaultValue=r.get("defaultValue", ""),
        **{k: v for k, v in r.items() if k not in ("name", "dataType", "dataSource", "defaultValue")})
    return {}
