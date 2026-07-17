def handler(store, r: dict) -> dict:
    return store.put_parameter(r["Name"], r["Value"], r.get("Type", "String"), r.get("Description", ""), r.get("Overwrite", False))