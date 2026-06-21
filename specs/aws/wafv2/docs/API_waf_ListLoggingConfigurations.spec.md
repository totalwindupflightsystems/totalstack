---
id: "@specs/aws/wafv2/docs/API_waf_ListLoggingConfigurations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListLoggingConfigurations"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListLoggingConfigurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_waf_ListLoggingConfigurations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListLoggingConfigurations
<a name="API_waf_ListLoggingConfigurations"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Returns an array of [LoggingConfiguration](API_waf_LoggingConfiguration.md) objects.

## Request Syntax
<a name="API_waf_ListLoggingConfigurations_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}"
}
```

## Request Parameters
<a name="API_waf_ListLoggingConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_waf_ListLoggingConfigurations_RequestSyntax) **   <a name="WAF-waf_ListLoggingConfigurations-request-Limit"></a>
Specifies the number of `LoggingConfigurations` that you want AWS WAF to return for this request. If you have more `LoggingConfigurations` than the number that you specify for `Limit`, the response includes a `NextMarker` value that you can use to get another batch of `LoggingConfigurations`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** [NextMarker](#API_waf_ListLoggingConfigurations_RequestSyntax) **   <a name="WAF-waf_ListLoggingConfigurations-request-NextMarker"></a>
If you specify a value for `Limit` and you have more `LoggingConfigurations` than the value of `Limit`, AWS WAF returns a `NextMarker` value in the response that allows you to list another group of `LoggingConfigurations`. For the second and subsequent `ListLoggingConfigurations` requests, specify the value of `NextMarker` from the previous response to get information about another batch of `ListLoggingConfigurations`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*`   
Required: No

## Response Syntax
<a name="API_waf_ListLoggingConfigurations_ResponseSyntax"></a>

```
{
   "LoggingConfigurations": [ 
      { 
         "LogDestinationConfigs": [ "string" ],
         "RedactedFields": [ 
            { 
               "Data": "string",
               "Type": "string"
            }
         ],
         "ResourceArn": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_waf_ListLoggingConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LoggingConfigurations](#API_waf_ListLoggingConfigurations_ResponseSyntax) **   <a name="WAF-waf_ListLoggingConfigurations-response-LoggingConfigurations"></a>
An array of [LoggingConfiguration](API_waf_LoggingConfiguration.md) objects.  
Type: Array of [LoggingConfiguration](API_waf_LoggingConfiguration.md) objects

 ** [NextMarker](#API_waf_ListLoggingConfigurations_ResponseSyntax) **   <a name="WAF-waf_ListLoggingConfigurations-response-NextMarker"></a>
If you have more `LoggingConfigurations` than the number that you specified for `Limit` in the request, the response includes a `NextMarker` value. To list more `LoggingConfigurations`, submit another `ListLoggingConfigurations` request, and specify the `NextMarker` value from the response in the `NextMarker` value in the next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `.*\S.*` 

## Errors
<a name="API_waf_ListLoggingConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

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

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## See Also
<a name="API_waf_ListLoggingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-2015-08-24/ListLoggingConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ListLoggingConfigurations) 