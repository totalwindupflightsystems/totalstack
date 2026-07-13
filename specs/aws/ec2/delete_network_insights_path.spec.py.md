---
id: "@specs/aws/ec2/delete_network_insights_path"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInsightsPath"
---

# DeleteNetworkInsightsPath

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_insights_path
> **spec:implements:** @kind:operation DeleteNetworkInsightsPath
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInsightsPath.spec.md

Deletes the specified path.

## Input Shape: DeleteNetworkInsightsPathRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsPathId | Any  # complex shape | ✓ | The ID of the path. |

## Output Shape: DeleteNetworkInsightsPathResult

- **NetworkInsightsPathId** (Any  # complex shape): The ID of the path.

## Implementation

```speclang
def delete_network_insights_path(store, request: dict) -> dict:
    """Deletes the specified path."""
    network_insights_path_id = request.get("NetworkInsightsPathId", "").strip() if isinstance(request.get("NetworkInsightsPathId"), str) else request.get("NetworkInsightsPathId")

    if not store.network_insights_paths(network_insights_path_id):
        raise ResourceNotFoundException(f"Resource network_insights_path_id not found")
    store.delete_network_insights_paths(network_insights_path_id)
    return {}
```
