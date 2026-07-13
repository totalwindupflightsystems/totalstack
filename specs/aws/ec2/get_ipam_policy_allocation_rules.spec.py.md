---
id: "@specs/aws/ec2/get_ipam_policy_allocation_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPolicyAllocationRules"
---

# GetIpamPolicyAllocationRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_policy_allocation_rules
> **spec:implements:** @kind:operation GetIpamPolicyAllocationRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPolicyAllocationRules.spec.md

Gets the allocation rules for an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations. Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

## Input Shape: GetIpamPolicyAllocationRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the allocation rules. |
| IpamPolicyId | Any  # complex shape | ✓ | The ID of the IPAM policy for which to get allocation rules. |
| Locale | str |  | The locale for which to get the allocation rules. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| ResourceType | Any  # complex shape |  | The resource type for which to get the allocation rules. The Amazon Web Services service or resource type that can use I |

## Output Shape: GetIpamPolicyAllocationRulesResult

- **IpamPolicyDocuments** (Any  # complex shape): The IPAM policy documents containing the allocation rules. Allocation rules are optional configurations within an IPAM p
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results.

## Implementation

```speclang
def get_ipam_policy_allocation_rules(store, request: dict) -> dict:
    """Gets the allocation rules for an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an A"""
    ipam_policy_id = request.get("IpamPolicyId", "").strip() if isinstance(request.get("IpamPolicyId"), str) else request.get("IpamPolicyId")
    if not ipam_policy_id:
        raise ValidationException("IpamPolicyId is required")

    resource = store.ipam_policy_allocation_ruless(ipam_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_policy_id not found")
    return {"IpamPolicyId": ipam_policy_id, **resource}
```
