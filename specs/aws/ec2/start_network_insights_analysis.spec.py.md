---
id: "@specs/aws/ec2/start_network_insights_analysis"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_StartNetworkInsightsAnalysis"
---

# StartNetworkInsightsAnalysis

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/start_network_insights_analysis
> **spec:implements:** @kind:operation StartNetworkInsightsAnalysis
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_StartNetworkInsightsAnalysis.spec.md

Starts analyzing the specified path. If the path is reachable, the operation returns the shortest feasible path.

## Input Shape: StartNetworkInsightsAnalysisRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AdditionalAccounts | list[str] |  | The member accounts that contain resources that the path can traverse. |
| ClientToken | str | ✓ | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FilterInArns | list[str] |  | The Amazon Resource Names (ARN) of the resources that the path must traverse. |
| FilterOutArns | list[str] |  | The Amazon Resource Names (ARN) of the resources that the path will ignore. |
| NetworkInsightsPathId | Any  # complex shape | ✓ | The ID of the path. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply. |

## Output Shape: StartNetworkInsightsAnalysisResult

- **NetworkInsightsAnalysis** (Any  # complex shape): Information about the network insights analysis.

## Implementation

```speclang
def start_network_insights_analysis(store, request: dict) -> dict:
    """Starts analyzing the specified path. If the path is reachable, the operation returns the shortest feasible path."""
    client_token = request.get("ClientToken", "").strip() if isinstance(request.get("ClientToken"), str) else request.get("ClientToken")
    if not client_token:
        raise ValidationException("ClientToken is required")
    network_insights_path_id = request.get("NetworkInsightsPathId", "").strip() if isinstance(request.get("NetworkInsightsPathId"), str) else request.get("NetworkInsightsPathId")
    if not network_insights_path_id:
        raise ValidationException("NetworkInsightsPathId is required")

    if store.network_insights_analysiss(network_insights_path_id):
        raise ResourceInUseException(f"Resource network_insights_path_id already exists")

    record = {
        "NetworkInsightsPathId": network_insights_path_id,
        "AdditionalAccounts": additional_accounts,
        "FilterInArns": filter_in_arns,
        "FilterOutArns": filter_out_arns,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.network_insights_analysiss(network_insights_path_id, record)

    return {
        "NetworkInsightsAnalysis": record.get("NetworkInsightsAnalysis", {}),
    }
```
