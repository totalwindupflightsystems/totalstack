---
id: "@specs/aws/wafv2/docs/API_wafRegional_ListByteMatchSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListByteMatchSets"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListByteMatchSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_ListByteMatchSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListByteMatchSets
<a name="API_wafRegional_ListByteMatchSets"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns an array of [ByteMatchSetSummary](API_wafRegional_ByteMatchSetSummary.md) objects.

## Request Syntax
<a name="API_wafRegional_ListByteMatchSets_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_ListByteMatchSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_wafRegional_ListByteMatchSets_RequestSyntax) **   <a name="WAF-wafRegional_ListByteMatchSets-request-Limit"></a>
Specifies the number of `ByteMatchSet` objects that you want AWS WAF to return for this request. If you have more `ByteMatchSets` objects than the number you specify for `Limit`, the response includes a `NextMarker` value that you can use to get another batch of `ByteMatchSet` objects.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** [NextMarker](#API_wafRegional_ListByteMatchSets_RequestSyntax) **   <a name="WAF-wafRegional_ListByteMatchSets-request-NextMarker"></a>
If you specify a value for `Limit` and you have more `ByteMatchSets` than the value of `Limit`, AWS WAF returns a `NextMarker` value in the response that allows you to list another group of `ByteMatchSets`. For the second and subsequent `ListByteMatchSets` requests, specify the value of `NextMarker` from the previous response to get information about another batch of `ByteMatchSets`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: No

## Response Syntax
<a name="API_wafRegional_ListByteMatchSets_ResponseSyntax"></a>

```
{
   "ByteMatchSets": [ 
      { 
         "ByteMatchSetId": "string",
         "Name": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_wafRegional_ListByteMatchSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByteMatchSets](#API_wafRegional_ListByteMatchSets_ResponseSyntax) **   <a name="WAF-wafRegional_ListByteMatchSets-response-ByteMatchSets"></a>
An array of [ByteMatchSetSummary](API_wafRegional_ByteMatchSetSummary.md) objects.  
Type: Array of [ByteMatchSetSummary](API_wafRegional_ByteMatchSetSummary.md) objects

 ** [NextMarker](#API_wafRegional_ListByteMatchSets_ResponseSyntax) **   <a name="WAF-wafRegional_ListByteMatchSets-response-NextMarker"></a>
If you have more `ByteMatchSet` objects than the number that you specified for `Limit` in the request, the response includes a `NextMarker` value. To list more `ByteMatchSet` objects, submit another `ListByteMatchSets` request, and specify the `NextMarker` value from the response in the `NextMarker` value in the next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*` 

## Errors
<a name="API_wafRegional_ListByteMatchSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_ListByteMatchSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/ListByteMatchSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/ListByteMatchSets) 