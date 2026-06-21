---
id: "@specs/aws/wafv2/docs/API_waf_GetPermissionPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPermissionPolicy"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetPermissionPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_GetPermissionPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPermissionPolicy
<a name="API_waf_GetPermissionPolicy"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the IAM policy attached to the RuleGroup.

## Request Syntax
<a name="API_waf_GetPermissionPolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_GetPermissionPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_waf_GetPermissionPolicy_RequestSyntax) **   <a name="WAF-waf_GetPermissionPolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_GetPermissionPolicy_ResponseSyntax"></a>

```
{
   "Policy": "string"
}
```

## Response Elements
<a name="API_waf_GetPermissionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_waf_GetPermissionPolicy_ResponseSyntax) **   <a name="WAF-waf_GetPermissionPolicy-response-Policy"></a>
The IAM policy attached to the specified RuleGroup.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 395000.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_GetPermissionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_waf_GetPermissionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/GetPermissionPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GetPermissionPolicy) 