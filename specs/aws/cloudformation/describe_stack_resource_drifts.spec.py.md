---
id: "@specs/aws/cloudformation/describe_stack_resource_drifts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackResourceDrifts"
---

# DescribeStackResourceDrifts

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_resource_drifts
> **spec:implements:** @kind:operation DescribeStackResourceDrifts
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackResourceDrifts.spec.md

Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift. For a given stack, there will be one StackResourceDrift for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see Resource type support for imports and drift detection . Use DetectStackResourceDrift to detect drift on individual resources, or DetectStackDrift to detect drift on all supported resources for a given stack.

## Input Shape: DescribeStackResourceDriftsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape | ✓ | The name of the stack for which you want drift information. |
| StackResourceDriftStatusFilters | Any  # complex shape |  | The resource drift status values to use as filters for the resource drift results returned. DELETED : The resource diffe |

## Output Shape: DescribeStackResourceDriftsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **StackResourceDrifts** (Any  # complex shape): Drift information for the resources that have been checked for drift in the specified stack. This includes actual and ex

## Implementation

```speclang
def describe_stack_resource_drifts(store, request: dict) -> dict:
    """Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects c"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.stack_resource_driftss(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")
    return {"StackName": stack_name, **resource}
```
