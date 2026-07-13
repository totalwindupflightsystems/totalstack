---
id: "@specs/aws/cloudformation/delete_stack_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeleteStackInstances"
---

# DeleteStackInstances

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/delete_stack_instances
> **spec:implements:** @kind:operation DeleteStackInstances
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeleteStackInstances.spec.md

Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions. The maximum number of organizational unit (OUs) supported by a DeleteStackInstances operation is 50. If you need more than 50, consider the following options: Batch processing: If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each. Parent OU strategy: If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.

## Input Shape: DeleteStackInstancesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Accounts | list[Any  # complex shape] |  | [Self-managed permissions] The account IDs of the Amazon Web Services accounts that you want to delete stack instances f |
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| DeploymentTargets | Any  # complex shape |  | [Service-managed permissions] The Organizations accounts from which to delete stack instances. You can specify Accounts  |
| OperationId | Any  # complex shape |  | The unique identifier for this StackSet operation. If you don't specify an operation ID, the SDK generates one automatic |
| OperationPreferences | Any  # complex shape |  | Preferences for how CloudFormation performs this StackSet operation. |
| Regions | list[Any  # complex shape] | ✓ | The Amazon Web Services Regions where you want to delete StackSet instances. |
| RetainStacks | Any  # complex shape | ✓ | Removes the stack instances from the specified StackSet, but doesn't delete the stacks. You can't reassociate a retained |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to delete stack instances for. |

## Output Shape: DeleteStackInstancesOutput

- **OperationId** (Any  # complex shape): The unique identifier for this StackSet operation.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **OperationIdAlreadyExistsException**: The specified operation ID already exists.
- **StaleRequestException**: Another operation has been performed on this StackSet since the specified operation was performed.
- **InvalidOperationException**: The specified operation isn't valid.

## Implementation

```speclang
def delete_stack_instances(store, request: dict) -> dict:
    """Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions. The maximum number of organizational unit (OUs) supported by a DeleteStackInstances operation is 50. I"""
    regions = request.get("Regions", "").strip() if isinstance(request.get("Regions"), str) else request.get("Regions")
    retain_stacks = request.get("RetainStacks", "").strip() if isinstance(request.get("RetainStacks"), str) else request.get("RetainStacks")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")

    if not store.stack_instancess(stack_set_name):
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    store.delete_stack_instancess(stack_set_name)
    return {}
```
