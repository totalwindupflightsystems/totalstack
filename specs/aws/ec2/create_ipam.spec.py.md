---
id: "@specs/aws/ec2/create_ipam"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpam"
---

# CreateIpam

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam
> **spec:implements:** @kind:operation CreateIpam
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpam.spec.md

Create an IPAM. Amazon VPC IP Address Manager (IPAM) is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization. For more information, see Create an IPAM in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| Description | str |  | A description for the IPAM. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| EnablePrivateGua | bool |  | Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default. |
| MeteredAccount | Any  # complex shape |  | A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more in |
| OperatingRegions | Any  # complex shape |  | The operating Regions for the IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manag |
| TagSpecifications | list[Any  # complex shape] |  | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the |
| Tier | Any  # complex shape |  | IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and  |

## Output Shape: CreateIpamResult

- **Ipam** (Any  # complex shape): Information about the IPAM created.

## Implementation

```speclang
def create_ipam(store, request: dict) -> dict:
    """Create an IPAM. Amazon VPC IP Address Manager (IPAM) is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP """


    record = {
        "DryRun": dry_run,
        "Description": description,
        "OperatingRegions": operating_regions,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "Tier": tier,
        "EnablePrivateGua": enable_private_gua,
        "MeteredAccount": metered_account,
    }

    store.ipams(record)

    return {
        "Ipam": record.get("Ipam", {}),
    }
```
