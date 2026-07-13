---
id: "@specs/aws/ec2/create_network_insights_access_scope"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkInsightsAccessScope"
---

# CreateNetworkInsightsAccessScope

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_insights_access_scope
> **spec:implements:** @kind:operation CreateNetworkInsightsAccessScope
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkInsightsAccessScope.spec.md

Creates a Network Access Scope. Amazon Web Services Network Access Analyzer enables cloud networking and cloud operations teams to verify that their networks on Amazon Web Services conform to their network security and governance objectives. For more information, see the Amazon Web Services Network Access Analyzer Guide .

## Input Shape: CreateNetworkInsightsAccessScopeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str | ✓ | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExcludePaths | Any  # complex shape |  | The paths to exclude. |
| MatchPaths | Any  # complex shape |  | The paths to match. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply. |

## Output Shape: CreateNetworkInsightsAccessScopeResult

- **NetworkInsightsAccessScope** (Any  # complex shape): The Network Access Scope.
- **NetworkInsightsAccessScopeContent** (Any  # complex shape): The Network Access Scope content.

## Implementation

```speclang
def create_network_insights_access_scope(store, request: dict) -> dict:
    """Creates a Network Access Scope. Amazon Web Services Network Access Analyzer enables cloud networking and cloud operations teams to verify that their networks on Amazon Web Services conform to their ne"""
    client_token = request.get("ClientToken", "").strip() if isinstance(request.get("ClientToken"), str) else request.get("ClientToken")
    if not client_token:
        raise ValidationException("ClientToken is required")

    if store.network_insights_access_scopes(client_token):
        raise ResourceInUseException(f"Resource client_token already exists")

    record = {
        "MatchPaths": match_paths,
        "ExcludePaths": exclude_paths,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.network_insights_access_scopes(client_token, record)

    return {
        "NetworkInsightsAccessScope": record.get("NetworkInsightsAccessScope", {}),
        "NetworkInsightsAccessScopeContent": record.get("NetworkInsightsAccessScopeContent", {}),
    }
```
