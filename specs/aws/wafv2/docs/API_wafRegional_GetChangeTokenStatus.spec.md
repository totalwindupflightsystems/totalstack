---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetChangeTokenStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetChangeTokenStatus"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetChangeTokenStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetChangeTokenStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetChangeTokenStatus
<a name="API_wafRegional_GetChangeTokenStatus"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the status of a `ChangeToken` that you got by calling [GetChangeToken](API_wafRegional_GetChangeToken.md). `ChangeTokenStatus` is one of the following values:
+  `PROVISIONED`: You requested the change token by calling `GetChangeToken`, but you haven't used it yet in a call to create, update, or delete an AWS WAF object.
+  `PENDING`: AWS WAF is propagating the create, update, or delete request to all AWS WAF servers.
+  `INSYNC`: Propagation is complete.

## Request Syntax
<a name="API_wafRegional_GetChangeTokenStatus_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetChangeTokenStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_GetChangeTokenStatus_RequestSyntax) **   <a name="WAF-wafRegional_GetChangeTokenStatus-request-ChangeToken"></a>
The change token for which you want to get the status. This change token was previously returned in the `GetChangeToken` response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetChangeTokenStatus_ResponseSyntax"></a>

```
{
   "ChangeTokenStatus": "string"
}
```

## Response Elements
<a name="API_wafRegional_GetChangeTokenStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeTokenStatus](#API_wafRegional_GetChangeTokenStatus_ResponseSyntax) **   <a name="WAF-wafRegional_GetChangeTokenStatus-response-ChangeTokenStatus"></a>
The status of the change token.  
Type: String  
Valid Values: `PROVISIONED | PENDING | INSYNC` 

## Errors
<a name="API_wafRegional_GetChangeTokenStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_GetChangeTokenStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetChangeTokenStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetChangeTokenStatus) 