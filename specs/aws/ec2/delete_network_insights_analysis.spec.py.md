---
id: "@specs/aws/ec2/delete_network_insights_analysis"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInsightsAnalysis"
---

# DeleteNetworkInsightsAnalysis

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_insights_analysis
> **spec:implements:** @kind:operation DeleteNetworkInsightsAnalysis
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInsightsAnalysis.spec.md

Deletes the specified network insights analysis.

## Input Shape: DeleteNetworkInsightsAnalysisRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsAnalysisId | Any  # complex shape | ✓ | The ID of the network insights analysis. |

## Output Shape: DeleteNetworkInsightsAnalysisResult

- **NetworkInsightsAnalysisId** (Any  # complex shape): The ID of the network insights analysis.

## Implementation

```speclang
def delete_network_insights_analysis(store, request: dict) -> dict:
    """Deletes the specified network insights analysis."""
    network_insights_analysis_id = request.get("NetworkInsightsAnalysisId", "").strip() if isinstance(request.get("NetworkInsightsAnalysisId"), str) else request.get("NetworkInsightsAnalysisId")

    if not store.network_insights_analysiss(network_insights_analysis_id):
        raise ResourceNotFoundException(f"Resource network_insights_analysis_id not found")
    store.delete_network_insights_analysiss(network_insights_analysis_id)
    return {}
```
