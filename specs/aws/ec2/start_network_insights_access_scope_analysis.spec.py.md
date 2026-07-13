---
id: "@specs/aws/ec2/start_network_insights_access_scope_analysis"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StartNetworkInsightsAccessScopeAnalysis"
---

# StartNetworkInsightsAccessScopeAnalysis

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/start_network_insights_access_scope_analysis
> **spec:implements:** @kind:operation StartNetworkInsightsAccessScopeAnalysis
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StartNetworkInsightsAccessScopeAnalysis.spec.md

Starts analyzing the specified Network Access Scope.

## Input Shape: StartNetworkInsightsAccessScopeAnalysisRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str | ✓ | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInsightsAccessScopeId | Any  # complex shape | ✓ | The ID of the Network Access Scope. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply. |

## Output Shape: StartNetworkInsightsAccessScopeAnalysisResult

- **NetworkInsightsAccessScopeAnalysis** (Any  # complex shape): The Network Access Scope analysis.

## Implementation

```speclang
def start_network_insights_access_scope_analysis(store, request: dict) -> dict:
    """Starts analyzing the specified Network Access Scope."""
    client_token = request.get("ClientToken", "").strip() if isinstance(request.get("ClientToken"), str) else request.get("ClientToken")
    if not client_token:
        raise ValidationException("ClientToken is required")
    network_insights_access_scope_id = request.get("NetworkInsightsAccessScopeId", "").strip() if isinstance(request.get("NetworkInsightsAccessScopeId"), str) else request.get("NetworkInsightsAccessScopeId")
    if not network_insights_access_scope_id:
        raise ValidationException("NetworkInsightsAccessScopeId is required")

    if store.network_insights_access_scope_analysiss(network_insights_access_scope_id):
        raise ResourceInUseException(f"Resource network_insights_access_scope_id already exists")

    record = {
        "NetworkInsightsAccessScopeId": network_insights_access_scope_id,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.network_insights_access_scope_analysiss(network_insights_access_scope_id, record)

    return {
        "NetworkInsightsAccessScopeAnalysis": record.get("NetworkInsightsAccessScopeAnalysis", {}),
    }
```
