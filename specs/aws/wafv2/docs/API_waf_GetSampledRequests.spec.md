---
id: "@specs/aws/wafv2/docs/API_waf_GetSampledRequests"
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
> **spec:id:** @specs/aws/wafv2/docs/API_waf_GetSampledRequests
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSampledRequests
<a name="API_waf_GetSampledRequests"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.

 `GetSampledRequests` returns a time range, which is usually the time range that you specified. However, if your resource (such as an Amazon CloudFront distribution) received 5,000 requests before the specified time range elapsed, `GetSampledRequests` returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.

## Request Syntax
<a name="API_waf_GetSampledRequests_RequestSyntax"></a>

```
{
   "MaxItems": {{number}},
   "RuleId": "{{string}}",
   "TimeWindow": { 
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "WebAclId": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_GetSampledRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxItems](#API_waf_GetSampledRequests_RequestSyntax) **   <a name="WAF-waf_GetSampledRequests-request-MaxItems"></a>
The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of `MaxItems`, `GetSampledRequests` returns information about all of them.   
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: Yes

 ** [RuleId](#API_waf_GetSampledRequests_RequestSyntax) **   <a name="WAF-waf_GetSampledRequests-request-RuleId"></a>
 `RuleId` is one of three values:  
+ The `RuleId` of the `Rule` or the `RuleGroupId` of the `RuleGroup` for which you want `GetSampledRequests` to return a sample of requests.
+  `Default_Action`, which causes `GetSampledRequests` to return a sample of the requests that didn't match any of the rules in the specified `WebACL`.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [TimeWindow](#API_waf_GetSampledRequests_RequestSyntax) **   <a name="WAF-waf_GetSampledRequests-request-TimeWindow"></a>
The start date and time and the end date and time of the range for which you want `GetSampledRequests` to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z`. For example, `"2016-09-27T14:50Z"`. You can specify any time range in the previous three hours.  
Type: [TimeWindow](API_waf_TimeWindow.md) object  
Required: Yes

 ** [WebAclId](#API_waf_GetSampledRequests_RequestSyntax) **   <a name="WAF-waf_GetSampledRequests-request-WebAclId"></a>
The `WebACLId` of the `WebACL` for which you want `GetSampledRequests` to return a sample of requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_GetSampledRequests_ResponseSyntax"></a>

```
{
   "PopulationSize": number,
   "SampledRequests": [ 
      { 
         "Action": "string",
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
         "RuleWithinRuleGroup": "string",
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
<a name="API_waf_GetSampledRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PopulationSize](#API_waf_GetSampledRequests_ResponseSyntax) **   <a name="WAF-waf_GetSampledRequests-response-PopulationSize"></a>
The total number of requests from which `GetSampledRequests` got a sample of `MaxItems` requests. If `PopulationSize` is less than `MaxItems`, the sample includes every request that your AWS resource received during the specified time range.  
Type: Long

 ** [SampledRequests](#API_waf_GetSampledRequests_ResponseSyntax) **   <a name="WAF-waf_GetSampledRequests-response-SampledRequests"></a>
A complex type that contains detailed information about each of the requests in the sample.  
Type: Array of [SampledHTTPRequest](API_waf_SampledHTTPRequest.md) objects

 ** [TimeWindow](#API_waf_GetSampledRequests_ResponseSyntax) **   <a name="WAF-waf_GetSampledRequests-response-TimeWindow"></a>
Usually, `TimeWindow` is the time range that you specified in the `GetSampledRequests` request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, `GetSampledRequests` returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.  
Type: [TimeWindow](API_waf_TimeWindow.md) object

## Errors
<a name="API_waf_GetSampledRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_waf_GetSampledRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/GetSampledRequests) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GetSampledRequests) 