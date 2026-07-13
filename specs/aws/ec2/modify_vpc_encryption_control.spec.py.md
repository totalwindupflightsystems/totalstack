---
id: "@specs/aws/ec2/modify_vpc_encryption_control"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEncryptionControl"
---

# ModifyVpcEncryptionControl

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_encryption_control
> **spec:implements:** @kind:operation ModifyVpcEncryptionControl
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEncryptionControl.spec.md

Modifies the encryption control configuration for a VPC. You can update the encryption mode and exclusion settings for various gateway types and peering connections. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide .

## Input Shape: ModifyVpcEncryptionControlRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EgressOnlyInternetGatewayExclusion | Any  # complex shape |  | Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement. |
| ElasticFileSystemExclusion | Any  # complex shape |  | Specifies whether to exclude Elastic File System traffic from encryption enforcement. |
| InternetGatewayExclusion | Any  # complex shape |  | Specifies whether to exclude internet gateway traffic from encryption enforcement. |
| LambdaExclusion | Any  # complex shape |  | Specifies whether to exclude Lambda function traffic from encryption enforcement. |
| Mode | Any  # complex shape |  | The encryption mode for the VPC Encryption Control configuration. |
| NatGatewayExclusion | Any  # complex shape |  | Specifies whether to exclude NAT gateway traffic from encryption enforcement. |
| VirtualPrivateGatewayExclusion | Any  # complex shape |  | Specifies whether to exclude virtual private gateway traffic from encryption enforcement. |
| VpcEncryptionControlId | Any  # complex shape | ✓ | The ID of the VPC Encryption Control resource to modify. |
| VpcLatticeExclusion | Any  # complex shape |  | Specifies whether to exclude VPC Lattice traffic from encryption enforcement. |
| VpcPeeringExclusion | Any  # complex shape |  | Specifies whether to exclude VPC peering connection traffic from encryption enforcement. |

## Output Shape: ModifyVpcEncryptionControlResult

- **VpcEncryptionControl** (Any  # complex shape): Information about the VPC Encryption Control configuration.

## Implementation

```speclang
def modify_vpc_encryption_control(store, request: dict) -> dict:
    """Modifies the encryption control configuration for a VPC. You can update the encryption mode and exclusion settings for various gateway types and peering connections. For more information, see Enforce """
    vpc_encryption_control_id = request.get("VpcEncryptionControlId", "").strip() if isinstance(request.get("VpcEncryptionControlId"), str) else request.get("VpcEncryptionControlId")
    if not vpc_encryption_control_id:
        raise ValidationException("VpcEncryptionControlId is required")

    resource = store.vpc_encryption_controls(vpc_encryption_control_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_encryption_control_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Mode" in request:
        resource["Mode"] = mode
    if "InternetGatewayExclusion" in request:
        resource["InternetGatewayExclusion"] = internet_gateway_exclusion
    if "EgressOnlyInternetGatewayExclusion" in request:
        resource["EgressOnlyInternetGatewayExclusion"] = egress_only_internet_gateway_exclusion
    if "NatGatewayExclusion" in request:
        resource["NatGatewayExclusion"] = nat_gateway_exclusion
    if "VirtualPrivateGatewayExclusion" in request:
        resource["VirtualPrivateGatewayExclusion"] = virtual_private_gateway_exclusion
    if "VpcPeeringExclusion" in request:
        resource["VpcPeeringExclusion"] = vpc_peering_exclusion
    if "LambdaExclusion" in request:
        resource["LambdaExclusion"] = lambda_exclusion
    if "VpcLatticeExclusion" in request:
        resource["VpcLatticeExclusion"] = vpc_lattice_exclusion
    if "ElasticFileSystemExclusion" in request:
        resource["ElasticFileSystemExclusion"] = elastic_file_system_exclusion

    store.vpc_encryption_controls(vpc_encryption_control_id, resource)
    return resource
```
