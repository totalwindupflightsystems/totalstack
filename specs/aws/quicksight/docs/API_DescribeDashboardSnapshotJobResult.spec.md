---
id: "@specs/aws/quicksight/docs/API_DescribeDashboardSnapshotJobResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDashboardSnapshotJobResult"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDashboardSnapshotJobResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDashboardSnapshotJobResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDashboardSnapshotJobResult
<a name="API_DescribeDashboardSnapshotJobResult"></a>

Describes the result of an existing snapshot job that has finished running.

A finished snapshot job will return a `COMPLETED` or `FAILED` status when you poll the job with a `DescribeDashboardSnapshotJob` API call.

If the job has not finished running, this operation returns a message that says `Dashboard Snapshot Job with id <SnapshotjobId> has not reached a terminal state.`.

 **Registered user support** 

This API can be called as before to get the result of a job started by the same Quick Sight user. The result for the user will be returned in `RegisteredUsers` response attribute. The attribute will contain a list with at most one object in it.

 **Possible error scenarios** 

The request fails with an Access Denied error in the following scenarios:
+ The credentials have expired.
+ The job was started by a different user.
+ The registered user doesn't have access to the specified dashboard.

The request succeeds but the job fails in the following scenarios:
+  `DASHBOARD_ACCESS_DENIED` - The registered user lost access to the dashboard.
+  `CAPABILITY_RESTRICTED` - The registered user is restricted from exporting data in **all** selected formats.

The request succeeds but the response contains an error code in the following scenarios:
+  `CAPABILITY_RESTRICTED` - The registered user is restricted from exporting data in **some** selected formats.
+  `RLS_CHANGED` - Row-level security settings have changed. Re-run the job with current settings.
+  `CLS_CHANGED` - Column-level security settings have changed. Re-run the job with current settings.
+  `DATASET_DELETED` - The dataset has been deleted. Verify the dataset exists before re-running the job.

## Request Syntax
<a name="API_DescribeDashboardSnapshotJobResult_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/snapshot-jobs/{{SnapshotJobId}}/result HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboardSnapshotJobResult_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDashboardSnapshotJobResult_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-request-uri-AwsAccountId"></a>
The ID of the AWS account that the dashboard snapshot job is executed in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_DescribeDashboardSnapshotJobResult_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-request-uri-DashboardId"></a>
The ID of the dashboard that you have started a snapshot job for.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [SnapshotJobId](#API_DescribeDashboardSnapshotJobResult_RequestSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-request-uri-SnapshotJobId"></a>
The ID of the job to be described. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_DescribeDashboardSnapshotJobResult_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboardSnapshotJobResult_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "ErrorInfo": { 
      "ErrorMessage": "string",
      "ErrorType": "string"
   },
   "JobStatus": "string",
   "LastUpdatedTime": number,
   "RequestId": "string",
   "Result": { 
      "AnonymousUsers": [ 
         { 
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
                  ],
                  "S3Results": [ 
                     { 
                        "ErrorInfo": [ 
                           { 
                              "ErrorMessage": "string",
                              "ErrorType": "string"
                           }
                        ],
                        "S3DestinationConfiguration": { 
                           "BucketConfiguration": { 
                              "BucketName": "string",
                              "BucketPrefix": "string",
                              "BucketRegion": "string"
                           }
                        },
                        "S3Uri": "string"
                     }
                  ]
               }
            ]
         }
      ],
      "RegisteredUsers": [ 
         { 
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
                  ],
                  "S3Results": [ 
                     { 
                        "ErrorInfo": [ 
                           { 
                              "ErrorMessage": "string",
                              "ErrorType": "string"
                           }
                        ],
                        "S3DestinationConfiguration": { 
                           "BucketConfiguration": { 
                              "BucketName": "string",
                              "BucketPrefix": "string",
                              "BucketRegion": "string"
                           }
                        },
                        "S3Uri": "string"
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeDashboardSnapshotJobResult_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-Status"></a>
The HTTP status of the request

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-Arn"></a>
The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a `StartDashboardSnapshotJob` API call.  
Type: String

 ** [CreatedTime](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-CreatedTime"></a>
The time that a snapshot job was created.  
Type: Timestamp

 ** [ErrorInfo](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-ErrorInfo"></a>
Displays information for the error that caused a job to fail.  
Type: [SnapshotJobErrorInfo](API_SnapshotJobErrorInfo.md) object

 ** [JobStatus](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-JobStatus"></a>
Indicates the status of a job after it has reached a terminal state. A finished snapshot job will retuen a `COMPLETED` or `FAILED` status.  
Type: String  
Valid Values: `QUEUED | RUNNING | COMPLETED | FAILED` 

 ** [LastUpdatedTime](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-LastUpdatedTime"></a>
The time that a snapshot job status was last updated.  
Type: Timestamp

 ** [RequestId](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

 ** [Result](#API_DescribeDashboardSnapshotJobResult_ResponseSyntax) **   <a name="QS-DescribeDashboardSnapshotJobResult-response-Result"></a>
The result of the snapshot job. Jobs that have successfully completed will return the S3Uri where they are located. Jobs that have failedwill return information on the error that caused the job to fail.  
Type: [SnapshotJobResult](API_SnapshotJobResult.md) object

## Errors
<a name="API_DescribeDashboardSnapshotJobResult_Errors"></a>

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

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

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
<a name="API_DescribeDashboardSnapshotJobResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult) 