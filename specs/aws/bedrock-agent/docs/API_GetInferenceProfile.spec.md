---
id: "@specs/aws/bedrock-agent/docs/API_GetInferenceProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetInferenceProfile"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetInferenceProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetInferenceProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetInferenceProfile
<a name="API_GetInferenceProfile"></a>

Gets information about an inference profile. For more information, see [Increase throughput and resilience with cross-region inference in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_GetInferenceProfile_RequestSyntax"></a>

```
GET /inference-profiles/{{inferenceProfileIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInferenceProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [inferenceProfileIdentifier](#API_GetInferenceProfile_RequestSyntax) **   <a name="bedrock-GetInferenceProfile-request-uri-inferenceProfileIdentifier"></a>
The ID or Amazon Resource Name (ARN) of the inference profile.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/)?[a-zA-Z0-9-:.]+`   
Required: Yes

## Request Body
<a name="API_GetInferenceProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInferenceProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "inferenceProfileArn": "string",
   "inferenceProfileId": "string",
   "inferenceProfileName": "string",
   "models": [ 
      { 
         "modelArn": "string"
      }
   ],
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetInferenceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-createdAt"></a>
The time at which the inference profile was created.  
Type: Timestamp

 ** [description](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-description"></a>
The description of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+` 

 ** [inferenceProfileArn](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-inferenceProfileArn"></a>
The Amazon Resource Name (ARN) of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+` 

 ** [inferenceProfileId](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-inferenceProfileId"></a>
The unique identifier of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-:.]+` 

 ** [inferenceProfileName](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-inferenceProfileName"></a>
The name of the inference profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+` 

 ** [models](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-models"></a>
A list of information about each model in the inference profile.  
Type: Array of [InferenceProfileModel](API_InferenceProfileModel.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [status](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-status"></a>
The status of the inference profile. `ACTIVE` means that the inference profile is ready to be used.  
Type: String  
Valid Values: `ACTIVE` 

 ** [type](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-type"></a>
The type of the inference profile. The following types are possible:  
+  `SYSTEM_DEFINED` – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.
+  `APPLICATION` – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.
Type: String  
Valid Values: `SYSTEM_DEFINED | APPLICATION` 

 ** [updatedAt](#API_GetInferenceProfile_ResponseSyntax) **   <a name="bedrock-GetInferenceProfile-response-updatedAt"></a>
The time at which the inference profile was last updated.  
Type: Timestamp

## Errors
<a name="API_GetInferenceProfile_Errors"></a>

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
<a name="API_GetInferenceProfile_Examples"></a>

### Get information about an inference profile
<a name="API_GetInferenceProfile_Example_1"></a>

Run the following example to get information about the US Anthropic Claude 3 Sonnet inference profile:

#### Sample Request
<a name="API_GetInferenceProfile_Example_1_Request"></a>

```
GET /inference-profiles/us.anthropic.claude-3-sonnet-20240229-v1:0 HTTP/1.1
```

## See Also
<a name="API_GetInferenceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetInferenceProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetInferenceProfile) 