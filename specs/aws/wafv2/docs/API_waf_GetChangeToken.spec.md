---
id: "@specs/aws/wafv2/docs/API_waf_GetChangeToken"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetChangeToken"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetChangeToken

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_GetChangeToken
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetChangeToken
<a name="API_waf_GetChangeToken"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn't submit conflicting requests to AWS WAF.

Each create, update, or delete request must use a unique change token. If your application submits a `GetChangeToken` request and then submits a second `GetChangeToken` request before submitting a create, update, or delete request, the second `GetChangeToken` request returns the same value as the first `GetChangeToken` request.

When you use a change token in a create, update, or delete request, the status of the change token changes to `PENDING`, which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use `GetChangeTokenStatus` to determine the status of your change token.

## Response Syntax
<a name="API_waf_GetChangeToken_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_waf_GetChangeToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_waf_GetChangeToken_ResponseSyntax) **   <a name="WAF-waf_GetChangeToken-response-ChangeToken"></a>
The `ChangeToken` that you used in the request. Use this value in a `GetChangeTokenStatus` request to get the current status of the request.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_GetChangeToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

## See Also
<a name="API_waf_GetChangeToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/GetChangeToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GetChangeToken) 