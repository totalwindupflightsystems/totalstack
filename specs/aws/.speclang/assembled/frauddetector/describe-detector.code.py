def handler(store, r: dict) -> dict:
    rec = store.detectors(r["detectorId"])
    if not rec: raise ResourceNotFoundException(f"Detector {r['detectorId']} not found")
    return rec.to_dict()
