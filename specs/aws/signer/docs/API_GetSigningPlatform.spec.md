---
id: "@specs/aws/signer/docs/API_GetSigningPlatform"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSigningPlatform"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# GetSigningPlatform

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_GetSigningPlatform
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSigningPlatform
<a name="API_GetSigningPlatform"></a>

Returns information on a specific signing platform.

## Request Syntax
<a name="API_GetSigningPlatform_RequestSyntax"></a>

```
GET /signing-platforms/{{platformId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSigningPlatform_RequestParameters"></a>

The request uses the following URI parameters.

 ** [platformId](#API_GetSigningPlatform_RequestSyntax) **   <a name="signer-GetSigningPlatform-request-uri-platformId"></a>
The ID of the target signing platform.  
Required: Yes

## Request Body
<a name="API_GetSigningPlatform_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSigningPlatform_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "category": "string",
   "displayName": "string",
   "maxSizeInMB": number,
   "partner": "string",
   "platformId": "string",
   "revocationSupported": boolean,
   "signingConfiguration": { 
      "encryptionAlgorithmOptions": { 
         "allowedValues": [ "string" ],
         "defaultValue": "string"
      },
      "hashAlgorithmOptions": { 
         "allowedValues": [ "string" ],
         "defaultValue": "string"
      }
   },
   "signingImageFormat": { 
      "defaultFormat": "string",
      "supportedFormats": [ "string" ]
   },
   "target": "string"
}
```

## Response Elements
<a name="API_GetSigningPlatform_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [category](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-category"></a>
The category type of the target signing platform.  
Type: String  
Valid Values: `AWSIoT` 

 ** [displayName](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-displayName"></a>
The display name of the target signing platform.  
Type: String

 ** [maxSizeInMB](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-maxSizeInMB"></a>
The maximum size (in MB) of the payload that can be signed by the target platform.  
Type: Integer

 ** [partner](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-partner"></a>
A list of partner entities that use the target signing platform.  
Type: String

 ** [platformId](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-platformId"></a>
The ID of the target signing platform.  
Type: String

 ** [revocationSupported](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-revocationSupported"></a>
A flag indicating whether signatures generated for the signing platform can be revoked.  
Type: Boolean

 ** [signingConfiguration](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-signingConfiguration"></a>
A list of configurations applied to the target platform at signing.  
Type: [SigningConfiguration](API_SigningConfiguration.md) object

 ** [signingImageFormat](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-signingImageFormat"></a>
The format of the target platform's signing image.  
Type: [SigningImageFormat](API_SigningImageFormat.md) object

 ** [target](#API_GetSigningPlatform_ResponseSyntax) **   <a name="signer-GetSigningPlatform-response-target"></a>
The validation template that is used by the target signing platform.  
Type: String

## Errors
<a name="API_GetSigningPlatform_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
A specified resource could not be found.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

## See Also
<a name="API_GetSigningPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/GetSigningPlatform) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/GetSigningPlatform) 