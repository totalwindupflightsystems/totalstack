---
id: "@specs/aws/bedrock/docs/API_CreateCustomModelDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomModelDeployment"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateCustomModelDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateCustomModelDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomModelDeployment
<a name="API_CreateCustomModelDeployment"></a>

Deploys a custom model for on-demand inference in Amazon Bedrock. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the `modelId` parameter when you submit prompts and generate responses with model inference.

 For more information about setting up on-demand inference for custom models, see [Set up inference for a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html). 

The following actions are related to the `CreateCustomModelDeployment` operation:
+  [GetCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html) 
+  [ListCustomModelDeployments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html) 
+  [DeleteCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html) 

## Request Syntax
<a name="API_CreateCustomModelDeployment_RequestSyntax"></a>

```
POST /model-customization/custom-model-deployments HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "modelArn": "{{string}}",
   "modelDeploymentName": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCustomModelDeployment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCustomModelDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-CreateCustomModelDeployment-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [description](#API_CreateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-CreateCustomModelDeployment-request-description"></a>
A description for the custom model deployment to help you identify its purpose.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*`   
Required: No

 ** [modelArn](#API_CreateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-CreateCustomModelDeployment-request-modelArn"></a>
The Amazon Resource Name (ARN) of the custom model to deploy for on-demand inference. The custom model must be in the `Active` state.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}`   
Required: Yes

 ** [modelDeploymentName](#API_CreateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-CreateCustomModelDeployment-request-modelDeploymentName"></a>
The name for the custom model deployment. The name must be unique within your AWS account and Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** [tags](#API_CreateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-CreateCustomModelDeployment-request-tags"></a>
Tags to assign to the custom model deployment. You can use tags to organize and track your AWS resources for cost allocation and management purposes.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateCustomModelDeployment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "customModelDeploymentArn": "string"
}
```

## Response Elements
<a name="API_CreateCustomModelDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [customModelDeploymentArn](#API_CreateCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-CreateCustomModelDeployment-response-customModelDeploymentArn"></a>
The Amazon Resource Name (ARN) of the custom model deployment. Use this ARN as the `modelId` parameter when invoking the model with the `InvokeModel` or `Converse` operations.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12}` 

## Errors
<a name="API_CreateCustomModelDeployment_Errors"></a>

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

## Examples
<a name="API_CreateCustomModelDeployment_Examples"></a>

### Example request
<a name="API_CreateCustomModelDeployment_Example_1"></a>

This example illustrates one usage of CreateCustomModelDeployment.

```
POST /model-customization/custom-model-deployments HTTP/1.1
Content-type: application/json

{
    "clientRequestToken": "unique-deployment-token-456",
    "description": "Production deployment of my custom model for customer support chatbot",
    "modelArn": "arn:aws:bedrock:us-west-2:123456789012:custom-model-deployment/abc123def456",
    "modelDeploymentName": "customer-support-model-deployment",
    "tags": [
        {
            "key": "Environment",
            "value": "Production"
        },
        {
            "key": "Application",
            "value": "CustomerSupport"
        },
        {
            "key": "CostCenter",
            "value": "Engineering"
        }
    ]
}
```

## See Also
<a name="API_CreateCustomModelDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateCustomModelDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateCustomModelDeployment) 