def handler(store, request: dict) -> dict:
    r = store.dashboards(request["AwsAccountId"], request["DashboardId"])
    if not r:
        raise ResourceNotFoundException(f"Dashboard {request['DashboardId']} not found")
    store.delete_dashboard(request["AwsAccountId"], request["DashboardId"])
    return {"Arn": r.Arn, "DashboardId": r.DashboardId, "RequestId": "", "Status": 200}
