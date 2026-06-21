---
id: "@specs/aws/lightsail/create_cloud_formation_stack"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateCloudFormationStack"
---

# CreateCloudFormationStack

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_cloud_formation_stack
> **spec:implements:** @kind:operation CreateCloudFormationStack
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateCloudFormationStack.spec.md

Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to track the AWS CloudFormation stack created. Use the get cloud formation stack records operation to get a list of the CloudFormation stacks created. Wait until after your new Amazon EC2 instance is created before running the create cloud formation stack operation again with the same export snapshot record.

## Input Shape: CreateCloudFormationStackRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instances | list[Any  # complex shape] | ✓ | An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at  |

## Output Shape: CreateCloudFormationStackResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def create_cloud_formation_stack(store, request: dict) -> dict:
    """Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to tra"""
    instances = request.get("instances", "").strip() if isinstance(request.get("instances"), str) else request.get("instances")
    if not instances:
        raise ValidationException("instances is required")

    if store.cloud_formation_stacks(instances):
        raise ResourceInUseException(f"Resource instances already exists")

    record = {
        "instances": instances,
    }

    store.cloud_formation_stacks(instances, record)

    return {
        "operations": record.get("operations", {}),
    }
```
