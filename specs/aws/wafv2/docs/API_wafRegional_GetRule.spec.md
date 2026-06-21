---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRule"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRule
<a name="API_wafRegional_GetRule"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [Rule](API_wafRegional_Rule.md) that is specified by the `RuleId` that you included in the `GetRule` request.

## Request Syntax
<a name="API_wafRegional_GetRule_RequestSyntax"></a>

```
{
   "RuleId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleId](#API_wafRegional_GetRule_RequestSyntax) **   <a name="WAF-wafRegional_GetRule-request-RuleId"></a>
The `RuleId` of the [Rule](API_wafRegional_Rule.md) that you want to get. `RuleId` is returned by [CreateRule](API_wafRegional_CreateRule.md) and by [ListRules](API_wafRegional_ListRules.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetRule_ResponseSyntax"></a>

```
{
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
<a name="API_wafRegional_GetRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rule](#API_wafRegional_GetRule_ResponseSyntax) **   <a name="WAF-wafRegional_GetRule-response-Rule"></a>
Information about the [Rule](API_wafRegional_Rule.md) that you specified in the `GetRule` request. For more information, see the following topics:  
+  [Rule](API_wafRegional_Rule.md): Contains `MetricName`, `Name`, an array of `Predicate` objects, and `RuleId` 
+  [Predicate](API_wafRegional_Predicate.md): Each `Predicate` object contains `DataId`, `Negated`, and `Type` 
Type: [Rule](API_wafRegional_Rule.md) object

## Errors
<a name="API_wafRegional_GetRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_GetRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetRule) 