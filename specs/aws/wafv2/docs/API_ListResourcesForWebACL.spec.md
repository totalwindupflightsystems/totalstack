---
id: "@specs/aws/wafv2/docs/API_ListResourcesForWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListResourcesForWebACL"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# ListResourcesForWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_ListResourcesForWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListResourcesForWebACL
<a name="API_ListResourcesForWebACL"></a>

Retrieves an array of the Amazon Resource Names (ARNs) for the resources that are associated with the specified web ACL. 

For Amazon CloudFront, don't use this call. Instead, use the CloudFront call `ListDistributionsByWebACLId`. For information, see [ListDistributionsByWebACLId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html) in the *Amazon CloudFront API Reference*. 

 **Required permissions for customer-managed IAM policies** 

This call requires permissions that are specific to the protected resource type. For details, see [Permissions for ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-ListResourcesForWebACL) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_ListResourcesForWebACL_RequestSyntax"></a>

```
{
   "ResourceType": "{{string}}",
   "WebACLArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcesForWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceType](#API_ListResourcesForWebACL_RequestSyntax) **   <a name="WAF-ListResourcesForWebACL-request-ResourceType"></a>
Retrieves the web ACLs that are used by the specified resource type.   
For Amazon CloudFront, don't use this call. Instead, use the CloudFront call `ListDistributionsByWebACLId`. For information, see [ListDistributionsByWebACLId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html) in the *Amazon CloudFront API Reference*.   
If you don't provide a resource type, the call uses the resource type `APPLICATION_LOAD_BALANCER`. 
Default: `APPLICATION_LOAD_BALANCER`   
Type: String  
Valid Values: `APPLICATION_LOAD_BALANCER | API_GATEWAY | APPSYNC | COGNITO_USER_POOL | APP_RUNNER_SERVICE | VERIFIED_ACCESS_INSTANCE | AMPLIFY`   
Required: No

 ** [WebACLArn](#API_ListResourcesForWebACL_RequestSyntax) **   <a name="WAF-ListResourcesForWebACL-request-WebACLArn"></a>
The Amazon Resource Name (ARN) of the web ACL.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_ListResourcesForWebACL_ResponseSyntax"></a>

```
{
   "ResourceArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListResourcesForWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceArns](#API_ListResourcesForWebACL_ResponseSyntax) **   <a name="WAF-ListResourcesForWebACL-response-ResourceArns"></a>
The array of Amazon Resource Names (ARNs) of the associated resources.  
Type: Array of strings  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*` 

## Errors
<a name="API_ListResourcesForWebACL_Errors"></a>

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
<a name="API_ListResourcesForWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/ListResourcesForWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ListResourcesForWebACL) 