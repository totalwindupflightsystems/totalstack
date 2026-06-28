def handler(store, request: dict) -> dict:
    r = store.dashboards(request["AwsAccountId"], request["DashboardId"])
    if not r:
        raise ResourceNotFoundException(f"Dashboard {request['DashboardId']} not found")
    return {"Dashboard": r.to_dict(), "RequestId": "", "Status": r.Status}
