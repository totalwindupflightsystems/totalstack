---
id: "@specs/aws/ec2/modify_instance_metadata_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceMetadataOptions"
---

# ModifyInstanceMetadataOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_metadata_options
> **spec:implements:** @kind:operation ModifyInstanceMetadataOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceMetadataOptions.spec.md

Modify the instance metadata parameters on a running or stopped instance. When you modify the parameters on a stopped instance, they are applied when the instance is started. When you modify the parameters on a running instance, the API responds with a state of “pending”. After the parameter modifications are successfully applied to the instance, the state of the modifications changes from “pending” to “applied” in subsequent describe-instances API calls. For more information, see Instance metadata and user data in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceMetadataOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| HttpEndpoint | Any  # complex shape |  | Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state |
| HttpProtocolIpv6 | Any  # complex shape |  | Enables or disables the IPv6 endpoint for the instance metadata service. Applies only if you enabled the HTTP metadata e |
| HttpPutResponseHopLimit | int |  | The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance meta |
| HttpTokens | Any  # complex shape |  | Indicates whether IMDSv2 is required. optional - IMDSv2 is optional. You can choose whether to send a session token in y |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| InstanceMetadataTags | Any  # complex shape |  | Set to enabled to allow access to instance tags from the instance metadata. Set to disabled to turn off access to instan |

## Output Shape: ModifyInstanceMetadataOptionsResult

- **InstanceId** (str): The ID of the instance.
- **InstanceMetadataOptions** (Any  # complex shape): The metadata options for the instance.

## Implementation

```speclang
def modify_instance_metadata_options(store, request: dict) -> dict:
    """Modify the instance metadata parameters on a running or stopped instance. When you modify the parameters on a stopped instance, they are applied when the instance is started. When you modify the param"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_metadata_optionss(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "HttpTokens" in request:
        resource["HttpTokens"] = http_tokens
    if "HttpPutResponseHopLimit" in request:
        resource["HttpPutResponseHopLimit"] = http_put_response_hop_limit
    if "HttpEndpoint" in request:
        resource["HttpEndpoint"] = http_endpoint
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "HttpProtocolIpv6" in request:
        resource["HttpProtocolIpv6"] = http_protocol_ipv6
    if "InstanceMetadataTags" in request:
        resource["InstanceMetadataTags"] = instance_metadata_tags

    store.instance_metadata_optionss(instance_id, resource)
    return resource
```
