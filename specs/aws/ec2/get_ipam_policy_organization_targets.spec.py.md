---
id: "@specs/aws/ec2/get_ipam_policy_organization_targets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPolicyOrganizationTargets"
---

# GetIpamPolicyOrganizationTargets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_policy_organization_targets
> **spec:implements:** @kind:operation GetIpamPolicyOrganizationTargets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPolicyOrganizationTargets.spec.md

Gets the Amazon Web Services Organizations targets for an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations. A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.

## Input Shape: GetIpamPolicyOrganizationTargetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the Amazon Web Services Organizations targets. |
| IpamPolicyId | Any  # complex shape | ✓ | The ID of the IPAM policy for which to get Amazon Web Services Organizations targets. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPolicyOrganizationTargetsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results.
- **OrganizationTargets** (Any  # complex shape): The IDs of the Amazon Web Services Organizations targets. A target can be an individual Amazon Web Services account or a

## Implementation

```speclang
def get_ipam_policy_organization_targets(store, request: dict) -> dict:
    """Gets the Amazon Web Services Organizations targets for an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resou"""
    ipam_policy_id = request.get("IpamPolicyId", "").strip() if isinstance(request.get("IpamPolicyId"), str) else request.get("IpamPolicyId")
    if not ipam_policy_id:
        raise ValidationException("IpamPolicyId is required")

    resource = store.ipam_policy_organization_targetss(ipam_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_policy_id not found")
    return {"IpamPolicyId": ipam_policy_id, **resource}
```
