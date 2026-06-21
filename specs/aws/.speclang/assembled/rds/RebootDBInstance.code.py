def handler(store, request: dict) -> dict:
    """RebootDBInstance handler."""
    return store.reboot_db_instance(
        db_instance_identifier=request["DBInstanceIdentifier"],
        force_failover=request.get("ForceFailover", False))
