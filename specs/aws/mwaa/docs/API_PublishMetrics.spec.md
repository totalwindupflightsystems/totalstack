---
id: "@specs/aws/mwaa/docs/API_PublishMetrics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PublishMetrics"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# PublishMetrics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_PublishMetrics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PublishMetrics
<a name="API_PublishMetrics"></a>

 *This action has been deprecated.* 

 **Internal only**. Publishes environment health metrics to Amazon CloudWatch.

## Request Syntax
<a name="API_PublishMetrics_RequestSyntax"></a>

```
POST /metrics/environments/{{EnvironmentName}} HTTP/1.1
Content-type: application/json

{
   "MetricData": [ 
      { 
         "Dimensions": [ 
            { 
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "MetricName": "{{string}}",
         "StatisticValues": { 
            "Maximum": {{number}},
            "Minimum": {{number}},
            "SampleCount": {{number}},
            "Sum": {{number}}
         },
         "Timestamp": {{number}},
         "Unit": "{{string}}",
         "Value": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_PublishMetrics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EnvironmentName](#API_PublishMetrics_RequestSyntax) **   <a name="mwaa-PublishMetrics-request-uri-EnvironmentName"></a>
 **Internal only**. The name of the environment.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_PublishMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MetricData](#API_PublishMetrics_RequestSyntax) **   <a name="mwaa-PublishMetrics-request-MetricData"></a>
 *This parameter has been deprecated.*   
 **Internal only**. Publishes metrics to Amazon CloudWatch. To learn more about the metrics published to Amazon CloudWatch, see [Amazon MWAA performance metrics in Amazon CloudWatch](https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html).  
Type: Array of [MetricDatum](API_MetricDatum.md) objects  
Required: Yes

## Response Syntax
<a name="API_PublishMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PublishMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PublishMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_PublishMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/PublishMetrics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/PublishMetrics) 