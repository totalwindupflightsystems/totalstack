---
id: "@specs/aws/sts/get_web_identity_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetWebIdentityToken"
---

# GetWebIdentityToken

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_web_identity_token
> **spec:implements:** @kind:operation GetWebIdentityToken
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetWebIdentityToken.spec.md

Returns a signed JSON Web Token (JWT) that represents the calling Amazon Web Services identity. The returned JWT can be used to authenticate with external services that support OIDC discovery. The token is signed by Amazon Web Services STS and can be publicly verified using the verification keys published at the issuer's JWKS endpoint.

## Input Shape: GetWebIdentityTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Audience | Any  # complex shape | ✓ | The intended recipient of the web identity token. This value populates the aud claim in the JWT and should identify the  |
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, for which the JSON Web Token (JWT) will remain valid. The value can range from 60 seconds (1 m |
| SigningAlgorithm | Any  # complex shape | ✓ | The cryptographic algorithm to use for signing the JSON Web Token (JWT). Valid values are RS256 (RSA with SHA-256) and E |
| Tags | Any  # complex shape |  | An optional list of tags to include in the JSON Web Token (JWT). These tags are added as custom claims to the JWT and ca |

## Output Shape: GetWebIdentityTokenResponse

- **Expiration** (Any  # complex shape): The date and time when the web identity token expires, in UTC. The expiration is determined by adding the DurationSecond
- **WebIdentityToken** (Any  # complex shape): A signed JSON Web Token (JWT) that represents the caller's Amazon Web Services identity. The token contains standard JWT

## Errors
- **SessionDurationEscalationException**: The requested token duration would extend the session beyond its original expiration time. You cannot use this operation to extend the lifetime of a session beyond what was granted when the session wa
- **OutboundWebIdentityFederationDisabledException**: The outbound web identity federation feature is not enabled for this account. To use this feature, you must first enable it through the Amazon Web Services Management Console or API.
- **JWTPayloadSizeExceededException**: The requested token payload size exceeds the maximum allowed size. Reduce the number of request tags included in the GetWebIdentityToken API call to reduce the token payload size.

## Implementation

```speclang
def get_web_identity_token(store, request: dict) -> dict:
    """Returns a signed JSON Web Token (JWT) that represents the calling Amazon Web Services identity. The returned JWT can be used to authenticate with external services that support OIDC discovery. The tok"""
    audience = request.get("Audience", "").strip() if isinstance(request.get("Audience"), str) else request.get("Audience")
    if not audience:
        raise ValidationException("Audience is required")
    signing_algorithm = request.get("SigningAlgorithm", "").strip() if isinstance(request.get("SigningAlgorithm"), str) else request.get("SigningAlgorithm")
    if not signing_algorithm:
        raise ValidationException("SigningAlgorithm is required")

    resource = store.web_identity_tokens(audience)
    if not resource:
        raise ResourceNotFoundException(f"Resource audience not found")
    return {"Audience": audience, **resource}
```
