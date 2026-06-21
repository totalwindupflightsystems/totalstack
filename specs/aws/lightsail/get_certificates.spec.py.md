---
id: "@specs/aws/lightsail/get_certificates"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetCertificates"
---

# GetCertificates

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_certificates
> **spec:implements:** @kind:operation GetCertificates
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetCertificates.spec.md

Returns information about one or more Amazon Lightsail SSL/TLS certificates. To get a summary of a certificate, omit includeCertificateDetails from your request. The response will include only the certificate Amazon Resource Name (ARN), certificate name, domain name, and tags.

## Input Shape: GetCertificatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape |  | The name for the certificate for which to return information. When omitted, the response includes all of your certificat |
| certificateStatuses | list[Any  # complex shape] |  | The status of the certificates for which to return information. For example, specify ISSUED to return only certificates  |
| includeCertificateDetails | Any  # complex shape |  | Indicates whether to include detailed information about the certificates in the response. When omitted, the response inc |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetCertifica |

## Output Shape: GetCertificatesResult

- **certificates** (list[Any  # complex shape]): An object that describes certificates.
- **nextPageToken** (Any  # complex shape): If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token f

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_certificates(store, request: dict) -> dict:
    """Returns information about one or more Amazon Lightsail SSL/TLS certificates. To get a summary of a certificate, omit includeCertificateDetails from your request. The response will include only the cer"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
