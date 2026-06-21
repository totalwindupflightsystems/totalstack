---
id: "@specs/aws/rds/docs/API_CancelExportTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelExportTask"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CancelExportTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CancelExportTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelExportTask
<a name="API_CancelExportTask"></a>

Cancels an export task in progress that is exporting a snapshot or cluster to Amazon S3. Any data that has already been written to the S3 bucket isn't removed.

## Request Parameters
<a name="API_CancelExportTask_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ExportTaskIdentifier **   
The identifier of the snapshot or cluster export task to cancel.  
Type: String  
Required: Yes

## Response Elements
<a name="API_CancelExportTask_ResponseElements"></a>

The following elements are returned by the service.

 **ExportOnly.member.N**   
The data exported from the snapshot or cluster.  
Valid Values:  
+  `database` - Export all the data from a specified database.
+  `database.table` *table-name* - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.
+  `database.schema` *schema-name* - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
+  `database.schema.table` *table-name* - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
Type: Array of strings

 ** ExportTaskIdentifier **   
A unique identifier for the snapshot or cluster export task. This ID isn't an identifier for the Amazon S3 bucket where the data is exported.  
Type: String

 ** FailureCause **   
The reason the export failed, if it failed.  
Type: String

 ** IamRoleArn **   
The name of the IAM role that is used to write to Amazon S3 when exporting a snapshot or cluster.  
Type: String

 ** KmsKeyId **   
The key identifier of the AWS KMS key that is used to encrypt the data when it's exported to Amazon S3. The KMS key identifier is its key ARN, key ID, alias ARN, or alias name. The IAM role used for the export must have encryption and decryption permissions to use this KMS key.  
Type: String

 ** PercentProgress **   
The progress of the snapshot or cluster export task as a percentage.  
Type: Integer

 ** S3Bucket **   
The Amazon S3 bucket where the snapshot or cluster is exported to.  
Type: String

 ** S3Prefix **   
The Amazon S3 bucket prefix that is the file name and path of the exported data.  
Type: String

 ** SnapshotTime **   
The time when the snapshot was created.  
Type: Timestamp

 ** SourceArn **   
The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.  
Type: String

 ** SourceType **   
The type of source for the export.  
Type: String  
Valid Values: `SNAPSHOT | CLUSTER` 

 ** Status **   
The progress status of the export task. The status can be one of the following:  
+  `CANCELED` 
+  `CANCELING` 
+  `COMPLETE` 
+  `FAILED` 
+  `IN_PROGRESS` 
+  `STARTING` 
Type: String

 ** TaskEndTime **   
The time when the snapshot or cluster export task ended.  
Type: Timestamp

 ** TaskStartTime **   
The time when the snapshot or cluster export task started.  
Type: Timestamp

 ** TotalExtractedDataInGB **   
The total amount of data exported, in gigabytes.  
Type: Integer

 ** WarningMessage **   
A warning about the snapshot or cluster export task.  
Type: String

## Errors
<a name="API_CancelExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExportTaskNotFound **   
The export task doesn't exist.  
HTTP Status Code: 404

 ** InvalidExportTaskStateFault **   
You can't cancel an export task that has completed.  
HTTP Status Code: 400

## See Also
<a name="API_CancelExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CancelExportTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CancelExportTask) 