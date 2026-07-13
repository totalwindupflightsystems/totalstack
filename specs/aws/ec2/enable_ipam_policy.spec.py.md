---
id: "@specs/aws/ec2/enable_ipam_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableIpamPolicy"
---

# EnableIpamPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_ipam_policy
> **spec:implements:** @kind:operation EnableIpamPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableIpamPolicy.spec.md

Enables an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations. For more information, see Define public IPv4 allocation strategy with IPAM policies in the Amazon VPC IPAM User Guide .

## Input Shape: EnableIpamPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPolicyId | Any  # complex shape | ✓ | The ID of the IPAM policy to enable. |
| OrganizationTargetId | str |  | The ID of the Amazon Web Services Organizations target for which to enable the IPAM policy. This parameter is required o |

## Output Shape: EnableIpamPolicyResult

- **IpamPolicyId** (Any  # complex shape): The ID of the IPAM policy that was enabled.

## Implementation

```speclang
def enable_ipam_policy(store, request: dict) -> dict:
    """Enables an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services ser"""
    ipam_policy_id = request.get("IpamPolicyId", "").strip() if isinstance(request.get("IpamPolicyId"), str) else request.get("IpamPolicyId")
    if not ipam_policy_id:
        raise ValidationException("IpamPolicyId is required")

    resource = store.enable_ipam_policys(ipam_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_policy_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "OrganizationTargetId" in request:
        resource["OrganizationTargetId"] = organization_target_id

    store.enable_ipam_policys(ipam_policy_id, resource)
    return resource
```
