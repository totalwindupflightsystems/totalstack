---
id: "@specs/aws/bedrock/docs/API_GetModelCustomizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetModelCustomizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetModelCustomizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetModelCustomizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetModelCustomizationJob
<a name="API_GetModelCustomizationJob"></a>

Retrieves the properties associated with a model-customization job, including the status of the job. For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_GetModelCustomizationJob_RequestSyntax"></a>

```
GET /model-customization-jobs/{{jobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelCustomizationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_GetModelCustomizationJob_RequestSyntax) **   <a name="bedrock-GetModelCustomizationJob-request-uri-jobIdentifier"></a>
Identifier for the customization job.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*)`   
Required: Yes

## Request Body
<a name="API_GetModelCustomizationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelCustomizationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "baseModelArn": "string",
   "clientRequestToken": "string",
   "creationTime": "string",
   "customizationConfig": { ... },
   "customizationType": "string",
   "endTime": "string",
   "failureMessage": "string",
   "hyperParameters": { 
      "string" : "string" 
   },
   "jobArn": "string",
   "jobName": "string",
   "lastModifiedTime": "string",
   "outputDataConfig": { 
      "s3Uri": "string"
   },
   "outputModelArn": "string",
   "outputModelKmsKeyArn": "string",
   "outputModelName": "string",
   "roleArn": "string",
   "status": "string",
   "statusDetails": { 
      "dataProcessingDetails": { 
         "creationTime": "string",
         "lastModifiedTime": "string",
         "status": "string"
      },
      "trainingDetails": { 
         "creationTime": "string",
         "lastModifiedTime": "string",
         "status": "string"
      },
      "validationDetails": { 
         "creationTime": "string",
         "lastModifiedTime": "string",
         "status": "string"
      }
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
   ],
   "vpcConfig": { 
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetModelCustomizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseModelArn](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-baseModelArn"></a>
Amazon Resource Name (ARN) of the base model.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}` 

 ** [clientRequestToken](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-clientRequestToken"></a>
The token that you specified in the `CreateCustomizationJob` request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?` 

 ** [creationTime](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-creationTime"></a>
Time that the resource was created.  
Type: Timestamp

 ** [customizationConfig](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-customizationConfig"></a>
The customization configuration for the model customization job.  
Type: [CustomizationConfig](API_CustomizationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [customizationType](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-customizationType"></a>
The type of model customization.  
Type: String  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION | REINFORCEMENT_FINE_TUNING | IMPORTED` 

 ** [endTime](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-endTime"></a>
Time that the resource transitioned to terminal state.  
Type: Timestamp

 ** [failureMessage](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-failureMessage"></a>
Information about why the job failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [hyperParameters](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-hyperParameters"></a>
The hyperparameter values for the job. For details on the format for different models, see [Custom model hyperparameters](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html).  
Type: String to string map

 ** [jobArn](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the customization job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}` 

 ** [jobName](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-jobName"></a>
The name of the customization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*` 

 ** [lastModifiedTime](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-lastModifiedTime"></a>
Time that the resource was last modified.  
Type: Timestamp

 ** [outputDataConfig](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-outputDataConfig"></a>
Output data configuration   
Type: [OutputDataConfig](API_OutputDataConfig.md) object

 ** [outputModelArn](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-outputModelArn"></a>
The Amazon Resource Name (ARN) of the output model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:custom-model/(imported|[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12}` 

 ** [outputModelKmsKeyArn](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-outputModelKmsKeyArn"></a>
The custom model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [outputModelName](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-outputModelName"></a>
The name of the output model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}` 

 ** [roleArn](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-status"></a>
The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the job failed.  
Type: String  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped` 

 ** [statusDetails](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-statusDetails"></a>
For a Distillation job, the details about the statuses of the sub-tasks of the customization job.   
Type: [StatusDetails](API_StatusDetails.md) object

 ** [trainingDataConfig](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-trainingDataConfig"></a>
Contains information about the training dataset.  
Type: [TrainingDataConfig](API_TrainingDataConfig.md) object

 ** [trainingMetrics](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-trainingMetrics"></a>
Contains training metrics from the job creation.  
Type: [TrainingMetrics](API_TrainingMetrics.md) object

 ** [validationDataConfig](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-validationDataConfig"></a>
Contains information about the validation dataset.  
Type: [ValidationDataConfig](API_ValidationDataConfig.md) object

 ** [validationMetrics](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-validationMetrics"></a>
The loss metric for each validator that you provided in the createjob request.  
Type: Array of [ValidatorMetric](API_ValidatorMetric.md) objects

 ** [vpcConfig](#API_GetModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-GetModelCustomizationJob-response-vpcConfig"></a>
VPC configuration for the custom model job.  
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_GetModelCustomizationJob_Errors"></a>

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
<a name="API_GetModelCustomizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetModelCustomizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetModelCustomizationJob) 