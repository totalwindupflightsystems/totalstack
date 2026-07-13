---
id: "@specs/aws/sts/get_delegated_access_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetDelegatedAccessToken"
---

# GetDelegatedAccessToken

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_delegated_access_token
> **spec:implements:** @kind:operation GetDelegatedAccessToken
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetDelegatedAccessToken.spec.md

Exchanges a trade-in token for temporary Amazon Web Services credentials with the permissions associated with the assumed principal. This operation allows you to obtain credentials for a specific principal based on a trade-in token, enabling delegation of access to Amazon Web Services resources.

## Input Shape: GetDelegatedAccessTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| TradeInToken | Any  # complex shape | ✓ | The token to exchange for temporary Amazon Web Services credentials. This token must be valid and unexpired at the time  |

## Output Shape: GetDelegatedAccessTokenResponse

- **AssumedPrincipal** (Any  # complex shape): The Amazon Resource Name (ARN) of the principal that was assumed when obtaining the delegated access token. This ARN ide
- **Credentials** (Any  # complex shape): 
- **PackedPolicySize** (Any  # complex shape): The percentage of the maximum policy size that is used by the session policy. The policy size is calculated as the sum o

## Errors
- **ExpiredTradeInTokenException**: The trade-in token provided in the request has expired and can no longer be exchanged for credentials. Request a new token and retry the operation.
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in
- **PackedPolicyTooLargeException**: The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, sessio

## Implementation

```speclang
def get_delegated_access_token(store, request: dict) -> dict:
    """Exchanges a trade-in token for temporary Amazon Web Services credentials with the permissions associated with the assumed principal. This operation allows you to obtain credentials for a specific prin"""
    trade_in_token = request.get("TradeInToken", "").strip() if isinstance(request.get("TradeInToken"), str) else request.get("TradeInToken")
    if not trade_in_token:
        raise ValidationException("TradeInToken is required")

    resource = store.delegated_access_tokens(trade_in_token)
    if not resource:
        raise ResourceNotFoundException(f"Resource trade_in_token not found")
    return {"TradeInToken": trade_in_token, **resource}
```
