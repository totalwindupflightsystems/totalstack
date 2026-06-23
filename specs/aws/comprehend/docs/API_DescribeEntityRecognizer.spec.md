---
id: "@specs/aws/comprehend/docs/API_DescribeEntityRecognizer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEntityRecognizer"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DescribeEntityRecognizer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DescribeEntityRecognizer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEntityRecognizer
<a name="API_DescribeEntityRecognizer"></a>

Provides details about an entity recognizer including status, S3 buckets containing training data, recognizer metadata, metrics, and so on.

## Request Syntax
<a name="API_DescribeEntityRecognizer_RequestSyntax"></a>

```
{
   "EntityRecognizerArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEntityRecognizer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EntityRecognizerArn](#API_DescribeEntityRecognizer_RequestSyntax) **   <a name="comprehend-DescribeEntityRecognizer-request-EntityRecognizerArn"></a>
The Amazon Resource Name (ARN) that identifies the entity recognizer.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: Yes

## Response Syntax
<a name="API_DescribeEntityRecognizer_ResponseSyntax"></a>

```
{
   "EntityRecognizerProperties": { 
      "DataAccessRoleArn": "string",
      "EndTime": number,
      "EntityRecognizerArn": "string",
      "FlywheelArn": "string",
      "InputDataConfig": { 
         "Annotations": { 
            "S3Uri": "string",
            "TestS3Uri": "string"
         },
         "AugmentedManifests": [ 
            { 
               "AnnotationDataS3Uri": "string",
               "AttributeNames": [ "string" ],
               "DocumentType": "string",
               "S3Uri": "string",
               "SourceDocumentsS3Uri": "string",
               "Split": "string"
            }
         ],
         "DataFormat": "string",
         "Documents": { 
            "InputFormat": "string",
            "S3Uri": "string",
            "TestS3Uri": "string"
         },
         "EntityList": { 
            "S3Uri": "string"
         },
         "EntityTypes": [ 
            { 
               "Type": "string"
            }
         ]
      },
      "LanguageCode": "string",
      "Message": "string",
      "ModelKmsKeyId": "string",
      "OutputDataConfig": { 
         "FlywheelStatsS3Prefix": "string"
      },
      "RecognizerMetadata": { 
         "EntityTypes": [ 
            { 
               "EvaluationMetrics": { 
                  "F1Score": number,
                  "Precision": number,
                  "Recall": number
               },
               "NumberOfTrainMentions": number,
               "Type": "string"
            }
         ],
         "EvaluationMetrics": { 
            "F1Score": number,
            "Precision": number,
            "Recall": number
         },
         "NumberOfTestDocuments": number,
         "NumberOfTrainedDocuments": number
      },
      "SourceModelArn": "string",
      "Status": "string",
      "SubmitTime": number,
      "TrainingEndTime": number,
      "TrainingStartTime": number,
      "VersionName": "string",
      "VolumeKmsKeyId": "string",
      "VpcConfig": { 
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_DescribeEntityRecognizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntityRecognizerProperties](#API_DescribeEntityRecognizer_ResponseSyntax) **   <a name="comprehend-DescribeEntityRecognizer-response-EntityRecognizerProperties"></a>
Describes information associated with an entity recognizer.  
Type: [EntityRecognizerProperties](API_EntityRecognizerProperties.md) object

## Errors
<a name="API_DescribeEntityRecognizer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeEntityRecognizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DescribeEntityRecognizer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DescribeEntityRecognizer) 