---
id: "@specs/aws/sesv2/docs/API_PutDeliverabilityDashboardOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutDeliverabilityDashboardOption"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutDeliverabilityDashboardOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutDeliverabilityDashboardOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutDeliverabilityDashboardOption
<a name="API_PutDeliverabilityDashboardOption"></a>

Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.

When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other AWS services. For more information about the features and cost of a Deliverability dashboard subscription, see [Amazon SES Pricing](http://aws.amazon.com/ses/pricing/).

## Request Syntax
<a name="API_PutDeliverabilityDashboardOption_RequestSyntax"></a>

```
PUT /v2/email/deliverability-dashboard HTTP/1.1
Content-type: application/json

{
   "DashboardEnabled": {{boolean}},
   "SubscribedDomains": [ 
      { 
         "Domain": "{{string}}",
         "InboxPlacementTrackingOption": { 
            "Global": {{boolean}},
            "TrackedIsps": [ "{{string}}" ]
         },
         "SubscriptionStartDate": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutDeliverabilityDashboardOption_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDeliverabilityDashboardOption_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DashboardEnabled](#API_PutDeliverabilityDashboardOption_RequestSyntax) **   <a name="SES-PutDeliverabilityDashboardOption-request-DashboardEnabled"></a>
Specifies whether to enable the Deliverability dashboard. To enable the dashboard, set this value to `true`.  
Type: Boolean  
Required: Yes

 ** [SubscribedDomains](#API_PutDeliverabilityDashboardOption_RequestSyntax) **   <a name="SES-PutDeliverabilityDashboardOption-request-SubscribedDomains"></a>
An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.  
Type: Array of [DomainDeliverabilityTrackingOption](API_DomainDeliverabilityTrackingOption.md) objects  
Required: No

## Response Syntax
<a name="API_PutDeliverabilityDashboardOption_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutDeliverabilityDashboardOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDeliverabilityDashboardOption_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutDeliverabilityDashboardOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutDeliverabilityDashboardOption) 