"""EnableAllFeatures handler."""


def handle_enable_all_features(store, request: dict) -> dict:
    store.enable_all_features()
    return {}
