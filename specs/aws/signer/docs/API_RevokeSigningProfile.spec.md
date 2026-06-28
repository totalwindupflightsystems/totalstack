---
id: "@specs/aws/signer/docs/API_RevokeSigningProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeSigningProfile"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# RevokeSigningProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_RevokeSigningProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeSigningProfile
<a name="API_RevokeSigningProfile"></a>

Changes the state of a signing profile to REVOKED. This indicates that signatures generated using the signing profile after an effective start date are no longer valid.

## Request Syntax
<a name="API_RevokeSigningProfile_RequestSyntax"></a>

```
PUT /signing-profiles/{{profileName}}/revoke HTTP/1.1
Content-type: application/json

{
   "effectiveTime": {{number}},
   "profileVersion": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RevokeSigningProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_RevokeSigningProfile_RequestSyntax) **   <a name="signer-RevokeSigningProfile-request-uri-profileName"></a>
The name of the signing profile to be revoked.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

## Request Body
<a name="API_RevokeSigningProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [effectiveTime](#API_RevokeSigningProfile_RequestSyntax) **   <a name="signer-RevokeSigningProfile-request-effectiveTime"></a>
A timestamp for when revocation of a Signing Profile should become effective. Signatures generated using the signing profile after this timestamp are not trusted.  
Type: Timestamp  
Required: Yes

 ** [profileVersion](#API_RevokeSigningProfile_RequestSyntax) **   <a name="signer-RevokeSigningProfile-request-profileVersion"></a>
The version of the signing profile to be revoked.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$`   
Required: Yes

 ** [reason](#API_RevokeSigningProfile_RequestSyntax) **   <a name="signer-RevokeSigningProfile-request-reason"></a>
The reason for revoking a signing profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_RevokeSigningProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RevokeSigningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeSigningProfile_Errors"></a>

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
<a name="API_RevokeSigningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/RevokeSigningProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/RevokeSigningProfile) 