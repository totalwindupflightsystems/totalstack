def handler(store, r): tags = store.list_tags_for_resource(r["resourceArn"]); return {"tags": [{"tagKey":k,"tagValue":v} for k,v in tags.items()]}
