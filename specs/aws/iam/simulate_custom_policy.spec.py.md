---
id: "@specs/aws/iam/simulate_custom_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_SimulateCustomPolicy"
---

# SimulateCustomPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/simulate_custom_policy
> **spec:implements:** @kind:operation SimulateCustomPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_SimulateCustomPolicy.spec.md

Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and Amazon Web Services resources to determine the policies' effective permissions. The policies are provided as strings. The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations. You can simulate resources that don't exist in your account. If you want to simulate existing policies that are attached to an IAM user, group, or role, use SimulatePrincipalPolicy instead. Context keys are variables that are maintained by Amazon Web Services and its services and which provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use GetContextKeysForCustomPolicy . If the output is long, you can use MaxItems and Marker parameters to paginate the results. The IAM policy simulator evaluates statements in the identity-based policy and the inputs that you provide during simulation. The policy simulator results can differ from your live Amazon Web Services environment. We recommend that you check your policies against your live Amazon Web Services environment after testing using the policy simulator to confirm that you have the desired results. For more information about using the policy simulator, see Testing IAM policies with the IAM policy simulator in the IAM User Guide .

## Input Shape: SimulateCustomPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ActionNames | Any  # complex shape | ✓ | A list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each |
| CallerArn | Any  # complex shape |  | The ARN of the IAM user that you want to use as the simulated caller of the API operations. CallerArn is required if you |
| ContextEntries | Any  # complex shape |  | A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PermissionsBoundaryPolicyInputList | Any  # complex shape |  | The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that an IAM entit |
| PolicyInputList | Any  # complex shape | ✓ | A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, |
| ResourceArns | Any  # complex shape |  | A list of ARNs of Amazon Web Services resources to include in the simulation. If this parameter is not provided, then th |
| ResourceHandlingOption | Any  # complex shape |  | Specifies the type of simulation to run. Different API operations that support resource-based policies require different |
| ResourceOwner | Any  # complex shape |  | An ARN representing the Amazon Web Services account ID that specifies the owner of any simulated resource that does not  |
| ResourcePolicy | Any  # complex shape |  | A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as |

## Output Shape: SimulatePolicyResponse

- **EvaluationResults** (Any  # complex shape): The results of the simulation.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **PolicyEvaluationException**: The request failed because a provided policy could not be successfully evaluated. An additional detailed message indicates the source of the failure.

## Implementation

```speclang
def simulate_custom_policy(store, request: dict) -> dict:
    """Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and Amazon Web Services resources to determine the policies' effective permissions. The po"""
    action_names = request.get("ActionNames", "").strip() if isinstance(request.get("ActionNames"), str) else request.get("ActionNames")
    if not action_names:
        raise ValidationException("ActionNames is required")
    policy_input_list = request.get("PolicyInputList", "").strip() if isinstance(request.get("PolicyInputList"), str) else request.get("PolicyInputList")
    if not policy_input_list:
        raise ValidationException("PolicyInputList is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SimulateCustomPolicy", request)
```
