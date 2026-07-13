---
id: "@specs/aws/ec2/restore_address_to_classic"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreAddressToClassic"
---

# RestoreAddressToClassic

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_address_to_classic
> **spec:implements:** @kind:operation RestoreAddressToClassic
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreAddressToClassic.spec.md

This action is deprecated. Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform. You cannot move an Elastic IP address that was originally allocated for use in EC2-VPC. The Elastic IP address must not be associated with an instance or network interface.

## Input Shape: RestoreAddressToClassicRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PublicIp | str | ✓ | The Elastic IP address. |

## Output Shape: RestoreAddressToClassicResult

- **PublicIp** (str): The Elastic IP address.
- **Status** (Any  # complex shape): The move status for the IP address.

## Implementation

```speclang
def restore_address_to_classic(store, request: dict) -> dict:
    """This action is deprecated. Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform. You cannot move an Elastic IP address that was originally """
    public_ip = request.get("PublicIp", "").strip() if isinstance(request.get("PublicIp"), str) else request.get("PublicIp")
    if not public_ip:
        raise ValidationException("PublicIp is required")

    if store.restore_address_to_classics(public_ip):
        raise ResourceInUseException(f"Resource public_ip already exists")

    record = {
        "DryRun": dry_run,
        "PublicIp": public_ip,
    }

    store.restore_address_to_classics(public_ip, record)

    return {
        "PublicIp": public_ip,
        "Status": record.get("Status", {}),
    }
```
