---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRuleGroup"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRuleGroup
<a name="API_wafRegional_GetRuleGroup"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [RuleGroup](API_wafRegional_RuleGroup.md) that is specified by the `RuleGroupId` that you included in the `GetRuleGroup` request.

To view the rules in a rule group, use [ListActivatedRulesInRuleGroup](API_wafRegional_ListActivatedRulesInRuleGroup.md).

## Request Syntax
<a name="API_wafRegional_GetRuleGroup_RequestSyntax"></a>

```
{
   "RuleGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleGroupId](#API_wafRegional_GetRuleGroup_RequestSyntax) **   <a name="WAF-wafRegional_GetRuleGroup-request-RuleGroupId"></a>
The `RuleGroupId` of the [RuleGroup](API_wafRegional_RuleGroup.md) that you want to get. `RuleGroupId` is returned by [CreateRuleGroup](API_wafRegional_CreateRuleGroup.md) and by [ListRuleGroups](API_wafRegional_ListRuleGroups.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetRuleGroup_ResponseSyntax"></a>

```
{
   "RuleGroup": { 
      "MetricName": "string",
      "Name": "string",
      "RuleGroupId": "string"
   }
}
```

## Response Elements
<a name="API_wafRegional_GetRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleGroup](#API_wafRegional_GetRuleGroup_ResponseSyntax) **   <a name="WAF-wafRegional_GetRuleGroup-response-RuleGroup"></a>
Information about the [RuleGroup](API_wafRegional_RuleGroup.md) that you specified in the `GetRuleGroup` request.   
Type: [RuleGroup](API_wafRegional_RuleGroup.md) object

## Errors
<a name="API_wafRegional_GetRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_GetRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetRuleGroup) 