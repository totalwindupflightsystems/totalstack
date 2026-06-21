---
id: "@specs/aws/wafv2/docs/API_waf_UpdateIPSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateIPSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# UpdateIPSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_UpdateIPSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateIPSet
<a name="API_waf_UpdateIPSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Inserts or deletes [IPSetDescriptor](API_waf_IPSetDescriptor.md) objects in an `IPSet`. For each `IPSetDescriptor` object, you specify the following values: 
+ Whether to insert or delete the object from the array. If you want to change an `IPSetDescriptor` object, you delete the existing object and add a new one.
+ The IP address version, `IPv4` or `IPv6`. 
+ The IP address in CIDR notation, for example, `192.0.2.0/24` (for the range of IP addresses from `192.0.2.0` to `192.0.2.255`) or `192.0.2.44/32` (for the individual IP address `192.0.2.44`). 

 AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

IPv6 addresses can be represented using any of the following formats:
+ 1111:0000:0000:0000:0000:0000:0000:0111/128
+ 1111:0:0:0:0:0:0:0111/128
+ 1111::0111/128
+ 1111::111/128

You use an `IPSet` to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you're receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an `IPSet` that specifies those IP addresses, and then configure AWS WAF to block the requests. 

To create and configure an `IPSet`, perform the following steps:

1. Submit a [CreateIPSet](API_waf_CreateIPSet.md) request.

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of an [UpdateIPSet](#API_waf_UpdateIPSet) request.

1. Submit an `UpdateIPSet` request to specify the IP addresses that you want AWS WAF to watch for.

When you update an `IPSet`, you specify the IP addresses that you want to add and the IP addresses that you want to delete. If you want to change an IP address, delete the existing IP address and add the new one.

You can update a maximum of 1,000 addresses in a single request.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_UpdateIPSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "IPSetId": "{{string}}",
   "Updates": [ 
      { 
         "Action": "{{string}}",
         "IPSetDescriptor": { 
            "Type": "{{string}}",
            "Value": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_waf_UpdateIPSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_UpdateIPSet_RequestSyntax) **   <a name="WAF-waf_UpdateIPSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [IPSetId](#API_waf_UpdateIPSet_RequestSyntax) **   <a name="WAF-waf_UpdateIPSet-request-IPSetId"></a>
The `IPSetId` of the [IPSet](API_waf_IPSet.md) that you want to update. `IPSetId` is returned by [CreateIPSet](API_waf_CreateIPSet.md) and by [ListIPSets](API_waf_ListIPSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Updates](#API_waf_UpdateIPSet_RequestSyntax) **   <a name="WAF-waf_UpdateIPSet-request-Updates"></a>
An array of `IPSetUpdate` objects that you want to insert into or delete from an [IPSet](API_waf_IPSet.md). For more information, see the applicable data types:  
+  [IPSetUpdate](API_waf_IPSetUpdate.md): Contains `Action` and `IPSetDescriptor` 
+  [IPSetDescriptor](API_waf_IPSetDescriptor.md): Contains `Type` and `Value` 
You can specify a maximum of 1,000 addresses in a single request, for example, in a single request you can insert 999 addresses and delete 1 address, but you can't insert 999 addresses and delete 2 addresses.  
Type: Array of [IPSetUpdate](API_waf_IPSetUpdate.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_waf_UpdateIPSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_UpdateIPSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_UpdateIPSet_ResponseSyntax) **   <a name="WAF-waf_UpdateIPSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateIPSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_UpdateIPSet_Errors"></a>

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
<a name="API_waf_UpdateIPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/UpdateIPSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/UpdateIPSet) 