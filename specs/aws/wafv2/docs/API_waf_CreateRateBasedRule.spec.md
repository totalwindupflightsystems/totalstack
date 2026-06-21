---
id: "@specs/aws/wafv2/docs/API_waf_CreateRateBasedRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRateBasedRule"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateRateBasedRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_CreateRateBasedRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRateBasedRule
<a name="API_waf_CreateRateBasedRule"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a [RateBasedRule](API_waf_RateBasedRule.md). The `RateBasedRule` contains a `RateLimit`, which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The `RateBasedRule` also contains the `IPSet` objects, `ByteMatchSet` objects, and other predicates that identify the requests that you want to count or block if these requests exceed the `RateLimit`.

If you add more than one predicate to a `RateBasedRule`, a request not only must exceed the `RateLimit`, but it also must match all the conditions to be counted or blocked. For example, suppose you add the following to a `RateBasedRule`:
+ An `IPSet` that matches the IP address `192.0.2.44/32` 
+ A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

Further, you specify a `RateLimit` of 1,000.

You then add the `RateBasedRule` to a `WebACL` and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the `User-Agent` header in the request must contain the value `BadBot`. Further, requests that match these two conditions must be received at a rate of more than 1,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 1,000 for a five-minute period, AWS WAF no longer blocks the requests.

As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a `RateBasedRule`:
+ A `ByteMatchSet` with `FieldToMatch` of `URI` 
+ A `PositionalConstraint` of `STARTS_WITH` 
+ A `TargetString` of `login` 

Further, you specify a `RateLimit` of 1,000.

By adding this `RateBasedRule` to a `WebACL`, you could limit requests to your login page without affecting the rest of your site.

To create and configure a `RateBasedRule`, perform the following steps:

1. Create and update the predicates that you want to include in the rule. For more information, see [CreateByteMatchSet](API_waf_CreateByteMatchSet.md), [CreateIPSet](API_waf_CreateIPSet.md), and [CreateSqlInjectionMatchSet](API_waf_CreateSqlInjectionMatchSet.md).

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateRule` request.

1. Submit a `CreateRateBasedRule` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateRule](API_waf_UpdateRule.md) request.

1. Submit an `UpdateRateBasedRule` request to specify the predicates that you want to include in the rule.

1. Create and update a `WebACL` that contains the `RateBasedRule`. For more information, see [CreateWebACL](API_waf_CreateWebACL.md).

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_CreateRateBasedRule_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "MetricName": "{{string}}",
   "Name": "{{string}}",
   "RateKey": "{{string}}",
   "RateLimit": {{number}},
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_waf_CreateRateBasedRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRateBasedRule` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [MetricName](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-MetricName"></a>
A friendly name or description for the metrics for this `RateBasedRule`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `RateBasedRule`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-Name"></a>
A friendly name or description of the [RateBasedRule](API_waf_RateBasedRule.md). You can't change the name of a `RateBasedRule` after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [RateKey](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-RateKey"></a>
The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for `RateKey` is `IP`. `IP` indicates that requests that arrive from the same IP address are subject to the `RateLimit` that is specified in the `RateBasedRule`.  
Type: String  
Valid Values: `IP`   
Required: Yes

 ** [RateLimit](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-RateLimit"></a>
The maximum number of requests, which have an identical value in the field that is specified by `RateKey`, allowed in a five-minute period. If the number of requests exceeds the `RateLimit` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.  
Type: Long  
Valid Range: Minimum value of 100. Maximum value of 2000000000.  
Required: Yes

 ** [Tags](#API_waf_CreateRateBasedRule_RequestSyntax) **   <a name="WAF-waf_CreateRateBasedRule-request-Tags"></a>
  
Type: Array of [Tag](API_waf_Tag.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## Response Syntax
<a name="API_waf_CreateRateBasedRule_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "Rule": { 
      "MatchPredicates": [ 
         { 
            "DataId": "string",
            "Negated": boolean,
            "Type": "string"
         }
      ],
      "MetricName": "string",
      "Name": "string",
      "RateKey": "string",
      "RateLimit": number,
      "RuleId": "string"
   }
}
```

## Response Elements
<a name="API_waf_CreateRateBasedRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_CreateRateBasedRule_ResponseSyntax) **   <a name="WAF-waf_CreateRateBasedRule-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRateBasedRule` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [Rule](#API_waf_CreateRateBasedRule_ResponseSyntax) **   <a name="WAF-waf_CreateRateBasedRule-response-Rule"></a>
The [RateBasedRule](API_waf_RateBasedRule.md) that is returned in the `CreateRateBasedRule` response.  
Type: [RateBasedRule](API_waf_RateBasedRule.md) object

## Errors
<a name="API_waf_CreateRateBasedRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFBadRequestException **   
  
HTTP Status Code: 400

 ** WAFDisallowedNameException **   
The name specified is invalid.  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:  
+ You specified an invalid parameter name.
+ You specified an invalid value.
+ You tried to update an object (`ByteMatchSet`, `IPSet`, `Rule`, or `WebACL`) using an action other than `INSERT` or `DELETE`.
+ You tried to create a `WebACL` with a `DefaultAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to create a `RateBasedRule` with a `RateKey` value other than `IP`.
+ You tried to update a `WebACL` with a `WafAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to update a `ByteMatchSet` with a `FieldToMatch` `Type` other than HEADER, METHOD, QUERY\_STRING, URI, or BODY.
+ You tried to update a `ByteMatchSet` with a `Field` of `HEADER` but no value for `Data`.
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.
HTTP Status Code: 400

 ** WAFLimitsExceededException **   
The operation exceeds a resource limit, for example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html) in the * AWS WAF Developer Guide*.  
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

 ** WAFTagOperationException **   
  
HTTP Status Code: 400

 ** WAFTagOperationInternalErrorException **   
  
HTTP Status Code: 500

## See Also
<a name="API_waf_CreateRateBasedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/CreateRateBasedRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/CreateRateBasedRule) 