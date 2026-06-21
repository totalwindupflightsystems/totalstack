---
id: "@specs/aws/cloudfront/docs/API_CreateVpcOrigin"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVpcOrigin"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateVpcOrigin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateVpcOrigin
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVpcOrigin
<a name="API_CreateVpcOrigin"></a>

Create an Amazon CloudFront VPC origin.

## Request Syntax
<a name="API_CreateVpcOrigin_RequestSyntax"></a>

```
POST /2020-05-31/vpc-origin HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateVpcOriginRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
   <VpcOriginEndpointConfig>
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
</CreateVpcOriginRequest>
```

## URI Request Parameters
<a name="API_CreateVpcOrigin_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVpcOrigin_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateVpcOriginRequest](#API_CreateVpcOrigin_RequestSyntax) **   <a name="cloudfront-CreateVpcOrigin-request-CreateVpcOriginRequest"></a>
Root level tag for the CreateVpcOriginRequest parameters.  
Required: Yes

 ** [Tags](#API_CreateVpcOrigin_RequestSyntax) **   <a name="cloudfront-CreateVpcOrigin-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: No

 ** [VpcOriginEndpointConfig](#API_CreateVpcOrigin_RequestSyntax) **   <a name="cloudfront-CreateVpcOrigin-request-VpcOriginEndpointConfig"></a>
The VPC origin endpoint configuration.  
Type: [VpcOriginEndpointConfig](API_VpcOriginEndpointConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateVpcOrigin_ResponseSyntax"></a>

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
<a name="API_CreateVpcOrigin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in XML format by the service.

 ** [VpcOrigin](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-VpcOrigin"></a>
Root level tag for the VpcOrigin parameters.  
Required: Yes

 ** [Arn](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-Arn"></a>
The VPC origin ARN.  
Type: String

 ** [CreatedTime](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-CreatedTime"></a>
The VPC origin created time.  
Type: Timestamp

 ** [Id](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-Id"></a>
The VPC origin ID.  
Type: String

 ** [LastModifiedTime](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-LastModifiedTime"></a>
The VPC origin last modified time.  
Type: Timestamp

 ** [Status](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-Status"></a>
The VPC origin status.  
Type: String

 ** [VpcOriginEndpointConfig](#API_CreateVpcOrigin_ResponseSyntax) **   <a name="cloudfront-CreateVpcOrigin-response-VpcOriginEndpointConfig"></a>
The VPC origin endpoint configuration.  
Type: [VpcOriginEndpointConfig](API_VpcOriginEndpointConfig.md) object

## Errors
<a name="API_CreateVpcOrigin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityAlreadyExists **   
The entity already exists. You must provide a unique entity.  
HTTP Status Code: 409

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidTagging **   
The tagging specified is not valid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_CreateVpcOrigin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateVpcOrigin) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateVpcOrigin) 