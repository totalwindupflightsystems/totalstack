def handler(store, r): store.untag_resource(r["ResourceArn"], r["TagKeys"]); return {}
