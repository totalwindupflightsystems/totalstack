---
id: "@specs/aws/bedrock-agent/docs/API_ListModelCopyJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListModelCopyJobs"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListModelCopyJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListModelCopyJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListModelCopyJobs
<a name="API_ListModelCopyJobs"></a>

Returns a list of model copy jobs that you have submitted. You can filter the jobs to return based on one or more criteria. For more information, see [Copy models to be used in other regions](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_ListModelCopyJobs_RequestSyntax"></a>

```
GET /model-copy-jobs?creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}}&outputModelNameContains={{targetModelNameContains}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&sourceAccountEquals={{sourceAccountEquals}}&sourceModelArnEquals={{sourceModelArnEquals}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListModelCopyJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [creationTimeAfter](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-creationTimeAfter"></a>
Filters for model copy jobs created after the specified time.

 ** [creationTimeBefore](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-creationTimeBefore"></a>
Filters for model copy jobs created before the specified time. 

 ** [maxResults](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-sortBy"></a>
The field to sort by in the returned list of model copy jobs.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-sortOrder"></a>
Specifies whether to sort the results in ascending or descending order.  
Valid Values: `Ascending | Descending` 

 ** [sourceAccountEquals](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-sourceAccountEquals"></a>
Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify.  
Pattern: `[0-9]{12}` 

 ** [sourceModelArnEquals](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-sourceModelArnEquals"></a>
Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [statusEquals](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-statusEquals"></a>
Filters for model copy jobs whose status matches the value that you specify.  
Valid Values: `InProgress | Completed | Failed` 

 ** [targetModelNameContains](#API_ListModelCopyJobs_RequestSyntax) **   <a name="bedrock-ListModelCopyJobs-request-uri-targetModelNameContains"></a>
Filters for model copy jobs in which the name of the copied model contains the string that you specify.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

## Request Body
<a name="API_ListModelCopyJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListModelCopyJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "modelCopyJobSummaries": [ 
      { 
         "creationTime": "string",
         "failureMessage": "string",
         "jobArn": "string",
         "sourceAccountId": "string",
         "sourceModelArn": "string",
         "sourceModelName": "string",
         "status": "string",
         "targetModelArn": "string",
         "targetModelKmsKeyArn": "string",
         "targetModelName": "string",
         "targetModelTags": [ 
            { 
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListModelCopyJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [modelCopyJobSummaries](#API_ListModelCopyJobs_ResponseSyntax) **   <a name="bedrock-ListModelCopyJobs-response-modelCopyJobSummaries"></a>
A list of information about each model copy job.  
Type: Array of [ModelCopyJobSummary](API_ModelCopyJobSummary.md) objects

 ** [nextToken](#API_ListModelCopyJobs_ResponseSyntax) **   <a name="bedrock-ListModelCopyJobs-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListModelCopyJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_ListModelCopyJobs_Examples"></a>

### List model copy jobs (CLI)
<a name="API_ListModelCopyJobs_Example_1"></a>

The following example shows how to return information about ten model copy jobs in an account, using the AWS CLI.

```
aws bedrock list-model-copy-jobs --max-results 10
```

## See Also
<a name="API_ListModelCopyJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListModelCopyJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListModelCopyJobs) 