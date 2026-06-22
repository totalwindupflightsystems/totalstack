---
id: "@specs/aws/sesv2/docs/API_CreateExportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateExportJob"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateExportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateExportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateExportJob
<a name="API_CreateExportJob"></a>

Creates an export job for a data source and destination.

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_CreateExportJob_RequestSyntax"></a>

```
POST /v2/email/export-jobs HTTP/1.1
Content-type: application/json

{
   "ExportDataSource": { 
      "MessageInsightsDataSource": { 
         "EndDate": {{number}},
         "Exclude": { 
            "Destination": [ "{{string}}" ],
            "FromEmailAddress": [ "{{string}}" ],
            "Isp": [ "{{string}}" ],
            "LastDeliveryEvent": [ "{{string}}" ],
            "LastEngagementEvent": [ "{{string}}" ],
            "Subject": [ "{{string}}" ]
         },
         "Include": { 
            "Destination": [ "{{string}}" ],
            "FromEmailAddress": [ "{{string}}" ],
            "Isp": [ "{{string}}" ],
            "LastDeliveryEvent": [ "{{string}}" ],
            "LastEngagementEvent": [ "{{string}}" ],
            "Subject": [ "{{string}}" ]
         },
         "MaxResults": {{number}},
         "StartDate": {{number}}
      },
      "MetricsDataSource": { 
         "Dimensions": { 
            "{{string}}" : [ "{{string}}" ]
         },
         "EndDate": {{number}},
         "Metrics": [ 
            { 
               "Aggregation": "{{string}}",
               "Name": "{{string}}"
            }
         ],
         "Namespace": "{{string}}",
         "StartDate": {{number}}
      }
   },
   "ExportDestination": { 
      "DataFormat": "{{string}}",
      "S3Url": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateExportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExportDataSource](#API_CreateExportJob_RequestSyntax) **   <a name="SES-CreateExportJob-request-ExportDataSource"></a>
The data source for the export job.  
Type: [ExportDataSource](API_ExportDataSource.md) object  
Required: Yes

 ** [ExportDestination](#API_CreateExportJob_RequestSyntax) **   <a name="SES-CreateExportJob-request-ExportDestination"></a>
The destination for the export job.  
Type: [ExportDestination](API_ExportDestination.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobId": "string"
}
```

## Response Elements
<a name="API_CreateExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_CreateExportJob_ResponseSyntax) **   <a name="SES-CreateExportJob-response-JobId"></a>
A string that represents the export job ID.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateExportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateExportJob) 