def list_tapes(store, request: dict) -> dict:
    return store.list_tapes(
        TapeARNs=request.get("TapeARNs"),
        Marker=request.get("Marker"),
        Limit=request.get("Limit"),
    )
