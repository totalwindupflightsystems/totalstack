---
id: "@specs/aws/rds/docs/API_StartExportTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartExportTask"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StartExportTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StartExportTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartExportTask
<a name="API_StartExportTask"></a>

Starts an export of DB snapshot or DB cluster data to Amazon S3. The provided IAM role must have access to the S3 bucket.

You can't export snapshot data from RDS Custom DB instances. For more information, see [ Supported Regions and DB engines for exporting snapshots to S3 in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html).

For more information on exporting DB snapshot data, see [Exporting DB snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html) in the *Amazon RDS User Guide* or [Exporting DB cluster snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.html) in the *Amazon Aurora User Guide*.

For more information on exporting DB cluster data, see [Exporting DB cluster data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_StartExportTask_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ExportTaskIdentifier **   
A unique identifier for the export task. This ID isn't an identifier for the Amazon S3 bucket where the data is to be exported.  
Type: String  
Required: Yes

 ** IamRoleArn **   
The name of the IAM role to use for writing to the Amazon S3 bucket when exporting a snapshot or cluster.  
In the IAM policy attached to your IAM role, include the following required actions to allow the transfer of files from Amazon RDS or Amazon Aurora to an S3 bucket:  
+ s3:PutObject\*
+ s3:GetObject\*
+ s3:ListBucket
+ s3:DeleteObject\*
+ s3:GetBucketLocation 
In the policy, include the resources to identify the S3 bucket and objects in the bucket. The following list of resources shows the Amazon Resource Name (ARN) format for accessing S3:  
+  `arn:aws:s3:::your-s3-bucket ` 
+  `arn:aws:s3:::your-s3-bucket/*` 
Type: String  
Required: Yes

 ** KmsKeyId **   
The ID of the AWS KMS key to use to encrypt the data exported to Amazon S3. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. The caller of this operation must be authorized to run the following operations. These can be set in the AWS KMS key policy:  
+ kms:CreateGrant
+ kms:DescribeKey
Type: String  
Required: Yes

 ** S3BucketName **   
The name of the Amazon S3 bucket to export the snapshot or cluster data to.  
Type: String  
Required: Yes

 ** SourceArn **   
The Amazon Resource Name (ARN) of the snapshot or cluster to export to Amazon S3.  
Type: String  
Required: Yes

 **ExportOnly.member.N**   
The data to be exported from the snapshot or cluster. If this parameter isn't provided, all of the data is exported.  
Valid Values:  
+  `database` - Export all the data from a specified database.
+  `database.table` *table-name* - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.
+  `database.schema` *schema-name* - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
+  `database.schema.table` *table-name* - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
Type: Array of strings  
Required: No

 ** S3Prefix **   
The Amazon S3 bucket prefix to use as the file name and path of the exported data.  
Type: String  
Required: No

## Response Elements
<a name="API_StartExportTask_ResponseElements"></a>

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
<a name="API_StartExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** ExportTaskAlreadyExists **   
You can't start an export task that's already running.  
HTTP Status Code: 400

 ** IamRoleMissingPermissions **   
The IAM role requires additional permissions to export to an Amazon S3 bucket.  
HTTP Status Code: 400

 ** IamRoleNotFound **   
The IAM role is missing for exporting to an Amazon S3 bucket.  
HTTP Status Code: 404

 ** InvalidExportOnly **   
The export is invalid for exporting to an Amazon S3 bucket.  
HTTP Status Code: 400

 ** InvalidExportSourceState **   
The state of the export snapshot is invalid for exporting to an Amazon S3 bucket.  
HTTP Status Code: 400

 ** InvalidS3BucketFault **   
The specified Amazon S3 bucket name can't be found or Amazon RDS isn't authorized to access the specified Amazon S3 bucket. Verify the **SourceS3BucketName** and **S3IngestionRoleArn** values and try again.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

## See Also
<a name="API_StartExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StartExportTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StartExportTask) 