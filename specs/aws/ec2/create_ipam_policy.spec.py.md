---
id: "@specs/aws/ec2/create_ipam_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamPolicy"
---

# CreateIpamPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_policy
> **spec:implements:** @kind:operation CreateIpamPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamPolicy.spec.md

Creates an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations. For more information, see Define public IPv4 allocation strategy with IPAM policies in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier to ensure the idempotency of the request. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM for which you're creating the policy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the IPAM policy. |

## Output Shape: CreateIpamPolicyResult

- **IpamPolicy** (Any  # complex shape): Information about the created IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from I

## Implementation

```speclang
def create_ipam_policy(store, request: dict) -> dict:
    """Creates an IPAM policy. An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services ser"""
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    if store.ipam_policys(ipam_id):
        raise ResourceInUseException(f"Resource ipam_id already exists")

    record = {
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "IpamId": ipam_id,
    }

    store.ipam_policys(ipam_id, record)

    return {
        "IpamPolicy": record.get("IpamPolicy", {}),
    }
```
