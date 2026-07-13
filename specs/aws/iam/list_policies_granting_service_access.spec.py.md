---
id: "@specs/aws/iam/list_policies_granting_service_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListPoliciesGrantingServiceAccess"
---

# ListPoliciesGrantingServiceAccess

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_policies_granting_service_access
> **spec:implements:** @kind:operation ListPoliciesGrantingServiceAccess
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListPoliciesGrantingServiceAccess.spec.md

Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service. This operation does not use other policy types when determining whether a resource could access a service. These other policy types include resource-based policies, access control lists, Organizations policies, IAM permissions boundaries, and STS assume role policies. It only applies permissions policy logic. For more about the evaluation of policy types, see Evaluating policies in the IAM User Guide . The list of policies returned by the operation depends on the ARN of the identity that you provide. User – The list of policies includes the managed and inline policies that are attached to the user directly. The list also includes any additional managed and inline policies that are attached to the group to which the user belongs. Group – The list of policies includes only the managed and inline policies that are attached to the group directly. Policies that are attached to the group’s user are not included. Role – The list of policies includes only the managed and inline policies that are attached to the role. For each managed policy, this operation returns the ARN and policy name. For each inline policy, it returns the policy name and the entity to which it is attached. Inline policies do not have an ARN. For more information about these policy types, see Managed policies and inline policies in the IAM User Guide . Policies that are attached to users and roles as permissions boundaries are not returned. To view which managed policy is currently used to set the permissions boundary for a user or role, use the GetUser or GetRole operations.

## Input Shape: ListPoliciesGrantingServiceAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape | ✓ | The ARN of the IAM identity (user, group, or role) whose policies you want to list. |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| ServiceNamespaces | Any  # complex shape | ✓ | The service namespace for the Amazon Web Services services whose policies you want to list. To learn the service namespa |

## Output Shape: ListPoliciesGrantingServiceAccessResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **PoliciesGrantingServiceAccess** (Any  # complex shape): A ListPoliciesGrantingServiceAccess object that contains details about the permissions policies attached to the specifie

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def list_policies_granting_service_access(store, request: dict) -> dict:
    """Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service. This operation does not use other policy types when determining whether a resource c"""
    arn = request.get("Arn", "").strip() if isinstance(request.get("Arn"), str) else request.get("Arn")
    if not arn:
        raise ValidationException("Arn is required")
    service_namespaces = request.get("ServiceNamespaces", "").strip() if isinstance(request.get("ServiceNamespaces"), str) else request.get("ServiceNamespaces")
    if not service_namespaces:
        raise ValidationException("ServiceNamespaces is required")

    items = store.list_policies_granting_service_accesss()
    return {"PoliciesGrantingServiceAccess": list(items.values())}
```
