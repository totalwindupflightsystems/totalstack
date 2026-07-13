---
id: "@specs/aws/ec2/create_ipam_prefix_list_resolver"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamPrefixListResolver"
---

# CreateIpamPrefixListResolver

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_prefix_list_resolver
> **spec:implements:** @kind:operation CreateIpamPrefixListResolver
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamPrefixListResolver.spec.md

Creates an IPAM prefix list resolver. An IPAM prefix list resolver is a component that manages the synchronization between IPAM's CIDR selection rules and customer-managed prefix lists. It automates connectivity configurations by selecting CIDRs from IPAM's database based on your business logic and synchronizing them with prefix lists used in resources such as VPC route tables and security groups. For more information about IPAM prefix list resolver, see Automate prefix list updates with IPAM in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamPrefixListResolverRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddressFamily | Any  # complex shape | ✓ | The address family for the IPAM prefix list resolver. Valid values are ipv4 and ipv6 . You must create separate resolver |
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| Description | str |  | A description for the IPAM prefix list resolver to help you identify its purpose and configuration. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM that will serve as the source of the IP address database for CIDR selection. The IPAM must be in the  |
| Rules | Any  # complex shape |  | The CIDR selection rules for the resolver. CIDR selection rules define the business logic for selecting CIDRs from IPAM. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the IPAM prefix list resolver during creation. Tags help you organize and manage your Amazon Web Se |

## Output Shape: CreateIpamPrefixListResolverResult

- **IpamPrefixListResolver** (Any  # complex shape): Information about the IPAM prefix list resolver that was created.

## Implementation

```speclang
def create_ipam_prefix_list_resolver(store, request: dict) -> dict:
    """Creates an IPAM prefix list resolver. An IPAM prefix list resolver is a component that manages the synchronization between IPAM's CIDR selection rules and customer-managed prefix lists. It automates c"""
    address_family = request.get("AddressFamily", "").strip() if isinstance(request.get("AddressFamily"), str) else request.get("AddressFamily")
    if not address_family:
        raise ValidationException("AddressFamily is required")
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    if store.ipam_prefix_list_resolvers(ipam_id):
        raise ResourceInUseException(f"Resource ipam_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamId": ipam_id,
        "Description": description,
        "AddressFamily": address_family,
        "Rules": rules,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.ipam_prefix_list_resolvers(ipam_id, record)

    return {
        "IpamPrefixListResolver": record.get("IpamPrefixListResolver", {}),
    }
```
