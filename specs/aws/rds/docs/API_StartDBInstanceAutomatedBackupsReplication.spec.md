---
id: "@specs/aws/rds/docs/API_StartDBInstanceAutomatedBackupsReplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartDBInstanceAutomatedBackupsReplication"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StartDBInstanceAutomatedBackupsReplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StartDBInstanceAutomatedBackupsReplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartDBInstanceAutomatedBackupsReplication
<a name="API_StartDBInstanceAutomatedBackupsReplication"></a>

Enables replication of automated backups to a different AWS Region.

This command doesn't apply to RDS Custom.

For more information, see [ Replicating Automated Backups to Another AWS Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_StartDBInstanceAutomatedBackupsReplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBInstanceArn **   
The Amazon Resource Name (ARN) of the source DB instance for the replicated automated backups, for example, `arn:aws:rds:us-west-2:123456789012:db:mydatabase`.  
Type: String  
Required: Yes

 ** BackupRetentionPeriod **   
The retention period for the replicated automated backups.  
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for encryption of the replicated automated backups. The KMS key ID is the Amazon Resource Name (ARN) for the KMS encryption key in the destination AWS Region, for example, `arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE`.  
Type: String  
Required: No

 ** PreSignedUrl **   
In an AWS GovCloud (US) Region, an URL that contains a Signature Version 4 signed request for the `StartDBInstanceAutomatedBackupsReplication` operation to call in the AWS Region of the source DB instance. The presigned URL must be a valid request for the `StartDBInstanceAutomatedBackupsReplication` API operation that can run in the AWS Region that contains the source DB instance.  
This setting applies only to AWS GovCloud (US) Regions. It's ignored in other AWS Regions.  
To learn how to generate a Signature Version 4 signed request, see [ Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [ Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).  
If you are using an AWS SDK tool or the AWS CLI, you can specify `SourceRegion` (or `--source-region` for the AWS CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source AWS Region.
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags to associate with the replicated automated backups.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_StartDBInstanceAutomatedBackupsReplication_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstanceAutomatedBackup **   
An automated backup of a DB instance. It consists of system backups, transaction logs, and the database instance properties that existed at the time you deleted the source instance.  
Type: [DBInstanceAutomatedBackup](API_DBInstanceAutomatedBackup.md) object

## Errors
<a name="API_StartDBInstanceAutomatedBackupsReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceAutomatedBackupQuotaExceeded **   
The quota for retained automated backups was exceeded. This prevents you from retaining any additional automated backups. The retained automated backups quota is the same as your DB instance quota.  
HTTP Status Code: 400

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceAutomatedBackupState **   
The automated backup is in an invalid state. For example, this automated backup is associated with an active instance.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

## See Also
<a name="API_StartDBInstanceAutomatedBackupsReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StartDBInstanceAutomatedBackupsReplication) 