---
id: "@specs/aws/signer/docs/API_AddProfilePermission"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddProfilePermission"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# AddProfilePermission

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_AddProfilePermission
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddProfilePermission
<a name="API_AddProfilePermission"></a>

Adds cross-account permissions to a signing profile.

## Request Syntax
<a name="API_AddProfilePermission_RequestSyntax"></a>

```
POST /signing-profiles/{{profileName}}/permissions HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "principal": "{{string}}",
   "profileVersion": "{{string}}",
   "revisionId": "{{string}}",
   "statementId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddProfilePermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-uri-profileName"></a>
The human-readable name of the signing profile.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

## Request Body
<a name="API_AddProfilePermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-action"></a>
For cross-account signing. Grant a designated account permission to perform one or more of the following actions. Each action is associated with a specific API's operations. For more information about cross-account signing, see [Using cross-account signing with signing profiles](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profile-cross-account.html) in the *AWS Signer Developer Guide*.  
You can designate the following actions to an account.  
+  `signer:StartSigningJob`. This action isn't supported for container image workflows. For details, see [StartSigningJob](API_StartSigningJob.md).
+  `signer:SignPayload`. This action isn't supported for AWS Lambda workflows. For details, see [SignPayload](API_SignPayload.md) 
+  `signer:GetSigningProfile`. For details, see [GetSigningProfile](API_GetSigningProfile.md).
+  `signer:RevokeSignature`. For details, see [RevokeSignature](API_RevokeSignature.md).
Type: String  
Required: Yes

 ** [principal](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-principal"></a>
The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.  
Type: String  
Required: Yes

 ** [profileVersion](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-profileVersion"></a>
The version of the signing profile.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$`   
Required: No

 ** [revisionId](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-revisionId"></a>
A unique identifier for the current profile revision.  
Type: String  
Required: No

 ** [statementId](#API_AddProfilePermission_RequestSyntax) **   <a name="signer-AddProfilePermission-request-statementId"></a>
A unique identifier for the cross-account permission statement.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_AddProfilePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "revisionId": "string"
}
```

## Response Elements
<a name="API_AddProfilePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [revisionId](#API_AddProfilePermission_ResponseSyntax) **   <a name="signer-AddProfilePermission-response-revisionId"></a>
A unique identifier for the current profile revision.  
Type: String

## Errors
<a name="API_AddProfilePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ConflictException **   
The resource encountered a conflicting state.  
HTTP Status Code: 409

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
A specified resource could not be found.  
HTTP Status Code: 404

 ** ServiceLimitExceededException **   
The client is making a request that exceeds service limits.  
HTTP Status Code: 402

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## See Also
<a name="API_AddProfilePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/AddProfilePermission) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/AddProfilePermission) 