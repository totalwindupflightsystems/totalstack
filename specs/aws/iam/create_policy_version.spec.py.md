---
id: "@specs/aws/iam/create_policy_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreatePolicyVersion"
---

# CreatePolicyVersion

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_policy_version
> **spec:implements:** @kind:operation CreatePolicyVersion
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreatePolicyVersion.spec.md

Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must delete an existing version using DeletePolicyVersion before you create a new version. Optionally, you can set the new version as the policy's default version. The default version is the version that is in effect for the IAM users, groups, and roles to which the policy is attached. For more information about managed policy versions, see Versioning for managed policies in the IAM User Guide .

## Input Shape: CreatePolicyVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version. For more information about ARNs |
| PolicyDocument | Any  # complex shape | ✓ | The JSON policy document that you want to use as the content for this new version of the policy. You must provide polici |
| SetAsDefault | Any  # complex shape |  | Specifies whether to set this version as the policy's default version. When this parameter is true , the new policy vers |

## Output Shape: CreatePolicyVersionResponse

- **PolicyVersion** (Any  # complex shape): A structure containing details about the new policy version.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_policy_version(store, request: dict) -> dict:
    """Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you """
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")

    if store.policy_versions(policy_arn):
        raise ResourceInUseException(f"Resource policy_arn already exists")

    record = {
        "PolicyArn": policy_arn,
        "PolicyDocument": policy_document,
        "SetAsDefault": set_as_default,
    }

    store.policy_versions(policy_arn, record)

    return {
        "PolicyVersion": record.get("PolicyVersion", {}),
    }
```
