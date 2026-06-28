---
id: "@specs/aws/signer/docs/API_GetSigningProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSigningProfile"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# GetSigningProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_GetSigningProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSigningProfile
<a name="API_GetSigningProfile"></a>

Returns information on a specific signing profile.

## Request Syntax
<a name="API_GetSigningProfile_RequestSyntax"></a>

```
GET /signing-profiles/{{profileName}}?profileOwner={{profileOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSigningProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_GetSigningProfile_RequestSyntax) **   <a name="signer-GetSigningProfile-request-uri-profileName"></a>
The name of the target signing profile.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

 ** [profileOwner](#API_GetSigningProfile_RequestSyntax) **   <a name="signer-GetSigningProfile-request-uri-profileOwner"></a>
The AWS account ID of the profile owner.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

## Request Body
<a name="API_GetSigningProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSigningProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "overrides": { 
      "signingConfiguration": { 
         "encryptionAlgorithm": "string",
         "hashAlgorithm": "string"
      },
      "signingImageFormat": "string"
   },
   "platformDisplayName": "string",
   "platformId": "string",
   "profileName": "string",
   "profileVersion": "string",
   "profileVersionArn": "string",
   "revocationRecord": { 
      "revocationEffectiveFrom": number,
      "revokedAt": number,
      "revokedBy": "string"
   },
   "signatureValidityPeriod": { 
      "type": "string",
      "value": number
   },
   "signingMaterial": { 
      "certificateArn": "string"
   },
   "signingParameters": { 
      "string" : "string" 
   },
   "status": "string",
   "statusReason": "string",
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_GetSigningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-arn"></a>
The Amazon Resource Name (ARN) for the signing profile.  
Type: String

 ** [overrides](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-overrides"></a>
A list of overrides applied by the target signing profile for signing operations.  
Type: [SigningPlatformOverrides](API_SigningPlatformOverrides.md) object

 ** [platformDisplayName](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-platformDisplayName"></a>
A human-readable name for the signing platform associated with the signing profile.  
Type: String

 ** [platformId](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-platformId"></a>
The ID of the platform that is used by the target signing profile.  
Type: String

 ** [profileName](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-profileName"></a>
The name of the target signing profile.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}` 

 ** [profileVersion](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-profileVersion"></a>
The current version of the signing profile.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$` 

 ** [profileVersionArn](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-profileVersionArn"></a>
The signing profile ARN, including the profile version.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [revocationRecord](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-revocationRecord"></a>
Revocation information for a signing profile.  
Type: [SigningProfileRevocationRecord](API_SigningProfileRevocationRecord.md) object

 ** [signatureValidityPeriod](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-signatureValidityPeriod"></a>
The validity period for a signing job.  
Type: [SignatureValidityPeriod](API_SignatureValidityPeriod.md) object

 ** [signingMaterial](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-signingMaterial"></a>
The ARN of the certificate that the target profile uses for signing operations.  
Type: [SigningMaterial](API_SigningMaterial.md) object

 ** [signingParameters](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-signingParameters"></a>
A map of key-value pairs for signing operations that is attached to the target signing profile.  
Type: String to string map

 ** [status](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-status"></a>
The status of the target signing profile.  
Type: String  
Valid Values: `Active | Canceled | Revoked` 

 ** [statusReason](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-statusReason"></a>
Reason for the status of the target signing profile.  
Type: String

 ** [tags](#API_GetSigningProfile_ResponseSyntax) **   <a name="signer-GetSigningProfile-response-tags"></a>
A list of tags associated with the signing profile.  
Type: String to string map  
Map Entries: Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetSigningProfile_Errors"></a>

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
<a name="API_GetSigningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/GetSigningProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/GetSigningProfile) 