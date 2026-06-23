def handler(store, r): return store.describe_entity(r["EndpointArn"]).to_dict()
