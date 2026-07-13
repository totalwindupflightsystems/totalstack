---
id: "@specs/aws/ec2/modify_ipam_policy_allocation_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamPolicyAllocationRules"
---

# ModifyIpamPolicyAllocationRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_policy_allocation_rules
> **spec:implements:** @kind:operation ModifyIpamPolicyAllocationRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamPolicyAllocationRules.spec.md

Modifies the allocation rules in an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations. Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

## Input Shape: ModifyIpamPolicyAllocationRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationRules | Any  # complex shape |  | The new allocation rules to apply to the IPAM policy. Allocation rules are optional configurations within an IPAM policy |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPolicyId | Any  # complex shape | ✓ | The ID of the IPAM policy whose allocation rules you want to modify. |
| Locale | str | ✓ | The locale for which to modify the allocation rules. |
| ResourceType | Any  # complex shape | ✓ | The resource type for which to modify the allocation rules. The Amazon Web Services service or resource type that can us |

## Output Shape: ModifyIpamPolicyAllocationRulesResult

- **IpamPolicyDocument** (Any  # complex shape): The modified IPAM policy containing the updated allocation rules.

## Implementation

```speclang
def modify_ipam_policy_allocation_rules(store, request: dict) -> dict:
    """Modifies the allocation rules in an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps a"""
    ipam_policy_id = request.get("IpamPolicyId", "").strip() if isinstance(request.get("IpamPolicyId"), str) else request.get("IpamPolicyId")
    if not ipam_policy_id:
        raise ValidationException("IpamPolicyId is required")
    locale = request.get("Locale", "").strip() if isinstance(request.get("Locale"), str) else request.get("Locale")
    if not locale:
        raise ValidationException("Locale is required")
    resource_type = request.get("ResourceType", "").strip() if isinstance(request.get("ResourceType"), str) else request.get("ResourceType")
    if not resource_type:
        raise ValidationException("ResourceType is required")

    resource = store.ipam_policy_allocation_ruless(ipam_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_policy_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "AllocationRules" in request:
        resource["AllocationRules"] = allocation_rules

    store.ipam_policy_allocation_ruless(ipam_policy_id, resource)
    return resource
```
