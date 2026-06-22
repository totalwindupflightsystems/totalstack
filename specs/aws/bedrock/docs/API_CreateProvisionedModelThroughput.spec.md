---
id: "@specs/aws/bedrock/docs/API_CreateProvisionedModelThroughput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProvisionedModelThroughput"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateProvisionedModelThroughput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateProvisionedModelThroughput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProvisionedModelThroughput
<a name="API_CreateProvisionedModelThroughput"></a>

Creates dedicated throughput for a base or custom model with the model units and for the duration that you specify. For pricing details, see [Amazon Bedrock Pricing](http://aws.amazon.com/bedrock/pricing/). For more information, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_CreateProvisionedModelThroughput_RequestSyntax"></a>

```
POST /provisioned-model-throughput HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "commitmentDuration": "{{string}}",
   "modelId": "{{string}}",
   "modelUnits": {{number}},
   "provisionedModelName": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateProvisionedModelThroughput_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProvisionedModelThroughput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the Amazon S3 User Guide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [commitmentDuration](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-commitmentDuration"></a>
The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.  
Custom models support all levels of commitment. To see which base models support no commitment, see [Supported regions and models for Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html)   
Type: String  
Valid Values: `OneMonth | SixMonths`   
Required: No

 ** [modelId](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-modelId"></a>
The model ID (for a foundation model), name (for a custom model), or Amazon Resource Name (ARN) of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see [Amazon Bedrock model IDs for purchasing Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

 ** [modelUnits](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-modelUnits"></a>
Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the [AWS support center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase) to request MUs.  
For model unit quotas, see [Provisioned Throughput quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).  
For more information about what an MU specifies, contact your AWS account manager.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

 ** [provisionedModelName](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-provisionedModelName"></a>
The name for this Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: Yes

 ** [tags](#API_CreateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-request-tags"></a>
Tags to associate with this Provisioned Throughput.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateProvisionedModelThroughput_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "provisionedModelArn": "string"
}
```

## Response Elements
<a name="API_CreateProvisionedModelThroughput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [provisionedModelArn](#API_CreateProvisionedModelThroughput_ResponseSyntax) **   <a name="bedrock-CreateProvisionedModelThroughput-response-provisionedModelArn"></a>
The Amazon Resource Name (ARN) for this Provisioned Throughput.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}` 

## Errors
<a name="API_CreateProvisionedModelThroughput_Errors"></a>

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

## See Also
<a name="API_CreateProvisionedModelThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateProvisionedModelThroughput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateProvisionedModelThroughput) 