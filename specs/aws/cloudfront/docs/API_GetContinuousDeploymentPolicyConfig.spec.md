---
id: "@specs/aws/cloudfront/docs/API_GetContinuousDeploymentPolicyConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetContinuousDeploymentPolicyConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetContinuousDeploymentPolicyConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetContinuousDeploymentPolicyConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetContinuousDeploymentPolicyConfig
<a name="API_GetContinuousDeploymentPolicyConfig"></a>

Gets configuration information about a continuous deployment policy.

## Request Syntax
<a name="API_GetContinuousDeploymentPolicyConfig_RequestSyntax"></a>

```
GET /2020-05-31/continuous-deployment-policy/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetContinuousDeploymentPolicyConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetContinuousDeploymentPolicyConfig_RequestSyntax) **   <a name="cloudfront-GetContinuousDeploymentPolicyConfig-request-uri-Id"></a>
The identifier of the continuous deployment policy whose configuration you are getting.  
Required: Yes

## Request Body
<a name="API_GetContinuousDeploymentPolicyConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetContinuousDeploymentPolicyConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ContinuousDeploymentPolicyConfig>
   <Enabled>boolean</Enabled>
   <StagingDistributionDnsNames>
      <Items>
         <DnsName>string</DnsName>
      </Items>
      <Quantity>integer</Quantity>
   </StagingDistributionDnsNames>
   <TrafficConfig>
      <SingleHeaderConfig>
         <Header>string</Header>
         <Value>string</Value>
      </SingleHeaderConfig>
      <SingleWeightConfig>
         <SessionStickinessConfig>
            <IdleTTL>integer</IdleTTL>
            <MaximumTTL>integer</MaximumTTL>
         </SessionStickinessConfig>
         <Weight>float</Weight>
      </SingleWeightConfig>
      <Type>string</Type>
   </TrafficConfig>
</ContinuousDeploymentPolicyConfig>
```

## Response Elements
<a name="API_GetContinuousDeploymentPolicyConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ContinuousDeploymentPolicyConfig](#API_GetContinuousDeploymentPolicyConfig_ResponseSyntax) **   <a name="cloudfront-GetContinuousDeploymentPolicyConfig-response-ContinuousDeploymentPolicyConfig"></a>
Root level tag for the ContinuousDeploymentPolicyConfig parameters.  
Required: Yes

 ** [Enabled](#API_GetContinuousDeploymentPolicyConfig_ResponseSyntax) **   <a name="cloudfront-GetContinuousDeploymentPolicyConfig-response-Enabled"></a>
A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is `true`, this policy is enabled and in effect. When this value is `false`, this policy is not enabled and has no effect.  
Type: Boolean

 ** [StagingDistributionDnsNames](#API_GetContinuousDeploymentPolicyConfig_ResponseSyntax) **   <a name="cloudfront-GetContinuousDeploymentPolicyConfig-response-StagingDistributionDnsNames"></a>
The CloudFront domain name of the staging distribution. For example: `d111111abcdef8.cloudfront.net`.  
Type: [StagingDistributionDnsNames](API_StagingDistributionDnsNames.md) object

 ** [TrafficConfig](#API_GetContinuousDeploymentPolicyConfig_ResponseSyntax) **   <a name="cloudfront-GetContinuousDeploymentPolicyConfig-response-TrafficConfig"></a>
Contains the parameters for routing production traffic from your primary to staging distributions.  
Type: [TrafficConfig](API_TrafficConfig.md) object

## Errors
<a name="API_GetContinuousDeploymentPolicyConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchContinuousDeploymentPolicy **   
The continuous deployment policy doesn't exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetContinuousDeploymentPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicyConfig) 