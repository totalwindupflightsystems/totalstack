# spec:trace: aws/lightsail/create_distribution.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-distribution
# spec:generated: DO NOT EDIT — edit the spec instead

def create_distribution(store, request: dict) -> dict:
    """Creates an Amazon Lightsail content delivery network (CDN) distribution. A distribution is a globally distributed network of caching servers that improve the performance of your website or web applica"""
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")
    default_cache_behavior = request.get("defaultCacheBehavior", "").strip() if isinstance(request.get("defaultCacheBehavior"), str) else request.get("defaultCacheBehavior")
    if not default_cache_behavior:
        raise ValidationException("defaultCacheBehavior is required")
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")
    origin = request.get("origin", "").strip() if isinstance(request.get("origin"), str) else request.get("origin")
    if not origin:
        raise ValidationException("origin is required")

    if store.distributions(bundle_id):
        raise ResourceInUseException("Resource bundle_id already exists")

    record = {
        "distributionName": distribution_name,
        "origin": origin,
        "defaultCacheBehavior": default_cache_behavior,
        "cacheBehaviorSettings": cache_behavior_settings,
        "cacheBehaviors": cache_behaviors,
        "bundleId": bundle_id,
        "ipAddressType": ip_address_type,
        "tags": tags,
        "certificateName": certificate_name,
        "viewerMinimumTlsProtocolVersion": viewer_minimum_tls_protocol_version,
    }

    store.distributions(bundle_id, record)

    return {
        "distribution": record.get("distribution", {}),
        "operation": record.get("operation", {}),
    }

