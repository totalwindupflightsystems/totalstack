---
id: "@specs/aws/iam/put_group_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_PutGroupPolicy"
---

# PutGroupPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/put_group_policy
> **spec:implements:** @kind:operation PutGroupPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_PutGroupPolicy.spec.md

Adds or updates an inline policy document that is embedded in the specified IAM group. A user can also have managed policies attached to it. To attach a managed policy to a group, use AttachGroupPolicy . To create a new managed policy, use CreatePolicy . For information about policies, see Managed policies and inline policies in the IAM User Guide . For information about the maximum number of inline policies that you can embed in a group, see IAM and STS quotas in the IAM User Guide . Because policy documents can be large, you should use POST rather than GET when calling PutGroupPolicy . For general information about using the Query API with IAM, see Making query requests in the IAM User Guide .

## Input Shape: PutGroupPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group to associate the policy with. This parameter allows (through its regex pattern ) a string of chara |
| PolicyDocument | Any  # complex shape | ✓ | The policy document. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in |
| PolicyName | Any  # complex shape | ✓ | The name of the policy document. This parameter allows (through its regex pattern ) a string of characters consisting of |

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def put_group_policy(store, request: dict) -> dict:
    """Adds or updates an inline policy document that is embedded in the specified IAM group. A user can also have managed policies attached to it. To attach a managed policy to a group, use AttachGroupPolic"""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")

    if store.group_policys(group_name):
        raise ResourceInUseException(f"Resource group_name already exists")

    record = {
        "GroupName": group_name,
        "PolicyName": policy_name,
        "PolicyDocument": policy_document,
    }

    store.group_policys(group_name, record)

    return {
    }
```
