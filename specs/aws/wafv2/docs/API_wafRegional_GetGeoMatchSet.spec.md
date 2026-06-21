---
id: "@specs/aws/wafv2/docs/API_wafRegional_GetGeoMatchSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetGeoMatchSet"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# GetGeoMatchSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_GetGeoMatchSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetGeoMatchSet
<a name="API_wafRegional_GetGeoMatchSet"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns the [GeoMatchSet](API_wafRegional_GeoMatchSet.md) that is specified by `GeoMatchSetId`.

## Request Syntax
<a name="API_wafRegional_GetGeoMatchSet_RequestSyntax"></a>

```
{
   "GeoMatchSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_GetGeoMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GeoMatchSetId](#API_wafRegional_GetGeoMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_GetGeoMatchSet-request-GeoMatchSetId"></a>
The `GeoMatchSetId` of the [GeoMatchSet](API_wafRegional_GeoMatchSet.md) that you want to get. `GeoMatchSetId` is returned by [CreateGeoMatchSet](API_wafRegional_CreateGeoMatchSet.md) and by [ListGeoMatchSets](API_wafRegional_ListGeoMatchSets.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_GetGeoMatchSet_ResponseSyntax"></a>

```
{
   "GeoMatchSet": { 
      "GeoMatchConstraints": [ 
         { 
            "Type": "string",
            "Value": "string"
         }
      ],
      "GeoMatchSetId": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_wafRegional_GetGeoMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GeoMatchSet](#API_wafRegional_GetGeoMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_GetGeoMatchSet-response-GeoMatchSet"></a>
Information about the [GeoMatchSet](API_wafRegional_GeoMatchSet.md) that you specified in the `GetGeoMatchSet` request. This includes the `Type`, which for a `GeoMatchConstraint` is always `Country`, as well as the `Value`, which is the identifier for a specific country.  
Type: [GeoMatchSet](API_wafRegional_GeoMatchSet.md) object

## Errors
<a name="API_wafRegional_GetGeoMatchSet_Errors"></a>

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
<a name="API_wafRegional_GetGeoMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/GetGeoMatchSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GetGeoMatchSet) 