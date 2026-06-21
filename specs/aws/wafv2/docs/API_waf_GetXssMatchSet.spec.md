---
id: "@specs/aws/wafv2/docs/API_waf_GetXssMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetXssMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetXssMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_GetXssMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetXssMatchSet
<a name="API_waf_GetXssMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [XssMatchSet](API_waf_XssMatchSet.md) that is specified by `XssMatchSetId`.

## Request Syntax
<a name="API_waf_GetXssMatchSet_RequestSyntax"></a>

```
{
   "XssMatchSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_GetXssMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [XssMatchSetId](#API_waf_GetXssMatchSet_RequestSyntax) **   <a name="WAF-waf_GetXssMatchSet-request-XssMatchSetId"></a>
The `XssMatchSetId` of the [XssMatchSet](API_waf_XssMatchSet.md) that you want to get. `XssMatchSetId` is returned by [CreateXssMatchSet](API_waf_CreateXssMatchSet.md) and by [ListXssMatchSets](API_waf_ListXssMatchSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_waf_GetXssMatchSet_ResponseSyntax"></a>

```
{
   "XssMatchSet": { 
      "Name": "string",
      "XssMatchSetId": "string",
      "XssMatchTuples": [ 
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
<a name="API_waf_GetXssMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [XssMatchSet](#API_waf_GetXssMatchSet_ResponseSyntax) **   <a name="WAF-waf_GetXssMatchSet-response-XssMatchSet"></a>
Information about the [XssMatchSet](API_waf_XssMatchSet.md) that you specified in the `GetXssMatchSet` request. For more information, see the following topics:  
+  [XssMatchSet](API_waf_XssMatchSet.md): Contains `Name`, `XssMatchSetId`, and an array of `XssMatchTuple` objects
+  [XssMatchTuple](API_waf_XssMatchTuple.md): Each `XssMatchTuple` object contains `FieldToMatch` and `TextTransformation` 
+  [FieldToMatch](API_waf_FieldToMatch.md): Contains `Data` and `Type` 
Type: [XssMatchSet](API_waf_XssMatchSet.md) object

## Errors
<a name="API_waf_GetXssMatchSet_Errors"></a>

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
<a name="API_waf_GetXssMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/GetXssMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GetXssMatchSet) 