# spec:trace: aws/lightsail/update_distribution.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-distribution
# spec:generated: DO NOT EDIT — edit the spec instead

def update_distribution(store, request: dict) -> dict:
    """Updates an existing Amazon Lightsail content delivery network (CDN) distribution. Use this action to update the configuration of your existing distribution."""
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    resource = store.distributions(distribution_name)
    if not resource:
        raise ResourceNotFoundException("Resource distribution_name not found")

    # Update mutable fields
    if "origin" in request:
        resource["origin"] = origin
    if "defaultCacheBehavior" in request:
        resource["defaultCacheBehavior"] = default_cache_behavior
    if "cacheBehaviorSettings" in request:
        resource["cacheBehaviorSettings"] = cache_behavior_settings
    if "cacheBehaviors" in request:
        resource["cacheBehaviors"] = cache_behaviors
    if "isEnabled" in request:
        resource["isEnabled"] = is_enabled
    if "viewerMinimumTlsProtocolVersion" in request:
        resource["viewerMinimumTlsProtocolVersion"] = viewer_minimum_tls_protocol_version
    if "certificateName" in request:
        resource["certificateName"] = certificate_name
    if "useDefaultCertificate" in request:
        resource["useDefaultCertificate"] = use_default_certificate

    store.distributions(distribution_name, resource)
    return resource

