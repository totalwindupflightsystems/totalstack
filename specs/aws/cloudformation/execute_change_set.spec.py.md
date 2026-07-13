---
id: "@specs/aws/cloudformation/execute_change_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ExecuteChangeSet"
---

# ExecuteChangeSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/execute_change_set
> **spec:implements:** @kind:operation ExecuteChangeSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ExecuteChangeSet.spec.md

Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the DescribeStacks action to view the status of the update. When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack. If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy. To create a change set for the entire stack hierarchy, IncludeNestedStacks must have been set to True .

## Input Shape: ExecuteChangeSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack. |
| ClientRequestToken | Any  # complex shape |  | A unique identifier for this ExecuteChangeSet request. Specify this token if you plan to retry requests so that CloudFor |
| DisableRollback | Any  # complex shape |  | Preserves the state of previously provisioned resources when an operation fails. This parameter can't be specified when  |
| RetainExceptOnCreate | Any  # complex shape |  | When set to true , newly created resources are deleted when the operation rolls back. This includes newly created resour |
| StackName | Any  # complex shape |  | If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with t |

## Output Shape: ExecuteChangeSetOutput


## Errors
- **InvalidChangeSetStatusException**: The specified change set can't be used to update the stack. For example, the change set status might be CREATE_IN_PROGRESS , or the stack status might be UPDATE_IN_PROGRESS .
- **ChangeSetNotFoundException**: The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the ListChangeSets operation.
- **InsufficientCapabilitiesException**: The template contains resources with capabilities that weren't specified in the Capabilities parameter.
- **TokenAlreadyExistsException**: A client request token already exists.

## Implementation

```speclang
def execute_change_set(store, request: dict) -> dict:
    """Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the Descri"""
    change_set_name = request.get("ChangeSetName", "").strip() if isinstance(request.get("ChangeSetName"), str) else request.get("ChangeSetName")
    if not change_set_name:
        raise ValidationException("ChangeSetName is required")

    resource = store.execute_change_sets(change_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource change_set_name not found")

    # Update mutable fields
    if "StackName" in request:
        resource["StackName"] = stack_name
    if "ClientRequestToken" in request:
        resource["ClientRequestToken"] = client_request_token
    if "DisableRollback" in request:
        resource["DisableRollback"] = disable_rollback
    if "RetainExceptOnCreate" in request:
        resource["RetainExceptOnCreate"] = retain_except_on_create

    store.execute_change_sets(change_set_name, resource)
    return resource
```
