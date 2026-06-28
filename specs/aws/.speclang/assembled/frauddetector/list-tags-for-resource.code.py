def handler(store, r: dict) -> dict:
    tags = store.list_tags_for_resource(r["resourceARN"])
    tag_list = [{"key": k, "value": v} for k, v in tags.items()]
    return {"tags": tag_list}
