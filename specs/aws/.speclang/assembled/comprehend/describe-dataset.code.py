def handler(store, r): return store.describe_entity(r["DatasetArn"]).to_dict()
