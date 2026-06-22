---
id: "@specs/aws/bedrock-agent/docs/API_GetModelInvocationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetModelInvocationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetModelInvocationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetModelInvocationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetModelInvocationJob
<a name="API_GetModelInvocationJob"></a>

Gets details about a batch inference job. For more information, see [Monitor batch inference jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor) 

## Request Syntax
<a name="API_GetModelInvocationJob_RequestSyntax"></a>

```
GET /model-invocation-job/{{jobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelInvocationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_GetModelInvocationJob_RequestSyntax) **   <a name="bedrock-GetModelInvocationJob-request-uri-jobIdentifier"></a>
The Amazon Resource Name (ARN) of the batch inference job.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/)?[a-z0-9]{12})`   
Required: Yes

## Request Body
<a name="API_GetModelInvocationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelInvocationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetModelInvocationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientRequestToken](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]{1,256}(-*[a-zA-Z0-9]){0,256}` 

 ** [endTime](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-endTime"></a>
The time at which the batch inference job ended.  
Type: Timestamp

 ** [errorRecordCount](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-errorRecordCount"></a>
The number of records that failed to process in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.

 ** [inputDataConfig](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-inputDataConfig"></a>
Details about the location of the input to the batch inference job.  
Type: [ModelInvocationJobInputDataConfig](API_ModelInvocationJobInputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [jobArn](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the batch inference job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/[a-z0-9]{12})` 

 ** [jobExpirationTime](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-jobExpirationTime"></a>
The time at which the batch inference job times or timed out.  
Type: Timestamp

 ** [jobName](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-jobName"></a>
The name of the batch inference job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9]{1,63}(-*[a-zA-Z0-9\+\-\.]){0,63}` 

 ** [lastModifiedTime](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-lastModifiedTime"></a>
The time at which the batch inference job was last modified.  
Type: Timestamp

 ** [message](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-message"></a>
If the batch inference job failed, this field contains a message describing why the job failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [modelId](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-modelId"></a>
The unique identifier of the foundation model used for model inference.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-:]{1,63}/[a-z0-9]{12}$)|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)$)|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+$)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)` 

 ** [modelInvocationType](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-modelInvocationType"></a>
The invocation endpoint for ModelInvocationJob  
Type: String  
Valid Values: `InvokeModel | Converse` 

 ** [outputDataConfig](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-outputDataConfig"></a>
Details about the location of the output of the batch inference job.  
Type: [ModelInvocationJobOutputDataConfig](API_ModelInvocationJobOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [processedRecordCount](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-processedRecordCount"></a>
The number of records that have been processed in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.

 ** [roleArn](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-roleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-status"></a>
The status of the batch inference job.  
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
Type: String  
Valid Values: `Submitted | InProgress | Completed | Failed | Stopping | Stopped | PartiallyCompleted | Expired | Validating | Scheduled` 

 ** [submitTime](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-submitTime"></a>
The time at which the batch inference job was submitted.  
Type: Timestamp

 ** [successRecordCount](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-successRecordCount"></a>
The number of records that were successfully processed in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.

 ** [timeoutDurationInHours](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-timeoutDurationInHours"></a>
The number of hours after which batch inference job was set to time out.  
Type: Integer  
Valid Range: Minimum value of 24. Maximum value of 168.

 ** [totalRecordCount](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-totalRecordCount"></a>
The total number of records in the batch inference job.  
Type: Long  
Valid Range: Minimum value of 0.

 ** [vpcConfig](#API_GetModelInvocationJob_ResponseSyntax) **   <a name="bedrock-GetModelInvocationJob-response-vpcConfig"></a>
The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see [Protect batch inference jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc).  
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_GetModelInvocationJob_Errors"></a>

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
<a name="API_GetModelInvocationJob_Examples"></a>

### Get a batch inference job
<a name="API_GetModelInvocationJob_Example_1"></a>

This example illustrates one usage of GetModelInvocationJob.

```
GET /model-invocation-job/BATCHJOB1234 HTTP/1.1
```

## See Also
<a name="API_GetModelInvocationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetModelInvocationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetModelInvocationJob) 