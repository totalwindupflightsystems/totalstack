---
id: "@specs/aws/wafv2/docs/API_waf_CreateSqlInjectionMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSqlInjectionMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateSqlInjectionMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_CreateSqlInjectionMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSqlInjectionMatchSet
<a name="API_waf_CreateSqlInjectionMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md), which you use to allow, block, or count requests that contain snippets of SQL code in a specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.

To create and configure a `SqlInjectionMatchSet`, perform the following steps:

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateSqlInjectionMatchSet` request.

1. Submit a `CreateSqlInjectionMatchSet` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateSqlInjectionMatchSet](API_waf_UpdateSqlInjectionMatchSet.md) request.

1. Submit an [UpdateSqlInjectionMatchSet](API_waf_UpdateSqlInjectionMatchSet.md) request to specify the parts of web requests in which you want to allow, block, or count malicious SQL code.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_CreateSqlInjectionMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_CreateSqlInjectionMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_CreateSqlInjectionMatchSet_RequestSyntax) **   <a name="WAF-waf_CreateSqlInjectionMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_waf_CreateSqlInjectionMatchSet_RequestSyntax) **   <a name="WAF-waf_CreateSqlInjectionMatchSet-request-Name"></a>
A friendly name or description for the [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md) that you're creating. You can't change `Name` after you create the `SqlInjectionMatchSet`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_CreateSqlInjectionMatchSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "SqlInjectionMatchSet": { 
      "Name": "string",
      "SqlInjectionMatchSetId": "string",
      "SqlInjectionMatchTuples": [ 
         { 
            "FieldToMatch": { 
               "Data": "string",
               "Type": "string"
            },
            "TextTransformation": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_waf_CreateSqlInjectionMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_CreateSqlInjectionMatchSet_ResponseSyntax) **   <a name="WAF-waf_CreateSqlInjectionMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateSqlInjectionMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [SqlInjectionMatchSet](#API_waf_CreateSqlInjectionMatchSet_ResponseSyntax) **   <a name="WAF-waf_CreateSqlInjectionMatchSet-response-SqlInjectionMatchSet"></a>
A [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md).  
Type: [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md) object

## Errors
<a name="API_waf_CreateSqlInjectionMatchSet_Errors"></a>

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
<a name="API_waf_CreateSqlInjectionMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/CreateSqlInjectionMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/CreateSqlInjectionMatchSet) 