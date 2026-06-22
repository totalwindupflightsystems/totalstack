---
id: "@specs/aws/sesv2/docs/API_GetDeliverabilityTestReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDeliverabilityTestReport"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetDeliverabilityTestReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetDeliverabilityTestReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDeliverabilityTestReport
<a name="API_GetDeliverabilityTestReport"></a>

Retrieve the results of a predictive inbox placement test.

## Request Syntax
<a name="API_GetDeliverabilityTestReport_RequestSyntax"></a>

```
GET /v2/email/deliverability-dashboard/test-reports/{{ReportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeliverabilityTestReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ReportId](#API_GetDeliverabilityTestReport_RequestSyntax) **   <a name="SES-GetDeliverabilityTestReport-request-uri-ReportId"></a>
A unique string that identifies the predictive inbox placement test.  
Required: Yes

## Request Body
<a name="API_GetDeliverabilityTestReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeliverabilityTestReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeliverabilityTestReport": { 
      "CreateDate": number,
      "DeliverabilityTestStatus": "string",
      "FromEmailAddress": "string",
      "ReportId": "string",
      "ReportName": "string",
      "Subject": "string"
   },
   "IspPlacements": [ 
      { 
         "IspName": "string",
         "PlacementStatistics": { 
            "DkimPercentage": number,
            "InboxPercentage": number,
            "MissingPercentage": number,
            "SpamPercentage": number,
            "SpfPercentage": number
         }
      }
   ],
   "Message": "string",
   "OverallPlacement": { 
      "DkimPercentage": number,
      "InboxPercentage": number,
      "MissingPercentage": number,
      "SpamPercentage": number,
      "SpfPercentage": number
   },
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetDeliverabilityTestReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliverabilityTestReport](#API_GetDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-GetDeliverabilityTestReport-response-DeliverabilityTestReport"></a>
An object that contains the results of the predictive inbox placement test.  
Type: [DeliverabilityTestReport](API_DeliverabilityTestReport.md) object

 ** [IspPlacements](#API_GetDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-GetDeliverabilityTestReport-response-IspPlacements"></a>
An object that describes how the test email was handled by several email providers, including Gmail, Hotmail, Yahoo, AOL, and others.  
Type: Array of [IspPlacement](API_IspPlacement.md) objects

 ** [Message](#API_GetDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-GetDeliverabilityTestReport-response-Message"></a>
An object that contains the message that you sent when you performed this predictive inbox placement test.  
Type: String

 ** [OverallPlacement](#API_GetDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-GetDeliverabilityTestReport-response-OverallPlacement"></a>
An object that specifies how many test messages that were sent during the predictive inbox placement test were delivered to recipients' inboxes, how many were sent to recipients' spam folders, and how many weren't delivered.  
Type: [PlacementStatistics](API_PlacementStatistics.md) object

 ** [Tags](#API_GetDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-GetDeliverabilityTestReport-response-Tags"></a>
An array of objects that define the tags (keys and values) that are associated with the predictive inbox placement test.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_GetDeliverabilityTestReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetDeliverabilityTestReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetDeliverabilityTestReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetDeliverabilityTestReport) 