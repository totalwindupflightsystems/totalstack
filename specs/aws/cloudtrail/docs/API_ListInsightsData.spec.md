---
id: "@specs/aws/cloudtrail/docs/API_ListInsightsData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInsightsData"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListInsightsData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListInsightsData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInsightsData
<a name="API_ListInsightsData"></a>

Returns Insights events generated on a trail that logs data events. You can list Insights events that occurred in a Region within the last 90 days.

ListInsightsData supports the following Dimensions for Insights events:
+ Event ID
+ Event name
+ Event source

All dimensions are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.

The rate of ListInsightsData requests is limited to two per second, per account, per Region. If this limit is exceeded, a throttling error occurs.

**Note**  
For data event Insights on organization trails, only the management account and delegated administrator accounts can call `ListInsightsData`. For these callers, the API returns Insights events only for the caller's own account. Member accounts cannot call this API on organization trails.

## Request Syntax
<a name="API_ListInsightsData_RequestSyntax"></a>

```
{
   "DataType": "{{string}}",
   "Dimensions": { 
      "{{string}}" : "{{string}}" 
   },
   "EndTime": {{number}},
   "InsightSource": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_ListInsightsData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataType](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-DataType"></a>
Specifies the category of events returned. To fetch Insights events, specify `InsightsEvents` as the value of `DataType`   
Type: String  
Valid Values: `InsightsEvents`   
Required: Yes

 ** [Dimensions](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-Dimensions"></a>
Contains a map of dimensions. Currently the map can contain only one item.  
Type: String to string map  
Map Entries: Maximum number of 1 item.  
Valid Keys: `EventId | EventName | EventSource`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [EndTime](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-EndTime"></a>
Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.  
Type: Timestamp  
Required: No

 ** [InsightSource](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-InsightSource"></a>
The Amazon Resource Name(ARN) of the trail for which you want to retrieve Insights events.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [MaxResults](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-MaxResults"></a>
The number of events to return. Possible values are 1 through 50. The default is 50.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [NextToken](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-NextToken"></a>
The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified a EventName as a dimension with `PutObject` as a value, the call with NextToken should include those same parameters.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** [StartTime](#API_ListInsightsData_RequestSyntax) **   <a name="awscloudtrail-ListInsightsData-request-StartTime"></a>
Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.  
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_ListInsightsData_ResponseSyntax"></a>

```
{
   "Events": [ 
      { 
         "AccessKeyId": "string",
         "CloudTrailEvent": "string",
         "EventId": "string",
         "EventName": "string",
         "EventSource": "string",
         "EventTime": number,
         "ReadOnly": "string",
         "Resources": [ 
            { 
               "ResourceName": "string",
               "ResourceType": "string"
            }
         ],
         "Username": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInsightsData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_ListInsightsData_ResponseSyntax) **   <a name="awscloudtrail-ListInsightsData-response-Events"></a>
A list of events returned based on the InsightSource, DataType or Dimensions specified. The events list is sorted by time. The most recent event is listed first.  
Type: Array of [Event](API_Event.md) objects

 ** [NextToken](#API_ListInsightsData_ResponseSyntax) **   <a name="awscloudtrail-ListInsightsData-response-NextToken"></a>
The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified a EventName as a dimension with `PutObject` as a value, the call with NextToken should include those same parameters.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

## Errors
<a name="API_ListInsightsData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListInsightsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListInsightsData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListInsightsData) 