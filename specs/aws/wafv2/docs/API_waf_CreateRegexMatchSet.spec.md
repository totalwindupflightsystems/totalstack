---
id: "@specs/aws/wafv2/docs/API_waf_CreateRegexMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRegexMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateRegexMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_CreateRegexMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRegexMatchSet
<a name="API_waf_CreateRegexMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a [RegexMatchSet](API_waf_RegexMatchSet.md). You then use [UpdateRegexMatchSet](API_waf_UpdateRegexMatchSet.md) to identify the part of a web request that you want AWS WAF to inspect, such as the values of the `User-Agent` header or the query string. For example, you can create a `RegexMatchSet` that contains a `RegexMatchTuple` that looks for any requests with `User-Agent` headers that match a `RegexPatternSet` with pattern `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

To create and configure a `RegexMatchSet`, perform the following steps:

1. Use [GetChangeToken](API_waf_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexMatchSet` request.

1. Submit a `CreateRegexMatchSet` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexMatchSet` request.

1. Submit an [UpdateRegexMatchSet](API_waf_UpdateRegexMatchSet.md) request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI path) and the value, using a `RegexPatternSet`, that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_waf_CreateRegexMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_CreateRegexMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_waf_CreateRegexMatchSet_RequestSyntax) **   <a name="WAF-waf_CreateRegexMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_waf_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_waf_CreateRegexMatchSet_RequestSyntax) **   <a name="WAF-waf_CreateRegexMatchSet-request-Name"></a>
A friendly name or description of the [RegexMatchSet](API_waf_RegexMatchSet.md). You can't change `Name` after you create a `RegexMatchSet`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_CreateRegexMatchSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "RegexMatchSet": { 
      "Name": "string",
      "RegexMatchSetId": "string",
      "RegexMatchTuples": [ 
         { 
            "FieldToMatch": { 
               "Data": "string",
               "Type": "string"
            },
            "RegexPatternSetId": "string",
            "TextTransformation": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_waf_CreateRegexMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_CreateRegexMatchSet_ResponseSyntax) **   <a name="WAF-waf_CreateRegexMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRegexMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_waf_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [RegexMatchSet](#API_waf_CreateRegexMatchSet_ResponseSyntax) **   <a name="WAF-waf_CreateRegexMatchSet-response-RegexMatchSet"></a>
A [RegexMatchSet](API_waf_RegexMatchSet.md) that contains no `RegexMatchTuple` objects.  
Type: [RegexMatchSet](API_waf_RegexMatchSet.md) object

## Errors
<a name="API_waf_CreateRegexMatchSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFDisallowedNameException **   
The name specified is invalid.  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFLimitsExceededException **   
The operation exceeds a resource limit, for example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html) in the * AWS WAF Developer Guide*.  
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

## See Also
<a name="API_waf_CreateRegexMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/CreateRegexMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/CreateRegexMatchSet) 