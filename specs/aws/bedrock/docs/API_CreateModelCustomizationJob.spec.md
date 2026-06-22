---
id: "@specs/aws/bedrock/docs/API_CreateModelCustomizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateModelCustomizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateModelCustomizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateModelCustomizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateModelCustomizationJob
<a name="API_CreateModelCustomizationJob"></a>

Creates a fine-tuning job to customize a base model.

You specify the base foundation model and the location of the training data. After the model-customization job completes successfully, your custom model resource will be ready to use. Amazon Bedrock returns validation loss metrics and output generations after the job completes. 

For information on the format of training and validation data, see [Prepare the datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html).

 Model-customization jobs are asynchronous and the completion time depends on the base model and the training/validation data size. To monitor a job, use the `GetModelCustomizationJob` operation to retrieve the job status.

For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_CreateModelCustomizationJob_RequestSyntax"></a>

```
POST /model-customization-jobs HTTP/1.1
Content-type: application/json

{
   "baseModelIdentifier": "{{string}}",
   "clientRequestToken": "{{string}}",
   "customizationConfig": { ... },
   "customizationType": "{{string}}",
   "customModelKmsKeyId": "{{string}}",
   "customModelName": "{{string}}",
   "customModelTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "hyperParameters": { 
      "{{string}}" : "{{string}}" 
   },
   "jobName": "{{string}}",
   "jobTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "outputDataConfig": { 
      "s3Uri": "{{string}}"
   },
   "roleArn": "{{string}}",
   "trainingDataConfig": { 
      "invocationLogsConfig": { 
         "invocationLogSource": { ... },
         "requestMetadataFilters": { ... },
         "usePromptResponse": {{boolean}}
      },
      "s3Uri": "{{string}}"
   },
   "validationDataConfig": { 
      "validators": [ 
         { 
            "s3Uri": "{{string}}"
         }
      ]
   },
   "vpcConfig": { 
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateModelCustomizationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateModelCustomizationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [baseModelIdentifier](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-baseModelIdentifier"></a>
Name of the base model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

 ** [clientRequestToken](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [customizationConfig](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-customizationConfig"></a>
The customization configuration for the model customization job.  
Type: [CustomizationConfig](API_CustomizationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [customizationType](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-customizationType"></a>
The customization type.  
Type: String  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION`   
Required: No

 ** [customModelKmsKeyId](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-customModelKmsKeyId"></a>
The custom model is encrypted at rest using this key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [customModelName](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-customModelName"></a>
A name for the resulting custom model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?){1,63}`   
Required: Yes

 ** [customModelTags](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-customModelTags"></a>
Tags to attach to the resulting custom model.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [hyperParameters](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-hyperParameters"></a>
Parameters related to tuning the model. For details on the format for different models, see [Custom model hyperparameters](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html).  
Type: String to string map  
Required: No

 ** [jobName](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-jobName"></a>
A name for the fine-tuning job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9\+\-\.])*`   
Required: Yes

 ** [jobTags](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-jobTags"></a>
Tags to attach to the job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [outputDataConfig](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-outputDataConfig"></a>
S3 location for the output data.  
Type: [OutputDataConfig](API_OutputDataConfig.md) object  
Required: Yes

 ** [roleArn](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to read input data from an S3 bucket, write model artifacts to an S3 bucket. To pass this role to Amazon Bedrock, the caller of this API must have the `iam:PassRole` permission.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [trainingDataConfig](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-trainingDataConfig"></a>
Information about the training dataset.  
Type: [TrainingDataConfig](API_TrainingDataConfig.md) object  
Required: Yes

 ** [validationDataConfig](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-validationDataConfig"></a>
Information about the validation dataset.   
Type: [ValidationDataConfig](API_ValidationDataConfig.md) object  
Required: No

 ** [vpcConfig](#API_CreateModelCustomizationJob_RequestSyntax) **   <a name="bedrock-CreateModelCustomizationJob-request-vpcConfig"></a>
The configuration of the Virtual Private Cloud (VPC) that contains the resources that you're using for this job. For more information, see [Protect your model customization jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-model-customization.html).  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateModelCustomizationJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateModelCustomizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateModelCustomizationJob_ResponseSyntax) **   <a name="bedrock-CreateModelCustomizationJob-response-jobArn"></a>
Amazon Resource Name (ARN) of the fine tuning job  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-customization-job/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}/[a-z0-9]{12}` 

## Errors
<a name="API_CreateModelCustomizationJob_Errors"></a>

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

## See Also
<a name="API_CreateModelCustomizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateModelCustomizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateModelCustomizationJob) 