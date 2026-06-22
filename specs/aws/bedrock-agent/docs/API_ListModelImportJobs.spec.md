---
id: "@specs/aws/bedrock-agent/docs/API_ListModelImportJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListModelImportJobs"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListModelImportJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListModelImportJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListModelImportJobs
<a name="API_ListModelImportJobs"></a>

Returns a list of import jobs you've submitted. You can filter the results to return based on one or more criteria. For more information, see [Import a customized model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListModelImportJobs_RequestSyntax"></a>

```
GET /model-import-jobs?creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListModelImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [creationTimeAfter](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-creationTimeAfter"></a>
Return import jobs that were created after the specified time.

 ** [creationTimeBefore](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-creationTimeBefore"></a>
Return import jobs that were created before the specified time.

 ** [maxResults](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nameContains](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-nameContains"></a>
Return imported jobs only if the job name contains these characters.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [nextToken](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-sortBy"></a>
The field to sort by in the returned list of imported jobs.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-sortOrder"></a>
Specifies whether to sort the results in ascending or descending order.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListModelImportJobs_RequestSyntax) **   <a name="bedrock-ListModelImportJobs-request-uri-statusEquals"></a>
Return imported jobs with the specified status.  
Valid Values: `InProgress | Completed | Failed` 

## Request Body
<a name="API_ListModelImportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListModelImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelImportJobSummaries": [ 
      { 
         "creationTime": "string",
         "endTime": "string",
         "importedModelArn": "string",
         "importedModelName": "string",
         "jobArn": "string",
         "jobName": "string",
         "lastModifiedTime": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListModelImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelImportJobSummaries](#API_ListModelImportJobs_ResponseSyntax) **   <a name="bedrock-ListModelImportJobs-response-modelImportJobSummaries"></a>
Import job summaries.  
Type: Array of [ModelImportJobSummary](API_ModelImportJobSummary.md) objects

 ** [nextToken](#API_ListModelImportJobs_ResponseSyntax) **   <a name="bedrock-ListModelImportJobs-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListModelImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_ListModelImportJobs_Examples"></a>

### List model import jobs
<a name="API_ListModelImportJobs_Example_1"></a>

Gets a list of the import jobs that you have submitted.

```
GET /model-import-jobs/ HTTP/1.1
Content-type: application/json
```

### Example response
<a name="API_ListModelImportJobs_Example_2"></a>

Response for the above request.

```
HTTP/1.1 200
Content-type: application/json

{
    "modelImportJobSummaries": [
        {
            "jobArn": "arn:aws:bedrock:us-east-1:111122223333:model-import-job/yggb47n4xlml",
            "jobName": "MyImportedModelJobName",
            "status": "InProgress",
            "lastModifiedTime": "2024-08-13T23:40:47.517Z",
            "creationTime": "2024-08-13T23:38:42.457Z",
            "importedModelName": "ImportedModelName"
        },
        {
            "jobArn": "arn:aws:bedrock:us-east-1:111122223333:model-import-job/dchh9ny8e0dv",
            "jobName": "SomeJobName",
            "status": "Completed",
            "lastModifiedTime": "2024-08-13T19:36:33.674Z",
            "creationTime": "2024-08-13T19:20:14.058Z",
            "endTime": "2024-08-13T19:36:33.492Z",
            "importedModelArn": "arn:aws:bedrock:us-east-1:111122223333:imported-model/s4dt0wly5gud",
            "importedModelName": "SomeImportedModelName"
        }
    ]
}
```

## See Also
<a name="API_ListModelImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListModelImportJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListModelImportJobs) 