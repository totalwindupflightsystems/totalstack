---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetRateBasedRuleManagedKeys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRateBasedRuleManagedKeys"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRateBasedRuleManagedKeys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetRateBasedRuleManagedKeys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRateBasedRuleManagedKeys
<a name="API_wafRegional_GetRateBasedRuleManagedKeys"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns an array of IP addresses currently being blocked by the [RateBasedRule](API_wafRegional_RateBasedRule.md) that is specified by the `RuleId`. The maximum number of managed keys that will be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the 10,000 addresses with the highest rates will be blocked.

## Request Syntax
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_RequestSyntax"></a>

```
{
   "NextMarker": "{{string}}",
   "RuleId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextMarker](#API_wafRegional_GetRateBasedRuleManagedKeys_RequestSyntax) **   <a name="WAF-wafRegional_GetRateBasedRuleManagedKeys-request-NextMarker"></a>
A null value and not currently used. Do not include this in your request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: No

 ** [RuleId](#API_wafRegional_GetRateBasedRuleManagedKeys_RequestSyntax) **   <a name="WAF-wafRegional_GetRateBasedRuleManagedKeys-request-RuleId"></a>
The `RuleId` of the [RateBasedRule](API_wafRegional_RateBasedRule.md) for which you want to get a list of `ManagedKeys`. `RuleId` is returned by [CreateRateBasedRule](API_wafRegional_CreateRateBasedRule.md) and by [ListRateBasedRules](API_wafRegional_ListRateBasedRules.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_ResponseSyntax"></a>

```
{
   "ManagedKeys": [ "string" ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedKeys](#API_wafRegional_GetRateBasedRuleManagedKeys_ResponseSyntax) **   <a name="WAF-wafRegional_GetRateBasedRuleManagedKeys-response-ManagedKeys"></a>
An array of IP addresses that currently are blocked by the specified [RateBasedRule](API_wafRegional_RateBasedRule.md).   
Type: Array of strings

 ** [NextMarker](#API_wafRegional_GetRateBasedRuleManagedKeys_ResponseSyntax) **   <a name="WAF-wafRegional_GetRateBasedRuleManagedKeys-response-NextMarker"></a>
A null value and not currently used.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*` 

## Errors
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

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

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_GetRateBasedRuleManagedKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys) 