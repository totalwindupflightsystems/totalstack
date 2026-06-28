def handler(store, request: dict) -> dict:
    scraperId = request["scraperId"]
    kwargs = {}
    for k in ("alias", "destination", "roleConfiguration", "scrapeConfiguration"):
        if k in request:
            kwargs[k] = request[k]
    return store.update_scraper(scraperId, **kwargs)

