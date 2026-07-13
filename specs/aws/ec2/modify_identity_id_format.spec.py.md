---
id: "@specs/aws/ec2/modify_identity_id_format"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIdentityIdFormat"
---

# ModifyIdentityIdFormat

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_identity_id_format
> **spec:implements:** @kind:operation ModifyIdentityIdFormat
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIdentityIdFormat.spec.md

Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources should receive longer IDs (17-character IDs) when they are created. This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway . For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide . This setting applies to the principal specified in the request; it does not apply to the principal that makes the request. Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.

## Input Shape: ModifyIdentityIdFormatRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PrincipalArn | str | ✓ | The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for  |
| Resource | str | ✓ | The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-as |
| UseLongIds | bool | ✓ | Indicates whether the resource should use longer IDs (17-character IDs) |

## Implementation

```speclang
def modify_identity_id_format(store, request: dict) -> dict:
    """Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources """
    principal_arn = request.get("PrincipalArn", "").strip() if isinstance(request.get("PrincipalArn"), str) else request.get("PrincipalArn")
    if not principal_arn:
        raise ValidationException("PrincipalArn is required")
    resource = request.get("Resource", "").strip() if isinstance(request.get("Resource"), str) else request.get("Resource")
    if not resource:
        raise ValidationException("Resource is required")
    use_long_ids = request.get("UseLongIds", "").strip() if isinstance(request.get("UseLongIds"), str) else request.get("UseLongIds")
    if not use_long_ids:
        raise ValidationException("UseLongIds is required")

    resource = store.identity_id_formats(use_long_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource use_long_ids not found")

    # Update mutable fields

    store.identity_id_formats(use_long_ids, resource)
    return resource
```
