---
id: "@specs/aws/signer/docs/API_RevokeSignature"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeSignature"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# RevokeSignature

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_RevokeSignature
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeSignature
<a name="API_RevokeSignature"></a>

Changes the state of a signing job to REVOKED. This indicates that the signature is no longer valid.

## Request Syntax
<a name="API_RevokeSignature_RequestSyntax"></a>

```
PUT /signing-jobs/{{jobId}}/revoke HTTP/1.1
Content-type: application/json

{
   "jobOwner": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RevokeSignature_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_RevokeSignature_RequestSyntax) **   <a name="signer-RevokeSignature-request-uri-jobId"></a>
ID of the signing job to be revoked.  
Required: Yes

## Request Body
<a name="API_RevokeSignature_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobOwner](#API_RevokeSignature_RequestSyntax) **   <a name="signer-RevokeSignature-request-jobOwner"></a>
AWS account ID of the job owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: No

 ** [reason](#API_RevokeSignature_RequestSyntax) **   <a name="signer-RevokeSignature-request-reason"></a>
The reason for revoking the signing job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_RevokeSignature_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RevokeSignature_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeSignature_Errors"></a>

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
<a name="API_RevokeSignature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/RevokeSignature) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/RevokeSignature) 