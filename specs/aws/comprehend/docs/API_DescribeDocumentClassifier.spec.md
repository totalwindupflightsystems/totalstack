---
id: "@specs/aws/comprehend/docs/API_DescribeDocumentClassifier"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDocumentClassifier"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DescribeDocumentClassifier

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DescribeDocumentClassifier
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDocumentClassifier
<a name="API_DescribeDocumentClassifier"></a>

Gets the properties associated with a document classifier.

## Request Syntax
<a name="API_DescribeDocumentClassifier_RequestSyntax"></a>

```
{
   "DocumentClassifierArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDocumentClassifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentClassifierArn](#API_DescribeDocumentClassifier_RequestSyntax) **   <a name="comprehend-DescribeDocumentClassifier-request-DocumentClassifierArn"></a>
The Amazon Resource Name (ARN) that identifies the document classifier. The `CreateDocumentClassifier` operation returns this identifier in its response.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws[A-Za-z0-9-]{0,63}:comprehend:[A-Za-z0-9-]{0,63}:([0-9]{12}|aws):document-classifier/[A-Za-z0-9-]{0,63}(/version/[A-Za-z0-9-]{0,63})?`   
Required: Yes

## Response Syntax
<a name="API_DescribeDocumentClassifier_ResponseSyntax"></a>

```
{
   "DocumentClassifierProperties": { 
      "ClassifierMetadata": { 
         "EvaluationMetrics": { 
            "Accuracy": number,
            "F1Score": number,
            "HammingLoss": number,
            "MicroF1Score": number,
            "MicroPrecision": number,
            "MicroRecall": number,
            "Precision": number,
            "Recall": number
         },
         "NumberOfLabels": number,
         "NumberOfTestDocuments": number,
         "NumberOfTrainedDocuments": number
      },
      "DataAccessRoleArn": "string",
      "DocumentClassifierArn": "string",
      "EndTime": number,
      "FlywheelArn": "string",
      "InputDataConfig": { 
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
         "DocumentReaderConfig": { 
            "DocumentReadAction": "string",
            "DocumentReadMode": "string",
            "FeatureTypes": [ "string" ]
         },
         "Documents": { 
            "S3Uri": "string",
            "TestS3Uri": "string"
         },
         "DocumentType": "string",
         "LabelDelimiter": "string",
         "S3Uri": "string",
         "TestS3Uri": "string"
      },
      "LanguageCode": "string",
      "Message": "string",
      "Mode": "string",
      "ModelKmsKeyId": "string",
      "OutputDataConfig": { 
         "FlywheelStatsS3Prefix": "string",
         "KmsKeyId": "string",
         "S3Uri": "string"
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
<a name="API_DescribeDocumentClassifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentClassifierProperties](#API_DescribeDocumentClassifier_ResponseSyntax) **   <a name="comprehend-DescribeDocumentClassifier-response-DocumentClassifierProperties"></a>
An object that contains the properties associated with a document classifier.  
Type: [DocumentClassifierProperties](API_DocumentClassifierProperties.md) object

## Errors
<a name="API_DescribeDocumentClassifier_Errors"></a>

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
<a name="API_DescribeDocumentClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DescribeDocumentClassifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DescribeDocumentClassifier) 