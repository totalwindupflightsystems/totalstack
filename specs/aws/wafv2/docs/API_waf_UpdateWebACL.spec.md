---
id: "@specs/aws/wafv2/docs/API_waf_UpdateWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateWebACL"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateWebACL
<a name="API_waf_UpdateWebACL"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes [ActivatedRule](API_waf_ActivatedRule.md) objects in a `WebACL`. Each `Rule` identifies web requests that you want to allow, block, or count. When you update a `WebACL`, you specify the following values:
+ A default action for the `WebACL`, either `ALLOW` or `BLOCK`. AWS WAF performs the default action if a request doesn't match the criteria in any of the `Rules` in a `WebACL`.
+ The `Rules` that you want to add or delete. If you want to replace one `Rule` with another, you delete the existing `Rule` and add the new one.
+ For each `Rule`, whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the `Rule`.
+ The order in which you want AWS WAF to evaluate the `Rules` in a `WebACL`. If you add more than one `Rule` to a `WebACL`, AWS WAF evaluates each request against the `Rules` in order based on the value of `Priority`. (The `Rule` that has the lowest value for `Priority` is evaluated first.) When a web request matches all the predicates (such as `ByteMatchSets` and `IPSets`) in a `Rule`, AWS WAF immediately takes the corresponding action, allow or block, and doesn't evaluate the request against the remaining `Rules` in the `WebACL`, if any. 

To create and configure a `WebACL`, perform the following steps:

1. Create and update the predicates that you want to include in `Rules`. For more information, see [CreateByteMatchSet](API_waf_CreateByteMatchSet.md), [UpdateByteMatchSet](API_waf_UpdateByteMatchSet.md), [CreateIPSet](API_waf_CreateIPSet.md), [UpdateIPSet](API_waf_UpdateIPSet.md), [CreateSqlInjectionMatchSet](API_waf_CreateSqlInjectionMatchSet.md), and [UpdateSqlInjectionMatchSet](API_waf_UpdateSqlInjectionMatchSet.md).

1. Create and update the `Rules` that you want to include in the `WebACL`. For more information, see [CreateRule](API_waf_CreateRule.md) and [UpdateRule](API_waf_UpdateRule.md).

1. Create a `WebACL`. See [CreateWebACL](API_waf_CreateWebACL.md).

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateWebACL](#API_waf_UpdateWebACL) request.

1. Submit an `UpdateWebACL` request to specify the `Rules` that you want to include in the `WebACL`, to specify the default action, and to associate the `WebACL` with an Amazon CloudFront distribution. 

   The `ActivatedRule` can be a rule group. If you specify a rule group as your `ActivatedRule`, you can exclude specific rules from that rule group.

   If you already have a rule group associated with a web ACL and want to submit an `UpdateWebACL` request to exclude certain rules from that rule group, you must first remove the rule group from the web ACL, the re-insert it again, specifying the excluded rules. For details, see [ActivatedRule:ExcludedRules](API_waf_ActivatedRule.md#WAF-Type-waf_ActivatedRule-ExcludedRules). 

Be aware that if you try to add a RATE\_BASED rule to a web ACL without setting the rule type when first creating the rule, the [UpdateWebACL](#API_waf_UpdateWebACL) request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist. 

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateWebACL_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "DefaultAction": { 
      "Type": "{{string}}"
   },
   "Updates": [ 
      { 
         "Action": "{{string}}",
         "ActivatedRule": { 
            "Action": { 
               "Type": "{{string}}"
            },
            "ExcludedRules": [ 
               { 
                  "RuleId": "{{string}}"
               }
            ],
            "OverrideAction": { 
               "Type": "{{string}}"
            },
            "Priority": {{number}},
            "RuleId": "{{string}}",
            "Type": "{{string}}"
         }
      }
   ],
   "WebACLId": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_UpdateWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateWebACL_RequestSyntax) **   <a name="WAF-waf_UpdateWebACL-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [DefaultAction](#API_waf_UpdateWebACL_RequestSyntax) **   <a name="WAF-waf_UpdateWebACL-request-DefaultAction"></a>
  
Type: [WafAction](API_waf_WafAction.md) object  
Required: No

 ** [Updates](#API_waf_UpdateWebACL_RequestSyntax) **   <a name="WAF-waf_UpdateWebACL-request-Updates"></a>
An array of updates to make to the [WebACL](API_waf_WebACL.md).  
An array of `WebACLUpdate` objects that you want to insert into or delete from a [WebACL](API_waf_WebACL.md). For more information, see the applicable data types:  
+  [WebACLUpdate](API_waf_WebACLUpdate.md): Contains `Action` and `ActivatedRule` 
+  [ActivatedRule](API_waf_ActivatedRule.md): Contains `Action`, `OverrideAction`, `Priority`, `RuleId`, and `Type`. `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL`. In this case, you do not use `ActivatedRule|Action`. For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`. 
+  [WafAction](API_waf_WafAction.md): Contains `Type` 
Type: Array of [WebACLUpdate](API_waf_WebACLUpdate.md) objects  
Required: No

 ** [WebACLId](#API_waf_UpdateWebACL_RequestSyntax) **   <a name="WAF-waf_UpdateWebACL-request-WebACLId"></a>
The `WebACLId` of the [WebACL](API_waf_WebACL.md) that you want to update. `WebACLId` is returned by [CreateWebACL](API_waf_CreateWebACL.md) and by [ListWebACLs](API_waf_ListWebACLs.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_UpdateWebACL_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateWebACL_ResponseSyntax) **   <a name="WAF-waf_UpdateWebACL-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateWebACL` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateWebACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

 ** WAFInvalidOperationException **   
The operation failed because there was nothing to do. For example:  
+ You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the specified `WebACL`.
+ You tried to remove an IP address from an `IPSet`, but the IP address isn't in the specified `IPSet`.
+ You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the `ByteMatchTuple` isn't in the specified `WebACL`.
+ You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the specified `WebACL`.
+ You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple` already exists in the specified `WebACL`.
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

 ** WAFLimitsExceededException **   
The operation exceeds a resource limit, for example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html) in the * AWS WAF Developer Guide*.  
HTTP Status Code: 400

 ** WAFNonexistentContainerException **   
The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:  
+ You tried to add a `Rule` to or delete a `Rule` from a `WebACL` that doesn't exist.
+ You tried to add a `ByteMatchSet` to or delete a `ByteMatchSet` from a `Rule` that doesn't exist.
+ You tried to add an IP address to or delete an IP address from an `IPSet` that doesn't exist.
+ You tried to add a `ByteMatchTuple` to or delete a `ByteMatchTuple` from a `ByteMatchSet` that doesn't exist.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

 ** WAFReferencedItemException **   
The operation failed because you tried to delete an object that is still in use. For example:  
+ You tried to delete a `ByteMatchSet` that is still referenced by a `Rule`.
+ You tried to delete a `Rule` that is still referenced by a `WebACL`.
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

 ** WAFSubscriptionNotFoundException **   
The specified subscription does not exist.  
HTTP Status Code: 400

## See Also
<a name="API_waf_UpdateWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateWebACL) 