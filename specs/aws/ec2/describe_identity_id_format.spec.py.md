---
id: "@specs/aws/ec2/describe_identity_id_format"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIdentityIdFormat"
---

# DescribeIdentityIdFormat

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_identity_id_format
> **spec:implements:** @kind:operation DescribeIdentityIdFormat
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIdentityIdFormat.spec.md

Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide . The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway . These settings apply to the principal specified in the request. They do not apply to the principal that makes the request.

## Input Shape: DescribeIdentityIdFormatRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PrincipalArn | str | ✓ | The ARN of the principal, which can be an IAM role, IAM user, or the root user. |
| Resource | str |  | The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-as |

## Output Shape: DescribeIdentityIdFormatResult

- **Statuses** (list[Any  # complex shape]): Information about the ID format for the resources.

## Implementation

```speclang
def describe_identity_id_format(store, request: dict) -> dict:
    """Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only retur"""
    principal_arn = request.get("PrincipalArn", "").strip() if isinstance(request.get("PrincipalArn"), str) else request.get("PrincipalArn")
    if not principal_arn:
        raise ValidationException("PrincipalArn is required")

    resource = store.identity_id_formats(principal_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource principal_arn not found")
    return {"PrincipalArn": principal_arn, **resource}
```
