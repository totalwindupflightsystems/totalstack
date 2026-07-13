---
id: "@specs/aws/ec2/delete_secondary_network"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSecondaryNetwork"
---

# DeleteSecondaryNetwork

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_secondary_network
> **spec:implements:** @kind:operation DeleteSecondaryNetwork
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSecondaryNetwork.spec.md

Deletes a secondary network. You must delete all secondary subnets in the secondary network before you can delete the secondary network.

## Input Shape: DeleteSecondaryNetworkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SecondaryNetworkId | Any  # complex shape | ✓ | The ID of the secondary network. |

## Output Shape: DeleteSecondaryNetworkResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **SecondaryNetwork** (Any  # complex shape): Information about the secondary network.

## Implementation

```speclang
def delete_secondary_network(store, request: dict) -> dict:
    """Deletes a secondary network. You must delete all secondary subnets in the secondary network before you can delete the secondary network."""
    secondary_network_id = request.get("SecondaryNetworkId", "").strip() if isinstance(request.get("SecondaryNetworkId"), str) else request.get("SecondaryNetworkId")

    if not store.secondary_networks(secondary_network_id):
        raise ResourceNotFoundException(f"Resource secondary_network_id not found")
    store.delete_secondary_networks(secondary_network_id)
    return {}
```
