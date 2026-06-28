def handler(store, r):
    rec = store.datasets(r["datasetArn"])
    if not rec: raise ResourceNotFoundException("not found")
    return rec.to_dict()
