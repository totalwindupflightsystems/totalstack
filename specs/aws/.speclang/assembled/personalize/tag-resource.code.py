def handler(store, r): store.tag_resource(r["resourceArn"], r["tags"]); return {}
