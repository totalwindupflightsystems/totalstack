---
id: "@specs/aws/cloudfront/docs/API_UpdateResponseHeadersPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateResponseHeadersPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateResponseHeadersPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateResponseHeadersPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateResponseHeadersPolicy
<a name="API_UpdateResponseHeadersPolicy"></a>

Updates a response headers policy.

When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:

1. Use `GetResponseHeadersPolicyConfig` to get the current policy's configuration.

1. Modify the fields in the response headers policy configuration that you want to update.

1. Call `UpdateResponseHeadersPolicy`, providing the entire response headers policy configuration, including the fields that you modified and those that you didn't.

## Request Syntax
<a name="API_UpdateResponseHeadersPolicy_RequestSyntax"></a>

```
PUT /2020-05-31/response-headers-policy/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ResponseHeadersPolicyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>{{string}}</Comment>
   <CorsConfig>
      <AccessControlAllowCredentials>{{boolean}}</AccessControlAllowCredentials>
      <AccessControlAllowHeaders>
         <Items>
            <Header>{{string}}</Header>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </AccessControlAllowHeaders>
      <AccessControlAllowMethods>
         <Items>
            <Method>{{string}}</Method>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </AccessControlAllowMethods>
      <AccessControlAllowOrigins>
         <Items>
            <Origin>{{string}}</Origin>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </AccessControlAllowOrigins>
      <AccessControlExposeHeaders>
         <Items>
            <Header>{{string}}</Header>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </AccessControlExposeHeaders>
      <AccessControlMaxAgeSec>{{integer}}</AccessControlMaxAgeSec>
      <OriginOverride>{{boolean}}</OriginOverride>
   </CorsConfig>
   <CustomHeadersConfig>
      <Items>
         <ResponseHeadersPolicyCustomHeader>
            <Header>{{string}}</Header>
            <Override>{{boolean}}</Override>
            <Value>{{string}}</Value>
         </ResponseHeadersPolicyCustomHeader>
      </Items>
      <Quantity>{{integer}}</Quantity>
   </CustomHeadersConfig>
   <Name>{{string}}</Name>
   <RemoveHeadersConfig>
      <Items>
         <ResponseHeadersPolicyRemoveHeader>
            <Header>{{string}}</Header>
         </ResponseHeadersPolicyRemoveHeader>
      </Items>
      <Quantity>{{integer}}</Quantity>
   </RemoveHeadersConfig>
   <SecurityHeadersConfig>
      <ContentSecurityPolicy>
         <ContentSecurityPolicy>{{string}}</ContentSecurityPolicy>
         <Override>{{boolean}}</Override>
      </ContentSecurityPolicy>
      <ContentTypeOptions>
         <Override>{{boolean}}</Override>
      </ContentTypeOptions>
      <FrameOptions>
         <FrameOption>{{string}}</FrameOption>
         <Override>{{boolean}}</Override>
      </FrameOptions>
      <ReferrerPolicy>
         <Override>{{boolean}}</Override>
         <ReferrerPolicy>{{string}}</ReferrerPolicy>
      </ReferrerPolicy>
      <StrictTransportSecurity>
         <AccessControlMaxAgeSec>{{integer}}</AccessControlMaxAgeSec>
         <IncludeSubdomains>{{boolean}}</IncludeSubdomains>
         <Override>{{boolean}}</Override>
         <Preload>{{boolean}}</Preload>
      </StrictTransportSecurity>
      <XSSProtection>
         <ModeBlock>{{boolean}}</ModeBlock>
         <Override>{{boolean}}</Override>
         <Protection>{{boolean}}</Protection>
         <ReportUri>{{string}}</ReportUri>
      </XSSProtection>
   </SecurityHeadersConfig>
   <ServerTimingHeadersConfig>
      <Enabled>{{boolean}}</Enabled>
      <SamplingRate>{{double}}</SamplingRate>
   </ServerTimingHeadersConfig>
</ResponseHeadersPolicyConfig>
```

## URI Request Parameters
<a name="API_UpdateResponseHeadersPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateResponseHeadersPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ResponseHeadersPolicyConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-ResponseHeadersPolicyConfig"></a>
Root level tag for the ResponseHeadersPolicyConfig parameters.  
Required: Yes

 ** [Comment](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-Comment"></a>
A comment to describe the response headers policy.  
The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [CorsConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-CorsConfig"></a>
A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).  
Type: [ResponseHeadersPolicyCorsConfig](API_ResponseHeadersPolicyCorsConfig.md) object  
Required: No

 ** [CustomHeadersConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-CustomHeadersConfig"></a>
A configuration for a set of custom HTTP response headers.  
Type: [ResponseHeadersPolicyCustomHeadersConfig](API_ResponseHeadersPolicyCustomHeadersConfig.md) object  
Required: No

 ** [Name](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-Name"></a>
A name to identify the response headers policy.  
The name must be unique for response headers policies in this AWS account.  
Type: String  
Required: Yes

 ** [RemoveHeadersConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-RemoveHeadersConfig"></a>
A configuration for a set of HTTP headers to remove from the HTTP response.  
Type: [ResponseHeadersPolicyRemoveHeadersConfig](API_ResponseHeadersPolicyRemoveHeadersConfig.md) object  
Required: No

 ** [SecurityHeadersConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-SecurityHeadersConfig"></a>
A configuration for a set of security-related HTTP response headers.  
Type: [ResponseHeadersPolicySecurityHeadersConfig](API_ResponseHeadersPolicySecurityHeadersConfig.md) object  
Required: No

 ** [ServerTimingHeadersConfig](#API_UpdateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-request-ServerTimingHeadersConfig"></a>
A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront.  
Type: [ResponseHeadersPolicyServerTimingHeadersConfig](API_ResponseHeadersPolicyServerTimingHeadersConfig.md) object  
Required: No

## Response Syntax
<a name="API_UpdateResponseHeadersPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ResponseHeadersPolicy>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <ResponseHeadersPolicyConfig>
      <Comment>string</Comment>
      <CorsConfig>
         <AccessControlAllowCredentials>boolean</AccessControlAllowCredentials>
         <AccessControlAllowHeaders>
            <Items>
               <Header>string</Header>
            </Items>
            <Quantity>integer</Quantity>
         </AccessControlAllowHeaders>
         <AccessControlAllowMethods>
            <Items>
               <Method>string</Method>
            </Items>
            <Quantity>integer</Quantity>
         </AccessControlAllowMethods>
         <AccessControlAllowOrigins>
            <Items>
               <Origin>string</Origin>
            </Items>
            <Quantity>integer</Quantity>
         </AccessControlAllowOrigins>
         <AccessControlExposeHeaders>
            <Items>
               <Header>string</Header>
            </Items>
            <Quantity>integer</Quantity>
         </AccessControlExposeHeaders>
         <AccessControlMaxAgeSec>integer</AccessControlMaxAgeSec>
         <OriginOverride>boolean</OriginOverride>
      </CorsConfig>
      <CustomHeadersConfig>
         <Items>
            <ResponseHeadersPolicyCustomHeader>
               <Header>string</Header>
               <Override>boolean</Override>
               <Value>string</Value>
            </ResponseHeadersPolicyCustomHeader>
         </Items>
         <Quantity>integer</Quantity>
      </CustomHeadersConfig>
      <Name>string</Name>
      <RemoveHeadersConfig>
         <Items>
            <ResponseHeadersPolicyRemoveHeader>
               <Header>string</Header>
            </ResponseHeadersPolicyRemoveHeader>
         </Items>
         <Quantity>integer</Quantity>
      </RemoveHeadersConfig>
      <SecurityHeadersConfig>
         <ContentSecurityPolicy>
            <ContentSecurityPolicy>string</ContentSecurityPolicy>
            <Override>boolean</Override>
         </ContentSecurityPolicy>
         <ContentTypeOptions>
            <Override>boolean</Override>
         </ContentTypeOptions>
         <FrameOptions>
            <FrameOption>string</FrameOption>
            <Override>boolean</Override>
         </FrameOptions>
         <ReferrerPolicy>
            <Override>boolean</Override>
            <ReferrerPolicy>string</ReferrerPolicy>
         </ReferrerPolicy>
         <StrictTransportSecurity>
            <AccessControlMaxAgeSec>integer</AccessControlMaxAgeSec>
            <IncludeSubdomains>boolean</IncludeSubdomains>
            <Override>boolean</Override>
            <Preload>boolean</Preload>
         </StrictTransportSecurity>
         <XSSProtection>
            <ModeBlock>boolean</ModeBlock>
            <Override>boolean</Override>
            <Protection>boolean</Protection>
            <ReportUri>string</ReportUri>
         </XSSProtection>
      </SecurityHeadersConfig>
      <ServerTimingHeadersConfig>
         <Enabled>boolean</Enabled>
         <SamplingRate>double</SamplingRate>
      </ServerTimingHeadersConfig>
   </ResponseHeadersPolicyConfig>
</ResponseHeadersPolicy>
```

## Response Elements
<a name="API_UpdateResponseHeadersPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ResponseHeadersPolicy](#API_UpdateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-response-ResponseHeadersPolicy"></a>
Root level tag for the ResponseHeadersPolicy parameters.  
Required: Yes

 ** [Id](#API_UpdateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-response-Id"></a>
The identifier for the response headers policy.  
Type: String

 ** [LastModifiedTime](#API_UpdateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-response-LastModifiedTime"></a>
The date and time when the response headers policy was last modified.  
Type: Timestamp

 ** [ResponseHeadersPolicyConfig](#API_UpdateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateResponseHeadersPolicy-response-ResponseHeadersPolicyConfig"></a>
A response headers policy configuration.  
Type: [ResponseHeadersPolicyConfig](API_ResponseHeadersPolicyConfig.md) object

## Errors
<a name="API_UpdateResponseHeadersPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

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

 ** NoSuchResponseHeadersPolicy **   
The response headers policy does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** ResponseHeadersPolicyAlreadyExists **   
A response headers policy with this name already exists. You must provide a unique name. To modify an existing response headers policy, use `UpdateResponseHeadersPolicy`.  
HTTP Status Code: 409

 ** TooLongCSPInResponseHeadersPolicy **   
The length of the `Content-Security-Policy` header value in the response headers policy exceeds the maximum.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyCustomHeadersInResponseHeadersPolicy **   
The number of custom headers in the response headers policy exceeds the maximum.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyRemoveHeadersInResponseHeadersPolicy **   
The number of headers in `RemoveHeadersConfig` in the response headers policy exceeds the maximum.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateResponseHeadersPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateResponseHeadersPolicy) 