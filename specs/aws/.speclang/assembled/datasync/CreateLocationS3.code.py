def create_location_s3(store, request: dict) -> dict:
    return store.create_location_s3(
        S3BucketArn=request["S3BucketArn"],
        S3Config=request["S3Config"],
        Subdirectory=request.get("Subdirectory"),
        S3StorageClass=request.get("S3StorageClass"),
        AgentArns=request.get("AgentArns"),
        Tags=request.get("Tags"),
    )
