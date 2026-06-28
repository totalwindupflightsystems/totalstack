---
id: "@specs/aws/network-firewall/docs/API_GetAnalysisReportResults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAnalysisReportResults"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# GetAnalysisReportResults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_GetAnalysisReportResults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAnalysisReportResults
<a name="API_GetAnalysisReportResults"></a>

The results of a `COMPLETED` analysis report generated with [StartAnalysisReport](API_StartAnalysisReport.md).

For more information, see [AnalysisTypeReportResult](API_AnalysisTypeReportResult.md). 

## Request Syntax
<a name="API_GetAnalysisReportResults_RequestSyntax"></a>

```
{
   "AnalysisReportId": "{{string}}",
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAnalysisReportResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalysisReportId](#API_GetAnalysisReportResults_RequestSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-request-AnalysisReportId"></a>
The unique ID of the query that ran when you requested an analysis report.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `\S+`   
Required: Yes

 ** [FirewallArn](#API_GetAnalysisReportResults_RequestSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_GetAnalysisReportResults_RequestSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [MaxResults](#API_GetAnalysisReportResults_RequestSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_GetAnalysisReportResults_RequestSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## Response Syntax
<a name="API_GetAnalysisReportResults_ResponseSyntax"></a>

```
{
   "AnalysisReportResults": [ 
      { 
         "Domain": "string",
         "FirstAccessed": number,
         "Hits": { 
            "Count": number
         },
         "LastAccessed": number,
         "Protocol": "string",
         "UniqueSources": { 
            "Count": number
         }
      }
   ],
   "AnalysisType": "string",
   "EndTime": number,
   "NextToken": "string",
   "ReportTime": number,
   "StartTime": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetAnalysisReportResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisReportResults](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-AnalysisReportResults"></a>
Retrieves the results of a traffic analysis report.  
Type: Array of [AnalysisTypeReportResult](API_AnalysisTypeReportResult.md) objects

 ** [AnalysisType](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-AnalysisType"></a>
The type of traffic that will be used to generate a report.   
Type: String  
Valid Values: `TLS_SNI | HTTP_HOST` 

 ** [EndTime](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-EndTime"></a>
The date and time, up to the current date, from which to stop retrieving analysis data, in UTC format (for example, `YYYY-MM-DDTHH:MM:SSZ`).   
Type: Timestamp

 ** [NextToken](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ReportTime](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-ReportTime"></a>
The date and time the analysis report was ran.   
Type: Timestamp

 ** [StartTime](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-StartTime"></a>
 The date and time within the last 30 days from which to start retrieving analysis data, in UTC format (for example, `YYYY-MM-DDTHH:MM:SSZ`.   
Type: Timestamp

 ** [Status](#API_GetAnalysisReportResults_ResponseSyntax) **   <a name="networkfirewall-GetAnalysisReportResults-response-Status"></a>
The status of the analysis report you specify. Statuses include `RUNNING`, `COMPLETED`, or `FAILED`.  
Type: String

## Errors
<a name="API_GetAnalysisReportResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_GetAnalysisReportResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/GetAnalysisReportResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/GetAnalysisReportResults) 