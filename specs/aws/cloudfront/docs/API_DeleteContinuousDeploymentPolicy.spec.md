---
id: "@specs/aws/cloudfront/docs/API_DeleteContinuousDeploymentPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteContinuousDeploymentPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteContinuousDeploymentPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteContinuousDeploymentPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteContinuousDeploymentPolicy
<a name="API_DeleteContinuousDeploymentPolicy"></a>

Deletes a continuous deployment policy.

You cannot delete a continuous deployment policy that's attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.

## Request Syntax
<a name="API_DeleteContinuousDeploymentPolicy_RequestSyntax"></a>

```
DELETE /2020-05-31/continuous-deployment-policy/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteContinuousDeploymentPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-DeleteContinuousDeploymentPolicy-request-uri-Id"></a>
The identifier of the continuous deployment policy that you are deleting.  
Required: Yes

 ** [If-Match](#API_DeleteContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-DeleteContinuousDeploymentPolicy-request-IfMatch"></a>
The current version (`ETag` value) of the continuous deployment policy that you are deleting.

## Request Body
<a name="API_DeleteContinuousDeploymentPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteContinuousDeploymentPolicy_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteContinuousDeploymentPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteContinuousDeploymentPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** ContinuousDeploymentPolicyInUse **   
You cannot delete a continuous deployment policy that is associated with a primary distribution.  
HTTP Status Code: 409

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchContinuousDeploymentPolicy **   
The continuous deployment policy doesn't exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_DeleteContinuousDeploymentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteContinuousDeploymentPolicy) 