def handler(store, request: dict) -> dict:
    return store.describe_scraper(request["scraperId"])

