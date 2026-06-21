---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetIPSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetIPSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetIPSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetIPSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetIPSet
<a name="API_wafRegional_GetIPSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [IPSet](API_wafRegional_IPSet.md) that is specified by `IPSetId`.

## Request Syntax
<a name="API_wafRegional_GetIPSet_RequestSyntax"></a>

```
{
   "IPSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetIPSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IPSetId](#API_wafRegional_GetIPSet_RequestSyntax) **   <a name="WAF-wafRegional_GetIPSet-request-IPSetId"></a>
The `IPSetId` of the [IPSet](API_wafRegional_IPSet.md) that you want to get. `IPSetId` is returned by [CreateIPSet](API_wafRegional_CreateIPSet.md) and by [ListIPSets](API_wafRegional_ListIPSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetIPSet_ResponseSyntax"></a>

```
{
   "IPSet": { 
      "IPSetDescriptors": [ 
         { 
            "Type": "string",
            "Value": "string"
         }
      ],
      "IPSetId": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_wafRegional_GetIPSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IPSet](#API_wafRegional_GetIPSet_ResponseSyntax) **   <a name="WAF-wafRegional_GetIPSet-response-IPSet"></a>
Information about the [IPSet](API_wafRegional_IPSet.md) that you specified in the `GetIPSet` request. For more information, see the following topics:  
+  [IPSet](API_wafRegional_IPSet.md): Contains `IPSetDescriptors`, `IPSetId`, and `Name` 
+  `IPSetDescriptors`: Contains an array of [IPSetDescriptor](API_wafRegional_IPSetDescriptor.md) objects. Each `IPSetDescriptor` object contains `Type` and `Value` 
Type: [IPSet](API_wafRegional_IPSet.md) object

## Errors
<a name="API_wafRegional_GetIPSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_GetIPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetIPSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetIPSet) 