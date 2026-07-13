---
id: "@specs/aws/cloudformation/update_stack_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_UpdateStackInstances"
---

# UpdateStackInstances

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/update_stack_instances
> **spec:implements:** @kind:operation UpdateStackInstances
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_UpdateStackInstances.spec.md

Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use CreateStackInstances . During StackSet updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value. You can only update the parameter values that are specified in the StackSet. To add or delete a parameter itself, use UpdateStackSet to update the StackSet template. If you add a parameter to a template, before you can override the parameter value specified in the StackSet you must first use UpdateStackSet to update all stack instances with the updated template and parameter value specified in the StackSet. Once a stack instance has been updated with the new parameter, you can then override the parameter value using UpdateStackInstances . The maximum number of organizational unit (OUs) supported by a UpdateStackInstances operation is 50. If you need more than 50, consider the following options: Batch processing: If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each. Parent OU strategy: If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.

## Input Shape: UpdateStackInstancesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Accounts | list[Any  # complex shape] |  | [Self-managed permissions] The account IDs of one or more Amazon Web Services accounts in which you want to update param |
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| DeploymentTargets | Any  # complex shape |  | [Service-managed permissions] The Organizations accounts in which you want to update parameter values for stack instance |
| OperationId | Any  # complex shape |  | The unique identifier for this StackSet operation. The operation ID also functions as an idempotency token, to ensure th |
| OperationPreferences | Any  # complex shape |  | Preferences for how CloudFormation performs this StackSet operation. |
| ParameterOverrides | Any  # complex shape |  | A list of input parameters whose values you want to update for the specified stack instances. Any overridden parameter v |
| Regions | list[Any  # complex shape] | ✓ | The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. T |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet associated with the stack instances. |

## Output Shape: UpdateStackInstancesOutput

- **OperationId** (Any  # complex shape): The unique identifier for this StackSet operation.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **StackInstanceNotFoundException**: The specified stack instance doesn't exist.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **OperationIdAlreadyExistsException**: The specified operation ID already exists.
- **StaleRequestException**: Another operation has been performed on this StackSet since the specified operation was performed.
- **InvalidOperationException**: The specified operation isn't valid.

## Implementation

```speclang
def update_stack_instances(store, request: dict) -> dict:
    """Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You """
    regions = request.get("Regions", "").strip() if isinstance(request.get("Regions"), str) else request.get("Regions")
    if not regions:
        raise ValidationException("Regions is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_instancess(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")

    # Update mutable fields
    if "Accounts" in request:
        resource["Accounts"] = accounts
    if "DeploymentTargets" in request:
        resource["DeploymentTargets"] = deployment_targets
    if "ParameterOverrides" in request:
        resource["ParameterOverrides"] = parameter_overrides
    if "OperationPreferences" in request:
        resource["OperationPreferences"] = operation_preferences
    if "OperationId" in request:
        resource["OperationId"] = operation_id
    if "CallAs" in request:
        resource["CallAs"] = call_as

    store.stack_instancess(stack_set_name, resource)
    return resource
```
