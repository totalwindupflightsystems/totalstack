---
id: "@specs/aws/cloudfront/docs/API_CreateResponseHeadersPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateResponseHeadersPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateResponseHeadersPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateResponseHeadersPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateResponseHeadersPolicy
<a name="API_CreateResponseHeadersPolicy"></a>

Creates a response headers policy.

A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.

After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.

For more information, see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_CreateResponseHeadersPolicy_RequestSyntax"></a>

```
POST /2020-05-31/response-headers-policy HTTP/1.1
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
<a name="API_CreateResponseHeadersPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResponseHeadersPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ResponseHeadersPolicyConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-ResponseHeadersPolicyConfig"></a>
Root level tag for the ResponseHeadersPolicyConfig parameters.  
Required: Yes

 ** [Comment](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-Comment"></a>
A comment to describe the response headers policy.  
The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [CorsConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-CorsConfig"></a>
A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).  
Type: [ResponseHeadersPolicyCorsConfig](API_ResponseHeadersPolicyCorsConfig.md) object  
Required: No

 ** [CustomHeadersConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-CustomHeadersConfig"></a>
A configuration for a set of custom HTTP response headers.  
Type: [ResponseHeadersPolicyCustomHeadersConfig](API_ResponseHeadersPolicyCustomHeadersConfig.md) object  
Required: No

 ** [Name](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-Name"></a>
A name to identify the response headers policy.  
The name must be unique for response headers policies in this AWS account.  
Type: String  
Required: Yes

 ** [RemoveHeadersConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-RemoveHeadersConfig"></a>
A configuration for a set of HTTP headers to remove from the HTTP response.  
Type: [ResponseHeadersPolicyRemoveHeadersConfig](API_ResponseHeadersPolicyRemoveHeadersConfig.md) object  
Required: No

 ** [SecurityHeadersConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-SecurityHeadersConfig"></a>
A configuration for a set of security-related HTTP response headers.  
Type: [ResponseHeadersPolicySecurityHeadersConfig](API_ResponseHeadersPolicySecurityHeadersConfig.md) object  
Required: No

 ** [ServerTimingHeadersConfig](#API_CreateResponseHeadersPolicy_RequestSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-request-ServerTimingHeadersConfig"></a>
A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront.  
Type: [ResponseHeadersPolicyServerTimingHeadersConfig](API_ResponseHeadersPolicyServerTimingHeadersConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateResponseHeadersPolicy_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateResponseHeadersPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [ResponseHeadersPolicy](#API_CreateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-response-ResponseHeadersPolicy"></a>
Root level tag for the ResponseHeadersPolicy parameters.  
Required: Yes

 ** [Id](#API_CreateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-response-Id"></a>
The identifier for the response headers policy.  
Type: String

 ** [LastModifiedTime](#API_CreateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-response-LastModifiedTime"></a>
The date and time when the response headers policy was last modified.  
Type: Timestamp

 ** [ResponseHeadersPolicyConfig](#API_CreateResponseHeadersPolicy_ResponseSyntax) **   <a name="cloudfront-CreateResponseHeadersPolicy-response-ResponseHeadersPolicyConfig"></a>
A response headers policy configuration.  
Type: [ResponseHeadersPolicyConfig](API_ResponseHeadersPolicyConfig.md) object

## Errors
<a name="API_CreateResponseHeadersPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

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

 ** TooManyResponseHeadersPolicies **   
You have reached the maximum number of response headers policies for this AWS account.  
For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

## See Also
<a name="API_CreateResponseHeadersPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateResponseHeadersPolicy) 