---
id: "@specs/aws/ec2/delete_network_insights_access_scope"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInsightsAccessScope"
---

# DeleteNetworkInsightsAccessScope

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_insights_access_scope
> **spec:implements:** @kind:operation DeleteNetworkInsightsAccessScope
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInsightsAccessScope.spec.md

Deletes the specified Network Access Scope.

## Input Shape: DeleteNetworkInsightsAccessScopeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsAccessScopeId | Any  # complex shape | ✓ | The ID of the Network Access Scope. |

## Output Shape: DeleteNetworkInsightsAccessScopeResult

- **NetworkInsightsAccessScopeId** (Any  # complex shape): The ID of the Network Access Scope.

## Implementation

```speclang
def delete_network_insights_access_scope(store, request: dict) -> dict:
    """Deletes the specified Network Access Scope."""
    network_insights_access_scope_id = request.get("NetworkInsightsAccessScopeId", "").strip() if isinstance(request.get("NetworkInsightsAccessScopeId"), str) else request.get("NetworkInsightsAccessScopeId")

    if not store.network_insights_access_scopes(network_insights_access_scope_id):
        raise ResourceNotFoundException(f"Resource network_insights_access_scope_id not found")
    store.delete_network_insights_access_scopes(network_insights_access_scope_id)
    return {}
```
