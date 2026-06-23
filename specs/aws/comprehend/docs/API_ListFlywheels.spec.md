---
id: "@specs/aws/comprehend/docs/API_ListFlywheels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlywheels"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ListFlywheels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ListFlywheels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlywheels
<a name="API_ListFlywheels"></a>

Gets a list of the flywheels that you have created.

## Request Syntax
<a name="API_ListFlywheels_RequestSyntax"></a>

```
{
   "Filter": { 
      "CreationTimeAfter": {{number}},
      "CreationTimeBefore": {{number}},
      "Status": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFlywheels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListFlywheels_RequestSyntax) **   <a name="comprehend-ListFlywheels-request-Filter"></a>
Filters the flywheels that are returned. You can filter flywheels on their status, or the date and time that they were submitted. You can only set one filter at a time.   
Type: [FlywheelFilter](API_FlywheelFilter.md) object  
Required: No

 ** [MaxResults](#API_ListFlywheels_RequestSyntax) **   <a name="comprehend-ListFlywheels-request-MaxResults"></a>
Maximum number of results to return in a response. The default is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListFlywheels_RequestSyntax) **   <a name="comprehend-ListFlywheels-request-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ListFlywheels_ResponseSyntax"></a>

```
{
   "FlywheelSummaryList": [ 
      { 
         "ActiveModelArn": "string",
         "CreationTime": number,
         "DataLakeS3Uri": "string",
         "FlywheelArn": "string",
         "LastModifiedTime": number,
         "LatestFlywheelIteration": "string",
         "Message": "string",
         "ModelType": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFlywheels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlywheelSummaryList](#API_ListFlywheels_ResponseSyntax) **   <a name="comprehend-ListFlywheels-response-FlywheelSummaryList"></a>
A list of flywheel properties retrieved by the service in response to the request.   
Type: Array of [FlywheelSummary](API_FlywheelSummary.md) objects

 ** [NextToken](#API_ListFlywheels_ResponseSyntax) **   <a name="comprehend-ListFlywheels-response-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListFlywheels_Errors"></a>

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
<a name="API_ListFlywheels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListFlywheels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListFlywheels) 