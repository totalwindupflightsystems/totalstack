---
id: "@specs/aws/wafv2/docs/API_wafRegional_DeleteXssMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteXssMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DeleteXssMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_DeleteXssMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteXssMatchSet
<a name="API_wafRegional_DeleteXssMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Permanently deletes an [XssMatchSet](API_wafRegional_XssMatchSet.md). You can't delete an `XssMatchSet` if it's still used in any `Rules` or if it still contains any [XssMatchTuple](API_wafRegional_XssMatchTuple.md) objects.

If you just want to remove an `XssMatchSet` from a `Rule`, use [UpdateRule](API_wafRegional_UpdateRule.md).

To permanently delete an `XssMatchSet` from AWS WAF, perform the following steps:

1. Update the `XssMatchSet` to remove filters, if any. For more information, see [UpdateXssMatchSet](API_wafRegional_UpdateXssMatchSet.md).

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `DeleteXssMatchSet` request.

1. Submit a `DeleteXssMatchSet` request.

## Request Syntax
<a name="API_wafRegional_DeleteXssMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "XssMatchSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_DeleteXssMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_DeleteXssMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_DeleteXssMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [XssMatchSetId](#API_wafRegional_DeleteXssMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_DeleteXssMatchSet-request-XssMatchSetId"></a>
The `XssMatchSetId` of the [XssMatchSet](API_wafRegional_XssMatchSet.md) that you want to delete. `XssMatchSetId` is returned by [CreateXssMatchSet](API_wafRegional_CreateXssMatchSet.md) and by [ListXssMatchSets](API_wafRegional_ListXssMatchSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_DeleteXssMatchSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_wafRegional_DeleteXssMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_wafRegional_DeleteXssMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_DeleteXssMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `DeleteXssMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_wafRegional_DeleteXssMatchSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

 ** WAFNonEmptyEntityException **   
The operation failed because you tried to delete an object that isn't empty. For example:  
+ You tried to delete a `WebACL` that still contains one or more `Rule` objects.
+ You tried to delete a `Rule` that still contains one or more `ByteMatchSet` objects or other predicates.
+ You tried to delete a `ByteMatchSet` that contains one or more `ByteMatchTuple` objects.
+ You tried to delete an `IPSet` that references one or more IP addresses.
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

## See Also
<a name="API_wafRegional_DeleteXssMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/DeleteXssMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/DeleteXssMatchSet) 