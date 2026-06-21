---
id: "@specs/aws/cloudfront/docs/API_CopyDistribution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDistribution"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CopyDistribution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CopyDistribution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDistribution
<a name="API_CopyDistribution"></a>

Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.

After you create a staging distribution, you can use `UpdateDistribution` to modify the staging distribution's configuration. Then you can use `CreateContinuousDeploymentPolicy` to incrementally move traffic to the staging distribution.

This API operation requires the following IAM permissions:
+  [GetDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html) 
+  [CreateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html) 
+  [CopyDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html) 

## Request Syntax
<a name="API_CopyDistribution_RequestSyntax"></a>

```
POST /2020-05-31/distribution/{{PrimaryDistributionId}}/copy HTTP/1.1
Staging: {{Staging}}
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<CopyDistributionRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>{{string}}</CallerReference>
   <Enabled>{{boolean}}</Enabled>
</CopyDistributionRequest>
```

## URI Request Parameters
<a name="API_CopyDistribution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-IfMatch"></a>
The version identifier of the primary distribution whose configuration you are copying. This is the `ETag` value returned in the response to `GetDistribution` and `GetDistributionConfig`.

 ** [PrimaryDistributionId](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-uri-PrimaryDistributionId"></a>
The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use `ListDistributions`.  
Required: Yes

 ** [Staging](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-Staging"></a>
The type of distribution that your primary distribution will be copied to. The only valid value is `True`, indicating that you are copying to a staging distribution.

## Request Body
<a name="API_CopyDistribution_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CopyDistributionRequest](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-CopyDistributionRequest"></a>
Root level tag for the CopyDistributionRequest parameters.  
Required: Yes

 ** [CallerReference](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-CallerReference"></a>
A value that uniquely identifies a request to create a resource. This helps to prevent CloudFront from creating a duplicate resource if you accidentally resubmit an identical request.  
Type: String  
Required: Yes

 ** [Enabled](#API_CopyDistribution_RequestSyntax) **   <a name="cloudfront-CopyDistribution-request-Enabled"></a>
A Boolean flag to specify the state of the staging distribution when it's created. When you set this value to `True`, the staging distribution is enabled. When you set this value to `False`, the staging distribution is disabled.  
If you omit this field, the default value is `True`.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_CopyDistribution_ResponseSyntax"></a>

```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<Distribution>
   <ActiveTrustedKeyGroups>
      <Enabled>boolean</Enabled>
      <Items>
         <KeyGroup>
            <KeyGroupId>string</KeyGroupId>
            <KeyPairIds>
               <Items>
                  <KeyPairId>string</KeyPairId>
               </Items>
               <Quantity>integer</Quantity>
            </KeyPairIds>
         </KeyGroup>
      </Items>
      <Quantity>integer</Quantity>
   </ActiveTrustedKeyGroups>
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
   <AliasICPRecordals>
      <AliasICPRecordal>
         <CNAME>string</CNAME>
         <ICPRecordalStatus>string</ICPRecordalStatus>
      </AliasICPRecordal>
   </AliasICPRecordals>
   <ARN>string</ARN>
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
   <DomainName>string</DomainName>
   <Id>string</Id>
   <InProgressInvalidationBatches>integer</InProgressInvalidationBatches>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Status>string</Status>
</Distribution>
```

## Response Elements
<a name="API_CopyDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [Distribution](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-Distribution"></a>
Root level tag for the Distribution parameters.  
Required: Yes

 ** [ActiveTrustedKeyGroups](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-ActiveTrustedKeyGroups"></a>
This field contains a list of key groups and the public keys in each key group that CloudFront can use to verify the signatures of signed URLs or signed cookies.  
Type: [ActiveTrustedKeyGroups](API_ActiveTrustedKeyGroups.md) object

 ** [ActiveTrustedSigners](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-ActiveTrustedSigners"></a>
We recommend using `TrustedKeyGroups` instead of `TrustedSigners`.
This field contains a list of AWS account IDs and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs or signed cookies.  
Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md) object

 ** [AliasICPRecordals](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-AliasICPRecordals"></a>
 AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.  
For more information about ICP recordals, see [ Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with AWS services in China*.  
Type: Array of [AliasICPRecordal](API_AliasICPRecordal.md) objects

 ** [ARN](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-ARN"></a>
The distribution's Amazon Resource Name (ARN).  
Type: String

 ** [DistributionConfig](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-DistributionConfig"></a>
The distribution's configuration.  
Type: [DistributionConfig](API_DistributionConfig.md) object

 ** [DomainName](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-DomainName"></a>
The distribution's CloudFront domain name. For example: `d111111abcdef8.cloudfront.net`.  
Type: String

 ** [Id](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-Id"></a>
The distribution's identifier. For example: `E1U5RQF7T870K0`.  
Type: String

 ** [InProgressInvalidationBatches](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-InProgressInvalidationBatches"></a>
The number of invalidation batches currently in progress.  
Type: Integer

 ** [LastModifiedTime](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-LastModifiedTime"></a>
The date and time when the distribution was last modified.  
Type: Timestamp

 ** [Status](#API_CopyDistribution_ResponseSyntax) **   <a name="cloudfront-CopyDistribution-response-Status"></a>
The distribution's status. When the status is `Deployed`, the distribution's information is fully propagated to all CloudFront edge locations.  
Type: String

## Errors
<a name="API_CopyDistribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CNAMEAlreadyExists **   
The CNAME specified is already defined for CloudFront.  
HTTP Status Code: 409

 ** DistributionAlreadyExists **   
The caller reference you attempted to create the distribution with is associated with another distribution.  
HTTP Status Code: 409

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior **   
The specified configuration for field-level encryption can't be associated with the specified cache behavior.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidDefaultRootObject **   
The default root object file name is too big or contains an invalid character.  
HTTP Status Code: 400

 ** InvalidErrorCode **   
An invalid error code was specified.  
HTTP Status Code: 400

 ** InvalidForwardCookies **   
Your request contains forward cookies option which doesn't match with the expectation for the `whitelisted` list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.  
HTTP Status Code: 400

 ** InvalidFunctionAssociation **   
A CloudFront function association is invalid.  
HTTP Status Code: 400

 ** InvalidGeoRestrictionParameter **   
The specified geo restriction parameter is not valid.  
HTTP Status Code: 400

 ** InvalidHeadersForS3Origin **   
The headers specified are not valid for an Amazon S3 origin.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** InvalidLambdaFunctionAssociation **   
The specified Lambda@Edge function association is invalid.  
HTTP Status Code: 400

 ** InvalidLocationCode **   
The location code specified is not valid.  
HTTP Status Code: 400

 ** InvalidMinimumProtocolVersion **   
The minimum protocol version specified is not valid.  
HTTP Status Code: 400

 ** InvalidOrigin **   
The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.  
HTTP Status Code: 400

 ** InvalidOriginAccessControl **   
The origin access control is not valid.  
HTTP Status Code: 400

 ** InvalidOriginAccessIdentity **   
The origin access identity is not valid or doesn't exist.  
HTTP Status Code: 400

 ** InvalidOriginKeepaliveTimeout **   
The keep alive timeout specified for the origin is not valid.  
HTTP Status Code: 400

 ** InvalidOriginReadTimeout **   
The read timeout specified for the origin is not valid.  
HTTP Status Code: 400

 ** InvalidProtocolSettings **   
You cannot specify SSLv3 as the minimum protocol version if you only want to support only clients that support Server Name Indication (SNI).  
HTTP Status Code: 400

 ** InvalidQueryStringParameters **   
The query string parameters specified are not valid.  
HTTP Status Code: 400

 ** InvalidRelativePath **   
The relative path is too big, is not URL-encoded, or does not begin with a slash (/).  
HTTP Status Code: 400

 ** InvalidRequiredProtocol **   
This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the `RequiredProtocols` element from your distribution configuration.  
HTTP Status Code: 400

 ** InvalidResponseCode **   
A response code is not valid.  
HTTP Status Code: 400

 ** InvalidTTLOrder **   
The TTL order specified is not valid.  
HTTP Status Code: 400

 ** InvalidViewerCertificate **   
A viewer certificate specified is not valid.  
HTTP Status Code: 400

 ** InvalidWebACLId **   
A web ACL ID specified is not valid. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example `arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a`. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example `473e64fd-f30b-4765-81a0-62ad96dd167a`.  
HTTP Status Code: 400

 ** MissingBody **   
This operation requires a body. Ensure that the body is present and the `Content-Type` header is set.  
HTTP Status Code: 400

 ** NoSuchCachePolicy **   
The cache policy does not exist.  
HTTP Status Code: 404

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

 ** NoSuchFieldLevelEncryptionConfig **   
The specified configuration for field-level encryption doesn't exist.  
HTTP Status Code: 404

 ** NoSuchOrigin **   
No origin exists with the specified `Origin Id`.  
HTTP Status Code: 404

 ** NoSuchOriginRequestPolicy **   
The origin request policy does not exist.  
HTTP Status Code: 404

 ** NoSuchRealtimeLogConfig **   
The real-time log configuration does not exist.  
HTTP Status Code: 404

 ** NoSuchResponseHeadersPolicy **   
The response headers policy does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** RealtimeLogConfigOwnerMismatch **   
The specified real-time log configuration belongs to a different AWS account.  
HTTP Status Code: 401

 ** TooManyCacheBehaviors **   
You cannot create more cache behaviors for the distribution.  
HTTP Status Code: 400

 ** TooManyCertificates **   
You cannot create anymore custom SSL/TLS certificates.  
HTTP Status Code: 400

 ** TooManyCookieNamesInWhiteList **   
Your request contains more cookie names in the whitelist than are allowed per cache behavior.  
HTTP Status Code: 400

 ** TooManyDistributionCNAMEs **   
Your request contains more CNAMEs than are allowed per distribution.  
HTTP Status Code: 400

 ** TooManyDistributions **   
Processing your request would cause you to exceed the maximum number of distributions allowed.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToCachePolicy **   
The maximum number of distributions have been associated with the specified cache policy. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToFieldLevelEncryptionConfig **   
The maximum number of distributions have been associated with the specified configuration for field-level encryption.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToKeyGroup **   
The number of distributions that reference this key group is more than the maximum allowed. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToOriginAccessControl **   
The maximum number of distributions have been associated with the specified origin access control.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToOriginRequestPolicy **   
The maximum number of distributions have been associated with the specified origin request policy. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsAssociatedToResponseHeadersPolicy **   
The maximum number of distributions have been associated with the specified response headers policy.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsWithFunctionAssociations **   
You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyDistributionsWithLambdaAssociations **   
Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.  
HTTP Status Code: 400

 ** TooManyDistributionsWithSingleFunctionARN **   
The maximum number of distributions have been associated with the specified Lambda@Edge function.  
HTTP Status Code: 400

 ** TooManyFunctionAssociations **   
You have reached the maximum number of CloudFront function associations for this distribution. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyHeadersInForwardedValues **   
Your request contains too many headers in forwarded values.  
HTTP Status Code: 400

 ** TooManyKeyGroupsAssociatedToDistribution **   
The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyLambdaFunctionAssociations **   
Your request contains more Lambda@Edge function associations than are allowed per distribution.  
HTTP Status Code: 400

 ** TooManyOriginCustomHeaders **   
Your request contains too many origin custom headers.  
HTTP Status Code: 400

 ** TooManyOriginGroupsPerDistribution **   
Processing your request would cause you to exceed the maximum number of origin groups allowed.  
HTTP Status Code: 400

 ** TooManyOrigins **   
You cannot create more origins for the distribution.  
HTTP Status Code: 400

 ** TooManyQueryStringParameters **   
Your request contains too many query string parameters.  
HTTP Status Code: 400

 ** TooManyTrustedSigners **   
Your request contains more trusted signers than are allowed per distribution.  
HTTP Status Code: 400

 ** TrustedKeyGroupDoesNotExist **   
The specified key group does not exist.  
HTTP Status Code: 400

 ** TrustedSignerDoesNotExist **   
One or more of your trusted signers don't exist.  
HTTP Status Code: 400

## See Also
<a name="API_CopyDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CopyDistribution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CopyDistribution) 