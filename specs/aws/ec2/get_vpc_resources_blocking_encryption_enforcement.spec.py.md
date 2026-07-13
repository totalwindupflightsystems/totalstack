---
id: "@specs/aws/ec2/get_vpc_resources_blocking_encryption_enforcement"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVpcResourcesBlockingEncryptionEnforcement"
---

# GetVpcResourcesBlockingEncryptionEnforcement

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_vpc_resources_blocking_encryption_enforcement
> **spec:implements:** @kind:operation GetVpcResourcesBlockingEncryptionEnforcement
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVpcResourcesBlockingEncryptionEnforcement.spec.md

Gets information about resources in a VPC that are blocking encryption enforcement. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide .

## Input Shape: GetVpcResourcesBlockingEncryptionEnforcementRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC to check for resources blocking encryption enforcement. |

## Output Shape: GetVpcResourcesBlockingEncryptionEnforcementResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **NonCompliantResources** (list[Any  # complex shape]): Information about resources that are blocking encryption enforcement.

## Implementation

```speclang
def get_vpc_resources_blocking_encryption_enforcement(store, request: dict) -> dict:
    """Gets information about resources in a VPC that are blocking encryption enforcement. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide ."""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.vpc_resources_blocking_encryption_enforcements(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")
    return {"VpcId": vpc_id, **resource}
```
