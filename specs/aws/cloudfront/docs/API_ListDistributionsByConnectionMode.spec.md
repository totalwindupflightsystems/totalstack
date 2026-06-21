---
id: "@specs/aws/cloudfront/docs/API_ListDistributionsByConnectionMode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDistributionsByConnectionMode"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListDistributionsByConnectionMode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListDistributionsByConnectionMode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDistributionsByConnectionMode
<a name="API_ListDistributionsByConnectionMode"></a>

Lists the distributions by the connection mode that you specify.

## Request Syntax
<a name="API_ListDistributionsByConnectionMode_RequestSyntax"></a>

```
GET /2020-05-31/distributionsByConnectionMode/{{ConnectionMode}}?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDistributionsByConnectionMode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionMode](#API_ListDistributionsByConnectionMode_RequestSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-request-uri-ConnectionMode"></a>
This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).  
Valid Values: `direct | tenant-only`   
Required: Yes

 ** [Marker](#API_ListDistributionsByConnectionMode_RequestSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-request-uri-Marker"></a>
 The marker for the next set of distributions to retrieve.

 ** [MaxItems](#API_ListDistributionsByConnectionMode_RequestSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-request-uri-MaxItems"></a>
The maximum number of distributions to return.

## Request Body
<a name="API_ListDistributionsByConnectionMode_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDistributionsByConnectionMode_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionList>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <DistributionSummary>
         <Aliases>
            <Items>
               <CNAME>string</CNAME>
            </Items>
            <Quantity>integer</Quantity>
         </Aliases>
         <AliasICPRecordals>
            <AliasICPRecordal>
               <CNAME>string</CNAME>
               <ICPRecordalStatus>string</ICPRecordalStatus>
            </AliasICPRecordal>
         </AliasICPRecordals>
         <AnycastIpListId>string</AnycastIpListId>
         <ARN>string</ARN>
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
         <Comment>string</Comment>
         <ConnectionFunctionAssociation>
            <Id>string</Id>
         </ConnectionFunctionAssociation>
         <ConnectionMode>string</ConnectionMode>
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
         <DomainName>string</DomainName>
         <Enabled>boolean</Enabled>
         <ETag>string</ETag>
         <HttpVersion>string</HttpVersion>
         <Id>string</Id>
         <IsIPV6Enabled>boolean</IsIPV6Enabled>
         <LastModifiedTime>timestamp</LastModifiedTime>
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
         <Status>string</Status>
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
      </DistributionSummary>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</DistributionList>
```

## Response Elements
<a name="API_ListDistributionsByConnectionMode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DistributionList](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-DistributionList"></a>
Root level tag for the DistributionList parameters.  
Required: Yes

 ** [IsTruncated](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-IsTruncated"></a>
A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more distributions in the list.  
Type: Boolean

 ** [Items](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-Items"></a>
A complex type that contains one `DistributionSummary` element for each distribution that was created by the current AWS account.  
Type: Array of [DistributionSummary](API_DistributionSummary.md) objects

 ** [Marker](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-Marker"></a>
The value you provided for the `Marker` request parameter.  
Type: String

 ** [MaxItems](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-MaxItems"></a>
The value you provided for the `MaxItems` request parameter.  
Type: Integer

 ** [NextMarker](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value you can use for the `Marker` request parameter to continue listing your distributions where they left off.  
Type: String

 ** [Quantity](#API_ListDistributionsByConnectionMode_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByConnectionMode-response-Quantity"></a>
The number of distributions that were created by the current AWS account.  
Type: Integer

## Errors
<a name="API_ListDistributionsByConnectionMode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListDistributionsByConnectionMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByConnectionMode) 