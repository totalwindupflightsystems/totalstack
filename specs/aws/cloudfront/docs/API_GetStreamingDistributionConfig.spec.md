---
id: "@specs/aws/cloudfront/docs/API_GetStreamingDistributionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetStreamingDistributionConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetStreamingDistributionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetStreamingDistributionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetStreamingDistributionConfig
<a name="API_GetStreamingDistributionConfig"></a>

Get the configuration information about a streaming distribution.

## Request Syntax
<a name="API_GetStreamingDistributionConfig_RequestSyntax"></a>

```
GET /2020-05-31/streaming-distribution/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStreamingDistributionConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetStreamingDistributionConfig_RequestSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-request-uri-Id"></a>
The streaming distribution's ID.  
Required: Yes

## Request Body
<a name="API_GetStreamingDistributionConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStreamingDistributionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StreamingDistributionConfig>
   <Aliases>
      <Items>
         <CNAME>string</CNAME>
      </Items>
      <Quantity>integer</Quantity>
   </Aliases>
   <CallerReference>string</CallerReference>
   <Comment>string</Comment>
   <Enabled>boolean</Enabled>
   <Logging>
      <Bucket>string</Bucket>
      <Enabled>boolean</Enabled>
      <Prefix>string</Prefix>
   </Logging>
   <PriceClass>string</PriceClass>
   <S3Origin>
      <DomainName>string</DomainName>
      <OriginAccessIdentity>string</OriginAccessIdentity>
   </S3Origin>
   <TrustedSigners>
      <Enabled>boolean</Enabled>
      <Items>
         <AwsAccountNumber>string</AwsAccountNumber>
      </Items>
      <Quantity>integer</Quantity>
   </TrustedSigners>
</StreamingDistributionConfig>
```

## Response Elements
<a name="API_GetStreamingDistributionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [StreamingDistributionConfig](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-StreamingDistributionConfig"></a>
Root level tag for the StreamingDistributionConfig parameters.  
Required: Yes

 ** [Aliases](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-Aliases"></a>
A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.  
Type: [Aliases](API_Aliases.md) object

 ** [CallerReference](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-CallerReference"></a>
A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.  
If the value of `CallerReference` is new (regardless of the content of the `StreamingDistributionConfig` object), CloudFront creates a new distribution.  
If `CallerReference` is a value that you already sent in a previous request to create a distribution, CloudFront returns a `DistributionAlreadyExists` error.  
Type: String

 ** [Comment](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-Comment"></a>
Any comments you want to include about the streaming distribution.  
Type: String

 ** [Enabled](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-Enabled"></a>
Whether the streaming distribution is enabled to accept user requests for content.  
Type: Boolean

 ** [Logging](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-Logging"></a>
A complex type that controls whether access logs are written for the streaming distribution.  
Type: [StreamingLoggingConfig](API_StreamingLoggingConfig.md) object

 ** [PriceClass](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-PriceClass"></a>
A complex type that contains information about price class for this streaming distribution.  
Type: String  
Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None` 

 ** [S3Origin](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-S3Origin"></a>
A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.  
Type: [S3Origin](API_S3Origin.md) object

 ** [TrustedSigners](#API_GetStreamingDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistributionConfig-response-TrustedSigners"></a>
A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.  
Type: [TrustedSigners](API_TrustedSigners.md) object

## Errors
<a name="API_GetStreamingDistributionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchStreamingDistribution **   
The specified streaming distribution does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetStreamingDistributionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetStreamingDistributionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetStreamingDistributionConfig) 