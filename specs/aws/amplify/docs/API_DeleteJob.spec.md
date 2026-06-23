---
id: "@specs/aws/amplify/docs/API_DeleteJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteJob"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# DeleteJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_DeleteJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteJob
<a name="API_DeleteJob"></a>

 Deletes a job for a branch of an Amplify app. 

## Request Syntax
<a name="API_DeleteJob_RequestSyntax"></a>

```
DELETE /apps/{{appId}}/branches/{{branchName}}/jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_DeleteJob_RequestSyntax) **   <a name="amplify-DeleteJob-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_DeleteJob_RequestSyntax) **   <a name="amplify-DeleteJob-request-uri-branchName"></a>
The name of the branch to use for the job.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [jobId](#API_DeleteJob_RequestSyntax) **   <a name="amplify-DeleteJob-request-uri-jobId"></a>
 The unique ID for the job.   
Length Constraints: Maximum length of 255.  
Pattern: `[0-9]+`   
Required: Yes

## Request Body
<a name="API_DeleteJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummary": { 
      "commitId": "string",
      "commitMessage": "string",
      "commitTime": number,
      "endTime": number,
      "jobArn": "string",
      "jobId": "string",
      "jobType": "string",
      "sourceUrl": "string",
      "sourceUrlType": "string",
      "startTime": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummary](#API_DeleteJob_ResponseSyntax) **   <a name="amplify-DeleteJob-response-jobSummary"></a>
 Describes the summary for an execution job for an Amplify app.   
Type: [JobSummary](API_JobSummary.md) object

## Errors
<a name="API_DeleteJob_Errors"></a>

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

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_DeleteJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/DeleteJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/DeleteJob) 