---
id: "@specs/aws/cloudfront/docs/API_DeleteResponseHeadersPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteResponseHeadersPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteResponseHeadersPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteResponseHeadersPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteResponseHeadersPolicy
<a name="API_DeleteResponseHeadersPolicy"></a>

Deletes a response headers policy.

You cannot delete a response headers policy if it's attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.

To delete a response headers policy, you must provide the policy's identifier and version. To get these values, you can use `ListResponseHeadersPolicies` or `GetResponseHeadersPolicy`.

## Request Syntax
<a name="API_DeleteResponseHeadersPolicy_RequestSyntax"></a>

```
DELETE /2020-05-31/response-headers-policy/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteResponseHeadersPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-DeleteResponseHeadersPolicy-request-uri-Id"></a>
The identifier for the response headers policy that you are deleting.  
To get the identifier, you can use `ListResponseHeadersPolicies`.  
Required: Yes

 ** [If-Match](#API_DeleteResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-DeleteResponseHeadersPolicy-request-IfMatch"></a>
The version of the response headers policy that you are deleting.  
The version is the response headers policy's `ETag` value, which you can get using `ListResponseHeadersPolicies`, `GetResponseHeadersPolicy`, or `GetResponseHeadersPolicyConfig`.

## Request Body
<a name="API_DeleteResponseHeadersPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteResponseHeadersPolicy_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteResponseHeadersPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteResponseHeadersPolicy_Errors"></a>

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

 ** NoSuchResponseHeadersPolicy **   
The response headers policy does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** ResponseHeadersPolicyInUse **   
Cannot delete the response headers policy because it is attached to one or more cache behaviors in a CloudFront distribution.  
HTTP Status Code: 409

## See Also
<a name="API_DeleteResponseHeadersPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteResponseHeadersPolicy) 