---
id: "@specs/aws/ec2/describe_launch_template_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLaunchTemplateVersions"
---

# DescribeLaunchTemplateVersions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_launch_template_versions
> **spec:implements:** @kind:operation DescribeLaunchTemplateVersions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLaunchTemplateVersions.spec.md

Describes one or more versions of a specified launch template. You can describe all versions, individual versions, or a range of versions. You can also describe all the latest versions or all the default versions of all the launch templates in your account.

## Input Shape: DescribeLaunchTemplateVersionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. create-time - The time the launch template version was created. ebs-optimized - A boolean that indi |
| LaunchTemplateId | Any  # complex shape |  | The ID of the launch template. To describe one or more versions of a specified launch template, you must specify either  |
| LaunchTemplateName | Any  # complex shape |  | The name of the launch template. To describe one or more versions of a specified launch template, you must specify eithe |
| MaxResults | int |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| MaxVersion | str |  | The version number up to which to describe launch template versions. |
| MinVersion | str |  | The version number after which to describe launch template versions. |
| NextToken | str |  | The token to request the next page of results. |
| ResolveAlias | bool |  | If true , and if a Systems Manager parameter is specified for ImageId , the AMI ID is displayed in the response for imag |
| Versions | list[str] |  | One or more versions of the launch template. Valid values depend on whether you are describing a specified launch templa |

## Output Shape: DescribeLaunchTemplateVersionsResult

- **LaunchTemplateVersions** (Any  # complex shape): Information about the launch template versions.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_launch_template_versions(store, request: dict) -> dict:
    """Describes one or more versions of a specified launch template. You can describe all versions, individual versions, or a range of versions. You can also describe all the latest versions or all the defa"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
