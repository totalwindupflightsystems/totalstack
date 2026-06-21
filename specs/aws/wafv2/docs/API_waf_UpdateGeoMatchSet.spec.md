---
id: "@specs/aws/wafv2/docs/API_waf_UpdateGeoMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateGeoMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateGeoMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateGeoMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateGeoMatchSet
<a name="API_waf_UpdateGeoMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes [GeoMatchConstraint](API_waf_GeoMatchConstraint.md) objects in an `GeoMatchSet`. For each `GeoMatchConstraint` object, you specify the following values: 
+ Whether to insert or delete the object from the array. If you want to change an `GeoMatchConstraint` object, you delete the existing object and add a new one.
+ The `Type`. The only valid value for `Type` is `Country`.
+ The `Value`, which is a two character code for the country to add to the `GeoMatchConstraint` object. Valid codes are listed in [GeoMatchConstraint:Value](API_waf_GeoMatchConstraint.md#WAF-Type-waf_GeoMatchConstraint-Value).

To create and configure an `GeoMatchSet`, perform the following steps:

1. Submit a [CreateGeoMatchSet](API_waf_CreateGeoMatchSet.md) request.

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of an [UpdateGeoMatchSet](#API_waf_UpdateGeoMatchSet) request.

1. Submit an `UpdateGeoMatchSet` request to specify the country that you want AWS WAF to watch for.

When you update an `GeoMatchSet`, you specify the country that you want to add and/or the country that you want to delete. If you want to change a country, you delete the existing country and add the new one.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateGeoMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "GeoMatchSetId": "{{string}}",
   "Updates": [ 
      { 
         "Action": "{{string}}",
         "GeoMatchConstraint": { 
            "Type": "{{string}}",
            "Value": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_waf_UpdateGeoMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateGeoMatchSet_RequestSyntax) **   <a name="WAF-waf_UpdateGeoMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [GeoMatchSetId](#API_waf_UpdateGeoMatchSet_RequestSyntax) **   <a name="WAF-waf_UpdateGeoMatchSet-request-GeoMatchSetId"></a>
The `GeoMatchSetId` of the [GeoMatchSet](API_waf_GeoMatchSet.md) that you want to update. `GeoMatchSetId` is returned by [CreateGeoMatchSet](API_waf_CreateGeoMatchSet.md) and by [ListGeoMatchSets](API_waf_ListGeoMatchSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Updates](#API_waf_UpdateGeoMatchSet_RequestSyntax) **   <a name="WAF-waf_UpdateGeoMatchSet-request-Updates"></a>
An array of `GeoMatchSetUpdate` objects that you want to insert into or delete from an [GeoMatchSet](API_waf_GeoMatchSet.md). For more information, see the applicable data types:  
+  [GeoMatchSetUpdate](API_waf_GeoMatchSetUpdate.md): Contains `Action` and `GeoMatchConstraint` 
+  [GeoMatchConstraint](API_waf_GeoMatchConstraint.md): Contains `Type` and `Value` 

  You can have only one `Type` and `Value` per `GeoMatchConstraint`. To add multiple countries, include multiple `GeoMatchSetUpdate` objects in your request.
Type: Array of [GeoMatchSetUpdate](API_waf_GeoMatchSetUpdate.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_waf_UpdateGeoMatchSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateGeoMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateGeoMatchSet_ResponseSyntax) **   <a name="WAF-waf_UpdateGeoMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateGeoMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateGeoMatchSet_Errors"></a>

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
<a name="API_waf_UpdateGeoMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateGeoMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateGeoMatchSet) 