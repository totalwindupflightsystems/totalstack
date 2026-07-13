---
id: "@specs/aws/cloudformation/list_type_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListTypeVersions"
---

# ListTypeVersions

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_type_versions
> **spec:implements:** @kind:operation ListTypeVersions
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListTypeVersions.spec.md

Returns summary information about the versions of an extension.

## Input Shape: ListTypeVersionsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension for which you want version summary information. Conditional: You must sp |
| DeprecatedStatus | Any  # complex shape |  | The deprecation status of the extension versions that you want to get summary information about. Valid values include: L |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| PublisherId | Any  # complex shape |  | The publisher ID of the extension publisher. Extensions published by Amazon aren't assigned a publisher ID. |
| Type | Any  # complex shape |  | The kind of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeName | Any  # complex shape |  | The name of the extension for which you want version summary information. Conditional: You must specify either TypeName  |

## Output Shape: ListTypeVersionsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all of the remaining results, NextToken is set to a token. To retrieve the next set of res
- **TypeVersionSummaries** (Any  # complex shape): A list of TypeVersionSummary structures that contain information about the specified extension's versions.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def list_type_versions(store, request: dict) -> dict:
    """Returns summary information about the versions of an extension."""

    items = store.list_type_versionss()
    return {"TypeVersionSummaries": list(items.values())}
```
