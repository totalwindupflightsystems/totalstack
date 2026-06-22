---
id: "@specs/aws/bedrock-agent/docs/API_ListModelInvocationJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListModelInvocationJobs"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListModelInvocationJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListModelInvocationJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListModelInvocationJobs
<a name="API_ListModelInvocationJobs"></a>

Lists all batch inference jobs in the account. For more information, see [View details about a batch inference job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html).

## Request Syntax
<a name="API_ListModelInvocationJobs_RequestSyntax"></a>

```
GET /model-invocation-jobs?maxResults={{maxResults}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}}&submitTimeAfter={{submitTimeAfter}}&submitTimeBefore={{submitTimeBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListModelInvocationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-maxResults"></a>
The maximum number of results to return. If there are more results than the number that you specify, a `nextToken` value is returned. Use the `nextToken` in a request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nameContains](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-nameContains"></a>
Specify a string to filter for batch inference jobs whose names contain the string.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9]{1,63}(-*[a-zA-Z0-9\+\-\.]){0,63}` 

 ** [nextToken](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-nextToken"></a>
If there were more results than the value you specified in the `maxResults` field in a previous `ListModelInvocationJobs` request, the response would have returned a `nextToken` value. To see the next batch of results, send the `nextToken` value in another request.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-sortBy"></a>
An attribute by which to sort the results.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-sortOrder"></a>
Specifies whether to sort the results by ascending or descending order.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-statusEquals"></a>
Specify a status to filter for batch inference jobs whose statuses match the string you specify.  
The following statuses are possible:  
+ Submitted – This job has been submitted to a queue for validation.
+ Validating – This job is being validated for the requirements described in [Format and upload your batch inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html). The criteria include the following:
  + Your IAM service role has access to the Amazon S3 buckets containing your files.
  + Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the `modelInput` value matches the request body for the model.
  + Your files fulfill the requirements for file size and number of records. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html).
+ Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.
+ Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.
+ InProgress – This job has begun. You can start viewing the results in the output S3 location.
+ Completed – This job has successfully completed. View the output files in the output S3 location.
+ PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.
+ Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the [Support Center](https://console.aws.amazon.com/support/home/).
+ Stopped – This job was stopped by a user.
+ Stopping – This job is being stopped by a user.
Valid Values: `Submitted | InProgress | Completed | Failed | Stopping | Stopped | PartiallyCompleted | Expired | Validating | Scheduled` 

 ** [submitTimeAfter](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-submitTimeAfter"></a>
Specify a time to filter for batch inference jobs that were submitted after the time you specify.

 ** [submitTimeBefore](#API_ListModelInvocationJobs_RequestSyntax) **   <a name="bedrock-ListModelInvocationJobs-request-uri-submitTimeBefore"></a>
Specify a time to filter for batch inference jobs that were submitted before the time you specify.

## Request Body
<a name="API_ListModelInvocationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListModelInvocationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invocationJobSummaries": [ 
      { 
         "clientRequestToken": "string",
         "endTime": "string",
         "errorRecordCount": number,
         "inputDataConfig": { ... },
         "jobArn": "string",
         "jobExpirationTime": "string",
         "jobName": "string",
         "lastModifiedTime": "string",
         "message": "string",
         "modelId": "string",
         "modelInvocationType": "string",
         "outputDataConfig": { ... },
         "processedRecordCount": number,
         "roleArn": "string",
         "status": "string",
         "submitTime": "string",
         "successRecordCount": number,
         "timeoutDurationInHours": number,
         "totalRecordCount": number,
         "vpcConfig": { 
            "securityGroupIds": [ "string" ],
            "subnetIds": [ "string" ]
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListModelInvocationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationJobSummaries](#API_ListModelInvocationJobs_ResponseSyntax) **   <a name="bedrock-ListModelInvocationJobs-response-invocationJobSummaries"></a>
A list of items, each of which contains a summary about a batch inference job.  
Type: Array of [ModelInvocationJobSummary](API_ModelInvocationJobSummary.md) objects

 ** [nextToken](#API_ListModelInvocationJobs_ResponseSyntax) **   <a name="bedrock-ListModelInvocationJobs-response-nextToken"></a>
If there are more results than can fit in the response, a `nextToken` is returned. Use the `nextToken` in a request to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListModelInvocationJobs_Errors"></a>

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
<a name="API_ListModelInvocationJobs_Examples"></a>

### List up to ten model invocation jobs
<a name="API_ListModelInvocationJobs_Example_1"></a>

This example illustrates one usage of ListModelInvocationJobs.

```
GET /model-invocation-jobs?maxResults=10&sortBy=CreationTime&sortOrder=Descending HTTP/1.1
```

## See Also
<a name="API_ListModelInvocationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListModelInvocationJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListModelInvocationJobs) 