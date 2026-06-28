def handler(store, r):
    rec = store.campaigns(r["campaignArn"])
    if not rec: raise ResourceNotFoundException("not found")
    return rec.to_dict()
