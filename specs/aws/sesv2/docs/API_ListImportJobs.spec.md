---
id: "@specs/aws/sesv2/docs/API_ListImportJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListImportJobs"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListImportJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListImportJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListImportJobs
<a name="API_ListImportJobs"></a>

Lists all of the import jobs.

## Request Syntax
<a name="API_ListImportJobs_RequestSyntax"></a>

```
POST /v2/email/import-jobs/list HTTP/1.1
Content-type: application/json

{
   "ImportDestinationType": "{{string}}",
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListImportJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImportJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ImportDestinationType](#API_ListImportJobs_RequestSyntax) **   <a name="SES-ListImportJobs-request-ImportDestinationType"></a>
The destination of the import job, which can be used to list import jobs that have a certain `ImportDestinationType`.  
Type: String  
Valid Values: `SUPPRESSION_LIST | CONTACT_LIST`   
Required: No

 ** [NextToken](#API_ListImportJobs_RequestSyntax) **   <a name="SES-ListImportJobs-request-NextToken"></a>
A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to `ListImportJobs` with the same parameters to retrieve the next page of import jobs.  
Type: String  
Required: No

 ** [PageSize](#API_ListImportJobs_RequestSyntax) **   <a name="SES-ListImportJobs-request-PageSize"></a>
Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the `NextToken` element is sent in the response. Use the `NextToken` value in subsequent requests to retrieve additional addresses.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ImportJobs": [ 
      { 
         "CreatedTimestamp": number,
         "FailedRecordsCount": number,
         "ImportDestination": { 
            "ContactListDestination": { 
               "ContactListImportAction": "string",
               "ContactListName": "string"
            },
            "SuppressionListDestination": { 
               "SuppressionListImportAction": "string"
            }
         },
         "JobId": "string",
         "JobStatus": "string",
         "ProcessedRecordsCount": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportJobs](#API_ListImportJobs_ResponseSyntax) **   <a name="SES-ListImportJobs-response-ImportJobs"></a>
A list of the import job summaries.  
Type: Array of [ImportJobSummary](API_ImportJobSummary.md) objects

 ** [NextToken](#API_ListImportJobs_ResponseSyntax) **   <a name="SES-ListImportJobs-response-NextToken"></a>
A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to `ListImportJobs` with the same parameters to retrieve the next page of import jobs.  
Type: String

## Errors
<a name="API_ListImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListImportJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListImportJobs) 