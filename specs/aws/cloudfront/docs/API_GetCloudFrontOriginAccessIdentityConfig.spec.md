---
id: "@specs/aws/cloudfront/docs/API_GetCloudFrontOriginAccessIdentityConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCloudFrontOriginAccessIdentityConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetCloudFrontOriginAccessIdentityConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetCloudFrontOriginAccessIdentityConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCloudFrontOriginAccessIdentityConfig
<a name="API_GetCloudFrontOriginAccessIdentityConfig"></a>

Get the configuration information about an origin access identity.

## Request Syntax
<a name="API_GetCloudFrontOriginAccessIdentityConfig_RequestSyntax"></a>

```
GET /2020-05-31/origin-access-identity/cloudfront/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCloudFrontOriginAccessIdentityConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetCloudFrontOriginAccessIdentityConfig_RequestSyntax) **   <a name="cloudfront-GetCloudFrontOriginAccessIdentityConfig-request-uri-Id"></a>
The identity's ID.  
Required: Yes

## Request Body
<a name="API_GetCloudFrontOriginAccessIdentityConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCloudFrontOriginAccessIdentityConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CloudFrontOriginAccessIdentityConfig>
   <CallerReference>string</CallerReference>
   <Comment>string</Comment>
</CloudFrontOriginAccessIdentityConfig>
```

## Response Elements
<a name="API_GetCloudFrontOriginAccessIdentityConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CloudFrontOriginAccessIdentityConfig](#API_GetCloudFrontOriginAccessIdentityConfig_ResponseSyntax) **   <a name="cloudfront-GetCloudFrontOriginAccessIdentityConfig-response-CloudFrontOriginAccessIdentityConfig"></a>
Root level tag for the CloudFrontOriginAccessIdentityConfig parameters.  
Required: Yes

 ** [CallerReference](#API_GetCloudFrontOriginAccessIdentityConfig_ResponseSyntax) **   <a name="cloudfront-GetCloudFrontOriginAccessIdentityConfig-response-CallerReference"></a>
A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.  
If the value of `CallerReference` is new (regardless of the content of the `CloudFrontOriginAccessIdentityConfig` object), a new origin access identity is created.  
If the `CallerReference` is a value already sent in a previous identity request, and the content of the `CloudFrontOriginAccessIdentityConfig` is identical to the original request (ignoring white space), the response includes the same information returned to the original request.  
If the `CallerReference` is a value you already sent in a previous request to create an identity, but the content of the `CloudFrontOriginAccessIdentityConfig` is different from the original request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.   
Type: String

 ** [Comment](#API_GetCloudFrontOriginAccessIdentityConfig_ResponseSyntax) **   <a name="cloudfront-GetCloudFrontOriginAccessIdentityConfig-response-Comment"></a>
A comment to describe the origin access identity. The comment cannot be longer than 128 characters.  
Type: String

## Errors
<a name="API_GetCloudFrontOriginAccessIdentityConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchCloudFrontOriginAccessIdentity **   
The specified origin access identity does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetCloudFrontOriginAccessIdentityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetCloudFrontOriginAccessIdentityConfig) 