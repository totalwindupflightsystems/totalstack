def handler(store, request: dict) -> dict:
    r = store.update_dashboard(request["AwsAccountId"], request["DashboardId"],
        Name=request["Name"],
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "DashboardId", "Name")})
    return {"Arn": r.Arn, "CreationStatus": r.CreationStatus, "DashboardId": r.DashboardId,
            "RequestId": "", "Status": r.Status, "VersionArn": r.VersionArn}
