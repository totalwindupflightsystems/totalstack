---
id: "@specs/aws/cloudfront/docs/API_DeleteOriginAccessControl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteOriginAccessControl"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteOriginAccessControl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteOriginAccessControl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteOriginAccessControl
<a name="API_DeleteOriginAccessControl"></a>

Deletes a CloudFront origin access control.

You cannot delete an origin access control if it's in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.

## Request Syntax
<a name="API_DeleteOriginAccessControl_RequestSyntax"></a>

```
DELETE /2020-05-31/origin-access-control/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteOriginAccessControl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteOriginAccessControl_RequestSyntax) **   <a name="cloudfront-DeleteOriginAccessControl-request-uri-Id"></a>
The unique identifier of the origin access control that you are deleting.  
Required: Yes

 ** [If-Match](#API_DeleteOriginAccessControl_RequestSyntax) **   <a name="cloudfront-DeleteOriginAccessControl-request-IfMatch"></a>
The current version (`ETag` value) of the origin access control that you are deleting.

## Request Body
<a name="API_DeleteOriginAccessControl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteOriginAccessControl_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteOriginAccessControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteOriginAccessControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchOriginAccessControl **   
The origin access control does not exist.  
HTTP Status Code: 404

 ** OriginAccessControlInUse **   
Cannot delete the origin access control because it's in use by one or more distributions.  
HTTP Status Code: 409

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_DeleteOriginAccessControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteOriginAccessControl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteOriginAccessControl) 