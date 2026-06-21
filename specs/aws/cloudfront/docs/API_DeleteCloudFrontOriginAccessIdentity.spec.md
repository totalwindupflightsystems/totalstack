---
id: "@specs/aws/cloudfront/docs/API_DeleteCloudFrontOriginAccessIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCloudFrontOriginAccessIdentity"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteCloudFrontOriginAccessIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteCloudFrontOriginAccessIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCloudFrontOriginAccessIdentity
<a name="API_DeleteCloudFrontOriginAccessIdentity"></a>

Delete an origin access identity.

## Request Syntax
<a name="API_DeleteCloudFrontOriginAccessIdentity_RequestSyntax"></a>

```
DELETE /2020-05-31/origin-access-identity/cloudfront/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteCloudFrontOriginAccessIdentity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteCloudFrontOriginAccessIdentity_RequestSyntax) **   <a name="cloudfront-DeleteCloudFrontOriginAccessIdentity-request-uri-Id"></a>
The origin access identity's ID.  
Required: Yes

 ** [If-Match](#API_DeleteCloudFrontOriginAccessIdentity_RequestSyntax) **   <a name="cloudfront-DeleteCloudFrontOriginAccessIdentity-request-IfMatch"></a>
The value of the `ETag` header you received from a previous `GET` or `PUT` request. For example: `E2QWRUHAPOMQZL`.

## Request Body
<a name="API_DeleteCloudFrontOriginAccessIdentity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCloudFrontOriginAccessIdentity_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteCloudFrontOriginAccessIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteCloudFrontOriginAccessIdentity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CloudFrontOriginAccessIdentityInUse **   
The Origin Access Identity specified is already in use.  
HTTP Status Code: 409

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchCloudFrontOriginAccessIdentity **   
The specified origin access identity does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_DeleteCloudFrontOriginAccessIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteCloudFrontOriginAccessIdentity) 