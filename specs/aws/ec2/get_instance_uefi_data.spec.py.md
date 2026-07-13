---
id: "@specs/aws/ec2/get_instance_uefi_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetInstanceUefiData"
---

# GetInstanceUefiData

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_instance_uefi_data
> **spec:implements:** @kind:operation GetInstanceUefiData
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetInstanceUefiData.spec.md

A binary representation of the UEFI variable store. Only non-volatile variables are stored. This is a base64 encoded and zlib compressed binary value that must be properly encoded. When you use register-image to create an AMI, you can create an exact copy of your variable store by passing the UEFI data in the UefiData parameter. You can modify the UEFI data by using the python-uefivars tool on GitHub. You can use the tool to convert the UEFI data into a human-readable format (JSON), which you can inspect and modify, and then convert back into the binary format to use with register-image. For more information, see UEFI Secure Boot in the Amazon EC2 User Guide .

## Input Shape: GetInstanceUefiDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance from which to retrieve the UEFI data. |

## Output Shape: GetInstanceUefiDataResult

- **InstanceId** (Any  # complex shape): The ID of the instance from which to retrieve the UEFI data.
- **UefiData** (str): Base64 representation of the non-volatile UEFI variable store.

## Implementation

```speclang
def get_instance_uefi_data(store, request: dict) -> dict:
    """A binary representation of the UEFI variable store. Only non-volatile variables are stored. This is a base64 encoded and zlib compressed binary value that must be properly encoded. When you use regist"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_uefi_datas(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")
    return {"InstanceId": instance_id, **resource}
```
