---
id: "@specs/aws/sesv2/docs/API_GetDeliverabilityDashboardOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDeliverabilityDashboardOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetDeliverabilityDashboardOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetDeliverabilityDashboardOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDeliverabilityDashboardOptions
<a name="API_GetDeliverabilityDashboardOptions"></a>

Retrieve information about the status of the Deliverability dashboard for your account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.

When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other AWS services. For more information about the features and cost of a Deliverability dashboard subscription, see [Amazon SES Pricing](http://aws.amazon.com/ses/pricing/).

## Request Syntax
<a name="API_GetDeliverabilityDashboardOptions_RequestSyntax"></a>

```
GET /v2/email/deliverability-dashboard HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeliverabilityDashboardOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDeliverabilityDashboardOptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeliverabilityDashboardOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountStatus": "string",
   "ActiveSubscribedDomains": [ 
      { 
         "Domain": "string",
         "InboxPlacementTrackingOption": { 
            "Global": boolean,
            "TrackedIsps": [ "string" ]
         },
         "SubscriptionStartDate": number
      }
   ],
   "DashboardEnabled": boolean,
   "PendingExpirationSubscribedDomains": [ 
      { 
         "Domain": "string",
         "InboxPlacementTrackingOption": { 
            "Global": boolean,
            "TrackedIsps": [ "string" ]
         },
         "SubscriptionStartDate": number
      }
   ],
   "SubscriptionExpiryDate": number
}
```

## Response Elements
<a name="API_GetDeliverabilityDashboardOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountStatus](#API_GetDeliverabilityDashboardOptions_ResponseSyntax) **   <a name="SES-GetDeliverabilityDashboardOptions-response-AccountStatus"></a>
The current status of your Deliverability dashboard subscription. If this value is `PENDING_EXPIRATION`, your subscription is scheduled to expire at the end of the current calendar month.  
Type: String  
Valid Values: `ACTIVE | PENDING_EXPIRATION | DISABLED` 

 ** [ActiveSubscribedDomains](#API_GetDeliverabilityDashboardOptions_ResponseSyntax) **   <a name="SES-GetDeliverabilityDashboardOptions-response-ActiveSubscribedDomains"></a>
An array of objects, one for each verified domain that you use to send email and currently has an active Deliverability dashboard subscription that isn’t scheduled to expire at the end of the current calendar month.  
Type: Array of [DomainDeliverabilityTrackingOption](API_DomainDeliverabilityTrackingOption.md) objects

 ** [DashboardEnabled](#API_GetDeliverabilityDashboardOptions_ResponseSyntax) **   <a name="SES-GetDeliverabilityDashboardOptions-response-DashboardEnabled"></a>
Specifies whether the Deliverability dashboard is enabled. If this value is `true`, the dashboard is enabled.  
Type: Boolean

 ** [PendingExpirationSubscribedDomains](#API_GetDeliverabilityDashboardOptions_ResponseSyntax) **   <a name="SES-GetDeliverabilityDashboardOptions-response-PendingExpirationSubscribedDomains"></a>
An array of objects, one for each verified domain that you use to send email and currently has an active Deliverability dashboard subscription that's scheduled to expire at the end of the current calendar month.  
Type: Array of [DomainDeliverabilityTrackingOption](API_DomainDeliverabilityTrackingOption.md) objects

 ** [SubscriptionExpiryDate](#API_GetDeliverabilityDashboardOptions_ResponseSyntax) **   <a name="SES-GetDeliverabilityDashboardOptions-response-SubscriptionExpiryDate"></a>
The date when your current subscription to the Deliverability dashboard is scheduled to expire, if your subscription is scheduled to expire at the end of the current calendar month. This value is null if you have an active subscription that isn’t due to expire at the end of the month.  
Type: Timestamp

## Errors
<a name="API_GetDeliverabilityDashboardOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetDeliverabilityDashboardOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetDeliverabilityDashboardOptions) 