---
id: "@specs/aws/sesv2/docs/API_CreateImportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateImportJob"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateImportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateImportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateImportJob
<a name="API_CreateImportJob"></a>

Creates an import job for a data destination.

## Request Syntax
<a name="API_CreateImportJob_RequestSyntax"></a>

```
POST /v2/email/import-jobs HTTP/1.1
Content-type: application/json

{
   "ImportDataSource": { 
      "DataFormat": "{{string}}",
      "S3Url": "{{string}}"
   },
   "ImportDestination": { 
      "ContactListDestination": { 
         "ContactListImportAction": "{{string}}",
         "ContactListName": "{{string}}"
      },
      "SuppressionListDestination": { 
         "SuppressionListImportAction": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateImportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ImportDataSource](#API_CreateImportJob_RequestSyntax) **   <a name="SES-CreateImportJob-request-ImportDataSource"></a>
The data source for the import job.  
Type: [ImportDataSource](API_ImportDataSource.md) object  
Required: Yes

 ** [ImportDestination](#API_CreateImportJob_RequestSyntax) **   <a name="SES-CreateImportJob-request-ImportDestination"></a>
The destination for the import job.  
Type: [ImportDestination](API_ImportDestination.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobId": "string"
}
```

## Response Elements
<a name="API_CreateImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_CreateImportJob_ResponseSyntax) **   <a name="SES-CreateImportJob-response-JobId"></a>
A string that represents the import job ID.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateImportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateImportJob) 