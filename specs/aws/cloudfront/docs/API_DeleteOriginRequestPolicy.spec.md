---
id: "@specs/aws/cloudfront/docs/API_DeleteOriginRequestPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteOriginRequestPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteOriginRequestPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteOriginRequestPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteOriginRequestPolicy
<a name="API_DeleteOriginRequestPolicy"></a>

Deletes an origin request policy.

You cannot delete an origin request policy if it's attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.

To delete an origin request policy, you must provide the policy's identifier and version. To get the identifier, you can use `ListOriginRequestPolicies` or `GetOriginRequestPolicy`.

## Request Syntax
<a name="API_DeleteOriginRequestPolicy_RequestSyntax"></a>

```
DELETE /2020-05-31/origin-request-policy/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteOriginRequestPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteOriginRequestPolicy_RequestSyntax) **   <a name="cloudfront-DeleteOriginRequestPolicy-request-uri-Id"></a>
The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use `ListOriginRequestPolicies`.  
Required: Yes

 ** [If-Match](#API_DeleteOriginRequestPolicy_RequestSyntax) **   <a name="cloudfront-DeleteOriginRequestPolicy-request-IfMatch"></a>
The version of the origin request policy that you are deleting. The version is the origin request policy's `ETag` value, which you can get using `ListOriginRequestPolicies`, `GetOriginRequestPolicy`, or `GetOriginRequestPolicyConfig`.

## Request Body
<a name="API_DeleteOriginRequestPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteOriginRequestPolicy_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteOriginRequestPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteOriginRequestPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** IllegalDelete **   
Deletion is not allowed for this entity.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchOriginRequestPolicy **   
The origin request policy does not exist.  
HTTP Status Code: 404

 ** OriginRequestPolicyInUse **   
Cannot delete the origin request policy because it is attached to one or more cache behaviors.  
HTTP Status Code: 409

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_DeleteOriginRequestPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteOriginRequestPolicy) 