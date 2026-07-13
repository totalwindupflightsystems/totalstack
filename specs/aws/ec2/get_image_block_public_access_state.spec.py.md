---
id: "@specs/aws/ec2/get_image_block_public_access_state"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetImageBlockPublicAccessState"
---

# GetImageBlockPublicAccessState

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_image_block_public_access_state
> **spec:implements:** @kind:operation GetImageBlockPublicAccessState
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetImageBlockPublicAccessState.spec.md

Gets the current state of block public access for AMIs at the account level in the specified Amazon Web Services Region. For more information, see Block public access to your AMIs in the Amazon EC2 User Guide .

## Input Shape: GetImageBlockPublicAccessStateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetImageBlockPublicAccessStateResult

- **ImageBlockPublicAccessState** (str): The current state of block public access for AMIs at the account level in the specified Amazon Web Services Region. Poss
- **ManagedBy** (Any  # complex shape): The entity that manages the state for block public access for AMIs. Possible values include: account - The state is mana

## Implementation

```speclang
def get_image_block_public_access_state(store, request: dict) -> dict:
    """Gets the current state of block public access for AMIs at the account level in the specified Amazon Web Services Region. For more information, see Block public access to your AMIs in the Amazon EC2 Us"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
