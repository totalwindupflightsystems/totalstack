---
id: "@specs/aws/wafv2/docs/API_DisassociateWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateWebACL"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DisassociateWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_DisassociateWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateWebACL
<a name="API_DisassociateWebACL"></a>

Disassociates the specified resource from its web ACL association, if it has one. 

Use this for all resource types except for Amazon CloudFront distributions. For Amazon CloudFront, call `UpdateDistribution` for the distribution and provide an empty web ACL ID. For information, see [UpdateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html) in the *Amazon CloudFront API Reference*. 

 **Required permissions for customer-managed IAM policies** 

This call requires permissions that are specific to the protected resource type. For details, see [Permissions for DisassociateWebACL](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-DisassociateWebACL) in the * AWS WAF Developer Guide*.

## Request Syntax
<a name="API_DisassociateWebACL_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DisassociateWebACL_RequestSyntax) **   <a name="WAF-DisassociateWebACL-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to disassociate from the web ACL.   
The ARN must be in one of the following formats:  
+ For an Application Load Balancer: `arn:partition:elasticloadbalancing:region:account-id:loadbalancer/app/load-balancer-name/load-balancer-id ` 
+ For an Amazon API Gateway REST API: `arn:partition:apigateway:region::/restapis/api-id/stages/stage-name ` 
+ For an AWS AppSync GraphQL API: `arn:partition:appsync:region:account-id:apis/GraphQLApiId ` 
+ For an Amazon Cognito user pool: `arn:partition:cognito-idp:region:account-id:userpool/user-pool-id ` 
+ For an AWS App Runner service: `arn:partition:apprunner:region:account-id:service/apprunner-service-name/apprunner-service-id ` 
+ For an AWS Verified Access instance: `arn:partition:ec2:region:account-id:verified-access-instance/instance-id ` 
+ For an AWS Amplify application: `arn:partition:amplify:region:account-id:apps/app-id ` 
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*`   
Required: Yes

## Response Elements
<a name="API_DisassociateWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateWebACL_Errors"></a>

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
<a name="API_DisassociateWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/DisassociateWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DisassociateWebACL) 