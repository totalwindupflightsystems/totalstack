def handler(store, r: dict) -> dict:
    store.create_detector(r["detectorId"], eventTypeName=r.get("eventTypeName", ""),
        **{k: v for k, v in r.items() if k not in ("detectorId", "eventTypeName")})
    return {}
