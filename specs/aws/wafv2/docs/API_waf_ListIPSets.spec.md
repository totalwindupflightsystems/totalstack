---
id: "@specs/aws/wafv2/docs/API_waf_ListIPSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIPSets"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListIPSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_ListIPSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIPSets
<a name="API_waf_ListIPSets"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns an array of [IPSetSummary](API_waf_IPSetSummary.md) objects in the response.

## Request Syntax
<a name="API_waf_ListIPSets_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_ListIPSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_waf_ListIPSets_RequestSyntax) **   <a name="WAF-waf_ListIPSets-request-Limit"></a>
Specifies the number of `IPSet` objects that you want AWS WAF to return for this request. If you have more `IPSet` objects than the number you specify for `Limit`, the response includes a `NextMarker` value that you can use to get another batch of `IPSet` objects.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** [NextMarker](#API_waf_ListIPSets_RequestSyntax) **   <a name="WAF-waf_ListIPSets-request-NextMarker"></a>
 AWS WAF returns a `NextMarker` value in the response that allows you to list another group of `IPSets`. For the second and subsequent `ListIPSets` requests, specify the value of `NextMarker` from the previous response to get information about another batch of `IPSets`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: No

## Response Syntax
<a name="API_waf_ListIPSets_ResponseSyntax"></a>

```
{
   "IPSets": [ 
      { 
         "IPSetId": "string",
         "Name": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_waf_ListIPSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IPSets](#API_waf_ListIPSets_ResponseSyntax) **   <a name="WAF-waf_ListIPSets-response-IPSets"></a>
An array of [IPSetSummary](API_waf_IPSetSummary.md) objects.  
Type: Array of [IPSetSummary](API_waf_IPSetSummary.md) objects

 ** [NextMarker](#API_waf_ListIPSets_ResponseSyntax) **   <a name="WAF-waf_ListIPSets-response-NextMarker"></a>
To list more `IPSet` objects, submit another `ListIPSets` request, and in the next request use the `NextMarker` response value as the `NextMarker` value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_ListIPSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

## See Also
<a name="API_waf_ListIPSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/ListIPSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ListIPSets) 