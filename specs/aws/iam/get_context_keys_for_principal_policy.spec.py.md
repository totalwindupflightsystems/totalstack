---
id: "@specs/aws/iam/get_context_keys_for_principal_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetContextKeysForPrincipalPolicy"
---

# GetContextKeysForPrincipalPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_context_keys_for_principal_policy
> **spec:implements:** @kind:operation GetContextKeysForPrincipalPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetContextKeysForPrincipalPolicy.spec.md

Gets a list of all of the context keys referenced in all the IAM policies that are attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the request also includes all of the policies attached to groups that the user is a member of. You can optionally include a list of one or more additional policies, specified as strings. If you want to include only a list of policies by string, use GetContextKeysForCustomPolicy instead. Note: This operation discloses information about the permissions granted to other users. If you do not want users to see other user's permissions, then consider allowing them to use GetContextKeysForCustomPolicy instead. Context keys are variables maintained by Amazon Web Services and its services that provide details about the context of an API query request. Context keys can be evaluated by testing against a value in an IAM policy. Use GetContextKeysForPrincipalPolicy to understand what key names and values you must supply when you call SimulatePrincipalPolicy .

## Input Shape: GetContextKeysForPrincipalPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyInputList | Any  # complex shape |  | An optional list of additional policies for which you want the list of context keys that are referenced. The regex patte |
| PolicySourceArn | Any  # complex shape | ✓ | The ARN of a user, group, or role whose policies contain the context keys that you want listed. If you specify a user, t |

## Output Shape: GetContextKeysForPolicyResponse

- **ContextKeyNames** (Any  # complex shape): The list of context keys that are referenced in the input policies.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def get_context_keys_for_principal_policy(store, request: dict) -> dict:
    """Gets a list of all of the context keys referenced in all the IAM policies that are attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the """
    policy_source_arn = request.get("PolicySourceArn", "").strip() if isinstance(request.get("PolicySourceArn"), str) else request.get("PolicySourceArn")
    if not policy_source_arn:
        raise ValidationException("PolicySourceArn is required")

    resource = store.context_keys_for_principal_policys(policy_source_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource policy_source_arn not found")
    return {"PolicySourceArn": policy_source_arn, **resource}
```
