---
id: "@specs/aws/sesv2/docs/API_GetDomainStatisticsReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDomainStatisticsReport"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetDomainStatisticsReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetDomainStatisticsReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDomainStatisticsReport
<a name="API_GetDomainStatisticsReport"></a>

Retrieve inbox placement and engagement rates for the domains that you use to send email.

## Request Syntax
<a name="API_GetDomainStatisticsReport_RequestSyntax"></a>

```
GET /v2/email/deliverability-dashboard/statistics-report/{{Domain}}?EndDate={{EndDate}}&StartDate={{StartDate}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainStatisticsReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Domain](#API_GetDomainStatisticsReport_RequestSyntax) **   <a name="SES-GetDomainStatisticsReport-request-uri-Domain"></a>
The domain that you want to obtain deliverability metrics for.  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [EndDate](#API_GetDomainStatisticsReport_RequestSyntax) **   <a name="SES-GetDomainStatisticsReport-request-uri-EndDate"></a>
The last day (in Unix time) that you want to obtain domain deliverability metrics for. The `EndDate` that you specify has to be less than or equal to 30 days after the `StartDate`.  
Required: Yes

 ** [StartDate](#API_GetDomainStatisticsReport_RequestSyntax) **   <a name="SES-GetDomainStatisticsReport-request-uri-StartDate"></a>
The first day (in Unix time) that you want to obtain domain deliverability metrics for.  
Required: Yes

## Request Body
<a name="API_GetDomainStatisticsReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainStatisticsReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DailyVolumes": [ 
      { 
         "DomainIspPlacements": [ 
            { 
               "InboxPercentage": number,
               "InboxRawCount": number,
               "IspName": "string",
               "SpamPercentage": number,
               "SpamRawCount": number
            }
         ],
         "StartDate": number,
         "VolumeStatistics": { 
            "InboxRawCount": number,
            "ProjectedInbox": number,
            "ProjectedSpam": number,
            "SpamRawCount": number
         }
      }
   ],
   "OverallVolume": { 
      "DomainIspPlacements": [ 
         { 
            "InboxPercentage": number,
            "InboxRawCount": number,
            "IspName": "string",
            "SpamPercentage": number,
            "SpamRawCount": number
         }
      ],
      "ReadRatePercent": number,
      "VolumeStatistics": { 
         "InboxRawCount": number,
         "ProjectedInbox": number,
         "ProjectedSpam": number,
         "SpamRawCount": number
      }
   }
}
```

## Response Elements
<a name="API_GetDomainStatisticsReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DailyVolumes](#API_GetDomainStatisticsReport_ResponseSyntax) **   <a name="SES-GetDomainStatisticsReport-response-DailyVolumes"></a>
An object that contains deliverability metrics for the domain that you specified. This object contains data for each day, starting on the `StartDate` and ending on the `EndDate`.  
Type: Array of [DailyVolume](API_DailyVolume.md) objects

 ** [OverallVolume](#API_GetDomainStatisticsReport_ResponseSyntax) **   <a name="SES-GetDomainStatisticsReport-response-OverallVolume"></a>
An object that contains deliverability metrics for the domain that you specified. The data in this object is a summary of all of the data that was collected from the `StartDate` to the `EndDate`.  
Type: [OverallVolume](API_OverallVolume.md) object

## Errors
<a name="API_GetDomainStatisticsReport_Errors"></a>

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
<a name="API_GetDomainStatisticsReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetDomainStatisticsReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetDomainStatisticsReport) 