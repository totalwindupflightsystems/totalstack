---
id: "@specs/aws/iam/get_context_keys_for_custom_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetContextKeysForCustomPolicy"
---

# GetContextKeysForCustomPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_context_keys_for_custom_policy
> **spec:implements:** @kind:operation GetContextKeysForCustomPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetContextKeysForCustomPolicy.spec.md

Gets a list of all of the context keys referenced in the input policies. The policies are supplied as a list of one or more strings. To get the context keys from policies associated with an IAM user, group, or role, use GetContextKeysForPrincipalPolicy . Context keys are variables maintained by Amazon Web Services and its services that provide details about the context of an API query request. Context keys can be evaluated by testing against a value specified in an IAM policy. Use GetContextKeysForCustomPolicy to understand what key names and values you must supply when you call SimulateCustomPolicy . Note that all parameters are shown in unencoded form here for clarity but must be URL encoded to be included as a part of a real HTML request.

## Input Shape: GetContextKeysForCustomPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyInputList | Any  # complex shape | ✓ | A list of policies for which you want the list of context keys referenced in those policies. Each document is specified  |

## Output Shape: GetContextKeysForPolicyResponse

- **ContextKeyNames** (Any  # complex shape): The list of context keys that are referenced in the input policies.

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def get_context_keys_for_custom_policy(store, request: dict) -> dict:
    """Gets a list of all of the context keys referenced in the input policies. The policies are supplied as a list of one or more strings. To get the context keys from policies associated with an IAM user, """
    policy_input_list = request.get("PolicyInputList", "").strip() if isinstance(request.get("PolicyInputList"), str) else request.get("PolicyInputList")
    if not policy_input_list:
        raise ValidationException("PolicyInputList is required")

    resource = store.context_keys_for_custom_policys(policy_input_list)
    if not resource:
        raise ResourceNotFoundException(f"Resource policy_input_list not found")
    return {"PolicyInputList": policy_input_list, **resource}
```
