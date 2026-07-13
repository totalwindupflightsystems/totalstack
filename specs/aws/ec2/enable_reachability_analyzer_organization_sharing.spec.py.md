---
id: "@specs/aws/ec2/enable_reachability_analyzer_organization_sharing"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableReachabilityAnalyzerOrganizationSharing"
---

# EnableReachabilityAnalyzerOrganizationSharing

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_reachability_analyzer_organization_sharing
> **spec:implements:** @kind:operation EnableReachabilityAnalyzerOrganizationSharing
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableReachabilityAnalyzerOrganizationSharing.spec.md

Establishes a trust relationship between Reachability Analyzer and Organizations. This operation must be performed by the management account for the organization. After you establish a trust relationship, a user in the management account or a delegated administrator account can run a cross-account analysis using resources from the member accounts.

## Input Shape: EnableReachabilityAnalyzerOrganizationSharingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: EnableReachabilityAnalyzerOrganizationSharingResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, returns an error.

## Implementation

```speclang
def enable_reachability_analyzer_organization_sharing(store, request: dict) -> dict:
    """Establishes a trust relationship between Reachability Analyzer and Organizations. This operation must be performed by the management account for the organization. After you establish a trust relations"""

```
