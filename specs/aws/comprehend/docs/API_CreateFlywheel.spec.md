---
id: "@specs/aws/comprehend/docs/API_CreateFlywheel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFlywheel"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# CreateFlywheel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_CreateFlywheel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFlywheel
<a name="API_CreateFlywheel"></a>

A flywheel is an AWS resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.

When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.

To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.

To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.

For more information about flywheels, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_CreateFlywheel_RequestSyntax"></a>

```
{
   "ActiveModelArn": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DataLakeS3Uri": "{{string}}",
   "DataSecurityConfig": { 
      "DataLakeKmsKeyId": "{{string}}",
      "ModelKmsKeyId": "{{string}}",
      "VolumeKmsKeyId": "{{string}}",
      "VpcConfig": { 
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "FlywheelName": "{{string}}",
   "ModelType": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TaskConfig": { 
      "DocumentClassificationConfig": { 
         "Labels": [ "{{string}}" ],
         "Mode": "{{string}}"
      },
      "EntityRecognitionConfig": { 
         "EntityTypes": [ 
            { 
               "Type": "{{string}}"
            }
         ]
      },
      "LanguageCode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateFlywheel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActiveModelArn](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-ActiveModelArn"></a>
To associate an existing model with the flywheel, specify the Amazon Resource Number (ARN) of the model version. Do not set `TaskConfig` or `ModelType` if you specify an `ActiveModelArn`.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** [ClientRequestToken](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-ClientRequestToken"></a>
A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [DataAccessRoleArn](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: Yes

 ** [DataLakeS3Uri](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-DataLakeS3Uri"></a>
Enter the S3 location for the data lake. You can specify a new S3 bucket or a new folder of an existing S3 bucket. The flywheel creates the data lake at this location.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** [DataSecurityConfig](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-DataSecurityConfig"></a>
Data security configurations.  
Type: [DataSecurityConfig](API_DataSecurityConfig.md) object  
Required: No

 ** [FlywheelName](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-FlywheelName"></a>
Name for the flywheel.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`   
Required: Yes

 ** [ModelType](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-ModelType"></a>
The model type. You need to set `ModelType` if you are creating a flywheel for a new model.  
Type: String  
Valid Values: `DOCUMENT_CLASSIFIER | ENTITY_RECOGNIZER`   
Required: No

 ** [Tags](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-Tags"></a>
The tags to associate with this flywheel.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TaskConfig](#API_CreateFlywheel_RequestSyntax) **   <a name="comprehend-CreateFlywheel-request-TaskConfig"></a>
Configuration about the model associated with the flywheel. You need to set `TaskConfig` if you are creating a flywheel for a new model.  
Type: [TaskConfig](API_TaskConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateFlywheel_ResponseSyntax"></a>

```
{
   "ActiveModelArn": "string",
   "FlywheelArn": "string"
}
```

## Response Elements
<a name="API_CreateFlywheel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActiveModelArn](#API_CreateFlywheel_ResponseSyntax) **   <a name="comprehend-CreateFlywheel-response-ActiveModelArn"></a>
The Amazon Resource Number (ARN) of the active model version.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?` 

 ** [FlywheelArn](#API_CreateFlywheel_ResponseSyntax) **   <a name="comprehend-CreateFlywheel-response-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*` 

## Errors
<a name="API_CreateFlywheel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** KmsKeyValidationException **   
The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource name is already in use. Use a different name and try your request again.  
HTTP Status Code: 400

 ** ResourceLimitExceededException **   
The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** ResourceUnavailableException **   
The specified resource is not available. Check the resource and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.   
HTTP Status Code: 400

 ** UnsupportedLanguageException **   
Amazon Comprehend can't process the language of the input text. For a list of supported languages, [Supported languages](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html) in the Comprehend Developer Guide.   
HTTP Status Code: 400

## See Also
<a name="API_CreateFlywheel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/CreateFlywheel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/CreateFlywheel) 