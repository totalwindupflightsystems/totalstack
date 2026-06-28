def handler(store, request: dict) -> dict:
    return store.get_default_scraper_configuration()

