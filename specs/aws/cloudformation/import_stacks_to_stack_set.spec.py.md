---
id: "@specs/aws/cloudformation/import_stacks_to_stack_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ImportStacksToStackSet"
---

# ImportStacksToStackSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/import_stacks_to_stack_set
> **spec:implements:** @kind:operation ImportStacksToStackSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ImportStacksToStackSet.spec.md

Import existing stacks into a new StackSets. Use the stack import operation to import up to 10 stacks into a new StackSet in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.

## Input Shape: ImportStacksToStackSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | By default, SELF is specified. Use SELF for StackSets with self-managed permissions. If you are signed in to the managem |
| OperationId | Any  # complex shape |  | A unique, user defined, identifier for the StackSet operation. |
| OperationPreferences | Any  # complex shape |  | The user-specified preferences for how CloudFormation performs a StackSet operation. For more information about maximum  |
| OrganizationalUnitIds | list[Any  # complex shape] |  | The list of OU ID's to which the imported stacks must be mapped as deployment targets. |
| StackIds | list[Any  # complex shape] |  | The IDs of the stacks you are importing into a StackSet. You import up to 10 stacks per StackSet at a time. Specify eith |
| StackIdsUrl | Any  # complex shape |  | The Amazon S3 URL which contains list of stack ids to be inputted. Specify either StackIds or StackIdsUrl . |
| StackSetName | Any  # complex shape | ✓ | The name of the StackSet. The name must be unique in the Region where you create your StackSet. |

## Output Shape: ImportStacksToStackSetOutput

- **OperationId** (Any  # complex shape): The unique identifier for the StackSet operation.

## Errors
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **InvalidOperationException**: The specified operation isn't valid.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **OperationIdAlreadyExistsException**: The specified operation ID already exists.
- **StackNotFoundException**: The specified stack ARN doesn't exist or stack doesn't exist corresponding to the ARN in input.
- **StaleRequestException**: Another operation has been performed on this StackSet since the specified operation was performed.

## Implementation

```speclang
def import_stacks_to_stack_set(store, request: dict) -> dict:
    """Import existing stacks into a new StackSets. Use the stack import operation to import up to 10 stacks into a new StackSet in the same account as the source stack or in a different administrator accoun"""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.import_stacks_to_stack_sets(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")

    # Update mutable fields
    if "StackIds" in request:
        resource["StackIds"] = stack_ids
    if "StackIdsUrl" in request:
        resource["StackIdsUrl"] = stack_ids_url
    if "OrganizationalUnitIds" in request:
        resource["OrganizationalUnitIds"] = organizational_unit_ids
    if "OperationPreferences" in request:
        resource["OperationPreferences"] = operation_preferences
    if "OperationId" in request:
        resource["OperationId"] = operation_id
    if "CallAs" in request:
        resource["CallAs"] = call_as

    store.import_stacks_to_stack_sets(stack_set_name, resource)
    return resource
```
