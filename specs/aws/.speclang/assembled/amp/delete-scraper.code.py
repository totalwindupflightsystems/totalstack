def handler(store, request: dict) -> dict:
    return store.delete_scraper(request["scraperId"])

