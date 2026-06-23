def handler(store, r):
    rec = store.create_entity(r["EndpointArn"], r.get("EndpointName", "ep"), "endpoint", DesiredInferenceUnits=r.get("DesiredInferenceUnits", 1))
    return {"EndpointArn": rec.arn}
