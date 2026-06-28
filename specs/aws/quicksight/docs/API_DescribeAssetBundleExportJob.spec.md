---
id: "@specs/aws/quicksight/docs/API_DescribeAssetBundleExportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAssetBundleExportJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAssetBundleExportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAssetBundleExportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAssetBundleExportJob
<a name="API_DescribeAssetBundleExportJob"></a>

Describes an existing export job.

Poll job descriptions after a job starts to know the status of the job. When a job succeeds, a URL is provided to download the exported assets' data from. Download URLs are valid for five minutes after they are generated. You can call the `DescribeAssetBundleExportJob` API for a new download URL as needed.

Job descriptions are available for 14 days after the job starts.

## Request Syntax
<a name="API_DescribeAssetBundleExportJob_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/asset-bundle-export-jobs/{{AssetBundleExportJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetBundleExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetBundleExportJobId](#API_DescribeAssetBundleExportJob_RequestSyntax) **   <a name="QS-DescribeAssetBundleExportJob-request-uri-AssetBundleExportJobId"></a>
The ID of the job that you want described. The job ID is set when you start a new job with a `StartAssetBundleExportJob` API call.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_DescribeAssetBundleExportJob_RequestSyntax) **   <a name="QS-DescribeAssetBundleExportJob-request-uri-AwsAccountId"></a>
The ID of the AWS account the export job is executed in.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAssetBundleExportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetBundleExportJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AssetBundleExportJobId": "string",
   "AwsAccountId": "string",
   "CloudFormationOverridePropertyConfiguration": { 
      "Analyses": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "Dashboards": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "DataSets": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "DataSources": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "Folders": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "RefreshSchedules": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "ResourceIdOverrideConfiguration": { 
         "PrefixForAllResources": boolean
      },
      "Themes": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ],
      "VPCConnections": [ 
         { 
            "Arn": "string",
            "Properties": [ "string" ]
         }
      ]
   },
   "CreatedTime": number,
   "DownloadUrl": "string",
   "Errors": [ 
      { 
         "Arn": "string",
         "Message": "string",
         "Type": "string"
      }
   ],
   "ExportFormat": "string",
   "IncludeAllDependencies": boolean,
   "IncludeFolderMembers": "string",
   "IncludeFolderMemberships": boolean,
   "IncludePermissions": boolean,
   "IncludeTags": boolean,
   "JobStatus": "string",
   "RequestId": "string",
   "ResourceArns": [ "string" ],
   "ValidationStrategy": { 
      "StrictModeForAllResources": boolean
   },
   "Warnings": [ 
      { 
         "Arn": "string",
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAssetBundleExportJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-Status"></a>
The HTTP status of the response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the export job.  
Type: String

 ** [AssetBundleExportJobId](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-AssetBundleExportJobId"></a>
The ID of the job. The job ID is set when you start a new job with a `StartAssetBundleExportJob` API call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [AwsAccountId](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-AwsAccountId"></a>
The ID of the AWS account that the export job was executed in.   
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [CloudFormationOverridePropertyConfiguration](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-CloudFormationOverridePropertyConfiguration"></a>
The CloudFormation override property configuration for the export job.  
Type: [AssetBundleCloudFormationOverridePropertyConfiguration](API_AssetBundleCloudFormationOverridePropertyConfiguration.md) object

 ** [CreatedTime](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-CreatedTime"></a>
The time that the export job was created.  
Type: Timestamp

 ** [DownloadUrl](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-DownloadUrl"></a>
The URL to download the exported asset bundle data from.  
This URL is available only after the job has succeeded. This URL is valid for 5 minutes after issuance. Call `DescribeAssetBundleExportJob` again for a fresh URL if needed.  
The downloaded asset bundle is a zip file named `assetbundle-{jobId}.qs`. The file has a `.qs` extension.  
This URL can't be used in a `StartAssetBundleImportJob` API call and should only be used for download purposes.  
Type: String  
Pattern: `^(https|s3)://([^/]+)/?(.*)$` 

 ** [Errors](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-Errors"></a>
An array of error records that describes any failures that occurred during the export job processing.  
Error records accumulate while the job runs. The complete set of error records is available after the job has completed and failed.  
Type: Array of [AssetBundleExportJobError](API_AssetBundleExportJobError.md) objects

 ** [ExportFormat](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-ExportFormat"></a>
The format of the exported asset bundle. A `QUICKSIGHT_JSON` formatted file can be used to make a `StartAssetBundleImportJob` API call. A `CLOUDFORMATION_JSON` formatted file can be used in the CloudFormation console and with the CloudFormation APIs.  
Type: String  
Valid Values: `CLOUDFORMATION_JSON | QUICKSIGHT_JSON` 

 ** [IncludeAllDependencies](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-IncludeAllDependencies"></a>
The include dependencies flag.  
Type: Boolean

 ** [IncludeFolderMembers](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-IncludeFolderMembers"></a>
A setting that determines whether folder members are included.  
Type: String  
Valid Values: `RECURSE | ONE_LEVEL | NONE` 

 ** [IncludeFolderMemberships](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-IncludeFolderMemberships"></a>
The include folder memberships flag.  
Type: Boolean

 ** [IncludePermissions](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-IncludePermissions"></a>
The include permissions flag.  
Type: Boolean

 ** [IncludeTags](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-IncludeTags"></a>
The include tags flag.  
Type: Boolean

 ** [JobStatus](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-JobStatus"></a>
Indicates the status of a job through its queuing and execution.  
Poll this `DescribeAssetBundleExportApi` until `JobStatus` is either `SUCCESSFUL` or `FAILED`.  
Type: String  
Valid Values: `QUEUED_FOR_IMMEDIATE_EXECUTION | IN_PROGRESS | SUCCESSFUL | FAILED` 

 ** [RequestId](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

 ** [ResourceArns](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-ResourceArns"></a>
A list of resource ARNs that exported with the job.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [ValidationStrategy](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-ValidationStrategy"></a>
The validation strategy that is used to export the analysis or dashboard.  
Type: [AssetBundleExportJobValidationStrategy](API_AssetBundleExportJobValidationStrategy.md) object

 ** [Warnings](#API_DescribeAssetBundleExportJob_ResponseSyntax) **   <a name="QS-DescribeAssetBundleExportJob-response-Warnings"></a>
An array of warning records that describe the analysis or dashboard that is exported. This array includes UI errors that can be skipped during the validation process.  
This property only appears if `StrictModeForAllResources` in `ValidationStrategy` is set to `FALSE`.  
Type: Array of [AssetBundleExportJobWarning](API_AssetBundleExportJobWarning.md) objects

## Errors
<a name="API_DescribeAssetBundleExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeAssetBundleExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAssetBundleExportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAssetBundleExportJob) 