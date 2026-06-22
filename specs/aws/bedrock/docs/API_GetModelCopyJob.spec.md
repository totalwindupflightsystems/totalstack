---
id: "@specs/aws/bedrock/docs/API_GetModelCopyJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetModelCopyJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetModelCopyJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetModelCopyJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetModelCopyJob
<a name="API_GetModelCopyJob"></a>

Retrieves information about a model copy job. For more information, see [Copy models to be used in other regions](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_GetModelCopyJob_RequestSyntax"></a>

```
GET /model-copy-jobs/{{jobArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelCopyJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobArn](#API_GetModelCopyJob_RequestSyntax) **   <a name="bedrock-GetModelCopyJob-request-uri-jobArn"></a>
The Amazon Resource Name (ARN) of the model copy job.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-copy-job/[a-z0-9]{12}`   
Required: Yes

## Request Body
<a name="API_GetModelCopyJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelCopyJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetModelCopyJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-creationTime"></a>
The time at which the model copy job was created.  
Type: Timestamp

 ** [failureMessage](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-failureMessage"></a>
An error message for why the model copy job failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [jobArn](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the model copy job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-copy-job/[a-z0-9]{12}` 

 ** [sourceAccountId](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-sourceAccountId"></a>
The unique identifier of the account that the model being copied originated from.  
Type: String  
Pattern: `[0-9]{12}` 

 ** [sourceModelArn](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-sourceModelArn"></a>
The Amazon Resource Name (ARN) of the original model being copied.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [sourceModelName](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-sourceModelName"></a>
The name of the original model being copied.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [status](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-status"></a>
The status of the model copy job.  
Type: String  
Valid Values: `InProgress | Completed | Failed` 

 ** [targetModelArn](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-targetModelArn"></a>
The Amazon Resource Name (ARN) of the copied model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}` 

 ** [targetModelKmsKeyArn](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-targetModelKmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key encrypting the copied model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [targetModelName](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-targetModelName"></a>
The name of the copied model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [targetModelTags](#API_GetModelCopyJob_ResponseSyntax) **   <a name="bedrock-GetModelCopyJob-response-targetModelTags"></a>
The tags associated with the copied model.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_GetModelCopyJob_Errors"></a>

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
<a name="API_GetModelCopyJob_Examples"></a>

### Get a model copy job (CLI)
<a name="API_GetModelCopyJob_Example_1"></a>

The following example shows how to get information about a model copy job using the AWS CLI.

```
aws bedrock get-model-copy-job --job-arn arn:aws:bedrock:us-east-1:123456789012:model-copy-job/amazon.titan-text-lite-v1:0:4k/abcdef123456
```

## See Also
<a name="API_GetModelCopyJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetModelCopyJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetModelCopyJob) 