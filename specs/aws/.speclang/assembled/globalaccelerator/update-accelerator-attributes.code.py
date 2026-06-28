def handler(store, request: dict) -> dict:
    return store.update_accelerator_attributes(
        AcceleratorArn=request["AcceleratorArn"],
        FlowLogsEnabled=request.get("FlowLogsEnabled"),
        FlowLogsS3Bucket=request.get("FlowLogsS3Bucket"),
        FlowLogsS3Prefix=request.get("FlowLogsS3Prefix"),
    )
