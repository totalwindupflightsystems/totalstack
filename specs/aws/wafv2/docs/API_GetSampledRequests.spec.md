---
id: "@specs/aws/wafv2/docs/API_GetSampledRequests"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSampledRequests"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetSampledRequests

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_GetSampledRequests
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSampledRequests
<a name="API_GetSampledRequests"></a>

Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.

 `GetSampledRequests` returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, `GetSampledRequests` returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.

## Request Syntax
<a name="API_GetSampledRequests_RequestSyntax"></a>

```
{
   "MaxItems": {{number}},
   "RuleMetricName": "{{string}}",
   "Scope": "{{string}}",
   "TimeWindow": { 
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "WebAclArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSampledRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxItems](#API_GetSampledRequests_RequestSyntax) **   <a name="WAF-GetSampledRequests-request-MaxItems"></a>
The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of `MaxItems`, `GetSampledRequests` returns information about all of them.   
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: Yes

 ** [RuleMetricName](#API_GetSampledRequests_RequestSyntax) **   <a name="WAF-GetSampledRequests-request-RuleMetricName"></a>
The metric name assigned to the `Rule` or `RuleGroup` dimension for which you want a sample of requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[\w#:\.\-/]+$`   
Required: Yes

 ** [Scope](#API_GetSampledRequests_RequestSyntax) **   <a name="WAF-GetSampledRequests-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [TimeWindow](#API_GetSampledRequests_RequestSyntax) **   <a name="WAF-GetSampledRequests-request-TimeWindow"></a>
The start date and time and the end date and time of the range for which you want `GetSampledRequests` to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z`. For example, `"2016-09-27T14:50Z"`. You can specify any time range in the previous three hours. If you specify a start time that's earlier than three hours ago, AWS WAF sets it to three hours ago.  
Type: [TimeWindow](API_TimeWindow.md) object  
Required: Yes

 ** [WebAclArn](#API_GetSampledRequests_RequestSyntax) **   <a name="WAF-GetSampledRequests-request-WebAclArn"></a>
The Amazon resource name (ARN) of the `WebACL` for which you want a sample of requests.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_GetSampledRequests_ResponseSyntax"></a>

```
{
   "PopulationSize": number,
   "SampledRequests": [ 
      { 
         "Action": "string",
         "CaptchaResponse": { 
            "FailureReason": "string",
            "ResponseCode": number,
            "SolveTimestamp": number
         },
         "ChallengeResponse": { 
            "FailureReason": "string",
            "ResponseCode": number,
            "SolveTimestamp": number
         },
         "Labels": [ 
            { 
               "Name": "string"
            }
         ],
         "OverriddenAction": "string",
         "Request": { 
            "ClientIP": "string",
            "Country": "string",
            "Headers": [ 
               { 
                  "Name": "string",
                  "Value": "string"
               }
            ],
            "HTTPVersion": "string",
            "Method": "string",
            "URI": "string"
         },
         "RequestHeadersInserted": [ 
            { 
               "Name": "string",
               "Value": "string"
            }
         ],
         "ResponseCodeSent": number,
         "RuleNameWithinRuleGroup": "string",
         "Timestamp": number,
         "Weight": number
      }
   ],
   "TimeWindow": { 
      "EndTime": number,
      "StartTime": number
   }
}
```

## Response Elements
<a name="API_GetSampledRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PopulationSize](#API_GetSampledRequests_ResponseSyntax) **   <a name="WAF-GetSampledRequests-response-PopulationSize"></a>
The total number of requests from which `GetSampledRequests` got a sample of `MaxItems` requests. If `PopulationSize` is less than `MaxItems`, the sample includes every request that your AWS resource received during the specified time range.  
Type: Long

 ** [SampledRequests](#API_GetSampledRequests_ResponseSyntax) **   <a name="WAF-GetSampledRequests-response-SampledRequests"></a>
A complex type that contains detailed information about each of the requests in the sample.  
Type: Array of [SampledHTTPRequest](API_SampledHTTPRequest.md) objects

 ** [TimeWindow](#API_GetSampledRequests_ResponseSyntax) **   <a name="WAF-GetSampledRequests-response-TimeWindow"></a>
Usually, `TimeWindow` is the time range that you specified in the `GetSampledRequests` request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, `GetSampledRequests` returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.  
Type: [TimeWindow](API_TimeWindow.md) object

## Errors
<a name="API_GetSampledRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

## See Also
<a name="API_GetSampledRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetSampledRequests) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetSampledRequests) 