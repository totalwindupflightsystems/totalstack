---
id: "@specs/aws/wafv2/docs/API_waf_CreateRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRuleGroup"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_CreateRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRuleGroup
<a name="API_waf_CreateRuleGroup"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a `RuleGroup`. A rule group is a collection of predefined rules that you add to a web ACL. You use [UpdateRuleGroup](API_waf_UpdateRuleGroup.md) to add rules to the rule group.

Rule groups are subject to the following limits:
+ Three rule groups per account. You can request an increase to this limit by contacting customer support.
+ One rule group per web ACL.
+ Ten rules per rule group.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_CreateRuleGroup_RequestSyntax"></a>

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
<a name="API_waf_CreateRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_CreateRuleGroup_RequestSyntax) **   <a name="WAF-waf_CreateRuleGroup-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [MetricName](#API_waf_CreateRuleGroup_RequestSyntax) **   <a name="WAF-waf_CreateRuleGroup-request-MetricName"></a>
A friendly name or description for the metrics for this `RuleGroup`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change the name of the metric after you create the `RuleGroup`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_waf_CreateRuleGroup_RequestSyntax) **   <a name="WAF-waf_CreateRuleGroup-request-Name"></a>
A friendly name or description of the [RuleGroup](API_waf_RuleGroup.md). You can't change `Name` after you create a `RuleGroup`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Tags](#API_waf_CreateRuleGroup_RequestSyntax) **   <a name="WAF-waf_CreateRuleGroup-request-Tags"></a>
  
Type: Array of [Tag](API_waf_Tag.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## Response Syntax
<a name="API_waf_CreateRuleGroup_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "RuleGroup": { 
      "MetricName": "string",
      "Name": "string",
      "RuleGroupId": "string"
   }
}
```

## Response Elements
<a name="API_waf_CreateRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_CreateRuleGroup_ResponseSyntax) **   <a name="WAF-waf_CreateRuleGroup-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRuleGroup` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [RuleGroup](#API_waf_CreateRuleGroup_ResponseSyntax) **   <a name="WAF-waf_CreateRuleGroup-response-RuleGroup"></a>
An empty [RuleGroup](API_waf_RuleGroup.md).  
Type: [RuleGroup](API_waf_RuleGroup.md) object

## Errors
<a name="API_waf_CreateRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFBadRequestException **   
  
HTTP Status Code: 400

 ** WAFDisallowedNameException **   
The name specified is invalid.  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

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
<a name="API_waf_CreateRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/CreateRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/CreateRuleGroup) 