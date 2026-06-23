def handler(store, r):
    rec = store.create_entity(r["FlywheelArn"], r.get("FlywheelName", "fw"), "flywheel")
    return {"FlywheelArn": rec.arn}
