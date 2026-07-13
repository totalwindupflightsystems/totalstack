---
id: "@specs/aws/iam/create_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreatePolicy"
---

# CreatePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_policy
> **spec:implements:** @kind:operation CreatePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreatePolicy.spec.md

Creates a new managed policy for your Amazon Web Services account. This operation creates a policy version with a version identifier of v1 and sets v1 as the policy's default version. For more information about policy versions, see Versioning for managed policies in the IAM User Guide . As a best practice, you can validate your IAM policies. To learn more, see Validating IAM policies in the IAM User Guide . For more information about managed policies in general, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: CreatePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | A friendly description of the policy. Typically used to store information about the permissions defined in the policy. F |
| Path | Any  # complex shape |  | The path for the policy. For more information about paths, see IAM identifiers in the IAM User Guide . This parameter is |
| PolicyDocument | Any  # complex shape | ✓ | The JSON policy document that you want to use as the content for the new policy. You must provide policies in JSON forma |
| PolicyName | Any  # complex shape | ✓ | The friendly name of the policy. IAM user, group, role, and policy names must be unique within the account. Names are no |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new IAM customer managed policy. Each tag consists of a key name and an as |

## Output Shape: CreatePolicyResponse

- **Policy** (Any  # complex shape): A structure containing details about the new policy.

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_policy(store, request: dict) -> dict:
    """Creates a new managed policy for your Amazon Web Services account. This operation creates a policy version with a version identifier of v1 and sets v1 as the policy's default version. For more informa"""
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")

    if store.policys(policy_name):
        raise ResourceInUseException(f"Resource policy_name already exists")

    record = {
        "PolicyName": policy_name,
        "Path": path,
        "PolicyDocument": policy_document,
        "Description": description,
        "Tags": tags,
    }

    store.policys(policy_name, record)

    return {
        "Policy": record.get("Policy", {}),
    }
```
