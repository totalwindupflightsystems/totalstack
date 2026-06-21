---
id: "@specs/aws/wafv2/docs/API_waf_GetRateBasedRule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRateBasedRule"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRateBasedRule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_GetRateBasedRule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRateBasedRule
<a name="API_waf_GetRateBasedRule"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [RateBasedRule](API_waf_RateBasedRule.md) that is specified by the `RuleId` that you included in the `GetRateBasedRule` request.

## Request Syntax
<a name="API_waf_GetRateBasedRule_RequestSyntax"></a>

```
{
   "RuleId": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_GetRateBasedRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleId](#API_waf_GetRateBasedRule_RequestSyntax) **   <a name="WAF-waf_GetRateBasedRule-request-RuleId"></a>
The `RuleId` of the [RateBasedRule](API_waf_RateBasedRule.md) that you want to get. `RuleId` is returned by [CreateRateBasedRule](API_waf_CreateRateBasedRule.md) and by [ListRateBasedRules](API_waf_ListRateBasedRules.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_GetRateBasedRule_ResponseSyntax"></a>

```
{
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
<a name="API_waf_GetRateBasedRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rule](#API_waf_GetRateBasedRule_ResponseSyntax) **   <a name="WAF-waf_GetRateBasedRule-response-Rule"></a>
Information about the [RateBasedRule](API_waf_RateBasedRule.md) that you specified in the `GetRateBasedRule` request.  
Type: [RateBasedRule](API_waf_RateBasedRule.md) object

## Errors
<a name="API_waf_GetRateBasedRule_Errors"></a>

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
<a name="API_waf_GetRateBasedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/GetRateBasedRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GetRateBasedRule) 