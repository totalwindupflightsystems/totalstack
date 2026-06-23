def handler(store, r): store.tag_resource(r["ResourceArn"], r["Tags"]); return {}
