---
id: "@specs/aws/wafv2/docs/API_waf_UpdateSizeConstraintSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSizeConstraintSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateSizeConstraintSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateSizeConstraintSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSizeConstraintSet
<a name="API_waf_UpdateSizeConstraintSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes [SizeConstraint](API_waf_SizeConstraint.md) objects (filters) in a [SizeConstraintSet](API_waf_SizeConstraintSet.md). For each `SizeConstraint` object, you specify the following values: 
+ Whether to insert or delete the object from the array. If you want to change a `SizeConstraintSetUpdate` object, you delete the existing object and add a new one.
+ The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the `User-Agent` header.
+ Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first `8192` bytes of your request to AWS WAF.

  You can only specify a single type of TextTransformation.
+ A `ComparisonOperator` used for evaluating the selected part of the request against the specified `Size`, such as equals, greater than, less than, and so on.
+ The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation.

For example, you can add a `SizeConstraintSetUpdate` object that matches web requests in which the length of the `User-Agent` header is greater than 100 bytes. You can then configure AWS WAF to block those requests.

To create and configure a `SizeConstraintSet`, perform the following steps:

1. Create a `SizeConstraintSet.` For more information, see [CreateSizeConstraintSet](API_waf_CreateSizeConstraintSet.md).

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of an `UpdateSizeConstraintSet` request.

1. Submit an `UpdateSizeConstraintSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI path) and the value that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateSizeConstraintSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "SizeConstraintSetId": "{{string}}",
   "Updates": [ 
      { 
         "Action": "{{string}}",
         "SizeConstraint": { 
            "ComparisonOperator": "{{string}}",
            "FieldToMatch": { 
               "Data": "{{string}}",
               "Type": "{{string}}"
            },
            "Size": {{number}},
            "TextTransformation": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_waf_UpdateSizeConstraintSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateSizeConstraintSet_RequestSyntax) **   <a name="WAF-waf_UpdateSizeConstraintSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [SizeConstraintSetId](#API_waf_UpdateSizeConstraintSet_RequestSyntax) **   <a name="WAF-waf_UpdateSizeConstraintSet-request-SizeConstraintSetId"></a>
The `SizeConstraintSetId` of the [SizeConstraintSet](API_waf_SizeConstraintSet.md) that you want to update. `SizeConstraintSetId` is returned by [CreateSizeConstraintSet](API_waf_CreateSizeConstraintSet.md) and by [ListSizeConstraintSets](API_waf_ListSizeConstraintSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Updates](#API_waf_UpdateSizeConstraintSet_RequestSyntax) **   <a name="WAF-waf_UpdateSizeConstraintSet-request-Updates"></a>
An array of `SizeConstraintSetUpdate` objects that you want to insert into or delete from a [SizeConstraintSet](API_waf_SizeConstraintSet.md). For more information, see the applicable data types:  
+  [SizeConstraintSetUpdate](API_waf_SizeConstraintSetUpdate.md): Contains `Action` and `SizeConstraint` 
+  [SizeConstraint](API_waf_SizeConstraint.md): Contains `FieldToMatch`, `TextTransformation`, `ComparisonOperator`, and `Size` 
+  [FieldToMatch](API_waf_FieldToMatch.md): Contains `Data` and `Type` 
Type: Array of [SizeConstraintSetUpdate](API_waf_SizeConstraintSetUpdate.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_waf_UpdateSizeConstraintSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateSizeConstraintSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateSizeConstraintSet_ResponseSyntax) **   <a name="WAF-waf_UpdateSizeConstraintSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateSizeConstraintSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateSizeConstraintSet_Errors"></a>

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

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:  
+ You specified an invalid parameter name.
+ You specified an invalid value.
+ You tried to update an object (`ByteMatchSet`, `IPSet`, `Rule`, or `WebACL`) using an action other than `INSERT` or `DELETE`.
+ You tried to create a `WebACL` with a `DefaultAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to create a `RateBasedRule` with a `RateKey` value other than `IP`.
+ You tried to update a `WebACL` with a `WafAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to update a `ByteMatchSet` with a `FieldToMatch` `Type` other than HEADER, METHOD, QUERY\_STRING, URI, or BODY.
+ You tried to update a `ByteMatchSet` with a `Field` of `HEADER` but no value for `Data`.
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.
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

 ** WAFReferencedItemException **   
The operation failed because you tried to delete an object that is still in use. For example:  
+ You tried to delete a `ByteMatchSet` that is still referenced by a `Rule`.
+ You tried to delete a `Rule` that is still referenced by a `WebACL`.
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## See Also
<a name="API_waf_UpdateSizeConstraintSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateSizeConstraintSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateSizeConstraintSet) 