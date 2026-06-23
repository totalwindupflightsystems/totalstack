def handler(store, r): return store.describe_entity(r["DocumentClassifierArn"]).to_dict()
