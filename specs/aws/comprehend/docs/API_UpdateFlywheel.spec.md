---
id: "@specs/aws/comprehend/docs/API_UpdateFlywheel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFlywheel"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# UpdateFlywheel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_UpdateFlywheel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFlywheel
<a name="API_UpdateFlywheel"></a>

Update the configuration information for an existing flywheel.

## Request Syntax
<a name="API_UpdateFlywheel_RequestSyntax"></a>

```
{
   "ActiveModelArn": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DataSecurityConfig": { 
      "ModelKmsKeyId": "{{string}}",
      "VolumeKmsKeyId": "{{string}}",
      "VpcConfig": { 
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "FlywheelArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFlywheel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActiveModelArn](#API_UpdateFlywheel_RequestSyntax) **   <a name="comprehend-UpdateFlywheel-request-ActiveModelArn"></a>
The Amazon Resource Number (ARN) of the active model version.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** [DataAccessRoleArn](#API_UpdateFlywheel_RequestSyntax) **   <a name="comprehend-UpdateFlywheel-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** [DataSecurityConfig](#API_UpdateFlywheel_RequestSyntax) **   <a name="comprehend-UpdateFlywheel-request-DataSecurityConfig"></a>
Flywheel data security configuration.  
Type: [UpdateDataSecurityConfig](API_UpdateDataSecurityConfig.md) object  
Required: No

 ** [FlywheelArn](#API_UpdateFlywheel_RequestSyntax) **   <a name="comprehend-UpdateFlywheel-request-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel to update.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

## Response Syntax
<a name="API_UpdateFlywheel_ResponseSyntax"></a>

```
{
   "FlywheelProperties": { 
      "ActiveModelArn": "string",
      "CreationTime": number,
      "DataAccessRoleArn": "string",
      "DataLakeS3Uri": "string",
      "DataSecurityConfig": { 
         "DataLakeKmsKeyId": "string",
         "ModelKmsKeyId": "string",
         "VolumeKmsKeyId": "string",
         "VpcConfig": { 
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ]
         }
      },
      "FlywheelArn": "string",
      "LastModifiedTime": number,
      "LatestFlywheelIteration": "string",
      "Message": "string",
      "ModelType": "string",
      "Status": "string",
      "TaskConfig": { 
         "DocumentClassificationConfig": { 
            "Labels": [ "string" ],
            "Mode": "string"
         },
         "EntityRecognitionConfig": { 
            "EntityTypes": [ 
               { 
                  "Type": "string"
               }
            ]
         },
         "LanguageCode": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateFlywheel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlywheelProperties](#API_UpdateFlywheel_ResponseSyntax) **   <a name="comprehend-UpdateFlywheel-response-FlywheelProperties"></a>
The flywheel properties.  
Type: [FlywheelProperties](API_FlywheelProperties.md) object

## Errors
<a name="API_UpdateFlywheel_Errors"></a>

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

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateFlywheel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/UpdateFlywheel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/UpdateFlywheel) 