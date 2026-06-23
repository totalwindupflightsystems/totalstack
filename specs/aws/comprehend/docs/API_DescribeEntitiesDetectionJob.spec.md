---
id: "@specs/aws/comprehend/docs/API_DescribeEntitiesDetectionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEntitiesDetectionJob"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DescribeEntitiesDetectionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DescribeEntitiesDetectionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEntitiesDetectionJob
<a name="API_DescribeEntitiesDetectionJob"></a>

Gets the properties associated with an entities detection job. Use this operation to get the status of a detection job.

## Request Syntax
<a name="API_DescribeEntitiesDetectionJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEntitiesDetectionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeEntitiesDetectionJob_RequestSyntax) **   <a name="comprehend-DescribeEntitiesDetectionJob-request-JobId"></a>
The identifier that Amazon Comprehend generated for the job. The `StartEntitiesDetectionJob` operation returns this identifier in its response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`   
Required: Yes

## Response Syntax
<a name="API_DescribeEntitiesDetectionJob_ResponseSyntax"></a>

```
{
   "EntitiesDetectionJobProperties": { 
      "DataAccessRoleArn": "string",
      "EndTime": number,
      "EntityRecognizerArn": "string",
      "FlywheelArn": "string",
      "InputDataConfig": { 
         "DocumentReaderConfig": { 
            "DocumentReadAction": "string",
            "DocumentReadMode": "string",
            "FeatureTypes": [ "string" ]
         },
         "InputFormat": "string",
         "S3Uri": "string"
      },
      "JobArn": "string",
      "JobId": "string",
      "JobName": "string",
      "JobStatus": "string",
      "LanguageCode": "string",
      "Message": "string",
      "OutputDataConfig": { 
         "KmsKeyId": "string",
         "S3Uri": "string"
      },
      "SubmitTime": number,
      "VolumeKmsKeyId": "string",
      "VpcConfig": { 
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_DescribeEntitiesDetectionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntitiesDetectionJobProperties](#API_DescribeEntitiesDetectionJob_ResponseSyntax) **   <a name="comprehend-DescribeEntitiesDetectionJob-response-EntitiesDetectionJobProperties"></a>
An object that contains the properties associated with an entities detection job.  
Type: [EntitiesDetectionJobProperties](API_EntitiesDetectionJobProperties.md) object

## Errors
<a name="API_DescribeEntitiesDetectionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** JobNotFoundException **   
The specified job was not found. Check the job ID and try again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeEntitiesDetectionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DescribeEntitiesDetectionJob) 