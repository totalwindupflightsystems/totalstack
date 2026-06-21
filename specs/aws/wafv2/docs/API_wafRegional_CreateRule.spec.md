---
id: "@specs/aws/wafv2/docs/API_wafRegional_CreateRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRule"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_CreateRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRule
<a name="API_wafRegional_CreateRule"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a `Rule`, which contains the `IPSet` objects, `ByteMatchSet` objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a `Rule`, a request must match all of the specifications to be allowed or blocked. For example, suppose that you add the following to a `Rule`:
+ An `IPSet` that matches the IP address `192.0.2.44/32` 
+ A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

You then add the `Rule` to a `WebACL` and specify that you want to blocks requests that satisfy the `Rule`. For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the `User-Agent` header in the request must contain the value `BadBot`.

To create and configure a `Rule`, perform the following steps:

1. Create and update the predicates that you want to include in the `Rule`. For more information, see [CreateByteMatchSet](API_wafRegional_CreateByteMatchSet.md), [CreateIPSet](API_wafRegional_CreateIPSet.md), and [CreateSqlInjectionMatchSet](API_wafRegional_CreateSqlInjectionMatchSet.md).

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateRule` request.

1. Submit a `CreateRule` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateRule](API_wafRegional_UpdateRule.md) request.

1. Submit an `UpdateRule` request to specify the predicates that you want to include in the `Rule`.

1. Create and update a `WebACL` that contains the `Rule`. For more information, see [CreateWebACL](API_wafRegional_CreateWebACL.md).

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_wafRegional_CreateRule_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "MetricName": "{{string}}",
   "Name": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_wafRegional_CreateRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_CreateRule_RequestSyntax) **   <a name="WAF-wafRegional_CreateRule-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [MetricName](#API_wafRegional_CreateRule_RequestSyntax) **   <a name="WAF-wafRegional_CreateRule-request-MetricName"></a>
A friendly name or description for the metrics for this `Rule`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `Rule`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_wafRegional_CreateRule_RequestSyntax) **   <a name="WAF-wafRegional_CreateRule-request-Name"></a>
A friendly name or description of the [Rule](API_wafRegional_Rule.md). You can't change the name of a `Rule` after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Tags](#API_wafRegional_CreateRule_RequestSyntax) **   <a name="WAF-wafRegional_CreateRule-request-Tags"></a>
  
Type: Array of [Tag](API_wafRegional_Tag.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## Response Syntax
<a name="API_wafRegional_CreateRule_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "Rule": { 
      "MetricName": "string",
      "Name": "string",
      "Predicates": [ 
         { 
            "DataId": "string",
            "Negated": boolean,
            "Type": "string"
         }
      ],
      "RuleId": "string"
   }
}
```

## Response Elements
<a name="API_wafRegional_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_wafRegional_CreateRule_ResponseSyntax) **   <a name="WAF-wafRegional_CreateRule-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRule` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [Rule](#API_wafRegional_CreateRule_ResponseSyntax) **   <a name="WAF-wafRegional_CreateRule-response-Rule"></a>
The [Rule](API_wafRegional_Rule.md) returned in the `CreateRule` response.  
Type: [Rule](API_wafRegional_Rule.md) object

## Errors
<a name="API_wafRegional_CreateRule_Errors"></a>

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
<a name="API_wafRegional_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/CreateRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/CreateRule) 