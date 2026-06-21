---
id: "@specs/aws/wafv2/docs/API_wafRegional_CreateByteMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateByteMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateByteMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_CreateByteMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateByteMatchSet
<a name="API_wafRegional_CreateByteMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a `ByteMatchSet`. You then use [UpdateByteMatchSet](API_wafRegional_UpdateByteMatchSet.md) to identify the part of a web request that you want AWS WAF to inspect, such as the values of the `User-Agent` header or the query string. For example, you can create a `ByteMatchSet` that matches any requests with `User-Agent` headers that contain the string `BadBot`. You can then configure AWS WAF to reject those requests.

To create and configure a `ByteMatchSet`, perform the following steps:

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateByteMatchSet` request.

1. Submit a `CreateByteMatchSet` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateByteMatchSet` request.

1. Submit an [UpdateByteMatchSet](API_wafRegional_UpdateByteMatchSet.md) request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI path) and the value that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_wafRegional_CreateByteMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_CreateByteMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_CreateByteMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_CreateByteMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_wafRegional_CreateByteMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_CreateByteMatchSet-request-Name"></a>
A friendly name or description of the [ByteMatchSet](API_wafRegional_ByteMatchSet.md). You can't change `Name` after you create a `ByteMatchSet`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_CreateByteMatchSet_ResponseSyntax"></a>

```
{
   "ByteMatchSet": { 
      "ByteMatchSetId": "string",
      "ByteMatchTuples": [ 
         { 
            "FieldToMatch": { 
               "Data": "string",
               "Type": "string"
            },
            "PositionalConstraint": "string",
            "TargetString": blob,
            "TextTransformation": "string"
         }
      ],
      "Name": "string"
   },
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_wafRegional_CreateByteMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByteMatchSet](#API_wafRegional_CreateByteMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_CreateByteMatchSet-response-ByteMatchSet"></a>
A [ByteMatchSet](API_wafRegional_ByteMatchSet.md) that contains no `ByteMatchTuple` objects.  
Type: [ByteMatchSet](API_wafRegional_ByteMatchSet.md) object

 ** [ChangeToken](#API_wafRegional_CreateByteMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_CreateByteMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateByteMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_wafRegional_CreateByteMatchSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFDisallowedNameException **   
The name specified is invalid.  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
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

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_CreateByteMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/CreateByteMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/CreateByteMatchSet) 