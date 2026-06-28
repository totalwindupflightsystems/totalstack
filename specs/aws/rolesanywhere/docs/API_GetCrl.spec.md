---
id: "@specs/aws/rolesanywhere/docs/API_GetCrl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCrl"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# GetCrl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_GetCrl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCrl
<a name="API_GetCrl"></a>

Gets a certificate revocation list (CRL).

 **Required permissions: ** `rolesanywhere:GetCrl`. 

## Request Syntax
<a name="API_GetCrl_RequestSyntax"></a>

```
GET /crl/{{crlId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [crlId](#API_GetCrl_RequestSyntax) **   <a name="rolesanywhere-GetCrl-request-uri-crlId"></a>
The unique identifier of the certificate revocation list (CRL).  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_GetCrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCrl_ResponseSyntax"></a>

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
<a name="API_GetCrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [crl](#API_GetCrl_ResponseSyntax) **   <a name="rolesanywhere-GetCrl-response-crl"></a>
The state of the certificate revocation list (CRL) after a read or write operation.  
Type: [CrlDetail](API_CrlDetail.md) object

## Errors
<a name="API_GetCrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

## See Also
<a name="API_GetCrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/GetCrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/GetCrl) 