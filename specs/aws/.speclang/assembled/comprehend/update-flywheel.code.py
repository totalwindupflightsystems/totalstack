def handler(store, r): store.update_entity(r["FlywheelArn"], DataAccessRoleArn=r.get("DataAccessRoleArn")); return {}
