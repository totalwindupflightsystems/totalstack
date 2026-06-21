---
id: "@specs/aws/cloudfront/docs/API_ListContinuousDeploymentPolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListContinuousDeploymentPolicies"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListContinuousDeploymentPolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListContinuousDeploymentPolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListContinuousDeploymentPolicies
<a name="API_ListContinuousDeploymentPolicies"></a>

Gets a list of the continuous deployment policies in your AWS account.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListContinuousDeploymentPolicies_RequestSyntax"></a>

```
GET /2020-05-31/continuous-deployment-policy?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContinuousDeploymentPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListContinuousDeploymentPolicies_RequestSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListContinuousDeploymentPolicies_RequestSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-request-uri-MaxItems"></a>
The maximum number of continuous deployment policies that you want returned in the response.

## Request Body
<a name="API_ListContinuousDeploymentPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContinuousDeploymentPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ContinuousDeploymentPolicyList>
   <Items>
      <ContinuousDeploymentPolicySummary>
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
      </ContinuousDeploymentPolicySummary>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</ContinuousDeploymentPolicyList>
```

## Response Elements
<a name="API_ListContinuousDeploymentPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ContinuousDeploymentPolicyList](#API_ListContinuousDeploymentPolicies_ResponseSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-response-ContinuousDeploymentPolicyList"></a>
Root level tag for the ContinuousDeploymentPolicyList parameters.  
Required: Yes

 ** [Items](#API_ListContinuousDeploymentPolicies_ResponseSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-response-Items"></a>
A list of continuous deployment policy items.  
Type: Array of [ContinuousDeploymentPolicySummary](API_ContinuousDeploymentPolicySummary.md) objects

 ** [MaxItems](#API_ListContinuousDeploymentPolicies_ResponseSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-response-MaxItems"></a>
The maximum number of continuous deployment policies that were specified in your request.  
Type: Integer

 ** [NextMarker](#API_ListContinuousDeploymentPolicies_ResponseSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-response-NextMarker"></a>
Indicates the next page of continuous deployment policies. To get the next page of the list, use this value in the `Marker` field of your request.  
Type: String

 ** [Quantity](#API_ListContinuousDeploymentPolicies_ResponseSyntax) **   <a name="cloudfront-ListContinuousDeploymentPolicies-response-Quantity"></a>
The total number of continuous deployment policies in your AWS account, regardless of the `MaxItems` value.  
Type: Integer

## Errors
<a name="API_ListContinuousDeploymentPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchContinuousDeploymentPolicy **   
The continuous deployment policy doesn't exist.  
HTTP Status Code: 404

## See Also
<a name="API_ListContinuousDeploymentPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListContinuousDeploymentPolicies) 