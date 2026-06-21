---
id: "@specs/aws/cloudfront/docs/API_UpdateVpcOrigin"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateVpcOrigin"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateVpcOrigin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateVpcOrigin
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateVpcOrigin
<a name="API_UpdateVpcOrigin"></a>

Update an Amazon CloudFront VPC origin in your account.

## Request Syntax
<a name="API_UpdateVpcOrigin_RequestSyntax"></a>

```
PUT /2020-05-31/vpc-origin/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<VpcOriginEndpointConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Arn>{{string}}</Arn>
   <HTTPPort>{{integer}}</HTTPPort>
   <HTTPSPort>{{integer}}</HTTPSPort>
   <Name>{{string}}</Name>
   <OriginProtocolPolicy>{{string}}</OriginProtocolPolicy>
   <OriginSslProtocols>
      <Items>
         <SslProtocol>{{string}}</SslProtocol>
      </Items>
      <Quantity>{{integer}}</Quantity>
   </OriginSslProtocols>
</VpcOriginEndpointConfig>
```

## URI Request Parameters
<a name="API_UpdateVpcOrigin_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateVpcOrigin_RequestBody"></a>

The request accepts the following data in XML format.

 ** [VpcOriginEndpointConfig](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-VpcOriginEndpointConfig"></a>
Root level tag for the VpcOriginEndpointConfig parameters.  
Required: Yes

 ** [Arn](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-Arn"></a>
The ARN of the CloudFront VPC origin endpoint configuration.  
Type: String  
Required: Yes

 ** [HTTPPort](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-HTTPPort"></a>
The HTTP port for the CloudFront VPC origin endpoint configuration. The default value is `80`.  
Type: Integer  
Required: Yes

 ** [HTTPSPort](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-HTTPSPort"></a>
The HTTPS port of the CloudFront VPC origin endpoint configuration. The default value is `443`.  
Type: Integer  
Required: Yes

 ** [Name](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-Name"></a>
The name of the CloudFront VPC origin endpoint configuration.  
Type: String  
Required: Yes

 ** [OriginProtocolPolicy](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-OriginProtocolPolicy"></a>
The origin protocol policy for the CloudFront VPC origin endpoint configuration.  
Type: String  
Valid Values: `http-only | match-viewer | https-only`   
Required: Yes

 ** [OriginSslProtocols](#API_UpdateVpcOrigin_RequestSyntax) **   <a name="cloudfront-UpdateVpcOrigin-request-OriginSslProtocols"></a>
A complex type that contains information about the SSL/TLS protocols that CloudFront can use when establishing an HTTPS connection with your origin.  
Type: [OriginSslProtocols](API_OriginSslProtocols.md) object  
Required: No

## Response Syntax
<a name="API_UpdateVpcOrigin_ResponseSyntax"></a>

```
HTTP/1.1 202
<?xml version="1.0" encoding="UTF-8"?>
<VpcOrigin>
   <Arn>string</Arn>
   <CreatedTime>timestamp</CreatedTime>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Status>string</Status>
   <VpcOriginEndpointConfig>
      <Arn>string</Arn>
      <HTTPPort>integer</HTTPPort>
      <HTTPSPort>integer</HTTPSPort>
      <Name>string</Name>
      <OriginProtocolPolicy>string</OriginProtocolPolicy>
      <OriginSslProtocols>
         <Items>
            <SslProtocol>string</SslProtocol>
         </Items>
         <Quantity>integer</Quantity>
      </OriginSslProtocols>
   </VpcOriginEndpointConfig>
</VpcOrigin>
```

## Response Elements
<a name="API_UpdateVpcOrigin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in XML format by the service.

 ** [VpcOrigin](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-VpcOrigin"></a>
Root level tag for the VpcOrigin parameters.  
Required: Yes

 ** [Arn](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-Arn"></a>
The VPC origin ARN.  
Type: String

 ** [CreatedTime](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-CreatedTime"></a>
The VPC origin created time.  
Type: Timestamp

 ** [Id](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-Id"></a>
The VPC origin ID.  
Type: String

 ** [LastModifiedTime](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-LastModifiedTime"></a>
The VPC origin last modified time.  
Type: Timestamp

 ** [Status](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-Status"></a>
The VPC origin status.  
Type: String

 ** [VpcOriginEndpointConfig](#API_UpdateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-UpdateVpcOrigin-response-VpcOriginEndpointConfig"></a>
The VPC origin endpoint configuration.  
Type: [VpcOriginEndpointConfig](API_VpcOriginEndpointConfig.md) object

## Errors
<a name="API_UpdateVpcOrigin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CannotUpdateEntityWhileInUse **   
The entity cannot be updated while it is in use.  
HTTP Status Code: 409

 ** EntityAlreadyExists **   
The entity already exists. You must provide a unique entity.  
HTTP Status Code: 409

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** IllegalUpdate **   
The update contains modifications that are not allowed.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateVpcOrigin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateVpcOrigin) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateVpcOrigin) 