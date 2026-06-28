def handler(store, request: dict) -> dict:
    tags = store.list_tags_for_resource(request["ResourceArn"])
    tag_list = [{"Key": k, "Value": v} for k, v in tags.items()]
    return {"Tags": tag_list}
