---
id: "@specs/aws/cloudfront/docs/API_CreateDistributionWithTags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDistributionWithTags"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateDistributionWithTags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateDistributionWithTags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDistributionWithTags
<a name="API_CreateDistributionWithTags"></a>

Create a new distribution with tags. This API operation requires the following IAM permissions:
+  [CreateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html) 
+  [TagResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html) 

## Request Syntax
<a name="API_CreateDistributionWithTags_RequestSyntax"></a>

```
POST /2020-05-31/distribution?WithTags HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DistributionConfigWithTags xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <DistributionConfig>
      <Aliases>
         <Items>
            <CNAME>{{string}}</CNAME>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </Aliases>
      <AnycastIpListId>{{string}}</AnycastIpListId>
      <CacheBehaviors>
         <Items>
            <CacheBehavior>
               <AllowedMethods>
                  <CachedMethods>
                     <Items>
                        <Method>{{string}}</Method>
                     </Items>
                     <Quantity>{{integer}}</Quantity>
                  </CachedMethods>
                  <Items>
                     <Method>{{string}}</Method>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </AllowedMethods>
               <CachePolicyId>{{string}}</CachePolicyId>
               <Compress>{{boolean}}</Compress>
               <DefaultTTL>{{long}}</DefaultTTL>
               <FieldLevelEncryptionId>{{string}}</FieldLevelEncryptionId>
               <ForwardedValues>
                  <Cookies>
                     <Forward>{{string}}</Forward>
                     <WhitelistedNames>
                        <Items>
                           <Name>{{string}}</Name>
                        </Items>
                        <Quantity>{{integer}}</Quantity>
                     </WhitelistedNames>
                  </Cookies>
                  <Headers>
                     <Items>
                        <Name>{{string}}</Name>
                     </Items>
                     <Quantity>{{integer}}</Quantity>
                  </Headers>
                  <QueryString>{{boolean}}</QueryString>
                  <QueryStringCacheKeys>
                     <Items>
                        <Name>{{string}}</Name>
                     </Items>
                     <Quantity>{{integer}}</Quantity>
                  </QueryStringCacheKeys>
               </ForwardedValues>
               <FunctionAssociations>
                  <Items>
                     <FunctionAssociation>
                        <EventType>{{string}}</EventType>
                        <FunctionARN>{{string}}</FunctionARN>
                     </FunctionAssociation>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </FunctionAssociations>
               <GrpcConfig>
                  <Enabled>{{boolean}}</Enabled>
               </GrpcConfig>
               <LambdaFunctionAssociations>
                  <Items>
                     <LambdaFunctionAssociation>
                        <EventType>{{string}}</EventType>
                        <IncludeBody>{{boolean}}</IncludeBody>
                        <LambdaFunctionARN>{{string}}</LambdaFunctionARN>
                     </LambdaFunctionAssociation>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </LambdaFunctionAssociations>
               <MaxTTL>{{long}}</MaxTTL>
               <MinTTL>{{long}}</MinTTL>
               <OriginRequestPolicyId>{{string}}</OriginRequestPolicyId>
               <PathPattern>{{string}}</PathPattern>
               <RealtimeLogConfigArn>{{string}}</RealtimeLogConfigArn>
               <ResponseHeadersPolicyId>{{string}}</ResponseHeadersPolicyId>
               <SmoothStreaming>{{boolean}}</SmoothStreaming>
               <TargetOriginId>{{string}}</TargetOriginId>
               <TrustedKeyGroups>
                  <Enabled>{{boolean}}</Enabled>
                  <Items>
                     <KeyGroup>{{string}}</KeyGroup>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </TrustedKeyGroups>
               <TrustedSigners>
                  <Enabled>{{boolean}}</Enabled>
                  <Items>
                     <AwsAccountNumber>{{string}}</AwsAccountNumber>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </TrustedSigners>
               <ViewerProtocolPolicy>{{string}}</ViewerProtocolPolicy>
            </CacheBehavior>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </CacheBehaviors>
      <CacheTagConfig>
         <HeaderName>{{string}}</HeaderName>
      </CacheTagConfig>
      <CallerReference>{{string}}</CallerReference>
      <Comment>{{string}}</Comment>
      <ConnectionFunctionAssociation>
         <Id>{{string}}</Id>
      </ConnectionFunctionAssociation>
      <ConnectionMode>{{string}}</ConnectionMode>
      <ContinuousDeploymentPolicyId>{{string}}</ContinuousDeploymentPolicyId>
      <CustomErrorResponses>
         <Items>
            <CustomErrorResponse>
               <ErrorCachingMinTTL>{{long}}</ErrorCachingMinTTL>
               <ErrorCode>{{integer}}</ErrorCode>
               <ResponseCode>{{string}}</ResponseCode>
               <ResponsePagePath>{{string}}</ResponsePagePath>
            </CustomErrorResponse>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </CustomErrorResponses>
      <DefaultCacheBehavior>
         <AllowedMethods>
            <CachedMethods>
               <Items>
                  <Method>{{string}}</Method>
               </Items>
               <Quantity>{{integer}}</Quantity>
            </CachedMethods>
            <Items>
               <Method>{{string}}</Method>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </AllowedMethods>
         <CachePolicyId>{{string}}</CachePolicyId>
         <Compress>{{boolean}}</Compress>
         <DefaultTTL>{{long}}</DefaultTTL>
         <FieldLevelEncryptionId>{{string}}</FieldLevelEncryptionId>
         <ForwardedValues>
            <Cookies>
               <Forward>{{string}}</Forward>
               <WhitelistedNames>
                  <Items>
                     <Name>{{string}}</Name>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </WhitelistedNames>
            </Cookies>
            <Headers>
               <Items>
                  <Name>{{string}}</Name>
               </Items>
               <Quantity>{{integer}}</Quantity>
            </Headers>
            <QueryString>{{boolean}}</QueryString>
            <QueryStringCacheKeys>
               <Items>
                  <Name>{{string}}</Name>
               </Items>
               <Quantity>{{integer}}</Quantity>
            </QueryStringCacheKeys>
         </ForwardedValues>
         <FunctionAssociations>
            <Items>
               <FunctionAssociation>
                  <EventType>{{string}}</EventType>
                  <FunctionARN>{{string}}</FunctionARN>
               </FunctionAssociation>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </FunctionAssociations>
         <GrpcConfig>
            <Enabled>{{boolean}}</Enabled>
         </GrpcConfig>
         <LambdaFunctionAssociations>
            <Items>
               <LambdaFunctionAssociation>
                  <EventType>{{string}}</EventType>
                  <IncludeBody>{{boolean}}</IncludeBody>
                  <LambdaFunctionARN>{{string}}</LambdaFunctionARN>
               </LambdaFunctionAssociation>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </LambdaFunctionAssociations>
         <MaxTTL>{{long}}</MaxTTL>
         <MinTTL>{{long}}</MinTTL>
         <OriginRequestPolicyId>{{string}}</OriginRequestPolicyId>
         <RealtimeLogConfigArn>{{string}}</RealtimeLogConfigArn>
         <ResponseHeadersPolicyId>{{string}}</ResponseHeadersPolicyId>
         <SmoothStreaming>{{boolean}}</SmoothStreaming>
         <TargetOriginId>{{string}}</TargetOriginId>
         <TrustedKeyGroups>
            <Enabled>{{boolean}}</Enabled>
            <Items>
               <KeyGroup>{{string}}</KeyGroup>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </TrustedKeyGroups>
         <TrustedSigners>
            <Enabled>{{boolean}}</Enabled>
            <Items>
               <AwsAccountNumber>{{string}}</AwsAccountNumber>
            </Items>
            <Quantity>{{integer}}</Quantity>
         </TrustedSigners>
         <ViewerProtocolPolicy>{{string}}</ViewerProtocolPolicy>
      </DefaultCacheBehavior>
      <DefaultRootObject>{{string}}</DefaultRootObject>
      <Enabled>{{boolean}}</Enabled>
      <HttpVersion>{{string}}</HttpVersion>
      <IsIPV6Enabled>{{boolean}}</IsIPV6Enabled>
      <Logging>
         <Bucket>{{string}}</Bucket>
         <Enabled>{{boolean}}</Enabled>
         <IncludeCookies>{{boolean}}</IncludeCookies>
         <Prefix>{{string}}</Prefix>
      </Logging>
      <OriginGroups>
         <Items>
            <OriginGroup>
               <FailoverCriteria>
                  <StatusCodes>
                     <Items>
                        <StatusCode>{{integer}}</StatusCode>
                     </Items>
                     <Quantity>{{integer}}</Quantity>
                  </StatusCodes>
               </FailoverCriteria>
               <Id>{{string}}</Id>
               <Members>
                  <Items>
                     <OriginGroupMember>
                        <OriginId>{{string}}</OriginId>
                     </OriginGroupMember>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </Members>
               <SelectionCriteria>{{string}}</SelectionCriteria>
            </OriginGroup>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </OriginGroups>
      <Origins>
         <Items>
            <Origin>
               <ConnectionAttempts>{{integer}}</ConnectionAttempts>
               <ConnectionTimeout>{{integer}}</ConnectionTimeout>
               <CustomHeaders>
                  <Items>
                     <OriginCustomHeader>
                        <HeaderName>{{string}}</HeaderName>
                        <HeaderValue>{{string}}</HeaderValue>
                     </OriginCustomHeader>
                  </Items>
                  <Quantity>{{integer}}</Quantity>
               </CustomHeaders>
               <CustomOriginConfig>
                  <HTTPPort>{{integer}}</HTTPPort>
                  <HTTPSPort>{{integer}}</HTTPSPort>
                  <IpAddressType>{{string}}</IpAddressType>
                  <OriginKeepaliveTimeout>{{integer}}</OriginKeepaliveTimeout>
                  <OriginMtlsConfig>
                     <ClientCertificateArn>{{string}}</ClientCertificateArn>
                  </OriginMtlsConfig>
                  <OriginProtocolPolicy>{{string}}</OriginProtocolPolicy>
                  <OriginReadTimeout>{{integer}}</OriginReadTimeout>
                  <OriginSslProtocols>
                     <Items>
                        <SslProtocol>{{string}}</SslProtocol>
                     </Items>
                     <Quantity>{{integer}}</Quantity>
                  </OriginSslProtocols>
               </CustomOriginConfig>
               <DomainName>{{string}}</DomainName>
               <Id>{{string}}</Id>
               <OriginAccessControlId>{{string}}</OriginAccessControlId>
               <OriginPath>{{string}}</OriginPath>
               <OriginShield>
                  <Enabled>{{boolean}}</Enabled>
                  <OriginShieldRegion>{{string}}</OriginShieldRegion>
               </OriginShield>
               <ResponseCompletionTimeout>{{integer}}</ResponseCompletionTimeout>
               <S3OriginConfig>
                  <OriginAccessIdentity>{{string}}</OriginAccessIdentity>
                  <OriginReadTimeout>{{integer}}</OriginReadTimeout>
               </S3OriginConfig>
               <VpcOriginConfig>
                  <OriginKeepaliveTimeout>{{integer}}</OriginKeepaliveTimeout>
                  <OriginReadTimeout>{{integer}}</OriginReadTimeout>
                  <VpcOriginId>{{string}}</VpcOriginId>
               </VpcOriginConfig>
            </Origin>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </Origins>
      <PriceClass>{{string}}</PriceClass>
      <Restrictions>
         <GeoRestriction>
            <Items>
               <Location>{{string}}</Location>
            </Items>
            <Quantity>{{integer}}</Quantity>
            <RestrictionType>{{string}}</RestrictionType>
         </GeoRestriction>
      </Restrictions>
      <Staging>{{boolean}}</Staging>
      <TenantConfig>
         <ParameterDefinitions>
            <ParameterDefinition>
               <Definition>
                  <StringSchema>
                     <Comment>{{string}}</Comment>
                     <DefaultValue>{{string}}</DefaultValue>
                     <Required>{{boolean}}</Required>
                  </StringSchema>
               </Definition>
               <Name>{{string}}</Name>
            </ParameterDefinition>
         </ParameterDefinitions>
      </TenantConfig>
      <ViewerCertificate>
         <ACMCertificateArn>{{string}}</ACMCertificateArn>
         <Certificate>{{string}}</Certificate>
         <CertificateSource>{{string}}</CertificateSource>
         <CloudFrontDefaultCertificate>{{boolean}}</CloudFrontDefaultCertificate>
         <IAMCertificateId>{{string}}</IAMCertificateId>
         <MinimumProtocolVersion>{{string}}</MinimumProtocolVersion>
         <SSLSupportMethod>{{string}}</SSLSupportMethod>
      </ViewerCertificate>
      <ViewerMtlsConfig>
         <Mode>{{string}}</Mode>
         <TrustStoreConfig>
            <AdvertiseTrustStoreCaNames>{{boolean}}</AdvertiseTrustStoreCaNames>
            <IgnoreCertificateExpiry>{{boolean}}</IgnoreCertificateExpiry>
            <TrustStoreId>{{string}}</TrustStoreId>
         </TrustStoreConfig>
      </ViewerMtlsConfig>
      <WebACLId>{{string}}</WebACLId>
   </DistributionConfig>
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
</DistributionConfigWithTags>
```

## URI Request Parameters
<a name="API_CreateDistributionWithTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDistributionWithTags_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DistributionConfigWithTags](#API_CreateDistributionWithTags_RequestSyntax) **   <a name="cloudfront-CreateDistributionWithTags-request-DistributionConfigWithTags"></a>
Root level tag for the DistributionConfigWithTags parameters.  
Required: Yes

 ** [DistributionConfig](#API_CreateDistributionWithTags_RequestSyntax) **   <a name="cloudfront-CreateDistributionWithTags-request-DistributionConfig"></a>
A distribution configuration.  
Type: [DistributionConfig](API_DistributionConfig.md) object  
Required: Yes

 ** [Tags](#API_CreateDistributionWithTags_RequestSyntax) **   <a name="cloudfront-CreateDistributionWithTags-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateDistributionWithTags_ResponseSyntax"></a>

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
<a name="API_CreateDistributionWithTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [Distribution](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-Distribution"></a>
Root level tag for the Distribution parameters.  
Required: Yes

 ** [ActiveTrustedKeyGroups](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-ActiveTrustedKeyGroups"></a>
This field contains a list of key groups and the public keys in each key group that CloudFront can use to verify the signatures of signed URLs or signed cookies.  
Type: [ActiveTrustedKeyGroups](API_ActiveTrustedKeyGroups.md) object

 ** [ActiveTrustedSigners](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-ActiveTrustedSigners"></a>
We recommend using `TrustedKeyGroups` instead of `TrustedSigners`.
This field contains a list of AWS account IDs and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs or signed cookies.  
Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md) object

 ** [AliasICPRecordals](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-AliasICPRecordals"></a>
 AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.  
For more information about ICP recordals, see [ Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with AWS services in China*.  
Type: Array of [AliasICPRecordal](API_AliasICPRecordal.md) objects

 ** [ARN](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-ARN"></a>
The distribution's Amazon Resource Name (ARN).  
Type: String

 ** [DistributionConfig](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-DistributionConfig"></a>
The distribution's configuration.  
Type: [DistributionConfig](API_DistributionConfig.md) object

 ** [DomainName](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-DomainName"></a>
The distribution's CloudFront domain name. For example: `d111111abcdef8.cloudfront.net`.  
Type: String

 ** [Id](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-Id"></a>
The distribution's identifier. For example: `E1U5RQF7T870K0`.  
Type: String

 ** [InProgressInvalidationBatches](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-InProgressInvalidationBatches"></a>
The number of invalidation batches currently in progress.  
Type: Integer

 ** [LastModifiedTime](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-LastModifiedTime"></a>
The date and time when the distribution was last modified.  
Type: Timestamp

 ** [Status](#API_CreateDistributionWithTags_ResponseSyntax) **   <a name="cloudfront-CreateDistributionWithTags-response-Status"></a>
The distribution's status. When the status is `Deployed`, the distribution's information is fully propagated to all CloudFront edge locations.  
Type: String

## Errors
<a name="API_CreateDistributionWithTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CNAMEAlreadyExists **   
The CNAME specified is already defined for CloudFront.  
HTTP Status Code: 409

 ** ContinuousDeploymentPolicyInUse **   
You cannot delete a continuous deployment policy that is associated with a primary distribution.  
HTTP Status Code: 409

 ** DistributionAlreadyExists **   
The caller reference you attempted to create the distribution with is associated with another distribution.  
HTTP Status Code: 409

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior **   
The specified configuration for field-level encryption can't be associated with the specified cache behavior.  
HTTP Status Code: 400

 ** IllegalOriginAccessConfiguration **   
An origin cannot contain both an origin access control (OAC) and an origin access identity (OAI).  
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

 ** InvalidDomainNameForOriginAccessControl **   
An origin access control is associated with an origin whose domain name is not supported.  
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

 ** InvalidTagging **   
The tagging specified is not valid.  
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

 ** NoSuchContinuousDeploymentPolicy **   
The continuous deployment policy doesn't exist.  
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
<a name="API_CreateDistributionWithTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateDistributionWithTags) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateDistributionWithTags) 