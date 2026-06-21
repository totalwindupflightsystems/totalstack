---
id: "@specs/aws/cloudfront/docs/API_GetOriginAccessControlConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetOriginAccessControlConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetOriginAccessControlConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetOriginAccessControlConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetOriginAccessControlConfig
<a name="API_GetOriginAccessControlConfig"></a>

Gets a CloudFront origin access control configuration.

## Request Syntax
<a name="API_GetOriginAccessControlConfig_RequestSyntax"></a>

```
GET /2020-05-31/origin-access-control/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOriginAccessControlConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetOriginAccessControlConfig_RequestSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-request-uri-Id"></a>
The unique identifier of the origin access control.  
Required: Yes

## Request Body
<a name="API_GetOriginAccessControlConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOriginAccessControlConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControlConfig>
   <Description>string</Description>
   <Name>string</Name>
   <OriginAccessControlOriginType>string</OriginAccessControlOriginType>
   <SigningBehavior>string</SigningBehavior>
   <SigningProtocol>string</SigningProtocol>
</OriginAccessControlConfig>
```

## Response Elements
<a name="API_GetOriginAccessControlConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [OriginAccessControlConfig](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-OriginAccessControlConfig"></a>
Root level tag for the OriginAccessControlConfig parameters.  
Required: Yes

 ** [Description](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-Description"></a>
A description of the origin access control.  
Type: String

 ** [Name](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-Name"></a>
A name to identify the origin access control. You can specify up to 64 characters.  
Type: String

 ** [OriginAccessControlOriginType](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-OriginAccessControlOriginType"></a>
The type of origin that this origin access control is for.  
Type: String  
Valid Values: `s3 | mediastore | mediapackagev2 | lambda` 

 ** [SigningBehavior](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-SigningBehavior"></a>
Specifies which requests CloudFront signs (adds authentication information to). Specify `always` for the most common use case. For more information, see [origin access control advanced settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#oac-advanced-settings) in the *Amazon CloudFront Developer Guide*.  
This field can have one of the following values:  
+  `always` – CloudFront signs all origin requests, overwriting the `Authorization` header from the viewer request if one exists.
+  `never` – CloudFront doesn't sign any origin requests. This value turns off origin access control for all origins in all distributions that use this origin access control.
+  `no-override` – If the viewer request doesn't contain the `Authorization` header, then CloudFront signs the origin request. If the viewer request contains the `Authorization` header, then CloudFront doesn't sign the origin request and instead passes along the `Authorization` header from the viewer request. **WARNING: To pass along the `Authorization` header from the viewer request, you *must* add the `Authorization` header to a [cache policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) for all cache behaviors that use origins associated with this origin access control.** 
Type: String  
Valid Values: `never | always | no-override` 

 ** [SigningProtocol](#API_GetOriginAccessControlConfig_ResponseSyntax) **   <a name="cloudfront-GetOriginAccessControlConfig-response-SigningProtocol"></a>
The signing protocol of the origin access control, which determines how CloudFront signs (authenticates) requests. The only valid value is `sigv4`.  
Type: String  
Valid Values: `sigv4` 

## Errors
<a name="API_GetOriginAccessControlConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchOriginAccessControl **   
The origin access control does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetOriginAccessControlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetOriginAccessControlConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetOriginAccessControlConfig) 