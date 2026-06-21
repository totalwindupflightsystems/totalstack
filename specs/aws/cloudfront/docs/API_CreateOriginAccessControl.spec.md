---
id: "@specs/aws/cloudfront/docs/API_CreateOriginAccessControl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOriginAccessControl"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateOriginAccessControl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateOriginAccessControl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOriginAccessControl
<a name="API_CreateOriginAccessControl"></a>

Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.

This makes it possible to block public access to the origin, allowing viewers (users) to access the origin's content only through CloudFront.

For more information about using a CloudFront origin access control, see [Restricting access to an AWS origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_CreateOriginAccessControl_RequestSyntax"></a>

```
POST /2020-05-31/origin-access-control HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControlConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Description>{{string}}</Description>
   <Name>{{string}}</Name>
   <OriginAccessControlOriginType>{{string}}</OriginAccessControlOriginType>
   <SigningBehavior>{{string}}</SigningBehavior>
   <SigningProtocol>{{string}}</SigningProtocol>
</OriginAccessControlConfig>
```

## URI Request Parameters
<a name="API_CreateOriginAccessControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOriginAccessControl_RequestBody"></a>

The request accepts the following data in XML format.

 ** [OriginAccessControlConfig](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-OriginAccessControlConfig"></a>
Root level tag for the OriginAccessControlConfig parameters.  
Required: Yes

 ** [Description](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-Description"></a>
A description of the origin access control.  
Type: String  
Required: No

 ** [Name](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-Name"></a>
A name to identify the origin access control. You can specify up to 64 characters.  
Type: String  
Required: Yes

 ** [OriginAccessControlOriginType](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-OriginAccessControlOriginType"></a>
The type of origin that this origin access control is for.  
Type: String  
Valid Values: `s3 | mediastore | mediapackagev2 | lambda`   
Required: Yes

 ** [SigningBehavior](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-SigningBehavior"></a>
Specifies which requests CloudFront signs (adds authentication information to). Specify `always` for the most common use case. For more information, see [origin access control advanced settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#oac-advanced-settings) in the *Amazon CloudFront Developer Guide*.  
This field can have one of the following values:  
+  `always` – CloudFront signs all origin requests, overwriting the `Authorization` header from the viewer request if one exists.
+  `never` – CloudFront doesn't sign any origin requests. This value turns off origin access control for all origins in all distributions that use this origin access control.
+  `no-override` – If the viewer request doesn't contain the `Authorization` header, then CloudFront signs the origin request. If the viewer request contains the `Authorization` header, then CloudFront doesn't sign the origin request and instead passes along the `Authorization` header from the viewer request. **WARNING: To pass along the `Authorization` header from the viewer request, you *must* add the `Authorization` header to a [cache policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) for all cache behaviors that use origins associated with this origin access control.** 
Type: String  
Valid Values: `never | always | no-override`   
Required: Yes

 ** [SigningProtocol](#API_CreateOriginAccessControl_RequestSyntax) **   <a name="cloudfront-CreateOriginAccessControl-request-SigningProtocol"></a>
The signing protocol of the origin access control, which determines how CloudFront signs (authenticates) requests. The only valid value is `sigv4`.  
Type: String  
Valid Values: `sigv4`   
Required: Yes

## Response Syntax
<a name="API_CreateOriginAccessControl_ResponseSyntax"></a>

```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<OriginAccessControl>
   <Id>string</Id>
   <OriginAccessControlConfig>
      <Description>string</Description>
      <Name>string</Name>
      <OriginAccessControlOriginType>string</OriginAccessControlOriginType>
      <SigningBehavior>string</SigningBehavior>
      <SigningProtocol>string</SigningProtocol>
   </OriginAccessControlConfig>
</OriginAccessControl>
```

## Response Elements
<a name="API_CreateOriginAccessControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [OriginAccessControl](#API_CreateOriginAccessControl_ResponseSyntax) **   <a name="cloudfront-CreateOriginAccessControl-response-OriginAccessControl"></a>
Root level tag for the OriginAccessControl parameters.  
Required: Yes

 ** [Id](#API_CreateOriginAccessControl_ResponseSyntax) **   <a name="cloudfront-CreateOriginAccessControl-response-Id"></a>
The unique identifier of the origin access control.  
Type: String

 ** [OriginAccessControlConfig](#API_CreateOriginAccessControl_ResponseSyntax) **   <a name="cloudfront-CreateOriginAccessControl-response-OriginAccessControlConfig"></a>
The origin access control.  
Type: [OriginAccessControlConfig](API_OriginAccessControlConfig.md) object

## Errors
<a name="API_CreateOriginAccessControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** OriginAccessControlAlreadyExists **   
An origin access control with the specified parameters already exists.  
HTTP Status Code: 409

 ** TooManyOriginAccessControls **   
The number of origin access controls in your AWS account exceeds the maximum allowed.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

## See Also
<a name="API_CreateOriginAccessControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateOriginAccessControl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateOriginAccessControl) 