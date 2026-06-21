---
id: "@specs/aws/wafv2/docs/API_GetMobileSdkRelease"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMobileSdkRelease"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetMobileSdkRelease

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_GetMobileSdkRelease
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMobileSdkRelease
<a name="API_GetMobileSdkRelease"></a>

Retrieves information for the specified mobile SDK release, including release notes and tags.

The mobile SDK is not generally available. Customers who have access to the mobile SDK can use it to establish and manage AWS WAF tokens for use in HTTP(S) requests from a mobile device to AWS WAF. For more information, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_GetMobileSdkRelease_RequestSyntax"></a>

```
{
   "Platform": "{{string}}",
   "ReleaseVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMobileSdkRelease_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Platform](#API_GetMobileSdkRelease_RequestSyntax) **   <a name="WAF-GetMobileSdkRelease-request-Platform"></a>
The device platform.  
Type: String  
Valid Values: `IOS | ANDROID`   
Required: Yes

 ** [ReleaseVersion](#API_GetMobileSdkRelease_RequestSyntax) **   <a name="WAF-GetMobileSdkRelease-request-ReleaseVersion"></a>
The release version. For the latest available version, specify `LATEST`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w#:\.\-/]+$`   
Required: Yes

## Response Syntax
<a name="API_GetMobileSdkRelease_ResponseSyntax"></a>

```
{
   "MobileSdkRelease": { 
      "ReleaseNotes": "string",
      "ReleaseVersion": "string",
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Timestamp": number
   }
}
```

## Response Elements
<a name="API_GetMobileSdkRelease_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MobileSdkRelease](#API_GetMobileSdkRelease_ResponseSyntax) **   <a name="WAF-GetMobileSdkRelease-response-MobileSdkRelease"></a>
Information for a specified SDK release, including release notes and tags.  
Type: [MobileSdkRelease](API_MobileSdkRelease.md) object

## Errors
<a name="API_GetMobileSdkRelease_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

## See Also
<a name="API_GetMobileSdkRelease_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetMobileSdkRelease) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetMobileSdkRelease) 