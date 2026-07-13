---
id: "@specs/aws/iam/simulate_principal_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_SimulatePrincipalPolicy"
---

# SimulatePrincipalPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/simulate_principal_policy
> **spec:implements:** @kind:operation SimulatePrincipalPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_SimulatePrincipalPolicy.spec.md

Simulate how a set of IAM policies attached to an IAM entity works with a list of API operations and Amazon Web Services resources to determine the policies' effective permissions. The entity can be an IAM user, group, or role. If you specify a user, then the simulation also includes all of the policies that are attached to groups that the user belongs to. You can simulate resources that don't exist in your account. You can optionally include a list of one or more additional policies specified as strings to include in the simulation. If you want to simulate only policies specified as strings, use SimulateCustomPolicy instead. You can also optionally include one resource-based policy to be evaluated with each of the resources included in the simulation for IAM users only. The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations. Note: This operation discloses information about the permissions granted to other users. If you do not want users to see other user's permissions, then consider allowing them to use SimulateCustomPolicy instead. Context keys are variables maintained by Amazon Web Services and its services that provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use GetContextKeysForPrincipalPolicy . If the output is long, you can use the MaxItems and Marker parameters to paginate the results. The IAM policy simulator evaluates statements in the identity-based policy and the inputs that you provide during simulation. The policy simulator results can differ from your live Amazon Web Services environment. We recommend that you check your policies against your live Amazon Web Services environment after testing using the policy simulator to confirm that you have the desired results. For more information about using the policy simulator, see Testing IAM policies with the IAM policy simulator in the IAM User Guide .

## Input Shape: SimulatePrincipalPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ActionNames | Any  # complex shape | ✓ | A list of names of API operations to evaluate in the simulation. Each operation is evaluated for each resource. Each ope |
| CallerArn | Any  # complex shape |  | The ARN of the IAM user that you want to specify as the simulated caller of the API operations. If you do not specify a  |
| ContextEntries | Any  # complex shape |  | A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PermissionsBoundaryPolicyInputList | Any  # complex shape |  | The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that the entity c |
| PolicyInputList | Any  # complex shape |  | An optional list of additional policy documents to include in the simulation. Each document is specified as a string con |
| PolicySourceArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you sp |
| ResourceArns | Any  # complex shape |  | A list of ARNs of Amazon Web Services resources to include in the simulation. If this parameter is not provided, then th |
| ResourceHandlingOption | Any  # complex shape |  | Specifies the type of simulation to run. Different API operations that support resource-based policies require different |
| ResourceOwner | Any  # complex shape |  | An Amazon Web Services account ID that specifies the owner of any simulated resource that does not identify its owner in |
| ResourcePolicy | Any  # complex shape |  | A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as |

## Output Shape: SimulatePolicyResponse

- **EvaluationResults** (Any  # complex shape): The results of the simulation.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **PolicyEvaluationException**: The request failed because a provided policy could not be successfully evaluated. An additional detailed message indicates the source of the failure.

## Implementation

```speclang
def simulate_principal_policy(store, request: dict) -> dict:
    """Simulate how a set of IAM policies attached to an IAM entity works with a list of API operations and Amazon Web Services resources to determine the policies' effective permissions. The entity can be a"""
    action_names = request.get("ActionNames", "").strip() if isinstance(request.get("ActionNames"), str) else request.get("ActionNames")
    if not action_names:
        raise ValidationException("ActionNames is required")
    policy_source_arn = request.get("PolicySourceArn", "").strip() if isinstance(request.get("PolicySourceArn"), str) else request.get("PolicySourceArn")
    if not policy_source_arn:
        raise ValidationException("PolicySourceArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SimulatePrincipalPolicy", request)
```
