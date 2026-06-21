---
id: "@specs/aws/wafv2/docs/API_wafRegional_CreateRegexPatternSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRegexPatternSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateRegexPatternSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_CreateRegexPatternSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRegexPatternSet
<a name="API_wafRegional_CreateRegexPatternSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a `RegexPatternSet`. You then use [UpdateRegexPatternSet](API_wafRegional_UpdateRegexPatternSet.md) to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

To create and configure a `RegexPatternSet`, perform the following steps:

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexPatternSet` request.

1. Submit a `CreateRegexPatternSet` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.

1. Submit an [UpdateRegexPatternSet](API_wafRegional_UpdateRegexPatternSet.md) request to specify the string that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_wafRegional_CreateRegexPatternSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_CreateRegexPatternSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_CreateRegexPatternSet_RequestSyntax) **   <a name="WAF-wafRegional_CreateRegexPatternSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_wafRegional_CreateRegexPatternSet_RequestSyntax) **   <a name="WAF-wafRegional_CreateRegexPatternSet-request-Name"></a>
A friendly name or description of the [RegexPatternSet](API_wafRegional_RegexPatternSet.md). You can't change `Name` after you create a `RegexPatternSet`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_CreateRegexPatternSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "RegexPatternSet": { 
      "Name": "string",
      "RegexPatternSetId": "string",
      "RegexPatternStrings": [ "string" ]
   }
}
```

## Response Elements
<a name="API_wafRegional_CreateRegexPatternSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_wafRegional_CreateRegexPatternSet_ResponseSyntax) **   <a name="WAF-wafRegional_CreateRegexPatternSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateRegexPatternSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [RegexPatternSet](#API_wafRegional_CreateRegexPatternSet_ResponseSyntax) **   <a name="WAF-wafRegional_CreateRegexPatternSet-response-RegexPatternSet"></a>
A [RegexPatternSet](API_wafRegional_RegexPatternSet.md) that contains no objects.  
Type: [RegexPatternSet](API_wafRegional_RegexPatternSet.md) object

## Errors
<a name="API_wafRegional_CreateRegexPatternSet_Errors"></a>

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
<a name="API_wafRegional_CreateRegexPatternSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/CreateRegexPatternSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/CreateRegexPatternSet) 