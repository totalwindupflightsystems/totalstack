---
id: "@specs/aws/ec2/modify_private_dns_name_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyPrivateDnsNameOptions"
---

# ModifyPrivateDnsNameOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_private_dns_name_options
> **spec:implements:** @kind:operation ModifyPrivateDnsNameOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyPrivateDnsNameOptions.spec.md

Modifies the options for instance hostnames for the specified instance.

## Input Shape: ModifyPrivateDnsNameOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EnableResourceNameDnsAAAARecord | bool |  | Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. |
| EnableResourceNameDnsARecord | bool |  | Indicates whether to respond to DNS queries for instance hostnames with DNS A records. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| PrivateDnsHostnameType | Any  # complex shape |  | The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 a |

## Output Shape: ModifyPrivateDnsNameOptionsResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_private_dns_name_options(store, request: dict) -> dict:
    """Modifies the options for instance hostnames for the specified instance."""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.private_dns_name_optionss(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "PrivateDnsHostnameType" in request:
        resource["PrivateDnsHostnameType"] = private_dns_hostname_type
    if "EnableResourceNameDnsARecord" in request:
        resource["EnableResourceNameDnsARecord"] = enable_resource_name_dns_a_record
    if "EnableResourceNameDnsAAAARecord" in request:
        resource["EnableResourceNameDnsAAAARecord"] = enable_resource_name_dns_aaaa_record

    store.private_dns_name_optionss(instance_id, resource)
    return resource
```
