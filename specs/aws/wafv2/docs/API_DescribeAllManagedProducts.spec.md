---
id: "@specs/aws/wafv2/docs/API_DescribeAllManagedProducts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAllManagedProducts"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DescribeAllManagedProducts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_DescribeAllManagedProducts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAllManagedProducts
<a name="API_DescribeAllManagedProducts"></a>

Provides high-level information for the AWS Managed Rules rule groups and AWS Marketplace managed rule groups. 

## Request Syntax
<a name="API_DescribeAllManagedProducts_RequestSyntax"></a>

```
{
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAllManagedProducts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Scope](#API_DescribeAllManagedProducts_RequestSyntax) **   <a name="WAF-DescribeAllManagedProducts-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

## Response Syntax
<a name="API_DescribeAllManagedProducts_ResponseSyntax"></a>

```
{
   "ManagedProducts": [ 
      { 
         "IsAdvancedManagedRuleSet": boolean,
         "IsVersioningSupported": boolean,
         "ManagedRuleSetName": "string",
         "ProductDescription": "string",
         "ProductId": "string",
         "ProductLink": "string",
         "ProductTitle": "string",
         "SnsTopicArn": "string",
         "VendorName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAllManagedProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedProducts](#API_DescribeAllManagedProducts_ResponseSyntax) **   <a name="WAF-DescribeAllManagedProducts-response-ManagedProducts"></a>
High-level information for the AWS Managed Rules rule groups and AWS Marketplace managed rule groups.   
Type: Array of [ManagedProductDescriptor](API_ManagedProductDescriptor.md) objects

## Errors
<a name="API_DescribeAllManagedProducts_Errors"></a>

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

## See Also
<a name="API_DescribeAllManagedProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/DescribeAllManagedProducts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DescribeAllManagedProducts) 