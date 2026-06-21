---
id: "@specs/aws/cloudfront/docs/API_UpdateContinuousDeploymentPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateContinuousDeploymentPolicy"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateContinuousDeploymentPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateContinuousDeploymentPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateContinuousDeploymentPolicy
<a name="API_UpdateContinuousDeploymentPolicy"></a>

Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.

When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:

1. Use `GetContinuousDeploymentPolicyConfig` to get the current configuration.

1. Locally modify the fields in the continuous deployment policy configuration that you want to update.

1. Use `UpdateContinuousDeploymentPolicy`, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn't.

## Request Syntax
<a name="API_UpdateContinuousDeploymentPolicy_RequestSyntax"></a>

```
PUT /2020-05-31/continuous-deployment-policy/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ContinuousDeploymentPolicyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Enabled>{{boolean}}</Enabled>
   <StagingDistributionDnsNames>
      <Items>
         <DnsName>{{string}}</DnsName>
      </Items>
      <Quantity>{{integer}}</Quantity>
   </StagingDistributionDnsNames>
   <TrafficConfig>
      <SingleHeaderConfig>
         <Header>{{string}}</Header>
         <Value>{{string}}</Value>
      </SingleHeaderConfig>
      <SingleWeightConfig>
         <SessionStickinessConfig>
            <IdleTTL>{{integer}}</IdleTTL>
            <MaximumTTL>{{integer}}</MaximumTTL>
         </SessionStickinessConfig>
         <Weight>{{float}}</Weight>
      </SingleWeightConfig>
      <Type>{{string}}</Type>
   </TrafficConfig>
</ContinuousDeploymentPolicyConfig>
```

## URI Request Parameters
<a name="API_UpdateContinuousDeploymentPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateContinuousDeploymentPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ContinuousDeploymentPolicyConfig](#API_UpdateContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-request-ContinuousDeploymentPolicyConfig"></a>
Root level tag for the ContinuousDeploymentPolicyConfig parameters.  
Required: Yes

 ** [Enabled](#API_UpdateContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-request-Enabled"></a>
A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is `true`, this policy is enabled and in effect. When this value is `false`, this policy is not enabled and has no effect.  
Type: Boolean  
Required: Yes

 ** [StagingDistributionDnsNames](#API_UpdateContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-request-StagingDistributionDnsNames"></a>
The CloudFront domain name of the staging distribution. For example: `d111111abcdef8.cloudfront.net`.  
Type: [StagingDistributionDnsNames](API_StagingDistributionDnsNames.md) object  
Required: Yes

 ** [TrafficConfig](#API_UpdateContinuousDeploymentPolicy_RequestSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-request-TrafficConfig"></a>
Contains the parameters for routing production traffic from your primary to staging distributions.  
Type: [TrafficConfig](API_TrafficConfig.md) object  
Required: No

## Response Syntax
<a name="API_UpdateContinuousDeploymentPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ContinuousDeploymentPolicy>
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
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
</ContinuousDeploymentPolicy>
```

## Response Elements
<a name="API_UpdateContinuousDeploymentPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ContinuousDeploymentPolicy](#API_UpdateContinuousDeploymentPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-response-ContinuousDeploymentPolicy"></a>
Root level tag for the ContinuousDeploymentPolicy parameters.  
Required: Yes

 ** [ContinuousDeploymentPolicyConfig](#API_UpdateContinuousDeploymentPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-response-ContinuousDeploymentPolicyConfig"></a>
Contains the configuration for a continuous deployment policy.  
Type: [ContinuousDeploymentPolicyConfig](API_ContinuousDeploymentPolicyConfig.md) object

 ** [Id](#API_UpdateContinuousDeploymentPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-response-Id"></a>
The identifier of the continuous deployment policy.  
Type: String

 ** [LastModifiedTime](#API_UpdateContinuousDeploymentPolicy_ResponseSyntax) **   <a name="cloudfront-UpdateContinuousDeploymentPolicy-response-LastModifiedTime"></a>
The date and time the continuous deployment policy was last modified.  
Type: Timestamp

## Errors
<a name="API_UpdateContinuousDeploymentPolicy_Errors"></a>

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

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchContinuousDeploymentPolicy **   
The continuous deployment policy doesn't exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** StagingDistributionInUse **   
A continuous deployment policy for this staging distribution already exists.  
HTTP Status Code: 409

## See Also
<a name="API_UpdateContinuousDeploymentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateContinuousDeploymentPolicy) 