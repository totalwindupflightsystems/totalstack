---
id: "@specs/aws/comprehend/docs/API_ListEntitiesDetectionJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEntitiesDetectionJobs"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ListEntitiesDetectionJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ListEntitiesDetectionJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEntitiesDetectionJobs
<a name="API_ListEntitiesDetectionJobs"></a>

Gets a list of the entity detection jobs that you have submitted.

## Request Syntax
<a name="API_ListEntitiesDetectionJobs_RequestSyntax"></a>

```
{
   "Filter": { 
      "JobName": "{{string}}",
      "JobStatus": "{{string}}",
      "SubmitTimeAfter": {{number}},
      "SubmitTimeBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEntitiesDetectionJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListEntitiesDetectionJobs_RequestSyntax) **   <a name="comprehend-ListEntitiesDetectionJobs-request-Filter"></a>
Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.  
Type: [EntitiesDetectionJobFilter](API_EntitiesDetectionJobFilter.md) object  
Required: No

 ** [MaxResults](#API_ListEntitiesDetectionJobs_RequestSyntax) **   <a name="comprehend-ListEntitiesDetectionJobs-request-MaxResults"></a>
The maximum number of results to return in each page. The default is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListEntitiesDetectionJobs_RequestSyntax) **   <a name="comprehend-ListEntitiesDetectionJobs-request-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ListEntitiesDetectionJobs_ResponseSyntax"></a>

```
{
   "EntitiesDetectionJobPropertiesList": [ 
      { 
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEntitiesDetectionJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntitiesDetectionJobPropertiesList](#API_ListEntitiesDetectionJobs_ResponseSyntax) **   <a name="comprehend-ListEntitiesDetectionJobs-response-EntitiesDetectionJobPropertiesList"></a>
A list containing the properties of each job that is returned.  
Type: Array of [EntitiesDetectionJobProperties](API_EntitiesDetectionJobProperties.md) objects

 ** [NextToken](#API_ListEntitiesDetectionJobs_ResponseSyntax) **   <a name="comprehend-ListEntitiesDetectionJobs-response-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListEntitiesDetectionJobs_Errors"></a>

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
<a name="API_ListEntitiesDetectionJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListEntitiesDetectionJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListEntitiesDetectionJobs) 