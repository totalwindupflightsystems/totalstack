---
id: "@specs/aws/cloudformation/describe_stack_resources"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackResources"
---

# DescribeStackResources

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_resources
> **spec:implements:** @kind:operation DescribeStackResources
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackResources.spec.md

Returns Amazon Web Services resource descriptions for running and deleted stacks. If StackName is specified, all the associated resources that are part of the stack are returned. If PhysicalResourceId is specified, the associated resources of the stack that the resource belongs to are returned. Only the first 100 resources will be returned. If your stack has more resources than this, you should use ListStackResources instead. For deleted stacks, DescribeStackResources returns resource information for up to 90 days after the stack has been deleted. You must specify either StackName or PhysicalResourceId , but not both. In addition, you can specify LogicalResourceId to filter the returned result. For more information about resources, the LogicalResourceId and PhysicalResourceId , see the CloudFormation User Guide . A ValidationError is returned if you specify both StackName and PhysicalResourceId in the same request.

## Input Shape: DescribeStackResourcesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LogicalResourceId | Any  # complex shape |  | The logical name of the resource as specified in the template. |
| PhysicalResourceId | Any  # complex shape |  | The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation. For  |
| StackName | Any  # complex shape |  | The name or the unique stack ID that is associated with the stack, which aren't always interchangeable: Running stacks:  |

## Output Shape: DescribeStackResourcesOutput

- **StackResources** (Any  # complex shape): A list of StackResource structures.

## Implementation

```speclang
def describe_stack_resources(store, request: dict) -> dict:
    """Returns Amazon Web Services resource descriptions for running and deleted stacks. If StackName is specified, all the associated resources that are part of the stack are returned. If PhysicalResourceId"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
