---
id: "@specs/aws/ec2/create_mac_system_integrity_protection_modification_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateMacSystemIntegrityProtectionModificationTask"
---

# CreateMacSystemIntegrityProtectionModificationTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_mac_system_integrity_protection_modification_task
> **spec:implements:** @kind:operation CreateMacSystemIntegrityProtectionModificationTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateMacSystemIntegrityProtectionModificationTask.spec.md

Creates a System Integrity Protection (SIP) modification task to configure the SIP settings for an x86 Mac instance or Apple silicon Mac instance. For more information, see Configure SIP for Amazon EC2 instances in the Amazon EC2 User Guide . When you configure the SIP settings for your instance, you can either enable or disable all SIP settings, or you can specify a custom SIP configuration that selectively enables or disables specific SIP settings. If you implement a custom configuration, connect to the instance and verify the settings to ensure that your requirements are properly implemented and functioning as intended. SIP configurations might change with macOS updates. We recommend that you review custom SIP settings after any macOS version upgrade to ensure continued compatibility and proper functionality of your security configurations. To enable or disable all SIP settings, use the MacSystemIntegrityProtectionStatus parameter only. For example, to enable all SIP settings, specify the following: MacSystemIntegrityProtectionStatus=enabled To specify a custom configuration that selectively enables or disables specific SIP settings, use the MacSystemIntegrityProtectionStatus parameter to enable or disable all SIP settings, and then use the MacSystemIntegrityProtectionConfiguration parameter to specify exceptions. In this case, the exceptions you specify for MacSystemIntegrityProtectionConfiguration override the value you specify for MacSystemIntegrityProtectionStatus . For example, to enable all SIP settings, except NvramProtections , specify the following: MacSystemIntegrityProtectionStatus=enabled MacSystemIntegrityProtectionConfigurationRequest "NvramProtections=disabled"

## Input Shape: CreateMacSystemIntegrityProtectionModificationTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the Amazon EC2 Mac instance. |
| MacCredentials | Any  # complex shape |  | [Apple silicon Mac instances only] Specifies the following credentials: Internal disk administrative user Username - Onl |
| MacSystemIntegrityProtectionConfiguration | Any  # complex shape |  | Specifies the overrides to selectively enable or disable individual SIP settings. The individual settings you specify he |
| MacSystemIntegrityProtectionStatus | Any  # complex shape | ✓ | Specifies the overall SIP status for the instance. To enable all SIP settings, specify enabled . To disable all SIP sett |
| TagSpecifications | list[Any  # complex shape] |  | Specifies tags to apply to the SIP modification task. |

## Output Shape: CreateMacSystemIntegrityProtectionModificationTaskResult

- **MacModificationTask** (Any  # complex shape): Information about the SIP modification task.

## Implementation

```speclang
def create_mac_system_integrity_protection_modification_task(store, request: dict) -> dict:
    """Creates a System Integrity Protection (SIP) modification task to configure the SIP settings for an x86 Mac instance or Apple silicon Mac instance. For more information, see Configure SIP for Amazon EC"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    mac_system_integrity_protection_status = request.get("MacSystemIntegrityProtectionStatus", "").strip() if isinstance(request.get("MacSystemIntegrityProtectionStatus"), str) else request.get("MacSystemIntegrityProtectionStatus")
    if not mac_system_integrity_protection_status:
        raise ValidationException("MacSystemIntegrityProtectionStatus is required")

    if store.mac_system_integrity_protection_modification_tasks(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "ClientToken": client_token,
        "DryRun": dry_run,
        "InstanceId": instance_id,
        "MacCredentials": mac_credentials,
        "MacSystemIntegrityProtectionConfiguration": mac_system_integrity_protection_configuration,
        "MacSystemIntegrityProtectionStatus": mac_system_integrity_protection_status,
        "TagSpecifications": tag_specifications,
    }

    store.mac_system_integrity_protection_modification_tasks(instance_id, record)

    return {
        "MacModificationTask": record.get("MacModificationTask", {}),
    }
```
