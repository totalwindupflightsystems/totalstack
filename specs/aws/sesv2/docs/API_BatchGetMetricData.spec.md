---
id: "@specs/aws/sesv2/docs/API_BatchGetMetricData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchGetMetricData"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# BatchGetMetricData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_BatchGetMetricData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchGetMetricData
<a name="API_BatchGetMetricData"></a>

Retrieves batches of metric data collected based on your sending activity.

You can execute this operation no more than 16 times per second, and with at most 160 queries from the batches per second (cumulative).

## Request Syntax
<a name="API_BatchGetMetricData_RequestSyntax"></a>

```
POST /v2/email/metrics/batch HTTP/1.1
Content-type: application/json

{
   "Queries": [ 
      { 
         "Dimensions": { 
            "{{string}}" : "{{string}}" 
         },
         "EndDate": {{number}},
         "Id": "{{string}}",
         "Metric": "{{string}}",
         "Namespace": "{{string}}",
         "StartDate": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetMetricData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetMetricData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Queries](#API_BatchGetMetricData_RequestSyntax) **   <a name="SES-BatchGetMetricData-request-Queries"></a>
A list of queries for metrics to be retrieved.  
Type: Array of [BatchGetMetricDataQuery](API_BatchGetMetricDataQuery.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## Response Syntax
<a name="API_BatchGetMetricData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [ 
      { 
         "Code": "string",
         "Id": "string",
         "Message": "string"
      }
   ],
   "Results": [ 
      { 
         "Id": "string",
         "Timestamps": [ number ],
         "Values": [ number ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetMetricData_ResponseSyntax) **   <a name="SES-BatchGetMetricData-response-Errors"></a>
A list of `MetricDataError` encountered while processing your metric data batch request.  
Type: Array of [MetricDataError](API_MetricDataError.md) objects

 ** [Results](#API_BatchGetMetricData_ResponseSyntax) **   <a name="SES-BatchGetMetricData-response-Results"></a>
A list of successfully retrieved `MetricDataResult`.  
Type: Array of [MetricDataResult](API_MetricDataResult.md) objects

## Errors
<a name="API_BatchGetMetricData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
The request couldn't be processed because an error occurred with the Amazon SES API v2.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_BatchGetMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/BatchGetMetricData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/BatchGetMetricData) 