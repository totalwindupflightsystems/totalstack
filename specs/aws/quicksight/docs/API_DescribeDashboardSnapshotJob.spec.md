---
id: "@specs/aws/quicksight/docs/API_DescribeDashboardSnapshotJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDashboardSnapshotJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDashboardSnapshotJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDashboardSnapshotJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDashboardSnapshotJob
<a name="API_DescribeDashboardSnapshotJob"></a>

Describes an existing snapshot job.

Poll job descriptions after a job starts to know the status of the job. For information on available status codes, see `JobStatus`.

 **Registered user support** 

This API can be called as before to get status of a job started by the same Quick Sight user.

 **Possible error scenarios** 

Request will fail with an Access Denied error in the following scenarios:
+ The credentials have expired.
+ Job has been started by a different user.
+ Impersonated Quick Sight user doesn't have access to the specified dashboard in the job.

## Request Syntax
<a name="API_DescribeDashboardSnapshotJob_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/snapshot-jobs/{{SnapshotJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboardSnapshotJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDashboardSnapshotJob_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-request-uri-AwsAccountId"></a>
The ID of the AWS account that the dashboard snapshot job is executed in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_DescribeDashboardSnapshotJob_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-request-uri-DashboardId"></a>
The ID of the dashboard that you have started a snapshot job for.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [SnapshotJobId](#API_DescribeDashboardSnapshotJob_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-request-uri-SnapshotJobId"></a>
The ID of the job to be described. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_DescribeDashboardSnapshotJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboardSnapshotJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AwsAccountId": "string",
   "CreatedTime": number,
   "DashboardId": "string",
   "JobStatus": "string",
   "LastUpdatedTime": number,
   "RequestId": "string",
   "SnapshotConfiguration": { 
      "DestinationConfiguration": { 
         "S3Destinations": [ 
            { 
               "BucketConfiguration": { 
                  "BucketName": "string",
                  "BucketPrefix": "string",
                  "BucketRegion": "string"
               }
            }
         ]
      },
      "FileGroups": [ 
         { 
            "Files": [ 
               { 
                  "FormatType": "string",
                  "SheetSelections": [ 
                     { 
                        "SelectionScope": "string",
                        "SheetId": "string",
                        "VisualIds": [ "string" ]
                     }
                  ]
               }
            ]
         }
      ],
      "Parameters": { 
         "DateTimeParameters": [ 
            { 
               "Name": "string",
               "Values": [ number ]
            }
         ],
         "DecimalParameters": [ 
            { 
               "Name": "string",
               "Values": [ number ]
            }
         ],
         "IntegerParameters": [ 
            { 
               "Name": "string",
               "Values": [ number ]
            }
         ],
         "StringParameters": [ 
            { 
               "Name": "string",
               "Values": [ "string" ]
            }
         ]
      }
   },
   "SnapshotJobId": "string",
   "Status": number,
   "UserConfiguration": { 
      "AnonymousUsers": [ 
         { 
            "RowLevelPermissionTagKeys": [ "string" ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeDashboardSnapshotJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a `StartDashboardSnapshotJob` API call.  
Type: String

 ** [AwsAccountId](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-AwsAccountId"></a>
 The ID of the AWS account that the dashboard snapshot job is executed in.   
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [CreatedTime](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-CreatedTime"></a>
 The time that the snapshot job was created.   
Type: Timestamp

 ** [DashboardId](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-DashboardId"></a>
The ID of the dashboard that you have started a snapshot job for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [JobStatus](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-JobStatus"></a>
Indicates the status of a job. The status updates as the job executes. This shows one of the following values.  
+  `COMPLETED` - The job was completed successfully.
+  `FAILED` - The job failed to execute.
+  `QUEUED` - The job is queued and hasn't started yet.
+  `RUNNING` - The job is still running.
Type: String  
Valid Values: `QUEUED | RUNNING | COMPLETED | FAILED` 

 ** [LastUpdatedTime](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-LastUpdatedTime"></a>
 The time that the snapshot job status was last updated.   
Type: Timestamp

 ** [RequestId](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-RequestId"></a>
 The AWS request ID for this operation.   
Type: String  
Pattern: `.*\S.*` 

 ** [SnapshotConfiguration](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-SnapshotConfiguration"></a>
The snapshot configuration of the job. This information is provided when you make a `StartDashboardSnapshotJob` API call.  
Type: [SnapshotConfiguration](API_SnapshotConfiguration.md) object

 ** [SnapshotJobId](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-SnapshotJobId"></a>
The ID of the job to be described. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Status](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-Status"></a>
The HTTP status of the request  
Type: Integer

 ** [UserConfiguration](#API_DescribeDashboardSnapshotJob_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJob-response-UserConfiguration"></a>
The user configuration for the snapshot job. This information is provided when you make a `StartDashboardSnapshotJob` API call.  
Type: [SnapshotUserConfigurationRedacted](API_SnapshotUserConfigurationRedacted.md) object

## Errors
<a name="API_DescribeDashboardSnapshotJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_DescribeDashboardSnapshotJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDashboardSnapshotJob) 