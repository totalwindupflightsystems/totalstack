---
id: "@specs/aws/cloudformation/describe_events"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeEvents"
---

# DescribeEvents

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_events
> **spec:implements:** @kind:operation DescribeEvents
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeEvents.spec.md

Returns CloudFormation events based on flexible query criteria. Groups events by operation ID, enabling you to focus on individual stack operations during deployment. An operation is any action performed on a stack, including stack lifecycle actions (Create, Update, Delete, Rollback), change set creation, nested stack creation, and automatic rollbacks triggered by failures. Each operation has a unique identifier (Operation ID) and represents a discrete change attempt on the stack. Returns different types of events including: Progress events - Status updates during stack operation execution. Validation errors - Failures from CloudFormation Early Validations. Provisioning errors - Resource creation and update failures. Hook invocation errors - Failures from CloudFormation Hook during stack operations. One of ChangeSetName , OperationId or StackName must be specified as input.

## Input Shape: DescribeEventsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape |  | The name or Amazon Resource Name (ARN) of the change set for which you want to retrieve events. |
| Filters | Any  # complex shape |  | Filters to apply when retrieving events. |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| OperationId | Any  # complex shape |  | The unique identifier of the operation for which you want to retrieve events. |
| StackName | Any  # complex shape |  | The name or unique stack ID for which you want to retrieve events. |

## Output Shape: DescribeEventsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **OperationEvents** (Any  # complex shape): A list of operation events that match the specified criteria.

## Implementation

```speclang
def describe_events(store, request: dict) -> dict:
    """Returns CloudFormation events based on flexible query criteria. Groups events by operation ID, enabling you to focus on individual stack operations during deployment. An operation is any action perfor"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
