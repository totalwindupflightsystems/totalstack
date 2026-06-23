---
id: "@specs/aws/amplify/docs/API_CreateDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDeployment"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CreateDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CreateDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDeployment
<a name="API_CreateDeployment"></a>

Creates a deployment for a manually deployed Amplify app. Manually deployed apps are not connected to a Git repository. 

The maximum duration between the `CreateDeployment` call and the `StartDeployment` call cannot exceed 8 hours. If the duration exceeds 8 hours, the `StartDeployment` call and the associated `Job` will fail.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
POST /apps/{{appId}}/branches/{{branchName}}/deployments HTTP/1.1
Content-type: application/json

{
   "fileMap": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateDeployment_RequestSyntax) **   <a name="amplify-CreateDeployment-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_CreateDeployment_RequestSyntax) **   <a name="amplify-CreateDeployment-request-uri-branchName"></a>
 The name of the branch to use for the job.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

## Request Body
<a name="API_CreateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fileMap](#API_CreateDeployment_RequestSyntax) **   <a name="amplify-CreateDeployment-request-fileMap"></a>
 An optional file map that contains the file name as the key and the file content md5 hash as the value. If this argument is provided, the service will generate a unique upload URL per file. Otherwise, the service will only generate a single upload URL for the zipped files.   
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 32.  
Value Pattern: `(?s).*`   
Required: No

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fileUploadUrls": { 
      "string" : "string" 
   },
   "jobId": "string",
   "zipUploadUrl": "string"
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileUploadUrls](#API_CreateDeployment_ResponseSyntax) **   <a name="amplify-CreateDeployment-response-fileUploadUrls"></a>
 When the `fileMap` argument is provided in the request, `fileUploadUrls` will contain a map of file names to upload URLs.   
Type: String to string map  
Key Length Constraints: Maximum length of 255.  
Key Pattern: `(?s).*`   
Value Length Constraints: Maximum length of 1000.

 ** [jobId](#API_CreateDeployment_ResponseSyntax) **   <a name="amplify-CreateDeployment-response-jobId"></a>
 The job ID for this deployment. will supply to start deployment api.   
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `[0-9]+` 

 ** [zipUploadUrl](#API_CreateDeployment_ResponseSyntax) **   <a name="amplify-CreateDeployment-response-zipUploadUrl"></a>
 When the `fileMap` argument is not provided in the request, this `zipUploadUrl` is returned.   
Type: String  
Length Constraints: Maximum length of 1000.

## Errors
<a name="API_CreateDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** LimitExceededException **   
A resource could not be created because service quotas were exceeded.   
HTTP Status Code: 429

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/CreateDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CreateDeployment) 