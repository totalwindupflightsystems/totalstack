---
id: "@specs/aws/cloudformation/describe_change_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeChangeSet"
---

# DescribeChangeSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_change_set
> **spec:implements:** @kind:operation DescribeChangeSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeChangeSet.spec.md

Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see Update CloudFormation stacks using change sets in the CloudFormation User Guide .

## Input Shape: DescribeChangeSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the change set that you want to describe. |
| IncludePropertyValues | Any  # complex shape |  | If true , the returned changes include detailed changes in the property values. |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape |  | If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe. |

## Output Shape: DescribeChangeSetOutput

- **Capabilities** (Any  # complex shape): If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was create
- **ChangeSetId** (Any  # complex shape): The Amazon Resource Name (ARN) of the change set.
- **ChangeSetName** (Any  # complex shape): The name of the change set.
- **Changes** (Any  # complex shape): A list of Change structures that describes the resources CloudFormation changes if you execute the change set.
- **CreationTime** (Any  # complex shape): The start time when the change set was created, in UTC.
- **DeploymentMode** (Any  # complex shape): The deployment mode specified when the change set was created. Valid value is REVERT_DRIFT . Only present for drift-awar
- **Description** (Any  # complex shape): Information about the change set.
- **ExecutionStatus** (Any  # complex shape): If the change set execution status is AVAILABLE , you can execute the change set. If you can't execute the change set, t
- **ImportExistingResources** (Any  # complex shape): Indicates if the change set imports resources that already exist. This parameter can only import resources that have cus
- **IncludeNestedStacks** (Any  # complex shape): Verifies if IncludeNestedStacks is set to True .
- **NextToken** (Any  # complex shape): If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this valu
- **NotificationARNs** (Any  # complex shape): The ARNs of the Amazon SNS topics that will be associated with the stack if you execute the change set.
- **OnStackFailure** (Any  # complex shape): Determines what action will be taken if stack creation fails. When this parameter is specified, the DisableRollback para
- **Parameters** (Any  # complex shape): A list of Parameter structures that describes the input parameters and their values used to create the change set. For m
- **ParentChangeSetId** (Any  # complex shape): Specifies the change set ID of the parent change set in the current nested change set hierarchy.
- **RollbackConfiguration** (Any  # complex shape): The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified
- **RootChangeSetId** (Any  # complex shape): Specifies the change set ID of the root change set in the current nested change set hierarchy.
- **StackDriftStatus** (Any  # complex shape): The drift status of the stack when the change set was created. Valid values: DRIFTED – The stack has drifted from its la
- **StackId** (Any  # complex shape): The Amazon Resource Name (ARN) of the stack that's associated with the change set.
- **StackName** (Any  # complex shape): The name of the stack that's associated with the change set.
- **Status** (Any  # complex shape): The current status of the change set, such as CREATE_PENDING , CREATE_COMPLETE , or FAILED .
- **StatusReason** (Any  # complex shape): A description of the change set's status. For example, if your attempt to create a change set failed, CloudFormation sho
- **Tags** (Any  # complex shape): If you execute the change set, the tags that will be associated with the stack.

## Errors
- **ChangeSetNotFoundException**: The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the ListChangeSets operation.

## Implementation

```speclang
def describe_change_set(store, request: dict) -> dict:
    """Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see Update CloudFormation stacks using change sets in the"""
    change_set_name = request.get("ChangeSetName", "").strip() if isinstance(request.get("ChangeSetName"), str) else request.get("ChangeSetName")
    if not change_set_name:
        raise ValidationException("ChangeSetName is required")

    resource = store.change_sets(change_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource change_set_name not found")
    return {"ChangeSetName": change_set_name, **resource}
```
