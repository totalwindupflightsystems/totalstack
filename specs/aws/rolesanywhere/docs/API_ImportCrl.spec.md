---
id: "@specs/aws/rolesanywhere/docs/API_ImportCrl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportCrl"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# ImportCrl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_ImportCrl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportCrl
<a name="API_ImportCrl"></a>

Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. 

 **Required permissions: ** `rolesanywhere:ImportCrl`. 

## Request Syntax
<a name="API_ImportCrl_RequestSyntax"></a>

```
POST /crls HTTP/1.1
Content-type: application/json

{
   "crlData": {{blob}},
   "enabled": {{boolean}},
   "name": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "trustAnchorArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportCrl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportCrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [crlData](#API_ImportCrl_RequestSyntax) **   <a name="rolesanywhere-ImportCrl-request-crlData"></a>
The x509 v3 specified certificate revocation list (CRL).  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 300000.  
Required: Yes

 ** [enabled](#API_ImportCrl_RequestSyntax) **   <a name="rolesanywhere-ImportCrl-request-enabled"></a>
Specifies whether the certificate revocation list (CRL) is enabled.  
Type: Boolean  
Required: No

 ** [name](#API_ImportCrl_RequestSyntax) **   <a name="rolesanywhere-ImportCrl-request-name"></a>
The name of the certificate revocation list (CRL).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: Yes

 ** [tags](#API_ImportCrl_RequestSyntax) **   <a name="rolesanywhere-ImportCrl-request-tags"></a>
A list of tags to attach to the certificate revocation list (CRL).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [trustAnchorArn](#API_ImportCrl_RequestSyntax) **   <a name="rolesanywhere-ImportCrl-request-trustAnchorArn"></a>
The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:trust-anchor.*)`   
Required: Yes

## Response Syntax
<a name="API_ImportCrl_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_ImportCrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [crl](#API_ImportCrl_ResponseSyntax) **   <a name="rolesanywhere-ImportCrl-response-crl"></a>
The state of the certificate revocation list (CRL) after a read or write operation.  
Type: [CrlDetail](API_CrlDetail.md) object

## Errors
<a name="API_ImportCrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_ImportCrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/ImportCrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/ImportCrl) 