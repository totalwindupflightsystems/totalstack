---
id: "@specs/aws/ec2/modify_verified_access_instance_logging_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessInstanceLoggingConfiguration"
---

# ModifyVerifiedAccessInstanceLoggingConfiguration

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_instance_logging_configuration
> **spec:implements:** @kind:operation ModifyVerifiedAccessInstanceLoggingConfiguration
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessInstanceLoggingConfiguration.spec.md

Modifies the logging configuration for the specified Amazon Web Services Verified Access instance.

## Input Shape: ModifyVerifiedAccessInstanceLoggingConfigurationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessLogs | Any  # complex shape | ✓ | The configuration options for Verified Access instances. |
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessInstanceId | Any  # complex shape | ✓ | The ID of the Verified Access instance. |

## Output Shape: ModifyVerifiedAccessInstanceLoggingConfigurationResult

- **LoggingConfiguration** (Any  # complex shape): The logging configuration for the Verified Access instance.

## Implementation

```speclang
def modify_verified_access_instance_logging_configuration(store, request: dict) -> dict:
    """Modifies the logging configuration for the specified Amazon Web Services Verified Access instance."""
    access_logs = request.get("AccessLogs", "").strip() if isinstance(request.get("AccessLogs"), str) else request.get("AccessLogs")
    if not access_logs:
        raise ValidationException("AccessLogs is required")
    verified_access_instance_id = request.get("VerifiedAccessInstanceId", "").strip() if isinstance(request.get("VerifiedAccessInstanceId"), str) else request.get("VerifiedAccessInstanceId")
    if not verified_access_instance_id:
        raise ValidationException("VerifiedAccessInstanceId is required")

    resource = store.verified_access_instance_logging_configurations(verified_access_instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_instance_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ClientToken" in request:
        resource["ClientToken"] = client_token

    store.verified_access_instance_logging_configurations(verified_access_instance_id, resource)
    return resource
```
