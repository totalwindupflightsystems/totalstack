def handler(store, request: dict) -> dict:
    r = store.forecasts(request["ForecastArn"])
    if not r:
        raise ResourceNotFoundException(f"Forecast {request['ForecastArn']} not found")
    return r.to_dict()
