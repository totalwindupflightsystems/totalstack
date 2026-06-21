---
id: "@specs/aws/lightsail/delete_distribution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteDistribution"
---

# DeleteDistribution

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_distribution
> **spec:implements:** @kind:operation DeleteDistribution
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteDistribution.spec.md

Deletes your Amazon Lightsail content delivery network (CDN) distribution.

## Input Shape: DeleteDistributionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| distributionName | Any  # complex shape |  | The name of the distribution to delete. Use the GetDistributions action to get a list of distribution names that you can |

## Output Shape: DeleteDistributionResult

- **operation** (Any  # complex shape): An object that describes the result of the action, such as the status of the request, the timestamp of the request, and 

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def delete_distribution(store, request: dict) -> dict:
    """Deletes your Amazon Lightsail content delivery network (CDN) distribution."""

    return {}
```
