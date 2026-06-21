---
id: "@specs/aws/cloudfront/docs/API_GetStreamingDistribution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetStreamingDistribution"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetStreamingDistribution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetStreamingDistribution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetStreamingDistribution
<a name="API_GetStreamingDistribution"></a>

Gets information about a specified RTMP distribution, including the distribution configuration.

## Request Syntax
<a name="API_GetStreamingDistribution_RequestSyntax"></a>

```
GET /2020-05-31/streaming-distribution/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStreamingDistribution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetStreamingDistribution_RequestSyntax) **   <a name="cloudfront-GetStreamingDistribution-request-uri-Id"></a>
The streaming distribution's ID.  
Required: Yes

## Request Body
<a name="API_GetStreamingDistribution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStreamingDistribution_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StreamingDistribution>
   <ActiveTrustedSigners>
      <Enabled>boolean</Enabled>
      <Items>
         <Signer>
            <AwsAccountNumber>string</AwsAccountNumber>
            <KeyPairIds>
               <Items>
                  <KeyPairId>string</KeyPairId>
               </Items>
               <Quantity>integer</Quantity>
            </KeyPairIds>
         </Signer>
      </Items>
      <Quantity>integer</Quantity>
   </ActiveTrustedSigners>
   <ARN>string</ARN>
   <DomainName>string</DomainName>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Status>string</Status>
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
</StreamingDistribution>
```

## Response Elements
<a name="API_GetStreamingDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [StreamingDistribution](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-StreamingDistribution"></a>
Root level tag for the StreamingDistribution parameters.  
Required: Yes

 ** [ActiveTrustedSigners](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-ActiveTrustedSigners"></a>
A complex type that lists the AWS accounts, if any, that you included in the `TrustedSigners` complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.  
The `Signer` complex type lists the AWS account number of the trusted signer or `self` if the signer is the AWS account that created the distribution. The `Signer` element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer's AWS account. If no `KeyPairId` element appears for a `Signer`, that signer can't create signed URLs.  
For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.  
Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md) object

 ** [ARN](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-ARN"></a>
The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.  
Type: String

 ** [DomainName](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-DomainName"></a>
The domain name that corresponds to the streaming distribution, for example, `s5c39gqb8ow64r.cloudfront.net`.  
Type: String

 ** [Id](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-Id"></a>
The identifier for the RTMP distribution. For example: `EGTXBD79EXAMPLE`.  
Type: String

 ** [LastModifiedTime](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-LastModifiedTime"></a>
The date and time that the distribution was last modified.  
Type: Timestamp

 ** [Status](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-Status"></a>
The current status of the RTMP distribution. When the status is `Deployed`, the distribution's information is propagated to all CloudFront edge locations.  
Type: String

 ** [StreamingDistributionConfig](#API_GetStreamingDistribution_ResponseSyntax) **   <a name="cloudfront-GetStreamingDistribution-response-StreamingDistributionConfig"></a>
The current configuration information for the RTMP distribution.  
Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md) object

## Errors
<a name="API_GetStreamingDistribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchStreamingDistribution **   
The specified streaming distribution does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetStreamingDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetStreamingDistribution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetStreamingDistribution) 