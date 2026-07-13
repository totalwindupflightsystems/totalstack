---
id: "@specs/aws/ec2/delete_network_insights_access_scope_analysis"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInsightsAccessScopeAnalysis"
---

# DeleteNetworkInsightsAccessScopeAnalysis

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_insights_access_scope_analysis
> **spec:implements:** @kind:operation DeleteNetworkInsightsAccessScopeAnalysis
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInsightsAccessScopeAnalysis.spec.md

Deletes the specified Network Access Scope analysis.

## Input Shape: DeleteNetworkInsightsAccessScopeAnalysisRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsAccessScopeAnalysisId | Any  # complex shape | ✓ | The ID of the Network Access Scope analysis. |

## Output Shape: DeleteNetworkInsightsAccessScopeAnalysisResult

- **NetworkInsightsAccessScopeAnalysisId** (Any  # complex shape): The ID of the Network Access Scope analysis.

## Implementation

```speclang
def delete_network_insights_access_scope_analysis(store, request: dict) -> dict:
    """Deletes the specified Network Access Scope analysis."""
    network_insights_access_scope_analysis_id = request.get("NetworkInsightsAccessScopeAnalysisId", "").strip() if isinstance(request.get("NetworkInsightsAccessScopeAnalysisId"), str) else request.get("NetworkInsightsAccessScopeAnalysisId")

    if not store.network_insights_access_scope_analysiss(network_insights_access_scope_analysis_id):
        raise ResourceNotFoundException(f"Resource network_insights_access_scope_analysis_id not found")
    store.delete_network_insights_access_scope_analysiss(network_insights_access_scope_analysis_id)
    return {}
```
