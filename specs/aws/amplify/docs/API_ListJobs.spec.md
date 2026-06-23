---
id: "@specs/aws/amplify/docs/API_ListJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListJobs"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# ListJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_ListJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListJobs
<a name="API_ListJobs"></a>

 Lists the jobs for a branch of an Amplify app. 

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
GET /apps/{{appId}}/branches/{{branchName}}/jobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ListJobs_RequestSyntax) **   <a name="amplify-ListJobs-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [branchName](#API_ListJobs_RequestSyntax) **   <a name="amplify-ListJobs-request-uri-branchName"></a>
The name of the branch to use for the request.   
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `(?s).+`   
Required: Yes

 ** [maxResults](#API_ListJobs_RequestSyntax) **   <a name="amplify-ListJobs-request-uri-maxResults"></a>
The maximum number of records to list in a single response.   
Valid Range: Minimum value of 0. Maximum value of 50.

 ** [nextToken](#API_ListJobs_RequestSyntax) **   <a name="amplify-ListJobs-request-uri-nextToken"></a>
A pagination token. Set to null to start listing steps from the start. If a non-null pagination token is returned in a result, pass its value in here to list more steps.   
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaries": [ 
      { 
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaries](#API_ListJobs_ResponseSyntax) **   <a name="amplify-ListJobs-response-jobSummaries"></a>
The result structure for the list job result request.   
Type: Array of [JobSummary](API_JobSummary.md) objects

 ** [nextToken](#API_ListJobs_ResponseSyntax) **   <a name="amplify-ListJobs-response-nextToken"></a>
A pagination token. If non-null the pagination token is returned in a result. Pass its value in another request to retrieve more entries.   
Type: String  
Length Constraints: Maximum length of 2000.  
Pattern: `(?s).*` 

## Errors
<a name="API_ListJobs_Errors"></a>

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
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/ListJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/ListJobs) 