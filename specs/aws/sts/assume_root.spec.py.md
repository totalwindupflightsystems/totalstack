---
id: "@specs/aws/sts/assume_root"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_AssumeRoot"
---

# AssumeRoot

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/assume_root
> **spec:implements:** @kind:operation AssumeRoot
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_AssumeRoot.spec.md

Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization. You must use credentials from an Organizations management account or a delegated administrator account for IAM to call AssumeRoot . You cannot use root user credentials to make this call. Before you can launch a privileged session, you must have centralized root access in your organization. For steps to enable this feature, see Centralize root access for member accounts in the IAM User Guide . The STS global endpoint is not supported for AssumeRoot. You must send this request to a Regional STS endpoint. For more information, see Endpoints . You can track AssumeRoot in CloudTrail logs to determine what actions were performed in a session. For more information, see Track privileged tasks in CloudTrail in the IAM User Guide . When granting access to privileged tasks you should only grant the necessary permissions required to perform that task. For more information, see Security best practices in IAM . In addition, you can use service control policies (SCPs) to manage and limit permissions in your organization. See General examples in the Organizations User Guide for more information on SCPs.

## Input Shape: AssumeRootRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, of the privileged session. The value can range from 0 seconds up to the maximum session durati |
| TargetPrincipal | Any  # complex shape | ✓ | The member account principal ARN or account ID. |
| TaskPolicyArn | Any  # complex shape | ✓ | The identity based policy that scopes the session to the privileged tasks that can be performed. You must use one of fol |

## Output Shape: AssumeRootResponse

- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security token. The size 
- **SourceIdentity** (Any  # complex shape): The source identity specified by the principal that is calling the AssumeRoot operation. You can use the aws:SourceIdent

## Errors
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in
- **ExpiredTokenException**: The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.

## Implementation

```speclang
def assume_root(store, request: dict) -> dict:
    """Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization. You must use credentials from an Organizations management account or a delegat"""
    target_principal = request.get("TargetPrincipal", "").strip() if isinstance(request.get("TargetPrincipal"), str) else request.get("TargetPrincipal")
    if not target_principal:
        raise ValidationException("TargetPrincipal is required")
    task_policy_arn = request.get("TaskPolicyArn", "").strip() if isinstance(request.get("TaskPolicyArn"), str) else request.get("TaskPolicyArn")
    if not task_policy_arn:
        raise ValidationException("TaskPolicyArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssumeRoot", request)
```
