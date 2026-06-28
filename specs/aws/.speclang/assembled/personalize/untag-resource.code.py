def handler(store, r): store.untag_resource(r["resourceArn"], r["tagKeys"]); return {}
