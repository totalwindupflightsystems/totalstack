---
id: "@specs/aws/cloudfront/docs/API_GetDistributionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDistributionConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetDistributionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetDistributionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDistributionConfig
<a name="API_GetDistributionConfig"></a>

Get the configuration information about a distribution.

## Request Syntax
<a name="API_GetDistributionConfig_RequestSyntax"></a>

```
GET /2020-05-31/distribution/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDistributionConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetDistributionConfig_RequestSyntax) **   <a name="cloudfront-GetDistributionConfig-request-uri-Id"></a>
The distribution's ID. If the ID is empty, an empty distribution configuration is returned.  
Required: Yes

## Request Body
<a name="API_GetDistributionConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDistributionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionConfig>
   <Aliases>
      <Items>
         <CNAME>string</CNAME>
      </Items>
      <Quantity>integer</Quantity>
   </Aliases>
   <AnycastIpListId>string</AnycastIpListId>
   <CacheBehaviors>
      <Items>
         <CacheBehavior>
            <AllowedMethods>
               <CachedMethods>
                  <Items>
                     <Method>string</Method>
                  </Items>
                  <Quantity>integer</Quantity>
               </CachedMethods>
               <Items>
                  <Method>string</Method>
               </Items>
               <Quantity>integer</Quantity>
            </AllowedMethods>
            <CachePolicyId>string</CachePolicyId>
            <Compress>boolean</Compress>
            <DefaultTTL>long</DefaultTTL>
            <FieldLevelEncryptionId>string</FieldLevelEncryptionId>
            <ForwardedValues>
               <Cookies>
                  <Forward>string</Forward>
                  <WhitelistedNames>
                     <Items>
                        <Name>string</Name>
                     </Items>
                     <Quantity>integer</Quantity>
                  </WhitelistedNames>
               </Cookies>
               <Headers>
                  <Items>
                     <Name>string</Name>
                  </Items>
                  <Quantity>integer</Quantity>
               </Headers>
               <QueryString>boolean</QueryString>
               <QueryStringCacheKeys>
                  <Items>
                     <Name>string</Name>
                  </Items>
                  <Quantity>integer</Quantity>
               </QueryStringCacheKeys>
            </ForwardedValues>
            <FunctionAssociations>
               <Items>
                  <FunctionAssociation>
                     <EventType>string</EventType>
                     <FunctionARN>string</FunctionARN>
                  </FunctionAssociation>
               </Items>
               <Quantity>integer</Quantity>
            </FunctionAssociations>
            <GrpcConfig>
               <Enabled>boolean</Enabled>
            </GrpcConfig>
            <LambdaFunctionAssociations>
               <Items>
                  <LambdaFunctionAssociation>
                     <EventType>string</EventType>
                     <IncludeBody>boolean</IncludeBody>
                     <LambdaFunctionARN>string</LambdaFunctionARN>
                  </LambdaFunctionAssociation>
               </Items>
               <Quantity>integer</Quantity>
            </LambdaFunctionAssociations>
            <MaxTTL>long</MaxTTL>
            <MinTTL>long</MinTTL>
            <OriginRequestPolicyId>string</OriginRequestPolicyId>
            <PathPattern>string</PathPattern>
            <RealtimeLogConfigArn>string</RealtimeLogConfigArn>
            <ResponseHeadersPolicyId>string</ResponseHeadersPolicyId>
            <SmoothStreaming>boolean</SmoothStreaming>
            <TargetOriginId>string</TargetOriginId>
            <TrustedKeyGroups>
               <Enabled>boolean</Enabled>
               <Items>
                  <KeyGroup>string</KeyGroup>
               </Items>
               <Quantity>integer</Quantity>
            </TrustedKeyGroups>
            <TrustedSigners>
               <Enabled>boolean</Enabled>
               <Items>
                  <AwsAccountNumber>string</AwsAccountNumber>
               </Items>
               <Quantity>integer</Quantity>
            </TrustedSigners>
            <ViewerProtocolPolicy>string</ViewerProtocolPolicy>
         </CacheBehavior>
      </Items>
      <Quantity>integer</Quantity>
   </CacheBehaviors>
   <CacheTagConfig>
      <HeaderName>string</HeaderName>
   </CacheTagConfig>
   <CallerReference>string</CallerReference>
   <Comment>string</Comment>
   <ConnectionFunctionAssociation>
      <Id>string</Id>
   </ConnectionFunctionAssociation>
   <ConnectionMode>string</ConnectionMode>
   <ContinuousDeploymentPolicyId>string</ContinuousDeploymentPolicyId>
   <CustomErrorResponses>
      <Items>
         <CustomErrorResponse>
            <ErrorCachingMinTTL>long</ErrorCachingMinTTL>
            <ErrorCode>integer</ErrorCode>
            <ResponseCode>string</ResponseCode>
            <ResponsePagePath>string</ResponsePagePath>
         </CustomErrorResponse>
      </Items>
      <Quantity>integer</Quantity>
   </CustomErrorResponses>
   <DefaultCacheBehavior>
      <AllowedMethods>
         <CachedMethods>
            <Items>
               <Method>string</Method>
            </Items>
            <Quantity>integer</Quantity>
         </CachedMethods>
         <Items>
            <Method>string</Method>
         </Items>
         <Quantity>integer</Quantity>
      </AllowedMethods>
      <CachePolicyId>string</CachePolicyId>
      <Compress>boolean</Compress>
      <DefaultTTL>long</DefaultTTL>
      <FieldLevelEncryptionId>string</FieldLevelEncryptionId>
      <ForwardedValues>
         <Cookies>
            <Forward>string</Forward>
            <WhitelistedNames>
               <Items>
                  <Name>string</Name>
               </Items>
               <Quantity>integer</Quantity>
            </WhitelistedNames>
         </Cookies>
         <Headers>
            <Items>
               <Name>string</Name>
            </Items>
            <Quantity>integer</Quantity>
         </Headers>
         <QueryString>boolean</QueryString>
         <QueryStringCacheKeys>
            <Items>
               <Name>string</Name>
            </Items>
            <Quantity>integer</Quantity>
         </QueryStringCacheKeys>
      </ForwardedValues>
      <FunctionAssociations>
         <Items>
            <FunctionAssociation>
               <EventType>string</EventType>
               <FunctionARN>string</FunctionARN>
            </FunctionAssociation>
         </Items>
         <Quantity>integer</Quantity>
      </FunctionAssociations>
      <GrpcConfig>
         <Enabled>boolean</Enabled>
      </GrpcConfig>
      <LambdaFunctionAssociations>
         <Items>
            <LambdaFunctionAssociation>
               <EventType>string</EventType>
               <IncludeBody>boolean</IncludeBody>
               <LambdaFunctionARN>string</LambdaFunctionARN>
            </LambdaFunctionAssociation>
         </Items>
         <Quantity>integer</Quantity>
      </LambdaFunctionAssociations>
      <MaxTTL>long</MaxTTL>
      <MinTTL>long</MinTTL>
      <OriginRequestPolicyId>string</OriginRequestPolicyId>
      <RealtimeLogConfigArn>string</RealtimeLogConfigArn>
      <ResponseHeadersPolicyId>string</ResponseHeadersPolicyId>
      <SmoothStreaming>boolean</SmoothStreaming>
      <TargetOriginId>string</TargetOriginId>
      <TrustedKeyGroups>
         <Enabled>boolean</Enabled>
         <Items>
            <KeyGroup>string</KeyGroup>
         </Items>
         <Quantity>integer</Quantity>
      </TrustedKeyGroups>
      <TrustedSigners>
         <Enabled>boolean</Enabled>
         <Items>
            <AwsAccountNumber>string</AwsAccountNumber>
         </Items>
         <Quantity>integer</Quantity>
      </TrustedSigners>
      <ViewerProtocolPolicy>string</ViewerProtocolPolicy>
   </DefaultCacheBehavior>
   <DefaultRootObject>string</DefaultRootObject>
   <Enabled>boolean</Enabled>
   <HttpVersion>string</HttpVersion>
   <IsIPV6Enabled>boolean</IsIPV6Enabled>
   <Logging>
      <Bucket>string</Bucket>
      <Enabled>boolean</Enabled>
      <IncludeCookies>boolean</IncludeCookies>
      <Prefix>string</Prefix>
   </Logging>
   <OriginGroups>
      <Items>
         <OriginGroup>
            <FailoverCriteria>
               <StatusCodes>
                  <Items>
                     <StatusCode>integer</StatusCode>
                  </Items>
                  <Quantity>integer</Quantity>
               </StatusCodes>
            </FailoverCriteria>
            <Id>string</Id>
            <Members>
               <Items>
                  <OriginGroupMember>
                     <OriginId>string</OriginId>
                  </OriginGroupMember>
               </Items>
               <Quantity>integer</Quantity>
            </Members>
            <SelectionCriteria>string</SelectionCriteria>
         </OriginGroup>
      </Items>
      <Quantity>integer</Quantity>
   </OriginGroups>
   <Origins>
      <Items>
         <Origin>
            <ConnectionAttempts>integer</ConnectionAttempts>
            <ConnectionTimeout>integer</ConnectionTimeout>
            <CustomHeaders>
               <Items>
                  <OriginCustomHeader>
                     <HeaderName>string</HeaderName>
                     <HeaderValue>string</HeaderValue>
                  </OriginCustomHeader>
               </Items>
               <Quantity>integer</Quantity>
            </CustomHeaders>
            <CustomOriginConfig>
               <HTTPPort>integer</HTTPPort>
               <HTTPSPort>integer</HTTPSPort>
               <IpAddressType>string</IpAddressType>
               <OriginKeepaliveTimeout>integer</OriginKeepaliveTimeout>
               <OriginMtlsConfig>
                  <ClientCertificateArn>string</ClientCertificateArn>
               </OriginMtlsConfig>
               <OriginProtocolPolicy>string</OriginProtocolPolicy>
               <OriginReadTimeout>integer</OriginReadTimeout>
               <OriginSslProtocols>
                  <Items>
                     <SslProtocol>string</SslProtocol>
                  </Items>
                  <Quantity>integer</Quantity>
               </OriginSslProtocols>
            </CustomOriginConfig>
            <DomainName>string</DomainName>
            <Id>string</Id>
            <OriginAccessControlId>string</OriginAccessControlId>
            <OriginPath>string</OriginPath>
            <OriginShield>
               <Enabled>boolean</Enabled>
               <OriginShieldRegion>string</OriginShieldRegion>
            </OriginShield>
            <ResponseCompletionTimeout>integer</ResponseCompletionTimeout>
            <S3OriginConfig>
               <OriginAccessIdentity>string</OriginAccessIdentity>
               <OriginReadTimeout>integer</OriginReadTimeout>
            </S3OriginConfig>
            <VpcOriginConfig>
               <OriginKeepaliveTimeout>integer</OriginKeepaliveTimeout>
               <OriginReadTimeout>integer</OriginReadTimeout>
               <VpcOriginId>string</VpcOriginId>
            </VpcOriginConfig>
         </Origin>
      </Items>
      <Quantity>integer</Quantity>
   </Origins>
   <PriceClass>string</PriceClass>
   <Restrictions>
      <GeoRestriction>
         <Items>
            <Location>string</Location>
         </Items>
         <Quantity>integer</Quantity>
         <RestrictionType>string</RestrictionType>
      </GeoRestriction>
   </Restrictions>
   <Staging>boolean</Staging>
   <TenantConfig>
      <ParameterDefinitions>
         <ParameterDefinition>
            <Definition>
               <StringSchema>
                  <Comment>string</Comment>
                  <DefaultValue>string</DefaultValue>
                  <Required>boolean</Required>
               </StringSchema>
            </Definition>
            <Name>string</Name>
         </ParameterDefinition>
      </ParameterDefinitions>
   </TenantConfig>
   <ViewerCertificate>
      <ACMCertificateArn>string</ACMCertificateArn>
      <Certificate>string</Certificate>
      <CertificateSource>string</CertificateSource>
      <CloudFrontDefaultCertificate>boolean</CloudFrontDefaultCertificate>
      <IAMCertificateId>string</IAMCertificateId>
      <MinimumProtocolVersion>string</MinimumProtocolVersion>
      <SSLSupportMethod>string</SSLSupportMethod>
   </ViewerCertificate>
   <ViewerMtlsConfig>
      <Mode>string</Mode>
      <TrustStoreConfig>
         <AdvertiseTrustStoreCaNames>boolean</AdvertiseTrustStoreCaNames>
         <IgnoreCertificateExpiry>boolean</IgnoreCertificateExpiry>
         <TrustStoreId>string</TrustStoreId>
      </TrustStoreConfig>
   </ViewerMtlsConfig>
   <WebACLId>string</WebACLId>
</DistributionConfig>
```

## Response Elements
<a name="API_GetDistributionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DistributionConfig](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-DistributionConfig"></a>
Root level tag for the DistributionConfig parameters.  
Required: Yes

 ** [Aliases](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Aliases"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.  
Type: [Aliases](API_Aliases.md) object

 ** [AnycastIpListId](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-AnycastIpListId"></a>
To use this field for a multi-tenant distribution, use a connection group instead. For more information, see [ConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html).
ID of the Anycast static IP list that is associated with the distribution.  
Type: String

 ** [CacheBehaviors](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-CacheBehaviors"></a>
A complex type that contains zero or more `CacheBehavior` elements.  
Type: [CacheBehaviors](API_CacheBehaviors.md) object

 ** [CacheTagConfig](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-CacheTagConfig"></a>
Configuration for cache tag extraction from origin responses. When specified, CloudFront reads the header named in `HeaderName` from origin responses and stores the comma-separated values as cache tags on the object.  
Distributions without `CacheTagConfig` do not extract tags. When `CacheTagConfig` is removed from a distribution via `UpdateDistribution`, CloudFront stops extracting tags from origin responses.  
Changing the `HeaderName` on an existing distribution does not retroactively affect previously cached objects. Tag-based invalidations will not apply to objects already cached using a previous header. To ensure tag invalidations function after updating the header name, use path-based invalidations to recache all objects that use cache tags.
Type: [CacheTagConfig](API_CacheTagConfig.md) object

 ** [CallerReference](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-CallerReference"></a>
A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.  
If the value of `CallerReference` is new (regardless of the content of the `DistributionConfig` object), CloudFront creates a new distribution.  
If `CallerReference` is a value that you already sent in a previous request to create a distribution, CloudFront returns a `DistributionAlreadyExists` error.  
Type: String

 ** [Comment](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Comment"></a>
A comment to describe the distribution. The comment cannot be longer than 128 characters.  
Type: String

 ** [ConnectionFunctionAssociation](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-ConnectionFunctionAssociation"></a>
The distribution's connection function association.  
Type: [ConnectionFunctionAssociation](API_ConnectionFunctionAssociation.md) object

 ** [ConnectionMode](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-ConnectionMode"></a>
This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).  
Type: String  
Valid Values: `direct | tenant-only` 

 ** [ContinuousDeploymentPolicyId](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-ContinuousDeploymentPolicyId"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
The identifier of a continuous deployment policy. For more information, see `CreateContinuousDeploymentPolicy`.  
Type: String

 ** [CustomErrorResponses](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-CustomErrorResponses"></a>
A complex type that controls the following:  
+ Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
+ How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
For more information about custom error pages, see [Customizing Error Responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html) in the *Amazon CloudFront Developer Guide*.  
Type: [CustomErrorResponses](API_CustomErrorResponses.md) object

 ** [DefaultCacheBehavior](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-DefaultCacheBehavior"></a>
A complex type that describes the default cache behavior if you don't specify a `CacheBehavior` element or if files don't match any of the values of `PathPattern` in `CacheBehavior` elements. You must create exactly one default cache behavior.  
Type: [DefaultCacheBehavior](API_DefaultCacheBehavior.md) object

 ** [DefaultRootObject](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-DefaultRootObject"></a>
When a viewer requests the root URL for your distribution, the default root object is the object that you want CloudFront to request from your origin. For example, if your root URL is `https://www.example.com`, you can specify CloudFront to return the `index.html` file as the default root object. You can specify a default root object so that viewers see a specific file or object, instead of another object in your distribution (for example, `https://www.example.com/product-description.html`). A default root object avoids exposing the contents of your distribution.  
You can specify the object name or a path to the object name (for example, `index.html` or `exampleFolderName/index.html`). Your string can't begin with a forward slash (`/`). Only specify the object name or the path to the object.  
If you don't want to specify a default root object when you create a distribution, include an empty `DefaultRootObject` element.  
To delete the default root object from an existing distribution, update the distribution configuration and include an empty `DefaultRootObject` element.  
To replace the default root object, update the distribution configuration and specify the new object.  
For more information about the default root object, see [Specify a default root object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html) in the *Amazon CloudFront Developer Guide*.  
Type: String

 ** [Enabled](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Enabled"></a>
From this field, you can enable or disable the selected distribution.  
Type: Boolean

 ** [HttpVersion](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-HttpVersion"></a>
(Optional) Specify the HTTP version(s) that you want viewers to use to communicate with CloudFront. The default value for new web distributions is `http2`. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.  
For viewers and CloudFront to use HTTP/2, viewers must support TLSv1.2 or later, and must support Server Name Indication (SNI).  
For viewers and CloudFront to use HTTP/3, viewers must support TLSv1.3 and Server Name Indication (SNI). CloudFront supports HTTP/3 connection migration to allow the viewer to switch networks without losing connection. For more information about connection migration, see [Connection Migration](https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration) at RFC 9000. For more information about supported TLSv1.3 ciphers, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).  
Type: String  
Valid Values: `http1.1 | http2 | http3 | http2and3` 

 ** [IsIPV6Enabled](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-IsIPV6Enabled"></a>
To use this field for a multi-tenant distribution, use a connection group instead. For more information, see [ConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html).
If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify `true`. If you specify `false`, CloudFront responds to IPv6 DNS requests with the DNS response code `NOERROR` and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.  
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the `IpAddress` parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see [Creating a Signed URL Using a Custom Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html) in the *Amazon CloudFront Developer Guide*.  
If you're using an Amazon Route 53 AWS Integration alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:  
+ You enable IPv6 for the distribution
+ You're using alternate domain names in the URLs for your objects
For more information, see [Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html) in the * Amazon Route 53 AWS Integration Developer Guide*.  
If you created a CNAME resource record set, either with Amazon Route 53 AWS Integration or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.  
Type: Boolean

 ** [Logging](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Logging"></a>
A complex type that controls whether access logs are written for the distribution.  
For more information about logging, see [Access Logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide*.  
Type: [LoggingConfig](API_LoggingConfig.md) object

 ** [OriginGroups](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-OriginGroups"></a>
A complex type that contains information about origin groups for this distribution.  
Type: [OriginGroups](API_OriginGroups.md) object

 ** [Origins](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Origins"></a>
A complex type that contains information about origins for this distribution.  
Type: [Origins](API_Origins.md) object

 ** [PriceClass](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-PriceClass"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify `PriceClass_All`, CloudFront responds to requests for your objects from all CloudFront edge locations.  
If you specify a price class other than `PriceClass_All`, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.  
For more information about price classes, see [Choosing the Price Class for a CloudFront Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html) in the *Amazon CloudFront Developer Guide*. For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see [Amazon CloudFront Pricing](http://aws.amazon.com/cloudfront/pricing/).  
Type: String  
Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None` 

 ** [Restrictions](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Restrictions"></a>
A complex type that identifies ways in which you want to restrict distribution of your content.  
Type: [Restrictions](API_Restrictions.md) object

 ** [Staging](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-Staging"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A Boolean that indicates whether this is a staging distribution. When this value is `true`, this is a staging distribution. When this value is `false`, this is not a staging distribution.  
Type: Boolean

 ** [TenantConfig](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-TenantConfig"></a>
This field only supports multi-tenant distributions. You can't specify this field for standard distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A distribution tenant configuration.  
Type: [TenantConfig](API_TenantConfig.md) object

 ** [ViewerCertificate](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-ViewerCertificate"></a>
A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.  
Type: [ViewerCertificate](API_ViewerCertificate.md) object

 ** [ViewerMtlsConfig](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-ViewerMtlsConfig"></a>
The distribution's viewer mTLS configuration.  
Type: [ViewerMtlsConfig](API_ViewerMtlsConfig.md) object

 ** [WebACLId](#API_GetDistributionConfig_ResponseSyntax) **   <a name="cloudfront-GetDistributionConfig-response-WebACLId"></a>
Multi-tenant distributions only support AWS WAF V2 web ACLs.
A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example `arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.  
 AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).  
Type: String

## Errors
<a name="API_GetDistributionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetDistributionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetDistributionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetDistributionConfig) 