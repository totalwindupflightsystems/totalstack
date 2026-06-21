---
id: "@specs/aws/wafv2/docs/API_waf_UpdateRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateRuleGroup"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateRuleGroup
<a name="API_waf_UpdateRuleGroup"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes [ActivatedRule](API_waf_ActivatedRule.md) objects in a `RuleGroup`.

You can only insert `REGULAR` rules into a rule group.

You can have a maximum of ten rules per rule group.

To create and configure a `RuleGroup`, perform the following steps:

1. Create and update the `Rules` that you want to include in the `RuleGroup`. See [CreateRule](API_waf_CreateRule.md).

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateRuleGroup](#API_waf_UpdateRuleGroup) request.

1. Submit an `UpdateRuleGroup` request to add `Rules` to the `RuleGroup`.

1. Create and update a `WebACL` that contains the `RuleGroup`. See [CreateWebACL](API_waf_CreateWebACL.md).

If you want to replace one `Rule` with another, you delete the existing one and add the new one.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateRuleGroup_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "RuleGroupId": "{{string}}",
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
   ]
}
```

## Request Parameters
<a name="API_waf_UpdateRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateRuleGroup_RequestSyntax) **   <a name="WAF-waf_UpdateRuleGroup-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [RuleGroupId](#API_waf_UpdateRuleGroup_RequestSyntax) **   <a name="WAF-waf_UpdateRuleGroup-request-RuleGroupId"></a>
The `RuleGroupId` of the [RuleGroup](API_waf_RuleGroup.md) that you want to update. `RuleGroupId` is returned by [CreateRuleGroup](API_waf_CreateRuleGroup.md) and by [ListRuleGroups](API_waf_ListRuleGroups.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Updates](#API_waf_UpdateRuleGroup_RequestSyntax) **   <a name="WAF-waf_UpdateRuleGroup-request-Updates"></a>
An array of `RuleGroupUpdate` objects that you want to insert into or delete from a [RuleGroup](API_waf_RuleGroup.md).  
You can only insert `REGULAR` rules into a rule group.  
 `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL`. In this case you do not use `ActivatedRule|Action`. For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction`.  
Type: Array of [RuleGroupUpdate](API_waf_RuleGroupUpdate.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_waf_UpdateRuleGroup_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateRuleGroup_ResponseSyntax) **   <a name="WAF-waf_UpdateRuleGroup-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateRuleGroup` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

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

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## See Also
<a name="API_waf_UpdateRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateRuleGroup) 