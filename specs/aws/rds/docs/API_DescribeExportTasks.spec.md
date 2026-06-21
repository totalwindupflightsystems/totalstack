---
id: "@specs/aws/rds/docs/API_DescribeExportTasks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeExportTasks"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeExportTasks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeExportTasks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeExportTasks
<a name="API_DescribeExportTasks"></a>

Returns information about a snapshot or cluster export to Amazon S3. This API operation supports pagination.

## Request Parameters
<a name="API_DescribeExportTasks_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ExportTaskIdentifier **   
The identifier of the snapshot or cluster export task to be described.  
Type: String  
Required: No

 **Filters.Filter.N**   
Filters specify one or more snapshot or cluster exports to describe. The filters are specified as name-value pairs that define what to include in the output. Filter names and values are case-sensitive.  
Supported filters include the following:  
+  `export-task-identifier` - An identifier for the snapshot or cluster export task.
+  `s3-bucket` - The Amazon S3 bucket the data is exported to.
+  `source-arn` - The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.
+  `status` - The status of the export task. Must be lowercase. Valid statuses are the following:
  +  `canceled` 
  +  `canceling` 
  +  `complete` 
  +  `failed` 
  +  `in_progress` 
  +  `starting` 
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeExportTasks` request. If you specify this parameter, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified value, a pagination token called a marker is included in the response. You can use the marker in a later `DescribeExportTasks` request to retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Valid Range: Minimum value of 20. Maximum value of 100.  
Required: No

 ** SourceArn **   
The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.  
Type: String  
Required: No

 ** SourceType **   
The type of source for the export.  
Type: String  
Valid Values: `SNAPSHOT | CLUSTER`   
Required: No

## Response Elements
<a name="API_DescribeExportTasks_ResponseElements"></a>

The following elements are returned by the service.

 **ExportTasks.ExportTask.N**   
Information about an export of a snapshot or cluster to Amazon S3.  
Type: Array of [ExportTask](API_ExportTask.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeExportTasks` request. A marker is used for pagination to identify the location to begin output for the next response of `DescribeExportTasks`.  
Type: String

## Errors
<a name="API_DescribeExportTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExportTaskNotFound **   
The export task doesn't exist.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeExportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeExportTasks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeExportTasks) 