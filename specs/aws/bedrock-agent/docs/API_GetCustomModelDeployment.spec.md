---
id: "@specs/aws/bedrock-agent/docs/API_GetCustomModelDeployment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCustomModelDeployment"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetCustomModelDeployment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetCustomModelDeployment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCustomModelDeployment
<a name="API_GetCustomModelDeployment"></a>

Retrieves information about a custom model deployment, including its status, configuration, and metadata. Use this operation to monitor the deployment status and retrieve details needed for inference requests.

The following actions are related to the `GetCustomModelDeployment` operation:
+  [CreateCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html) 
+  [ListCustomModelDeployments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html) 
+  [DeleteCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html) 

## Request Syntax
<a name="API_GetCustomModelDeployment_RequestSyntax"></a>

```
GET /model-customization/custom-model-deployments/{{customModelDeploymentIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomModelDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [customModelDeploymentIdentifier](#API_GetCustomModelDeployment_RequestSyntax) **   <a name="bedrock-GetCustomModelDeployment-request-uri-customModelDeploymentIdentifier"></a>
The Amazon Resource Name (ARN) or name of the custom model deployment to retrieve information about.  
Length Constraints: Minimum length of 1. Maximum length of 93.  
Pattern: `(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12})|^([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

## Request Body
<a name="API_GetCustomModelDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomModelDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "customModelDeploymentArn": "string",
   "description": "string",
   "failureMessage": "string",
   "lastUpdatedAt": "string",
   "modelArn": "string",
   "modelDeploymentName": "string",
   "status": "string",
   "updateDetails": { 
      "modelArn": "string",
      "updateStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetCustomModelDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-createdAt"></a>
The date and time when the custom model deployment was created.  
Type: Timestamp

 ** [customModelDeploymentArn](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-customModelDeploymentArn"></a>
The Amazon Resource Name (ARN) of the custom model deployment.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model-deployment/[a-z0-9]{12}` 

 ** [description](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-description"></a>
The description of the custom model deployment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*` 

 ** [failureMessage](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-failureMessage"></a>
If the deployment status is `FAILED`, this field contains a message describing the failure reason.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [lastUpdatedAt](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-lastUpdatedAt"></a>
The date and time when the custom model deployment was last updated.  
Type: Timestamp

 ** [modelArn](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-modelArn"></a>
The Amazon Resource Name (ARN) of the custom model associated with this deployment.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}` 

 ** [modelDeploymentName](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-modelDeploymentName"></a>
The name of the custom model deployment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [status](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-status"></a>
The status of the custom model deployment. Possible values are:  
+  `CREATING` - The deployment is being set up and prepared for inference.
+  `ACTIVE` - The deployment is ready and available for inference requests.
+  `FAILED` - The deployment failed to be created or became unavailable.
Type: String  
Valid Values: `Creating | Active | Failed` 

 ** [updateDetails](#API_GetCustomModelDeployment_ResponseSyntax) **   <a name="bedrock-GetCustomModelDeployment-response-updateDetails"></a>
 Details about any pending or completed updates to the custom model deployment, including the new model ARN and update status.   
Type: [CustomModelDeploymentUpdateDetails](API_CustomModelDeploymentUpdateDetails.md) object

## Errors
<a name="API_GetCustomModelDeployment_Errors"></a>

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
<a name="API_GetCustomModelDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetCustomModelDeployment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetCustomModelDeployment) 