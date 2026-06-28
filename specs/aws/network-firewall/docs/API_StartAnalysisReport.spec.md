---
id: "@specs/aws/network-firewall/docs/API_StartAnalysisReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAnalysisReport"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StartAnalysisReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StartAnalysisReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAnalysisReport
<a name="API_StartAnalysisReport"></a>

Generates a traffic analysis report for the timeframe and traffic type you specify.

For information on the contents of a traffic analysis report, see [AnalysisReport](API_AnalysisReport.md).

## Request Syntax
<a name="API_StartAnalysisReport_RequestSyntax"></a>

```
{
   "AnalysisType": "{{string}}",
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartAnalysisReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalysisType](#API_StartAnalysisReport_RequestSyntax) **   <a name="networkfirewall-StartAnalysisReport-request-AnalysisType"></a>
The type of traffic that will be used to generate a report.   
Type: String  
Valid Values: `TLS_SNI | HTTP_HOST`   
Required: Yes

 ** [FirewallArn](#API_StartAnalysisReport_RequestSyntax) **   <a name="networkfirewall-StartAnalysisReport-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_StartAnalysisReport_RequestSyntax) **   <a name="networkfirewall-StartAnalysisReport-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_StartAnalysisReport_ResponseSyntax"></a>

```
{
   "AnalysisReportId": "string"
}
```

## Response Elements
<a name="API_StartAnalysisReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisReportId](#API_StartAnalysisReport_ResponseSyntax) **   <a name="networkfirewall-StartAnalysisReport-response-AnalysisReportId"></a>
The unique ID of the query that ran when you requested an analysis report.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `\S+` 

## Errors
<a name="API_StartAnalysisReport_Errors"></a>

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
<a name="API_StartAnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/StartAnalysisReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StartAnalysisReport) 