---
id: "@specs/aws/ec2/modify_instance_metadata_defaults"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceMetadataDefaults"
---

# ModifyInstanceMetadataDefaults

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_metadata_defaults
> **spec:implements:** @kind:operation ModifyInstanceMetadataDefaults
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceMetadataDefaults.spec.md

Modifies the default instance metadata service (IMDS) settings at the account level in the specified Amazon Web Services Region. To remove a parameter's account-level default setting, specify no-preference . If an account-level setting is cleared with no-preference , then the instance launch considers the other instance metadata settings. For more information, see Order of precedence for instance metadata options in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceMetadataDefaultsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| HttpEndpoint | Any  # complex shape |  | Enables or disables the IMDS endpoint on an instance. When disabled, the instance metadata can't be accessed. |
| HttpPutResponseHopLimit | Any  # complex shape |  | The maximum number of hops that the metadata token can travel. To indicate no preference, specify -1 . Possible values:  |
| HttpTokens | Any  # complex shape |  | Indicates whether IMDSv2 is required. optional – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv |
| InstanceMetadataTags | Any  # complex shape |  | Enables or disables access to an instance's tags from the instance metadata. For more information, see View tags for you |

## Output Shape: ModifyInstanceMetadataDefaultsResult

- **Return** (bool): If the request succeeds, the response returns true . If the request fails, no response is returned, and instead an error

## Implementation

```speclang
def modify_instance_metadata_defaults(store, request: dict) -> dict:
    """Modifies the default instance metadata service (IMDS) settings at the account level in the specified Amazon Web Services Region. To remove a parameter's account-level default setting, specify no-prefe"""

```
