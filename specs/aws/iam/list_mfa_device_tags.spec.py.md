---
id: "@specs/aws/iam/list_mfa_device_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListMFADeviceTags"
---

# ListMFADeviceTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_mfa_device_tags
> **spec:implements:** @kind:operation ListMFADeviceTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListMFADeviceTags.spec.md

Lists the tags that are attached to the specified IAM virtual multi-factor authentication (MFA) device. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListMFADeviceTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| SerialNumber | Any  # complex shape | ✓ | The unique identifier for the IAM virtual MFA device whose tags you want to see. For virtual MFA devices, the serial num |

## Output Shape: ListMFADeviceTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the virtual MFA device. Each tag consists of a key name and an associate

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_mfa_device_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified IAM virtual multi-factor authentication (MFA) device. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging """
    serial_number = request.get("SerialNumber", "").strip() if isinstance(request.get("SerialNumber"), str) else request.get("SerialNumber")
    if not serial_number:
        raise ValidationException("SerialNumber is required")

    items = store.list_mfa_device_tagss()
    return {"Tags": list(items.values())}
```
