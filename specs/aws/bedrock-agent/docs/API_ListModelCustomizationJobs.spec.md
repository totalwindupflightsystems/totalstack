---
id: "@specs/aws/bedrock-agent/docs/API_ListModelCustomizationJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListModelCustomizationJobs"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListModelCustomizationJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListModelCustomizationJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListModelCustomizationJobs
<a name="API_ListModelCustomizationJobs"></a>

Returns a list of model customization jobs that you have submitted. You can filter the jobs to return based on one or more criteria.

For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListModelCustomizationJobs_RequestSyntax"></a>

```
GET /model-customization-jobs?creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListModelCustomizationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [creationTimeAfter](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-creationTimeAfter"></a>
Return customization jobs created after the specified time. 

 ** [creationTimeBefore](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-creationTimeBefore"></a>
Return customization jobs created before the specified time. 

 ** [maxResults](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nameContains](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-nameContains"></a>
Return customization jobs only if the job name contains these characters.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [nextToken](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-sortBy"></a>
The field to sort by in the returned list of jobs.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-sortOrder"></a>
The sort order of the results.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListModelCustomizationJobs_RequestSyntax) **   <a name="bedrock-ListModelCustomizationJobs-request-uri-statusEquals"></a>
Return customization jobs with the specified status.   
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped` 

## Request Body
<a name="API_ListModelCustomizationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListModelCustomizationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelCustomizationJobSummaries": [ 
      { 
         "baseModelArn": "string",
         "creationTime": "string",
         "customizationType": "string",
         "customModelArn": "string",
         "customModelName": "string",
         "endTime": "string",
         "jobArn": "string",
         "jobName": "string",
         "lastModifiedTime": "string",
         "status": "string",
         "statusDetails": { 
            "dataProcessingDetails": { 
               "creationTime": "string",
               "lastModifiedTime": "string",
               "status": "string"
            },
            "trainingDetails": { 
               "creationTime": "string",
               "lastModifiedTime": "string",
               "status": "string"
            },
            "validationDetails": { 
               "creationTime": "string",
               "lastModifiedTime": "string",
               "status": "string"
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListModelCustomizationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelCustomizationJobSummaries](#API_ListModelCustomizationJobs_ResponseSyntax) **   <a name="bedrock-ListModelCustomizationJobs-response-modelCustomizationJobSummaries"></a>
Job summaries.  
Type: Array of [ModelCustomizationJobSummary](API_ModelCustomizationJobSummary.md) objects

 ** [nextToken](#API_ListModelCustomizationJobs_ResponseSyntax) **   <a name="bedrock-ListModelCustomizationJobs-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListModelCustomizationJobs_Errors"></a>

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

## See Also
<a name="API_ListModelCustomizationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListModelCustomizationJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListModelCustomizationJobs) 