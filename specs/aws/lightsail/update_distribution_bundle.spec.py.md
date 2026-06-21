---
id: "@specs/aws/lightsail/update_distribution_bundle"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateDistributionBundle"
---

# UpdateDistributionBundle

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_distribution_bundle
> **spec:implements:** @kind:operation UpdateDistributionBundle
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateDistributionBundle.spec.md

Updates the bundle of your Amazon Lightsail content delivery network (CDN) distribution. A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution. Update your distribution's bundle if your distribution is going over its monthly network transfer quota and is incurring an overage fee. You can update your distribution's bundle only one time within your monthly Amazon Web Services billing cycle. To determine if you can update your distribution's bundle, use the GetDistributions action. The ableToUpdateBundle parameter in the result will indicate whether you can currently update your distribution's bundle.

## Input Shape: UpdateDistributionBundleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bundleId | Any  # complex shape |  | The bundle ID of the new bundle to apply to your distribution. Use the GetDistributionBundles action to get a list of di |
| distributionName | Any  # complex shape |  | The name of the distribution for which to update the bundle. Use the GetDistributions action to get a list of distributi |

## Output Shape: UpdateDistributionBundleResult

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
def update_distribution_bundle(store, request: dict) -> dict:
    """Updates the bundle of your Amazon Lightsail content delivery network (CDN) distribution. A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution. Updat"""

```
