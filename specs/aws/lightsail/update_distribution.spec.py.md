---
id: "@specs/aws/lightsail/update_distribution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateDistribution"
---

# UpdateDistribution

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_distribution
> **spec:implements:** @kind:operation UpdateDistribution
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateDistribution.spec.md

Updates an existing Amazon Lightsail content delivery network (CDN) distribution. Use this action to update the configuration of your existing distribution.

## Input Shape: UpdateDistributionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| cacheBehaviorSettings | Any  # complex shape |  | An object that describes the cache behavior settings for the distribution. The cacheBehaviorSettings specified in your U |
| cacheBehaviors | list[Any  # complex shape] |  | An array of objects that describe the per-path cache behavior for the distribution. |
| certificateName | Any  # complex shape |  | The name of the SSL/TLS certificate that you want to attach to the distribution. Only certificates with a status of ISSU |
| defaultCacheBehavior | Any  # complex shape |  | An object that describes the default cache behavior for the distribution. |
| distributionName | Any  # complex shape | ✓ | The name of the distribution to update. Use the GetDistributions action to get a list of distribution names that you can |
| isEnabled | Any  # complex shape |  | Indicates whether to enable the distribution. |
| origin | Any  # complex shape |  | An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balance |
| useDefaultCertificate | Any  # complex shape |  | Indicates whether the default SSL/TLS certificate is attached to the distribution. The default value is true . When true |
| viewerMinimumTlsProtocolVersion | Any  # complex shape |  | Use this parameter to update the minimum TLS protocol version for the SSL/TLS certificate that's attached to the distrib |

## Output Shape: UpdateDistributionResult

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
def update_distribution(store, request: dict) -> dict:
    """Updates an existing Amazon Lightsail content delivery network (CDN) distribution. Use this action to update the configuration of your existing distribution."""
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    resource = store.distributions(distribution_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource distribution_name not found")

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
```
