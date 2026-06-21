---
id: "@specs/aws/wafv2/docs/API_waf_ListRegexPatternSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRegexPatternSets"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListRegexPatternSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_ListRegexPatternSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRegexPatternSets
<a name="API_waf_ListRegexPatternSets"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns an array of [RegexPatternSetSummary](API_waf_RegexPatternSetSummary.md) objects.

## Request Syntax
<a name="API_waf_ListRegexPatternSets_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_ListRegexPatternSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_waf_ListRegexPatternSets_RequestSyntax) **   <a name="WAF-waf_ListRegexPatternSets-request-Limit"></a>
Specifies the number of `RegexPatternSet` objects that you want AWS WAF to return for this request. If you have more `RegexPatternSet` objects than the number you specify for `Limit`, the response includes a `NextMarker` value that you can use to get another batch of `RegexPatternSet` objects.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** [NextMarker](#API_waf_ListRegexPatternSets_RequestSyntax) **   <a name="WAF-waf_ListRegexPatternSets-request-NextMarker"></a>
If you specify a value for `Limit` and you have more `RegexPatternSet` objects than the value of `Limit`, AWS WAF returns a `NextMarker` value in the response that allows you to list another group of `RegexPatternSet` objects. For the second and subsequent `ListRegexPatternSets` requests, specify the value of `NextMarker` from the previous response to get information about another batch of `RegexPatternSet` objects.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: No

## Response Syntax
<a name="API_waf_ListRegexPatternSets_ResponseSyntax"></a>

```
{
   "NextMarker": "string",
   "RegexPatternSets": [ 
      { 
         "Name": "string",
         "RegexPatternSetId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_waf_ListRegexPatternSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextMarker](#API_waf_ListRegexPatternSets_ResponseSyntax) **   <a name="WAF-waf_ListRegexPatternSets-response-NextMarker"></a>
If you have more `RegexPatternSet` objects than the number that you specified for `Limit` in the request, the response includes a `NextMarker` value. To list more `RegexPatternSet` objects, submit another `ListRegexPatternSets` request, and specify the `NextMarker` value from the response in the `NextMarker` value in the next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*` 

 ** [RegexPatternSets](#API_waf_ListRegexPatternSets_ResponseSyntax) **   <a name="WAF-waf_ListRegexPatternSets-response-RegexPatternSets"></a>
An array of [RegexPatternSetSummary](API_waf_RegexPatternSetSummary.md) objects.  
Type: Array of [RegexPatternSetSummary](API_waf_RegexPatternSetSummary.md) objects

## Errors
<a name="API_waf_ListRegexPatternSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

## See Also
<a name="API_waf_ListRegexPatternSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/ListRegexPatternSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ListRegexPatternSets) 