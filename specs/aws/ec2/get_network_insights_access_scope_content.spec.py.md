---
id: "@specs/aws/ec2/get_network_insights_access_scope_content"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetNetworkInsightsAccessScopeContent"
---

# GetNetworkInsightsAccessScopeContent

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_network_insights_access_scope_content
> **spec:implements:** @kind:operation GetNetworkInsightsAccessScopeContent
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetNetworkInsightsAccessScopeContent.spec.md

Gets the content for the specified Network Access Scope.

## Input Shape: GetNetworkInsightsAccessScopeContentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsAccessScopeId | Any  # complex shape | ✓ | The ID of the Network Access Scope. |

## Output Shape: GetNetworkInsightsAccessScopeContentResult

- **NetworkInsightsAccessScopeContent** (Any  # complex shape): The Network Access Scope content.

## Implementation

```speclang
def get_network_insights_access_scope_content(store, request: dict) -> dict:
    """Gets the content for the specified Network Access Scope."""
    network_insights_access_scope_id = request.get("NetworkInsightsAccessScopeId", "").strip() if isinstance(request.get("NetworkInsightsAccessScopeId"), str) else request.get("NetworkInsightsAccessScopeId")
    if not network_insights_access_scope_id:
        raise ValidationException("NetworkInsightsAccessScopeId is required")

    resource = store.network_insights_access_scope_contents(network_insights_access_scope_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_insights_access_scope_id not found")
    return {"NetworkInsightsAccessScopeId": network_insights_access_scope_id, **resource}
```
