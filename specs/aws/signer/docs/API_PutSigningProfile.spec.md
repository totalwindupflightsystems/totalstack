---
id: "@specs/aws/signer/docs/API_PutSigningProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutSigningProfile"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# PutSigningProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_PutSigningProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutSigningProfile
<a name="API_PutSigningProfile"></a>

Creates a signing profile. A signing profile is a code-signing template that can be used to carry out a pre-defined signing job. 

## Request Syntax
<a name="API_PutSigningProfile_RequestSyntax"></a>

```
PUT /signing-profiles/{{profileName}} HTTP/1.1
Content-type: application/json

{
   "overrides": { 
      "signingConfiguration": { 
         "encryptionAlgorithm": "{{string}}",
         "hashAlgorithm": "{{string}}"
      },
      "signingImageFormat": "{{string}}"
   },
   "platformId": "{{string}}",
   "signatureValidityPeriod": { 
      "type": "{{string}}",
      "value": {{number}}
   },
   "signingMaterial": { 
      "certificateArn": "{{string}}"
   },
   "signingParameters": { 
      "{{string}}" : "{{string}}" 
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_PutSigningProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-uri-profileName"></a>
The name of the signing profile to be created.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

## Request Body
<a name="API_PutSigningProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [overrides](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-overrides"></a>
A subfield of `platform`. This specifies any different configuration options that you want to apply to the chosen platform (such as a different `hash-algorithm` or `signing-algorithm`).  
Type: [SigningPlatformOverrides](API_SigningPlatformOverrides.md) object  
Required: No

 ** [platformId](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-platformId"></a>
The ID of the signing platform to be created.  
Type: String  
Required: Yes

 ** [signatureValidityPeriod](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-signatureValidityPeriod"></a>
The default validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.  
Type: [SignatureValidityPeriod](API_SignatureValidityPeriod.md) object  
Required: No

 ** [signingMaterial](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-signingMaterial"></a>
The AWS Certificate Manager certificate that will be used to sign code with the new signing profile.  
Type: [SigningMaterial](API_SigningMaterial.md) object  
Required: No

 ** [signingParameters](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-signingParameters"></a>
Map of key-value pairs for signing. These can include any information that you want to use during signing.  
Type: String to string map  
Required: No

 ** [tags](#API_PutSigningProfile_RequestSyntax) **   <a name="signer-PutSigningProfile-request-tags"></a>
Tags to be associated with the signing profile that is being created.  
Type: String to string map  
Map Entries: Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_PutSigningProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "profileVersion": "string",
   "profileVersionArn": "string"
}
```

## Response Elements
<a name="API_PutSigningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_PutSigningProfile_ResponseSyntax) **   <a name="signer-PutSigningProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the signing profile created.  
Type: String

 ** [profileVersion](#API_PutSigningProfile_ResponseSyntax) **   <a name="signer-PutSigningProfile-response-profileVersion"></a>
The version of the signing profile being created.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$` 

 ** [profileVersionArn](#API_PutSigningProfile_ResponseSyntax) **   <a name="signer-PutSigningProfile-response-profileVersionArn"></a>
The signing profile ARN, including the profile version.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_PutSigningProfile_Errors"></a>

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

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## See Also
<a name="API_PutSigningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/PutSigningProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/PutSigningProfile) 