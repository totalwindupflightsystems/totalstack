def handler(store, r): store.update_entity(r["EndpointArn"], DesiredInferenceUnits=r.get("DesiredInferenceUnits")); return {}
