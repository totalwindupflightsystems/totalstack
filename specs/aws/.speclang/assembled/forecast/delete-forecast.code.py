def handler(store, request: dict) -> dict:
    r = store.forecasts(request["ForecastArn"])
    if not r:
        raise ResourceNotFoundException(f"Forecast {request['ForecastArn']} not found")
    store.delete_forecast(request["ForecastArn"])
    return {}
