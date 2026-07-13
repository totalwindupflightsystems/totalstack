---
id: "@specs/aws/ec2/get_instance_tpm_ek_pub"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetInstanceTpmEkPub"
---

# GetInstanceTpmEkPub

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_instance_tpm_ek_pub
> **spec:implements:** @kind:operation GetInstanceTpmEkPub
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetInstanceTpmEkPub.spec.md

Gets the public endorsement key associated with the Nitro Trusted Platform Module (NitroTPM) for the specified instance.

## Input Shape: GetInstanceTpmEkPubRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Specify this parameter to verify whether the request will succeed, without actually making the request. If the request w |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance for which to get the public endorsement key. |
| KeyFormat | Any  # complex shape | ✓ | The required public endorsement key format. Specify der for a DER-encoded public key that is compatible with OpenSSL. Sp |
| KeyType | Any  # complex shape | ✓ | The required public endorsement key type. |

## Output Shape: GetInstanceTpmEkPubResult

- **InstanceId** (Any  # complex shape): The ID of the instance.
- **KeyFormat** (Any  # complex shape): The public endorsement key format.
- **KeyType** (Any  # complex shape): The public endorsement key type.
- **KeyValue** (Any  # complex shape): The public endorsement key material.

## Implementation

```speclang
def get_instance_tpm_ek_pub(store, request: dict) -> dict:
    """Gets the public endorsement key associated with the Nitro Trusted Platform Module (NitroTPM) for the specified instance."""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    key_format = request.get("KeyFormat", "").strip() if isinstance(request.get("KeyFormat"), str) else request.get("KeyFormat")
    if not key_format:
        raise ValidationException("KeyFormat is required")
    key_type = request.get("KeyType", "").strip() if isinstance(request.get("KeyType"), str) else request.get("KeyType")
    if not key_type:
        raise ValidationException("KeyType is required")

    resource = store.instance_tpm_ek_pubs(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")
    return {"InstanceId": instance_id, **resource}
```
