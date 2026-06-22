---
id: "@specs/aws/bedrock/docs/API_UpdateProvisionedModelThroughput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateProvisionedModelThroughput"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateProvisionedModelThroughput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateProvisionedModelThroughput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateProvisionedModelThroughput
<a name="API_UpdateProvisionedModelThroughput"></a>

Updates the name or associated model for a Provisioned Throughput. For more information, see [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_UpdateProvisionedModelThroughput_RequestSyntax"></a>

```
PATCH /provisioned-model-throughput/{{provisionedModelId}} HTTP/1.1
Content-type: application/json

{
   "desiredModelId": "{{string}}",
   "desiredProvisionedModelName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateProvisionedModelThroughput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [provisionedModelId](#API_UpdateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-UpdateProvisionedModelThroughput-request-uri-provisionedModelId"></a>
The Amazon Resource Name (ARN) or ID of the Provisioned Throughput to update.  
Pattern: `((([0-9a-zA-Z][_-]?)+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))`   
Required: Yes

## Request Body
<a name="API_UpdateProvisionedModelThroughput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [desiredModelId](#API_UpdateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-UpdateProvisionedModelThroughput-request-desiredModelId"></a>
The model ID (for a foundation model), name (for a custom model), or Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model.  
If this Provisioned Throughput is associated with a custom model, you can specify one of the following options:  
+ The base model from which the custom model was customized.
+ Another custom model that was customized from the same base model as the custom model.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)`   
Required: No

 ** [desiredProvisionedModelName](#API_UpdateProvisionedModelThroughput_RequestSyntax) **   <a name="bedrock-UpdateProvisionedModelThroughput-request-desiredProvisionedModelName"></a>
The new name for this Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: No

## Response Syntax
<a name="API_UpdateProvisionedModelThroughput_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateProvisionedModelThroughput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateProvisionedModelThroughput_Errors"></a>

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

## See Also
<a name="API_UpdateProvisionedModelThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateProvisionedModelThroughput) 