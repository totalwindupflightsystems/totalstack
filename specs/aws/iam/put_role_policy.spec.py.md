---
id: "@specs/aws/iam/put_role_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_PutRolePolicy"
---

# PutRolePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/put_role_policy
> **spec:implements:** @kind:operation PutRolePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_PutRolePolicy.spec.md

Adds or updates an inline policy document that is embedded in the specified IAM role. When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using CreateRole . You can update a role's trust policy using UpdateAssumeRolePolicy . For more information about roles, see IAM roles in the IAM User Guide . A role can also have a managed policy attached to it. To attach a managed policy to a role, use AttachRolePolicy . To create a new managed policy, use CreatePolicy . For information about policies, see Managed policies and inline policies in the IAM User Guide . For information about the maximum number of inline policies that you can embed with a role, see IAM and STS quotas in the IAM User Guide . Because policy documents can be large, you should use POST rather than GET when calling PutRolePolicy . For general information about using the Query API with IAM, see Making query requests in the IAM User Guide .

## Input Shape: PutRolePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyDocument | Any  # complex shape | ✓ | The policy document. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in |
| PolicyName | Any  # complex shape | ✓ | The name of the policy document. This parameter allows (through its regex pattern ) a string of characters consisting of |
| RoleName | Any  # complex shape | ✓ | The name of the role to associate the policy with. This parameter allows (through its regex pattern ) a string of charac |

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def put_role_policy(store, request: dict) -> dict:
    """Adds or updates an inline policy document that is embedded in the specified IAM role. When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) po"""
    policy_document = request.get("PolicyDocument", "").strip() if isinstance(request.get("PolicyDocument"), str) else request.get("PolicyDocument")
    if not policy_document:
        raise ValidationException("PolicyDocument is required")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    if not policy_name:
        raise ValidationException("PolicyName is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    if store.role_policys(policy_name):
        raise ResourceInUseException(f"Resource policy_name already exists")

    record = {
        "RoleName": role_name,
        "PolicyName": policy_name,
        "PolicyDocument": policy_document,
    }

    store.role_policys(policy_name, record)

    return {
    }
```
