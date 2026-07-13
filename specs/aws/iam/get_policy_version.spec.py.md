---
id: "@specs/aws/iam/get_policy_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetPolicyVersion"
---

# GetPolicyVersion

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_policy_version
> **spec:implements:** @kind:operation GetPolicyVersion
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetPolicyVersion.spec.md

Retrieves information about the specified version of the specified managed policy, including the policy document. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically. To list the available versions for a policy, use ListPolicyVersions . This operation retrieves information about managed policies. To retrieve information about an inline policy that is embedded in a user, group, or role, use GetUserPolicy , GetGroupPolicy , or GetRolePolicy . For more information about the types of policies, see Managed policies and inline policies in the IAM User Guide . For more information about managed policy versions, see Versioning for managed policies in the IAM User Guide .

## Input Shape: GetPolicyVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the managed policy that you want information about. For more information about ARNs, s |
| VersionId | Any  # complex shape | ✓ | Identifies the policy version to retrieve. This parameter allows (through its regex pattern ) a string of characters tha |

## Output Shape: GetPolicyVersionResponse

- **PolicyVersion** (Any  # complex shape): A structure containing details about the policy version.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_policy_version(store, request: dict) -> dict:
    """Retrieves information about the specified version of the specified managed policy, including the policy document. Policies returned by this operation are URL-encoded compliant with RFC 3986 . You can """
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    version_id = request.get("VersionId", "").strip() if isinstance(request.get("VersionId"), str) else request.get("VersionId")
    if not version_id:
        raise ValidationException("VersionId is required")

    resource = store.policy_versions(version_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource version_id not found")
    return {"VersionId": version_id, **resource}
```
