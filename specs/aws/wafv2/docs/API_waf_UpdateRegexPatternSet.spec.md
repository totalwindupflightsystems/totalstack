---
id: "@specs/aws/wafv2/docs/API_waf_UpdateRegexPatternSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateRegexPatternSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateRegexPatternSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateRegexPatternSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateRegexPatternSet
<a name="API_waf_UpdateRegexPatternSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes `RegexPatternString` objects in a [RegexPatternSet](API_waf_RegexPatternSet.md). For each `RegexPatternString` object, you specify the following values: 
+ Whether to insert or delete the `RegexPatternString`.
+ The regular expression pattern that you want to insert or delete. For more information, see [RegexPatternSet](API_waf_RegexPatternSet.md). 

 For example, you can create a `RegexPatternString` such as `B[a@]dB[o0]t`. AWS WAF will match this `RegexPatternString` to:
+ BadBot
+ BadB0t
+ B@dBot
+ B@dB0t

To create and configure a `RegexPatternSet`, perform the following steps:

1. Create a `RegexPatternSet.` For more information, see [CreateRegexPatternSet](API_waf_CreateRegexPatternSet.md).

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.

1. Submit an `UpdateRegexPatternSet` request to specify the regular expression pattern that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateRegexPatternSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "RegexPatternSetId": "{{string}}",
   "Updates": [ 
      { 
         "Action": "{{string}}",
         "RegexPatternString": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_waf_UpdateRegexPatternSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-waf_UpdateRegexPatternSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [RegexPatternSetId](#API_waf_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-waf_UpdateRegexPatternSet-request-RegexPatternSetId"></a>
The `RegexPatternSetId` of the [RegexPatternSet](API_waf_RegexPatternSet.md) that you want to update. `RegexPatternSetId` is returned by [CreateRegexPatternSet](API_waf_CreateRegexPatternSet.md) and by [ListRegexPatternSets](API_waf_ListRegexPatternSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Updates](#API_waf_UpdateRegexPatternSet_RequestSyntax) **   <a name="WAF-waf_UpdateRegexPatternSet-request-Updates"></a>
An array of `RegexPatternSetUpdate` objects that you want to insert into or delete from a [RegexPatternSet](API_waf_RegexPatternSet.md).  
Type: Array of [RegexPatternSetUpdate](API_waf_RegexPatternSetUpdate.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_waf_UpdateRegexPatternSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateRegexPatternSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateRegexPatternSet_ResponseSyntax) **   <a name="WAF-waf_UpdateRegexPatternSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateRegexPatternSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateRegexPatternSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

 ** WAFInvalidOperationException **   
The operation failed because there was nothing to do. For example:  
+ You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the specified `WebACL`.
+ You tried to remove an IP address from an `IPSet`, but the IP address isn't in the specified `IPSet`.
+ You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the `ByteMatchTuple` isn't in the specified `WebACL`.
+ You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the specified `WebACL`.
+ You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple` already exists in the specified `WebACL`.
HTTP Status Code: 400

 ** WAFInvalidRegexPatternException **   
The regular expression (regex) you specified in `RegexPatternString` is invalid.  
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
<a name="API_waf_UpdateRegexPatternSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateRegexPatternSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateRegexPatternSet) 