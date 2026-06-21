---
id: "@specs/aws/lightsail/create_distribution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDistribution"
---

# CreateDistribution

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_distribution
> **spec:implements:** @kind:operation CreateDistribution
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDistribution.spec.md

Creates an Amazon Lightsail content delivery network (CDN) distribution. A distribution is a globally distributed network of caching servers that improve the performance of your website or web application hosted on a Lightsail instance. For more information, see Content delivery networks in Amazon Lightsail .

## Input Shape: CreateDistributionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bundleId | Any  # complex shape | ✓ | The bundle ID to use for the distribution. A distribution bundle describes the specifications of your distribution, such |
| cacheBehaviorSettings | Any  # complex shape |  | An object that describes the cache behavior settings for the distribution. |
| cacheBehaviors | list[Any  # complex shape] |  | An array of objects that describe the per-path cache behavior for the distribution. |
| certificateName | Any  # complex shape |  | The name of the SSL/TLS certificate that you want to attach to the distribution. Use the GetCertificates action to get a |
| defaultCacheBehavior | Any  # complex shape | ✓ | An object that describes the default cache behavior for the distribution. |
| distributionName | Any  # complex shape | ✓ | The name for the distribution. |
| ipAddressType | Any  # complex shape |  | The IP address type for the distribution. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. T |
| origin | Any  # complex shape | ✓ | An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balance |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the distribution during create. Use the TagResource action to tag a resource  |
| viewerMinimumTlsProtocolVersion | Any  # complex shape |  | The minimum TLS protocol version for the SSL/TLS certificate. |

## Output Shape: CreateDistributionResult

- **distribution** (Any  # complex shape): An object that describes the distribution created.
- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
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
        raise ResourceInUseException(f"Resource bundle_id already exists")

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
```
