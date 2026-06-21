---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetRegexMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRegexMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetRegexMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetRegexMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRegexMatchSet
<a name="API_wafRegional_GetRegexMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [RegexMatchSet](API_wafRegional_RegexMatchSet.md) specified by `RegexMatchSetId`.

## Request Syntax
<a name="API_wafRegional_GetRegexMatchSet_RequestSyntax"></a>

```
{
   "RegexMatchSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetRegexMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegexMatchSetId](#API_wafRegional_GetRegexMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_GetRegexMatchSet-request-RegexMatchSetId"></a>
The `RegexMatchSetId` of the [RegexMatchSet](API_wafRegional_RegexMatchSet.md) that you want to get. `RegexMatchSetId` is returned by [CreateRegexMatchSet](API_wafRegional_CreateRegexMatchSet.md) and by [ListRegexMatchSets](API_wafRegional_ListRegexMatchSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetRegexMatchSet_ResponseSyntax"></a>

```
{
   "RegexMatchSet": { 
      "Name": "string",
      "RegexMatchSetId": "string",
      "RegexMatchTuples": [ 
         { 
            "FieldToMatch": { 
               "Data": "string",
               "Type": "string"
            },
            "RegexPatternSetId": "string",
            "TextTransformation": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_wafRegional_GetRegexMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegexMatchSet](#API_wafRegional_GetRegexMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_GetRegexMatchSet-response-RegexMatchSet"></a>
Information about the [RegexMatchSet](API_wafRegional_RegexMatchSet.md) that you specified in the `GetRegexMatchSet` request. For more information, see [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md).  
Type: [RegexMatchSet](API_wafRegional_RegexMatchSet.md) object

## Errors
<a name="API_wafRegional_GetRegexMatchSet_Errors"></a>

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
<a name="API_wafRegional_GetRegexMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetRegexMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetRegexMatchSet) 