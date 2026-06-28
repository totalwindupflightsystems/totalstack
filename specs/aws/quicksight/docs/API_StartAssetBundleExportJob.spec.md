---
id: "@specs/aws/quicksight/docs/API_StartAssetBundleExportJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAssetBundleExportJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# StartAssetBundleExportJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_StartAssetBundleExportJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAssetBundleExportJob
<a name="API_StartAssetBundleExportJob"></a>

Starts an Asset Bundle export job.

An Asset Bundle export job exports specified Amazon Quick Sight assets. You can also choose to export any asset dependencies in the same job. Export jobs run asynchronously and can be polled with a `DescribeAssetBundleExportJob` API call. When a job is successfully completed, a download URL that contains the exported assets is returned. The URL is valid for 5 minutes and can be refreshed with a `DescribeAssetBundleExportJob` API call. Each Amazon Quick Sight account can run up to 5 export jobs concurrently.

The API caller must have the necessary permissions in their IAM role to access each resource before the resources can be exported.

## Request Syntax
<a name="API_StartAssetBundleExportJob_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/asset-bundle-export-jobs/export HTTP/1.1
Content-type: application/json

{
   "AssetBundleExportJobId": "{{string}}",
   "CloudFormationOverridePropertyConfiguration": { 
      "Analyses": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "Dashboards": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "DataSets": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "DataSources": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "Folders": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "RefreshSchedules": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "ResourceIdOverrideConfiguration": { 
         "PrefixForAllResources": {{boolean}}
      },
      "Themes": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ],
      "VPCConnections": [ 
         { 
            "Arn": "{{string}}",
            "Properties": [ "{{string}}" ]
         }
      ]
   },
   "ExportFormat": "{{string}}",
   "IncludeAllDependencies": {{boolean}},
   "IncludeFolderMembers": "{{string}}",
   "IncludeFolderMemberships": {{boolean}},
   "IncludePermissions": {{boolean}},
   "IncludeTags": {{boolean}},
   "ResourceArns": [ "{{string}}" ],
   "ValidationStrategy": { 
      "StrictModeForAllResources": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_StartAssetBundleExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-uri-AwsAccountId"></a>
The ID of the AWS account to export assets from.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_StartAssetBundleExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetBundleExportJobId](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-AssetBundleExportJobId"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [ExportFormat](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-ExportFormat"></a>
The export data format.  
Type: String  
Valid Values: `CLOUDFORMATION_JSON | QUICKSIGHT_JSON`   
Required: Yes

 ** [ResourceArns](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-ResourceArns"></a>
An array of resource ARNs to export. The following resources are supported.  
+  `Analysis` 
+  `Dashboard` 
+  `DataSet` 
+  `DataSource` 
+  `RefreshSchedule` 
+  `Theme` 
+  `VPCConnection` 
The API caller must have the necessary permissions in their IAM role to access each resource before the resources can be exported.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: Yes

 ** [CloudFormationOverridePropertyConfiguration](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-CloudFormationOverridePropertyConfiguration"></a>
An optional collection of structures that generate CloudFormation parameters to override the existing resource property values when the resource is exported to a new CloudFormation template.  
Use this field if the `ExportFormat` field of a `StartAssetBundleExportJobRequest` API call is set to `CLOUDFORMATION_JSON`.  
Type: [AssetBundleCloudFormationOverridePropertyConfiguration](API_AssetBundleCloudFormationOverridePropertyConfiguration.md) object  
Required: No

 ** [IncludeAllDependencies](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-IncludeAllDependencies"></a>
A Boolean that determines whether all dependencies of each resource ARN are recursively exported with the job. For example, say you provided a Dashboard ARN to the `ResourceArns` parameter. If you set `IncludeAllDependencies` to `TRUE`, any theme, dataset, and data source resource that is a dependency of the dashboard is also exported.  
Type: Boolean  
Required: No

 ** [IncludeFolderMembers](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-IncludeFolderMembers"></a>
A setting that indicates whether you want to include folder assets. You can also use this setting to recusrsively include all subfolders of an exported folder.  
Type: String  
Valid Values: `RECURSE | ONE_LEVEL | NONE`   
Required: No

 ** [IncludeFolderMemberships](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-IncludeFolderMemberships"></a>
A Boolean that determines if the exported asset carries over information about the folders that the asset is a member of.   
Type: Boolean  
Required: No

 ** [IncludePermissions](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-IncludePermissions"></a>
A Boolean that determines whether all permissions for each resource ARN are exported with the job. If you set `IncludePermissions` to `TRUE`, any permissions associated with each resource are exported.   
Type: Boolean  
Required: No

 ** [IncludeTags](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-IncludeTags"></a>
 A Boolean that determines whether all tags for each resource ARN are exported with the job. If you set `IncludeTags` to `TRUE`, any tags associated with each resource are exported.  
Type: Boolean  
Required: No

 ** [ValidationStrategy](#API_StartAssetBundleExportJob_RequestSyntax) **   <a name="QS-StartAssetBundleExportJob-request-ValidationStrategy"></a>
An optional parameter that determines which validation strategy to use for the export job. If `StrictModeForAllResources` is set to `TRUE`, strict validation for every error is enforced. If it is set to `FALSE`, validation is skipped for specific UI errors that are shown as warnings. The default value for `StrictModeForAllResources` is `FALSE`.  
Type: [AssetBundleExportJobValidationStrategy](API_AssetBundleExportJobValidationStrategy.md) object  
Required: No

## Response Syntax
<a name="API_StartAssetBundleExportJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "AssetBundleExportJobId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_StartAssetBundleExportJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_StartAssetBundleExportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleExportJob-response-Status"></a>
The HTTP status of the response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartAssetBundleExportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleExportJob-response-Arn"></a>
The Amazon Resource Name (ARN) for the export job.  
Type: String

 ** [AssetBundleExportJobId](#API_StartAssetBundleExportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleExportJob-response-AssetBundleExportJobId"></a>
The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [RequestId](#API_StartAssetBundleExportJob_ResponseSyntax) **   <a name="QS-StartAssetBundleExportJob-response-RequestId"></a>
The AWS response ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

## Errors
<a name="API_StartAssetBundleExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

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
<a name="API_StartAssetBundleExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/StartAssetBundleExportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StartAssetBundleExportJob) 