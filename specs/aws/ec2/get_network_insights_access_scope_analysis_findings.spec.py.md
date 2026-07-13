---
id: "@specs/aws/ec2/get_network_insights_access_scope_analysis_findings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetNetworkInsightsAccessScopeAnalysisFindings"
---

# GetNetworkInsightsAccessScopeAnalysisFindings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_network_insights_access_scope_analysis_findings
> **spec:implements:** @kind:operation GetNetworkInsightsAccessScopeAnalysisFindings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetNetworkInsightsAccessScopeAnalysisFindings.spec.md

Gets the findings for the specified Network Access Scope analysis.

## Input Shape: GetNetworkInsightsAccessScopeAnalysisFindingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NetworkInsightsAccessScopeAnalysisId | Any  # complex shape | ✓ | The ID of the Network Access Scope analysis. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetNetworkInsightsAccessScopeAnalysisFindingsResult

- **AnalysisFindings** (list[Any  # complex shape]): The findings associated with Network Access Scope Analysis.
- **AnalysisStatus** (Any  # complex shape): The status of Network Access Scope Analysis.
- **NetworkInsightsAccessScopeAnalysisId** (Any  # complex shape): The ID of the Network Access Scope analysis.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_network_insights_access_scope_analysis_findings(store, request: dict) -> dict:
    """Gets the findings for the specified Network Access Scope analysis."""
    network_insights_access_scope_analysis_id = request.get("NetworkInsightsAccessScopeAnalysisId", "").strip() if isinstance(request.get("NetworkInsightsAccessScopeAnalysisId"), str) else request.get("NetworkInsightsAccessScopeAnalysisId")
    if not network_insights_access_scope_analysis_id:
        raise ValidationException("NetworkInsightsAccessScopeAnalysisId is required")

    resource = store.network_insights_access_scope_analysis_findingss(network_insights_access_scope_analysis_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_insights_access_scope_analysis_id not found")
    return {"NetworkInsightsAccessScopeAnalysisId": network_insights_access_scope_analysis_id, **resource}
```
