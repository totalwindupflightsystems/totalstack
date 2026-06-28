---
id: "@specs/aws/kendra/docs/API_GetSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSnapshots"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# GetSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_GetSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSnapshots
<a name="API_GetSnapshots"></a>

Retrieves search metrics data. The data provides a snapshot of how your users interact with your search application and how effective the application is.

## Request Syntax
<a name="API_GetSnapshots_RequestSyntax"></a>

```
{
   "IndexId": "{{string}}",
   "Interval": "{{string}}",
   "MaxResults": {{number}},
   "MetricType": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IndexId](#API_GetSnapshots_RequestSyntax) **   <a name="kendra-GetSnapshots-request-IndexId"></a>
The identifier of the index to get search metrics data.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [Interval](#API_GetSnapshots_RequestSyntax) **   <a name="kendra-GetSnapshots-request-Interval"></a>
The time interval or time window to get search metrics data. The time interval uses the time zone of your index. You can view data in the following time windows:  
+  `THIS_WEEK`: The current week, starting on the Sunday and ending on the day before the current date.
+  `ONE_WEEK_AGO`: The previous week, starting on the Sunday and ending on the following Saturday.
+  `TWO_WEEKS_AGO`: The week before the previous week, starting on the Sunday and ending on the following Saturday.
+  `THIS_MONTH`: The current month, starting on the first day of the month and ending on the day before the current date.
+  `ONE_MONTH_AGO`: The previous month, starting on the first day of the month and ending on the last day of the month.
+  `TWO_MONTHS_AGO`: The month before the previous month, starting on the first day of the month and ending on last day of the month.
Type: String  
Valid Values: `THIS_MONTH | THIS_WEEK | ONE_WEEK_AGO | TWO_WEEKS_AGO | ONE_MONTH_AGO | TWO_MONTHS_AGO`   
Required: Yes

 ** [MaxResults](#API_GetSnapshots_RequestSyntax) **   <a name="kendra-GetSnapshots-request-MaxResults"></a>
The maximum number of returned data for the metric.  
Type: Integer  
Required: No

 ** [MetricType](#API_GetSnapshots_RequestSyntax) **   <a name="kendra-GetSnapshots-request-MetricType"></a>
The metric you want to retrieve. You can specify only one metric per call.  
For more information about the metrics you can view, see [Gaining insights with search analytics](https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html).  
Type: String  
Valid Values: `QUERIES_BY_COUNT | QUERIES_BY_ZERO_CLICK_RATE | QUERIES_BY_ZERO_RESULT_RATE | DOCS_BY_CLICK_COUNT | AGG_QUERY_DOC_METRICS | TREND_QUERY_DOC_METRICS`   
Required: Yes

 ** [NextToken](#API_GetSnapshots_RequestSyntax) **   <a name="kendra-GetSnapshots-request-NextToken"></a>
If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of search metrics data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.  
Required: No

## Response Syntax
<a name="API_GetSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SnapshotsData": [ 
      [ "string" ]
   ],
   "SnapshotsDataHeader": [ "string" ],
   "SnapShotTimeFilter": { 
      "EndTime": number,
      "StartTime": number
   }
}
```

## Response Elements
<a name="API_GetSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSnapshots_ResponseSyntax) **   <a name="kendra-GetSnapshots-response-NextToken"></a>
If the response is truncated, Amazon Kendra returns this token, which you can use in a later request to retrieve the next set of search metrics data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [SnapshotsData](#API_GetSnapshots_ResponseSyntax) **   <a name="kendra-GetSnapshots-response-SnapshotsData"></a>
The search metrics data. The data returned depends on the metric type you requested.  
Type: Array of arrays of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SnapshotsDataHeader](#API_GetSnapshots_ResponseSyntax) **   <a name="kendra-GetSnapshots-response-SnapshotsDataHeader"></a>
The column headers for the search metrics data.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SnapShotTimeFilter](#API_GetSnapshots_ResponseSyntax) **   <a name="kendra-GetSnapshots-response-SnapShotTimeFilter"></a>
The Unix timestamp for the beginning and end of the time window for the search metrics data.  
Type: [TimeRange](API_TimeRange.md) object

## Errors
<a name="API_GetSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The input to the request is not valid. Please provide the correct input and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

## See Also
<a name="API_GetSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/GetSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/GetSnapshots) 