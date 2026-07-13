---
id: "@specs/aws/ec2/get_instance_metadata_defaults"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetInstanceMetadataDefaults"
---

# GetInstanceMetadataDefaults

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_instance_metadata_defaults
> **spec:implements:** @kind:operation GetInstanceMetadataDefaults
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetInstanceMetadataDefaults.spec.md

Gets the default instance metadata service (IMDS) settings that are set at the account level in the specified Amazon Web Services Region. For more information, see Order of precedence for instance metadata options in the Amazon EC2 User Guide .

## Input Shape: GetInstanceMetadataDefaultsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |

## Output Shape: GetInstanceMetadataDefaultsResult

- **AccountLevel** (Any  # complex shape): The account-level default IMDS settings.

## Implementation

```speclang
def get_instance_metadata_defaults(store, request: dict) -> dict:
    """Gets the default instance metadata service (IMDS) settings that are set at the account level in the specified Amazon Web Services Region. For more information, see Order of precedence for instance met"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
