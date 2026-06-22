---
id: "@specs/aws/bedrock/docs/API_CreateInferenceProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateInferenceProfile"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateInferenceProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateInferenceProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateInferenceProfile
<a name="API_CreateInferenceProfile"></a>

Creates an application inference profile to track metrics and costs when invoking a model. To create an application inference profile for a foundation model in one region, specify the ARN of the model in that region. To create an application inference profile for a foundation model across multiple regions, specify the ARN of the system-defined inference profile that contains the regions that you want to route requests to. For more information, see [Increase throughput and resilience with cross-region inference in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_CreateInferenceProfile_RequestSyntax"></a>

```
POST /inference-profiles HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "inferenceProfileName": "{{string}}",
   "modelSource": { ... },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateInferenceProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInferenceProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateInferenceProfile_RequestSyntax) **   <a name="bedrock-CreateInferenceProfile-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [description](#API_CreateInferenceProfile_RequestSyntax) **   <a name="bedrock-CreateInferenceProfile-request-description"></a>
A description for the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+`   
Required: No

 ** [inferenceProfileName](#API_CreateInferenceProfile_RequestSyntax) **   <a name="bedrock-CreateInferenceProfile-request-inferenceProfileName"></a>
A name for the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+`   
Required: Yes

 ** [modelSource](#API_CreateInferenceProfile_RequestSyntax) **   <a name="bedrock-CreateInferenceProfile-request-modelSource"></a>
The foundation model or system-defined inference profile that the inference profile will track metrics and costs for.  
Type: [InferenceProfileModelSource](API_InferenceProfileModelSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_CreateInferenceProfile_RequestSyntax) **   <a name="bedrock-CreateInferenceProfile-request-tags"></a>
An array of objects, each of which contains a tag and its value. For more information, see [Tagging resources](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateInferenceProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "inferenceProfileArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateInferenceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [inferenceProfileArn](#API_CreateInferenceProfile_ResponseSyntax) **   <a name="bedrock-CreateInferenceProfile-response-inferenceProfileArn"></a>
The ARN of the inference profile that you created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+` 

 ** [status](#API_CreateInferenceProfile_ResponseSyntax) **   <a name="bedrock-CreateInferenceProfile-response-status"></a>
The status of the inference profile. `ACTIVE` means that the inference profile is ready to be used.  
Type: String  
Valid Values: `ACTIVE` 

## Errors
<a name="API_CreateInferenceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_CreateInferenceProfile_Examples"></a>

### Create an application inference profile from a foundation model
<a name="API_CreateInferenceProfile_Example_1"></a>

Run the following example to create an application inference profile from the Anthropic Claude 3 Sonnet model in the `us-west-2` region, replacing `${AccountId}` with your AWS account ID:

#### Sample Request
<a name="API_CreateInferenceProfile_Example_1_Request"></a>

```
POST /inference-profiles HTTP/1.1
Content-type: application/json

{
   "inferenceProfileName": "USClaudeSonnetApplicationIP",
   "modelSource": {
      "copyFrom": "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
   },
   "tags": [ 
      { 
         "key": "projectId",
         "value": "abcdef123456" 
      } 
   ]
}
```

### Create an application inference profile from a cross-region (system-defined) inference profile
<a name="API_CreateInferenceProfile_Example_2"></a>

Run the following example to create an application inference profile from the US Anthropic Claude 3 Sonnet inference profile in the `us-west-2` region, replacing `${AccountId}` with your AWS account ID:

#### Sample Request
<a name="API_CreateInferenceProfile_Example_2_Request"></a>

```
POST /inference-profiles HTTP/1.1
Content-type: application/json

{
   "inferenceProfileName": "USClaudeSonnetApplicationIP",
   "modelSource": {
      "copyFrom": "arn:aws:bedrock:us-west-2:${AccountId}:inference-profile/us.anthropic.claude-3-sonnet-20240229-v1:0"
   },
   "tags": [ 
      { 
         "key": "projectId",
         "value": "abcdef123456" 
      } 
   ]
}
```

## See Also
<a name="API_CreateInferenceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateInferenceProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateInferenceProfile) 