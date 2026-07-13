---
id: "@specs/aws/ec2/detach_network_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DetachNetworkInterface"
---

# DetachNetworkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/detach_network_interface
> **spec:implements:** @kind:operation DetachNetworkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DetachNetworkInterface.spec.md

Detaches a network interface from an instance.

## Input Shape: DetachNetworkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Force | bool |  | Specifies whether to force a detachment. Use the Force parameter only as a last resort to detach a network interface fro |

## Implementation

```speclang
def detach_network_interface(store, request: dict) -> dict:
    """Detaches a network interface from an instance."""
    attachment_id = request.get("AttachmentId", "").strip() if isinstance(request.get("AttachmentId"), str) else request.get("AttachmentId")
    if not attachment_id:
        raise ValidationException("AttachmentId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachNetworkInterface", request)
```
