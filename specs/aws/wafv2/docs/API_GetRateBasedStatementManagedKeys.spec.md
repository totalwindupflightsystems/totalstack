---
id: "@specs/aws/wafv2/docs/API_GetRateBasedStatementManagedKeys"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRateBasedStatementManagedKeys"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRateBasedStatementManagedKeys

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_GetRateBasedStatementManagedKeys
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRateBasedStatementManagedKeys
<a name="API_GetRateBasedStatementManagedKeys"></a>

Retrieves the IP addresses that are currently blocked by a rate-based rule instance. This is only available for rate-based rules that aggregate solely on the IP address or on the forwarded IP address. 

The maximum number of addresses that can be blocked for a single rate-based rule instance is 10,000. If more than 10,000 addresses exceed the rate limit, those with the highest rates are blocked.

For a rate-based rule that you've defined inside a rule group, provide the name of the rule group reference statement in your request, in addition to the rate-based rule name and the web ACL name. 

 AWS WAF monitors web requests and manages keys independently for each unique combination of web ACL, optional rule group, and rate-based rule. For example, if you define a rate-based rule inside a rule group, and then use the rule group in a web ACL, AWS WAF monitors web requests and manages keys for that web ACL, rule group reference statement, and rate-based rule instance. If you use the same rule group in a second web ACL, AWS WAF monitors web requests and manages keys for this second usage completely independent of your first. 

## Request Syntax
<a name="API_GetRateBasedStatementManagedKeys_RequestSyntax"></a>

```
{
   "RuleGroupRuleName": "{{string}}",
   "RuleName": "{{string}}",
   "Scope": "{{string}}",
   "WebACLId": "{{string}}",
   "WebACLName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRateBasedStatementManagedKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleGroupRuleName](#API_GetRateBasedStatementManagedKeys_RequestSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-request-RuleGroupRuleName"></a>
The name of the rule group reference statement in your web ACL. This is required only when you have the rate-based rule nested inside a rule group.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: No

 ** [RuleName](#API_GetRateBasedStatementManagedKeys_RequestSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-request-RuleName"></a>
The name of the rate-based rule to get the keys for. If you have the rule defined inside a rule group that you're using in your web ACL, also provide the name of the rule group reference statement in the request parameter `RuleGroupRuleName`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [Scope](#API_GetRateBasedStatementManagedKeys_RequestSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [WebACLId](#API_GetRateBasedStatementManagedKeys_RequestSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-request-WebACLId"></a>
The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [WebACLName](#API_GetRateBasedStatementManagedKeys_RequestSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-request-WebACLName"></a>
The name of the web ACL. You cannot change the name of a web ACL after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

## Response Syntax
<a name="API_GetRateBasedStatementManagedKeys_ResponseSyntax"></a>

```
{
   "ManagedKeysIPV4": { 
      "Addresses": [ "string" ],
      "IPAddressVersion": "string"
   },
   "ManagedKeysIPV6": { 
      "Addresses": [ "string" ],
      "IPAddressVersion": "string"
   }
}
```

## Response Elements
<a name="API_GetRateBasedStatementManagedKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedKeysIPV4](#API_GetRateBasedStatementManagedKeys_ResponseSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-response-ManagedKeysIPV4"></a>
The keys that are of Internet Protocol version 4 (IPv4).   
Type: [RateBasedStatementManagedKeysIPSet](API_RateBasedStatementManagedKeysIPSet.md) object

 ** [ManagedKeysIPV6](#API_GetRateBasedStatementManagedKeys_ResponseSyntax) **   <a name="WAF-GetRateBasedStatementManagedKeys-response-ManagedKeysIPV6"></a>
The keys that are of Internet Protocol version 6 (IPv6).   
Type: [RateBasedStatementManagedKeysIPSet](API_RateBasedStatementManagedKeysIPSet.md) object

## Errors
<a name="API_GetRateBasedStatementManagedKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

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

 ** WAFUnsupportedAggregateKeyTypeException **   
The rule that you've named doesn't aggregate solely on the IP address or solely on the forwarded IP address. This call is only available for rate-based rules with an `AggregateKeyType` setting of `IP` or `FORWARDED_IP`.  
HTTP Status Code: 400

## See Also
<a name="API_GetRateBasedStatementManagedKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetRateBasedStatementManagedKeys) 