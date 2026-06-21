---
id: "@specs/aws/wafv2/docs/API_wafRegional_CreateWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateWebACL"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_CreateWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateWebACL
<a name="API_wafRegional_CreateWebACL"></a>

**Note**  
 AWS WAF Classic support will end on September 30, 2025.   
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.  
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use. 

Creates a `WebACL`, which contains the `Rules` that identify the Amazon CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates `Rules` in order based on the value of `Priority` for each `Rule`.

You also specify a default action, either `ALLOW` or `BLOCK`. If a web request doesn't match any of the `Rules` in a `WebACL`, AWS WAF responds to the request with the default action. 

To create and configure a `WebACL`, perform the following steps:

1. Create and update the `ByteMatchSet` objects and other predicates that you want to include in `Rules`. For more information, see [CreateByteMatchSet](API_wafRegional_CreateByteMatchSet.md), [UpdateByteMatchSet](API_wafRegional_UpdateByteMatchSet.md), [CreateIPSet](API_wafRegional_CreateIPSet.md), [UpdateIPSet](API_wafRegional_UpdateIPSet.md), [CreateSqlInjectionMatchSet](API_wafRegional_CreateSqlInjectionMatchSet.md), and [UpdateSqlInjectionMatchSet](API_wafRegional_UpdateSqlInjectionMatchSet.md).

1. Create and update the `Rules` that you want to include in the `WebACL`. For more information, see [CreateRule](API_wafRegional_CreateRule.md) and [UpdateRule](API_wafRegional_UpdateRule.md).

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of a `CreateWebACL` request.

1. Submit a `CreateWebACL` request.

1. Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an [UpdateWebACL](API_wafRegional_UpdateWebACL.md) request.

1. Submit an [UpdateWebACL](API_wafRegional_UpdateWebACL.md) request to specify the `Rules` that you want to include in the `WebACL`, to specify the default action, and to associate the `WebACL` with an Amazon CloudFront distribution.

For more information about how to use the AWS WAF API, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_wafRegional_CreateWebACL_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "DefaultAction": { 
      "Type": "{{string}}"
   },
   "MetricName": "{{string}}",
   "Name": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_wafRegional_CreateWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_CreateWebACL_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACL-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [DefaultAction](#API_wafRegional_CreateWebACL_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACL-request-DefaultAction"></a>
The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the `Rule` objects that are associated with the `WebACL`.  
Type: [WafAction](API_wafRegional_WafAction.md) object  
Required: Yes

 ** [MetricName](#API_wafRegional_CreateWebACL_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACL-request-MetricName"></a>
A friendly name or description for the metrics for this `WebACL`.The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change `MetricName` after you create the `WebACL`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Name](#API_wafRegional_CreateWebACL_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACL-request-Name"></a>
A friendly name or description of the [WebACL](API_wafRegional_WebACL.md). You can't change `Name` after you create the `WebACL`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [Tags](#API_wafRegional_CreateWebACL_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACL-request-Tags"></a>
  
Type: Array of [Tag](API_wafRegional_Tag.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## Response Syntax
<a name="API_wafRegional_CreateWebACL_ResponseSyntax"></a>

```
{
   "ChangeToken": "string",
   "WebACL": { 
      "DefaultAction": { 
         "Type": "string"
      },
      "MetricName": "string",
      "Name": "string",
      "Rules": [ 
         { 
            "Action": { 
               "Type": "string"
            },
            "ExcludedRules": [ 
               { 
                  "RuleId": "string"
               }
            ],
            "OverrideAction": { 
               "Type": "string"
            },
            "Priority": number,
            "RuleId": "string",
            "Type": "string"
         }
      ],
      "WebACLArn": "string",
      "WebACLId": "string"
   }
}
```

## Response Elements
<a name="API_wafRegional_CreateWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_wafRegional_CreateWebACL_ResponseSyntax) **   <a name="WAF-wafRegional_CreateWebACL-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `CreateWebACL` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*` 

 ** [WebACL](#API_wafRegional_CreateWebACL_ResponseSyntax) **   <a name="WAF-wafRegional_CreateWebACL-response-WebACL"></a>
The [WebACL](API_wafRegional_WebACL.md) returned in the `CreateWebACL` response.  
Type: [WebACL](API_wafRegional_WebACL.md) object

## Errors
<a name="API_wafRegional_CreateWebACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFBadRequestException **   
  
HTTP Status Code: 400

 ** WAFDisallowedNameException **   
The name specified is invalid.  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidAccountException **   
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.  
HTTP Status Code: 400

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

 ** WAFLimitsExceededException **   
The operation exceeds a resource limit, for example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html) in the * AWS WAF Developer Guide*.  
HTTP Status Code: 400

 ** WAFStaleDataException **   
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.  
HTTP Status Code: 400

 ** WAFTagOperationException **   
  
HTTP Status Code: 400

 ** WAFTagOperationInternalErrorException **   
  
HTTP Status Code: 500

## See Also
<a name="API_wafRegional_CreateWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/CreateWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/CreateWebACL) 