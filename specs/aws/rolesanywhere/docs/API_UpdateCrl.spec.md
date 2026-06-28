---
id: "@specs/aws/rolesanywhere/docs/API_UpdateCrl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCrl"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# UpdateCrl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_UpdateCrl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCrl
<a name="API_UpdateCrl"></a>

Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.

 **Required permissions: ** `rolesanywhere:UpdateCrl`. 

## Request Syntax
<a name="API_UpdateCrl_RequestSyntax"></a>

```
PATCH /crl/{{crlId}} HTTP/1.1
Content-type: application/json

{
   "crlData": {{blob}},
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [crlId](#API_UpdateCrl_RequestSyntax) **   <a name="rolesanywhere-UpdateCrl-request-uri-crlId"></a>
The unique identifier of the certificate revocation list (CRL).  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_UpdateCrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [crlData](#API_UpdateCrl_RequestSyntax) **   <a name="rolesanywhere-UpdateCrl-request-crlData"></a>
The x509 v3 specified certificate revocation list (CRL).  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 300000.  
Required: No

 ** [name](#API_UpdateCrl_RequestSyntax) **   <a name="rolesanywhere-UpdateCrl-request-name"></a>
The name of the Crl.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: No

## Response Syntax
<a name="API_UpdateCrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "crl": { 
      "createdAt": "string",
      "crlArn": "string",
      "crlData": blob,
      "crlId": "string",
      "enabled": boolean,
      "name": "string",
      "trustAnchorArn": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateCrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [crl](#API_UpdateCrl_ResponseSyntax) **   <a name="rolesanywhere-UpdateCrl-response-crl"></a>
The state of the certificate revocation list (CRL) after a read or write operation.  
Type: [CrlDetail](API_CrlDetail.md) object

## Errors
<a name="API_UpdateCrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateCrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/UpdateCrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/UpdateCrl) 