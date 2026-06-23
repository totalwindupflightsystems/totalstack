---
id: "@specs/aws/comprehend/docs/API_ListDocumentClassifiers"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDocumentClassifiers"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ListDocumentClassifiers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ListDocumentClassifiers
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDocumentClassifiers
<a name="API_ListDocumentClassifiers"></a>

Gets a list of the document classifiers that you have created.

## Request Syntax
<a name="API_ListDocumentClassifiers_RequestSyntax"></a>

```
{
   "Filter": { 
      "DocumentClassifierName": "{{string}}",
      "Status": "{{string}}",
      "SubmitTimeAfter": {{number}},
      "SubmitTimeBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDocumentClassifiers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListDocumentClassifiers_RequestSyntax) **   <a name="comprehend-ListDocumentClassifiers-request-Filter"></a>
Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.  
Type: [DocumentClassifierFilter](API_DocumentClassifierFilter.md) object  
Required: No

 ** [MaxResults](#API_ListDocumentClassifiers_RequestSyntax) **   <a name="comprehend-ListDocumentClassifiers-request-MaxResults"></a>
The maximum number of results to return in each page. The default is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListDocumentClassifiers_RequestSyntax) **   <a name="comprehend-ListDocumentClassifiers-request-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ListDocumentClassifiers_ResponseSyntax"></a>

```
{
   "DocumentClassifierPropertiesList": [ 
      { 
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDocumentClassifiers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentClassifierPropertiesList](#API_ListDocumentClassifiers_ResponseSyntax) **   <a name="comprehend-ListDocumentClassifiers-response-DocumentClassifierPropertiesList"></a>
A list containing the properties of each job returned.  
Type: Array of [DocumentClassifierProperties](API_DocumentClassifierProperties.md) objects

 ** [NextToken](#API_ListDocumentClassifiers_ResponseSyntax) **   <a name="comprehend-ListDocumentClassifiers-response-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListDocumentClassifiers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidFilterException **   
The filter specified for the operation is invalid. Specify a different filter.  
HTTP Status Code: 400

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_ListDocumentClassifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListDocumentClassifiers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListDocumentClassifiers) 