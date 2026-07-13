---
id: "@specs/aws/iam/put_user_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_PutUserPolicy"
---

# PutUserPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/put_user_policy
> **spec:implements:** @kind:operation PutUserPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_PutUserPolicy.spec.md

Adds or updates an inline policy document that is embedded in the specified IAM user. An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use AttachUserPolicy . To create a new managed policy, use CreatePolicy . For information about policies, see Managed policies and inline policies in the IAM User Guide . For information about the maximum number of inline policies that you can embed in a user, see IAM and STS quotas in the IAM User Guide . Because policy documents can be large, you should use POST rather than GET when calling PutUserPolicy . For general information about using the Query API with IAM, see Making query requests in the IAM User Guide .

## Input Shape: PutUserPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyDocument | Any  # complex shape | ✓ | The policy document. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in |
| PolicyName | Any  # complex shape | ✓ | The name of the policy document. This parameter allows (through its regex pattern ) a string of characters consisting of |
| UserName | Any  # complex shape | ✓ | The name of the user to associate the policy with. This parameter allows (through its regex pattern ) a string of charac |

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def put_user_policy(store, request: dict) -> dict:
    """Adds or updates an inline policy document that is embedded in the specified IAM user. An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use AttachUserPol"""
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    if store.user_policys(user_name):
        raise ResourceInUseException(f"Resource user_name already exists")

    record = {
        "UserName": user_name,
        "PolicyName": policy_name,
        "PolicyDocument": policy_document,
    }

    store.user_policys(user_name, record)

    return {
    }
```
