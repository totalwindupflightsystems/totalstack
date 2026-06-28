---
id: "@specs/aws/kendra/docs/API_ListDataSourceSyncJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDataSourceSyncJobs"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ListDataSourceSyncJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ListDataSourceSyncJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDataSourceSyncJobs
<a name="API_ListDataSourceSyncJobs"></a>

Gets statistics about synchronizing a data source connector.

## Request Syntax
<a name="API_ListDataSourceSyncJobs_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "IndexId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTimeFilter": { 
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "StatusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataSourceSyncJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-Id"></a>
The identifier of the data source connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: Yes

 ** [IndexId](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-IndexId"></a>
The identifier of the index used with the data source connector.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [MaxResults](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-MaxResults"></a>
The maximum number of synchronization jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10.  
Required: No

 ** [NextToken](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-NextToken"></a>
If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of jobs.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.  
Required: No

 ** [StartTimeFilter](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-StartTimeFilter"></a>
When specified, the synchronization jobs returned in the list are limited to jobs between the specified dates.  
Type: [TimeRange](API_TimeRange.md) object  
Required: No

 ** [StatusFilter](#API_ListDataSourceSyncJobs_RequestSyntax) **   <a name="kendra-ListDataSourceSyncJobs-request-StatusFilter"></a>
Only returns synchronization jobs with the `Status` field equal to the specified status.  
Type: String  
Valid Values: `FAILED | SUCCEEDED | SYNCING | INCOMPLETE | STOPPING | ABORTED | SYNCING_INDEXING`   
Required: No

## Response Syntax
<a name="API_ListDataSourceSyncJobs_ResponseSyntax"></a>

```
{
   "History": [ 
      { 
         "DataSourceErrorCode": "string",
         "EndTime": number,
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ExecutionId": "string",
         "Metrics": { 
            "DocumentsAdded": "string",
            "DocumentsDeleted": "string",
            "DocumentsFailed": "string",
            "DocumentsModified": "string",
            "DocumentsScanned": "string"
         },
         "StartTime": number,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSourceSyncJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [History](#API_ListDataSourceSyncJobs_ResponseSyntax) **   <a name="kendra-ListDataSourceSyncJobs-response-History"></a>
A history of synchronization jobs for the data source connector.  
Type: Array of [DataSourceSyncJob](API_DataSourceSyncJob.md) objects

 ** [NextToken](#API_ListDataSourceSyncJobs_ResponseSyntax) **   <a name="kendra-ListDataSourceSyncJobs-response-NextToken"></a>
If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of jobs.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListDataSourceSyncJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** ConflictException **   
A conflict occurred with the request. Please fix any inconsistences with your resources and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_ListDataSourceSyncJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/ListDataSourceSyncJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ListDataSourceSyncJobs) 