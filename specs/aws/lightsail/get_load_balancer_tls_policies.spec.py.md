---
id: "@specs/aws/lightsail/get_load_balancer_tls_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetLoadBalancerTlsPolicies"
---

# GetLoadBalancerTlsPolicies

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_load_balancer_tls_policies
> **spec:implements:** @kind:operation GetLoadBalancerTlsPolicies
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetLoadBalancerTlsPolicies.spec.md

Returns a list of TLS security policies that you can apply to Lightsail load balancers. For more information about load balancer TLS security policies, see Configuring TLS security policies on your Amazon Lightsail load balancers in the Amazon Lightsail Developer Guide .

## Input Shape: GetLoadBalancerTlsPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetLoadBalan |

## Output Shape: GetLoadBalancerTlsPoliciesResult

- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo
- **tlsPolicies** (list[Any  # complex shape]): An array of objects that describe the TLS security policies that are available.

## Errors
- **ServiceException**: A general service exception.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 

## Implementation

```speclang
def get_load_balancer_tls_policies(store, request: dict) -> dict:
    """Returns a list of TLS security policies that you can apply to Lightsail load balancers. For more information about load balancer TLS security policies, see Configuring TLS security policies on your Am"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
