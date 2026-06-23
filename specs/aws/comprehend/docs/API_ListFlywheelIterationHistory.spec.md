---
id: "@specs/aws/comprehend/docs/API_ListFlywheelIterationHistory"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlywheelIterationHistory"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ListFlywheelIterationHistory

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ListFlywheelIterationHistory
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlywheelIterationHistory
<a name="API_ListFlywheelIterationHistory"></a>

Information about the history of a flywheel iteration. For more information about flywheels, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_ListFlywheelIterationHistory_RequestSyntax"></a>

```
{
   "Filter": { 
      "CreationTimeAfter": {{number}},
      "CreationTimeBefore": {{number}}
   },
   "FlywheelArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFlywheelIterationHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListFlywheelIterationHistory_RequestSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-request-Filter"></a>
Filter the flywheel iteration history based on creation time.  
Type: [FlywheelIterationFilter](API_FlywheelIterationFilter.md) object  
Required: No

 ** [FlywheelArn](#API_ListFlywheelIterationHistory_RequestSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-request-FlywheelArn"></a>
The ARN of the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

 ** [MaxResults](#API_ListFlywheelIterationHistory_RequestSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-request-MaxResults"></a>
Maximum number of iteration history results to return  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListFlywheelIterationHistory_RequestSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-request-NextToken"></a>
Next token  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ListFlywheelIterationHistory_ResponseSyntax"></a>

```
{
   "FlywheelIterationPropertiesList": [ 
      { 
         "CreationTime": number,
         "EndTime": number,
         "EvaluatedModelArn": "string",
         "EvaluatedModelMetrics": { 
            "AverageAccuracy": number,
            "AverageF1Score": number,
            "AveragePrecision": number,
            "AverageRecall": number
         },
         "EvaluationManifestS3Prefix": "string",
         "FlywheelArn": "string",
         "FlywheelIterationId": "string",
         "Message": "string",
         "Status": "string",
         "TrainedModelArn": "string",
         "TrainedModelMetrics": { 
            "AverageAccuracy": number,
            "AverageF1Score": number,
            "AveragePrecision": number,
            "AverageRecall": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFlywheelIterationHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlywheelIterationPropertiesList](#API_ListFlywheelIterationHistory_ResponseSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-response-FlywheelIterationPropertiesList"></a>
List of flywheel iteration properties  
Type: Array of [FlywheelIterationProperties](API_FlywheelIterationProperties.md) objects

 ** [NextToken](#API_ListFlywheelIterationHistory_ResponseSyntax) **   <a name="comprehend-ListFlywheelIterationHistory-response-NextToken"></a>
Next token  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListFlywheelIterationHistory_Errors"></a>

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

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_ListFlywheelIterationHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListFlywheelIterationHistory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListFlywheelIterationHistory) 