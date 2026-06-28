def start_task_execution(store, request: dict) -> dict:
    return store.start_task_execution(
        TaskArn=request["TaskArn"],
        OverrideOptions=request.get("OverrideOptions"),
        Includes=request.get("Includes"),
        Excludes=request.get("Excludes"),
        ManifestConfig=request.get("ManifestConfig"),
        TaskReportConfig=request.get("TaskReportConfig"),
        Tags=request.get("Tags"),
    )
