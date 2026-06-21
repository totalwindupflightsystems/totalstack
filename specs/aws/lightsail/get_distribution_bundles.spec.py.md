---
id: "@specs/aws/lightsail/get_distribution_bundles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDistributionBundles"
---

# GetDistributionBundles

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_distribution_bundles
> **spec:implements:** @kind:operation GetDistributionBundles
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDistributionBundles.spec.md

Returns the bundles that can be applied to your Amazon Lightsail content delivery network (CDN) distributions. A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution.

## Input Shape: GetDistributionBundlesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: GetDistributionBundlesResult

- **bundles** (list[Any  # complex shape]): An object that describes a distribution bundle.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_distribution_bundles(store, request: dict) -> dict:
    """Returns the bundles that can be applied to your Amazon Lightsail content delivery network (CDN) distributions. A distribution bundle specifies the monthly network transfer quota and monthly cost of yo"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
