---
id: "@specs/aws/cloudformation/create_stack_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateStackInstances"
---

# CreateStackInstances

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_stack_instances
> **spec:implements:** @kind:operation CreateStackInstances
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateStackInstances.spec.md

Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either Accounts or DeploymentTargets , and you must specify at least one value for Regions . The maximum number of organizational unit (OUs) supported by a CreateStackInstances operation is 50. If you need more than 50, consider the following options: Batch processing: If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each. Parent OU strategy: If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.

## Input Shape: CreateStackInstancesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Accounts | list[Any  # complex shape] |  | [Self-managed permissions] The account IDs of one or more Amazon Web Services accounts that you want to create stack ins |
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| DeploymentTargets | Any  # complex shape |  | [Service-managed permissions] The Organizations accounts in which to create stack instances in the specified Amazon Web  |
| OperationId | Any  # complex shape |  | The unique identifier for this StackSet operation. The operation ID also functions as an idempotency token, to ensure th |
| OperationPreferences | Any  # complex shape |  | Preferences for how CloudFormation performs this StackSet operation. |
| ParameterOverrides | Any  # complex shape |  | A list of StackSet parameters whose values you want to override in the selected stack instances. Any overridden paramete |
| Regions | list[Any  # complex shape] | ✓ | The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to create stack instances from. |

## Output Shape: CreateStackInstancesOutput

- **OperationId** (Any  # complex shape): The unique identifier for this StackSet operation.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **OperationIdAlreadyExistsException**: The specified operation ID already exists.
- **StaleRequestException**: Another operation has been performed on this StackSet since the specified operation was performed.
- **InvalidOperationException**: The specified operation isn't valid.
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .

## Implementation

```speclang
def create_stack_instances(store, request: dict) -> dict:
    """Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one"""
    regions = request.get("Regions", "").strip() if isinstance(request.get("Regions"), str) else request.get("Regions")
    if not regions:
        raise ValidationException("Regions is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    if store.stack_instancess(stack_set_name):
        raise ResourceInUseException(f"Resource stack_set_name already exists")

    record = {
        "StackSetName": stack_set_name,
        "Accounts": accounts,
        "DeploymentTargets": deployment_targets,
        "Regions": regions,
        "ParameterOverrides": parameter_overrides,
        "OperationPreferences": operation_preferences,
        "OperationId": operation_id,
        "CallAs": call_as,
    }

    store.stack_instancess(stack_set_name, record)

    return {
        "OperationId": record.get("OperationId", {}),
    }
```
