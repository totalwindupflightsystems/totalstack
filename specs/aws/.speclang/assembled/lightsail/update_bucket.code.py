# spec:trace: aws/lightsail/update_bucket.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-bucket
# spec:generated: DO NOT EDIT — edit the spec instead

def update_bucket(store, request: dict) -> dict:
    """Updates an existing Amazon Lightsail bucket. Use this action to update the configuration of an existing bucket, such as versioning, public accessibility, and the Amazon Web Services accounts that can """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    resource = store.buckets(bucket_name)
    if not resource:
        raise ResourceNotFoundException("Resource bucket_name not found")

    # Update mutable fields
    if "accessRules" in request:
        resource["accessRules"] = access_rules
    if "versioning" in request:
        resource["versioning"] = versioning
    if "readonlyAccessAccounts" in request:
        resource["readonlyAccessAccounts"] = readonly_access_accounts
    if "accessLogConfig" in request:
        resource["accessLogConfig"] = access_log_config
    if "cors" in request:
        resource["cors"] = cors

    store.buckets(bucket_name, resource)
    return resource

