---
id: "@specs/aws/bedrock-agent/docs/API_GetCustomModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCustomModel"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetCustomModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetCustomModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCustomModel
<a name="API_GetCustomModel"></a>

Get the properties associated with a Amazon Bedrock custom model that you have created. For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_GetCustomModel_RequestSyntax"></a>

```
GET /custom-models/{{modelIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelIdentifier](#API_GetCustomModel_RequestSyntax) **   <a name="bedrock-GetCustomModel-request-uri-modelIdentifier"></a>
Name or Amazon Resource Name (ARN) of the custom model.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

## Request Body
<a name="API_GetCustomModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "baseModelArn": "string",
   "creationTime": "string",
   "customizationConfig": { ... },
   "customizationType": "string",
   "failureMessage": "string",
   "hyperParameters": { 
      "string" : "string" 
   },
   "jobArn": "string",
   "jobName": "string",
   "modelArn": "string",
   "modelKmsKeyArn": "string",
   "modelName": "string",
   "modelStatus": "string",
   "outputDataConfig": { 
      "s3Uri": "string"
   },
   "trainingDataConfig": { 
      "invocationLogsConfig": { 
         "invocationLogSource": { ... },
         "requestMetadataFilters": { ... },
         "usePromptResponse": boolean
      },
      "s3Uri": "string"
   },
   "trainingMetrics": { 
      "trainingLoss": number
   },
   "validationDataConfig": { 
      "validators": [ 
         { 
            "s3Uri": "string"
         }
      ]
   },
   "validationMetrics": [ 
      { 
         "validationLoss": number
      }
   ]
}
```

## Response Elements
<a name="API_GetCustomModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseModelArn](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-baseModelArn"></a>
Amazon Resource Name (ARN) of the base model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [creationTime](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-creationTime"></a>
Creation time of the model.  
Type: Timestamp

 ** [customizationConfig](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-customizationConfig"></a>
The customization configuration for the custom model.  
Type: [CustomizationConfig](API_CustomizationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [customizationType](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-customizationType"></a>
The type of model customization.  
Type: String  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION | REINFORCEMENT_FINE_TUNING | IMPORTED` 

 ** [failureMessage](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-failureMessage"></a>
A failure message for any issues that occurred when creating the custom model. This is included for only a failed CreateCustomModel operation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [hyperParameters](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-hyperParameters"></a>
Hyperparameter values associated with this model. For details on the format for different models, see [Custom model hyperparameters](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html).  
Type: String to string map

 ** [jobArn](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-jobArn"></a>
Job Amazon Resource Name (ARN) associated with this model. For models that you create with the [CreateCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html) API operation, this is `NULL`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}` 

 ** [jobName](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-jobName"></a>
Job name associated with this model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [modelArn](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-modelArn"></a>
Amazon Resource Name (ARN) associated with this model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))` 

 ** [modelKmsKeyArn](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-modelKmsKeyArn"></a>
The custom model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [modelName](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-modelName"></a>
Model name associated with this model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [modelStatus](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-modelStatus"></a>
The current status of the custom model. Possible values include:  
+  `Creating` - The model is being created and validated.
+  `Active` - The model has been successfully created and is ready for use.
+  `Failed` - The model creation process failed. Check the `failureMessage` field for details.
Type: String  
Valid Values: `Active | Creating | Failed` 

 ** [outputDataConfig](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-outputDataConfig"></a>
Output data configuration associated with this custom model.  
Type: [OutputDataConfig](API_OutputDataConfig.md) object

 ** [trainingDataConfig](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-trainingDataConfig"></a>
Contains information about the training dataset.  
Type: [TrainingDataConfig](API_TrainingDataConfig.md) object

 ** [trainingMetrics](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-trainingMetrics"></a>
Contains training metrics from the job creation.  
Type: [TrainingMetrics](API_TrainingMetrics.md) object

 ** [validationDataConfig](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-validationDataConfig"></a>
Contains information about the validation dataset.  
Type: [ValidationDataConfig](API_ValidationDataConfig.md) object

 ** [validationMetrics](#API_GetCustomModel_ResponseSyntax) **   <a name="bedrock-GetCustomModel-response-validationMetrics"></a>
The validation metrics from the job creation.  
Type: Array of [ValidatorMetric](API_ValidatorMetric.md) objects

## Errors
<a name="API_GetCustomModel_Errors"></a>

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
<a name="API_GetCustomModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetCustomModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetCustomModel) 