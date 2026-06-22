---
id: "@specs/aws/sesv2/docs/API_ListExportJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListExportJobs"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListExportJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListExportJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListExportJobs
<a name="API_ListExportJobs"></a>

Lists all of the export jobs.

## Request Syntax
<a name="API_ListExportJobs_RequestSyntax"></a>

```
POST /v2/email/list-export-jobs HTTP/1.1
Content-type: application/json

{
   "ExportSourceType": "{{string}}",
   "JobStatus": "{{string}}",
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListExportJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListExportJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExportSourceType](#API_ListExportJobs_RequestSyntax) **   <a name="SES-ListExportJobs-request-ExportSourceType"></a>
A value used to list export jobs that have a certain `ExportSourceType`.  
Type: String  
Valid Values: `METRICS_DATA | MESSAGE_INSIGHTS`   
Required: No

 ** [JobStatus](#API_ListExportJobs_RequestSyntax) **   <a name="SES-ListExportJobs-request-JobStatus"></a>
A value used to list export jobs that have a certain `JobStatus`.  
Type: String  
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | CANCELLED`   
Required: No

 ** [NextToken](#API_ListExportJobs_RequestSyntax) **   <a name="SES-ListExportJobs-request-NextToken"></a>
The pagination token returned from a previous call to `ListExportJobs` to indicate the position in the list of export jobs.  
Type: String  
Required: No

 ** [PageSize](#API_ListExportJobs_RequestSyntax) **   <a name="SES-ListExportJobs-request-PageSize"></a>
Maximum number of export jobs to return at once. Use this parameter to paginate results. If additional export jobs exist beyond the specified limit, the `NextToken` element is sent in the response. Use the `NextToken` value in subsequent calls to `ListExportJobs` to retrieve additional export jobs.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExportJobs": [ 
      { 
         "CompletedTimestamp": number,
         "CreatedTimestamp": number,
         "ExportSourceType": "string",
         "JobId": "string",
         "JobStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportJobs](#API_ListExportJobs_ResponseSyntax) **   <a name="SES-ListExportJobs-response-ExportJobs"></a>
A list of the export job summaries.  
Type: Array of [ExportJobSummary](API_ExportJobSummary.md) objects

 ** [NextToken](#API_ListExportJobs_ResponseSyntax) **   <a name="SES-ListExportJobs-response-NextToken"></a>
A string token indicating that there might be additional export jobs available to be listed. Use this token to a subsequent call to `ListExportJobs` with the same parameters to retrieve the next page of export jobs.  
Type: String

## Errors
<a name="API_ListExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListExportJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListExportJobs) 