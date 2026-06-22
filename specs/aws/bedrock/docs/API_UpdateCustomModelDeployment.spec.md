---
id: "@specs/aws/bedrock/docs/API_UpdateCustomModelDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCustomModelDeployment"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateCustomModelDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateCustomModelDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCustomModelDeployment
<a name="API_UpdateCustomModelDeployment"></a>

 Updates a custom model deployment with a new custom model. This allows you to deploy updated models without creating new deployment endpoints. 

## Request Syntax
<a name="API_UpdateCustomModelDeployment_RequestSyntax"></a>

```
PATCH /model-customization/custom-model-deployments/{{customModelDeploymentIdentifier}} HTTP/1.1
Content-type: application/json

{
   "modelArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCustomModelDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [customModelDeploymentIdentifier](#API_UpdateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-UpdateCustomModelDeployment-request-uri-customModelDeploymentIdentifier"></a>
 Identifier of the custom model deployment to update with the new custom model.   
Length Constraints: Minimum length of 1. Maximum length of 93.  
Pattern: `(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12})|^([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

## Request Body
<a name="API_UpdateCustomModelDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [modelArn](#API_UpdateCustomModelDeployment_RequestSyntax) **   <a name="bedrock-UpdateCustomModelDeployment-request-modelArn"></a>
 ARN of the new custom model to deploy. This replaces the currently deployed model.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}`   
Required: Yes

## Response Syntax
<a name="API_UpdateCustomModelDeployment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "customModelDeploymentArn": "string"
}
```

## Response Elements
<a name="API_UpdateCustomModelDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [customModelDeploymentArn](#API_UpdateCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-UpdateCustomModelDeployment-response-customModelDeploymentArn"></a>
 ARN of the custom model deployment being updated.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12}` 

## Errors
<a name="API_UpdateCustomModelDeployment_Errors"></a>

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
<a name="API_UpdateCustomModelDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateCustomModelDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateCustomModelDeployment) 