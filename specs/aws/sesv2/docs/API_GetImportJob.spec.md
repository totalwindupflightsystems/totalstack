---
id: "@specs/aws/sesv2/docs/API_GetImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetImportJob"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetImportJob
<a name="API_GetImportJob"></a>

Provides information about an import job.

## Request Syntax
<a name="API_GetImportJob_RequestSyntax"></a>

```
GET /v2/email/import-jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_GetImportJob_RequestSyntax) **   <a name="SES-GetImportJob-request-uri-JobId"></a>
The ID of the import job.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_GetImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CompletedTimestamp": number,
   "CreatedTimestamp": number,
   "FailedRecordsCount": number,
   "FailureInfo": { 
      "ErrorMessage": "string",
      "FailedRecordsS3Url": "string"
   },
   "ImportDataSource": { 
      "DataFormat": "string",
      "S3Url": "string"
   },
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
```

## Response Elements
<a name="API_GetImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletedTimestamp](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-CompletedTimestamp"></a>
The time stamp of when the import job was completed.  
Type: Timestamp

 ** [CreatedTimestamp](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-CreatedTimestamp"></a>
The time stamp of when the import job was created.  
Type: Timestamp

 ** [FailedRecordsCount](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-FailedRecordsCount"></a>
The number of records that failed processing because of invalid input or other reasons.  
Type: Integer

 ** [FailureInfo](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-FailureInfo"></a>
The failure details about an import job.  
Type: [FailureInfo](API_FailureInfo.md) object

 ** [ImportDataSource](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-ImportDataSource"></a>
The data source of the import job.  
Type: [ImportDataSource](API_ImportDataSource.md) object

 ** [ImportDestination](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-ImportDestination"></a>
The destination of the import job.  
Type: [ImportDestination](API_ImportDestination.md) object

 ** [JobId](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-JobId"></a>
A string that represents the import job ID.  
Type: String  
Length Constraints: Minimum length of 1.

 ** [JobStatus](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-JobStatus"></a>
The status of the import job.  
Type: String  
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | CANCELLED` 

 ** [ProcessedRecordsCount](#API_GetImportJob_ResponseSyntax) **   <a name="SES-GetImportJob-response-ProcessedRecordsCount"></a>
The current number of records processed.  
Type: Integer

## Errors
<a name="API_GetImportJob_Errors"></a>

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
<a name="API_GetImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetImportJob) 