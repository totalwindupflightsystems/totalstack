---
id: "@specs/aws/ec2/describe_launch_templates"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLaunchTemplates"
---

# DescribeLaunchTemplates

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_launch_templates
> **spec:implements:** @kind:operation DescribeLaunchTemplates
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLaunchTemplates.spec.md

Describes one or more launch templates.

## Input Shape: DescribeLaunchTemplatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. create-time - The time the launch template was created. launch-template-name - The name of the laun |
| LaunchTemplateIds | list[Any  # complex shape] |  | One or more launch template IDs. |
| LaunchTemplateNames | list[Any  # complex shape] |  | One or more launch template names. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| NextToken | str |  | The token to request the next page of results. |

## Output Shape: DescribeLaunchTemplatesResult

- **LaunchTemplates** (Any  # complex shape): Information about the launch templates.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_launch_templates(store, request: dict) -> dict:
    """Describes one or more launch templates."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
