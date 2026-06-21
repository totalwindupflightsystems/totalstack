---
id: "@specs/aws/cloudfront/docs/API_GetMonitoringSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMonitoringSubscription"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetMonitoringSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetMonitoringSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMonitoringSubscription
<a name="API_GetMonitoringSubscription"></a>

Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.

## Request Syntax
<a name="API_GetMonitoringSubscription_RequestSyntax"></a>

```
GET /2020-05-31/distributions/{{DistributionId}}/monitoring-subscription HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMonitoringSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DistributionId](#API_GetMonitoringSubscription_RequestSyntax) **   <a name="cloudfront-GetMonitoringSubscription-request-uri-DistributionId"></a>
The ID of the distribution that you are getting metrics information for.  
Required: Yes

## Request Body
<a name="API_GetMonitoringSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMonitoringSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<MonitoringSubscription>
   <RealtimeMetricsSubscriptionConfig>
      <RealtimeMetricsSubscriptionStatus>string</RealtimeMetricsSubscriptionStatus>
   </RealtimeMetricsSubscriptionConfig>
</MonitoringSubscription>
```

## Response Elements
<a name="API_GetMonitoringSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [MonitoringSubscription](#API_GetMonitoringSubscription_ResponseSyntax) **   <a name="cloudfront-GetMonitoringSubscription-response-MonitoringSubscription"></a>
Root level tag for the MonitoringSubscription parameters.  
Required: Yes

 ** [RealtimeMetricsSubscriptionConfig](#API_GetMonitoringSubscription_ResponseSyntax) **   <a name="cloudfront-GetMonitoringSubscription-response-RealtimeMetricsSubscriptionConfig"></a>
A subscription configuration for additional CloudWatch metrics.  
Type: [RealtimeMetricsSubscriptionConfig](API_RealtimeMetricsSubscriptionConfig.md) object

## Errors
<a name="API_GetMonitoringSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

 ** NoSuchMonitoringSubscription **   
A monitoring subscription does not exist for the specified distribution.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_GetMonitoringSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetMonitoringSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetMonitoringSubscription) 