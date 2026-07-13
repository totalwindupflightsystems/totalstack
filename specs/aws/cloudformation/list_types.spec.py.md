---
id: "@specs/aws/cloudformation/list_types"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListTypes"
---

# ListTypes

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_types
> **spec:implements:** @kind:operation ListTypes
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListTypes.spec.md

Returns summary information about all extensions, including your private resource types, modules, and Hooks as well as all public extensions from Amazon Web Services and third-party publishers.

## Input Shape: ListTypesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DeprecatedStatus | Any  # complex shape |  | The deprecation status of the extension that you want to get summary information about. Valid values include: LIVE : The |
| Filters | Any  # complex shape |  | Filter criteria to use in determining which extensions to return. Filters must be compatible with Visibility to return v |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| ProvisioningType | Any  # complex shape |  | For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type duri |
| Type | Any  # complex shape |  | The type of extension. |
| Visibility | Any  # complex shape |  | The scope at which the extensions are visible and usable in CloudFormation operations. Valid values include: PRIVATE : E |

## Output Shape: ListTypesOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **TypeSummaries** (Any  # complex shape): A list of TypeSummary structures that contain information about the specified extensions.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def list_types(store, request: dict) -> dict:
    """Returns summary information about all extensions, including your private resource types, modules, and Hooks as well as all public extensions from Amazon Web Services and third-party publishers."""

    items = store.list_typess()
    return {"TypeSummaries": list(items.values())}
```
