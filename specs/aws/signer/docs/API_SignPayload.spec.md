---
id: "@specs/aws/signer/docs/API_SignPayload"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SignPayload"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# SignPayload

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_SignPayload
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SignPayload
<a name="API_SignPayload"></a>

Signs a binary payload and returns a signature envelope.

## Request Syntax
<a name="API_SignPayload_RequestSyntax"></a>

```
POST /signing-jobs/with-payload HTTP/1.1
Content-type: application/json

{
   "payload": {{blob}},
   "payloadFormat": "{{string}}",
   "profileName": "{{string}}",
   "profileOwner": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SignPayload_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SignPayload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [payload](#API_SignPayload_RequestSyntax) **   <a name="signer-SignPayload-request-payload"></a>
Specifies the object digest (hash) to sign.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: Yes

 ** [payloadFormat](#API_SignPayload_RequestSyntax) **   <a name="signer-SignPayload-request-payloadFormat"></a>
Payload content type. The single valid type is `application/vnd.cncf.notary.payload.v1+json`.  
Type: String  
Required: Yes

 ** [profileName](#API_SignPayload_RequestSyntax) **   <a name="signer-SignPayload-request-profileName"></a>
The name of the signing profile.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

 ** [profileOwner](#API_SignPayload_RequestSyntax) **   <a name="signer-SignPayload-request-profileOwner"></a>
The AWS account ID of the profile owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: No

## Response Syntax
<a name="API_SignPayload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string",
   "jobOwner": "string",
   "metadata": { 
      "string" : "string" 
   },
   "signature": blob
}
```

## Response Elements
<a name="API_SignPayload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_SignPayload_ResponseSyntax) **   <a name="signer-SignPayload-response-jobId"></a>
Unique identifier of the signing job.  
Type: String

 ** [jobOwner](#API_SignPayload_ResponseSyntax) **   <a name="signer-SignPayload-response-jobOwner"></a>
The AWS account ID of the job owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [metadata](#API_SignPayload_ResponseSyntax) **   <a name="signer-SignPayload-response-metadata"></a>
Information including the signing profile ARN and the signing job ID.  
Type: String to string map

 ** [signature](#API_SignPayload_ResponseSyntax) **   <a name="signer-SignPayload-response-signature"></a>
A cryptographic signature.  
Type: Base64-encoded binary data object

## Errors
<a name="API_SignPayload_Errors"></a>

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
<a name="API_SignPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/SignPayload) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/SignPayload) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SignPayload) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/SignPayload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SignPayload) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/SignPayload) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/SignPayload) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/SignPayload) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/SignPayload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SignPayload) 