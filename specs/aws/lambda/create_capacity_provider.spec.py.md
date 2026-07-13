---
id: "@specs/aws/lambda/create_capacity_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateCapacityProvider"
---

# CreateCapacityProvider

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_capacity_provider
> **spec:implements:** @kind:operation CreateCapacityProvider
> **AWS Protocol:** rest-json
> **HTTP:** POST /2025-11-30/capacity-providers
> **@ref:** specs/aws/lambda/docs/API_CreateCapacityProvider.spec.md

Creates a capacity provider that manages compute resources for Lambda functions

## Input Shape: CreateCapacityProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderName | Any  # complex shape | ✓ | The name of the capacity provider. |
| CapacityProviderScalingConfig | Any  # complex shape |  | The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count  |
| InstanceRequirements | Any  # complex shape |  | The instance requirements that specify the compute instance characteristics, including architectures and allowed or excl |
| KmsKeyArn | Any  # complex shape |  | The ARN of the KMS key used to encrypt data associated with the capacity provider. |
| PermissionsConfig | Any  # complex shape | ✓ | The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources. |
| Tags | Any  # complex shape |  | A list of tags to associate with the capacity provider. |
| VpcConfig | Any  # complex shape | ✓ | The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances wil |

## Output Shape: CreateCapacityProviderResponse

- **CapacityProvider** (Any  # complex shape): Information about the capacity provider that was created.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **CapacityProviderLimitExceededException**: The maximum number of capacity providers for your account has been exceeded. For more information, see Lambda quotas

## Implementation

```speclang
def create_capacity_provider(store, request: dict) -> dict:
    """Creates a capacity provider that manages compute resources for Lambda functions"""
    capacity_provider_name = request.get("CapacityProviderName", "").strip() if isinstance(request.get("CapacityProviderName"), str) else request.get("CapacityProviderName")
    if not capacity_provider_name:
        raise ValidationException("CapacityProviderName is required")
    permissions_config = request.get("PermissionsConfig", "").strip() if isinstance(request.get("PermissionsConfig"), str) else request.get("PermissionsConfig")
    if not permissions_config:
        raise ValidationException("PermissionsConfig is required")
    vpc_config = request.get("VpcConfig", "").strip() if isinstance(request.get("VpcConfig"), str) else request.get("VpcConfig")
    if not vpc_config:
        raise ValidationException("VpcConfig is required")

    if store.capacity_providers(capacity_provider_name):
        raise ResourceInUseException(f"Resource capacity_provider_name already exists")

    record = {
        "CapacityProviderName": capacity_provider_name,
        "VpcConfig": vpc_config,
        "PermissionsConfig": permissions_config,
        "InstanceRequirements": instance_requirements,
        "CapacityProviderScalingConfig": capacity_provider_scaling_config,
        "KmsKeyArn": kms_key_arn,
        "Tags": tags,
    }

    store.capacity_providers(capacity_provider_name, record)

    return {
        "CapacityProvider": record.get("CapacityProvider", {}),
    }
```
