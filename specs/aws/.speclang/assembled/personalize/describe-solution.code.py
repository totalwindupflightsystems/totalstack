def handler(store, r):
    rec = store.solutions(r["solutionArn"])
    if not rec: raise ResourceNotFoundException("not found")
    return rec.to_dict()
