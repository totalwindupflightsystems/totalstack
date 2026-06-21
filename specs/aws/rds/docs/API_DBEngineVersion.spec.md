---
id: "@specs/aws/rds/docs/API_DBEngineVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBEngineVersion"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBEngineVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBEngineVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBEngineVersion
<a name="API_DBEngineVersion"></a>

This data type is used as a response element in the action `DescribeDBEngineVersions`.

## Contents
<a name="API_DBEngineVersion_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CreateTime **   
The creation time of the DB engine version.  
Type: Timestamp  
Required: No

 ** CustomDBEngineVersionManifest **   
JSON string that lists the installation files and parameters that RDS Custom uses to create a custom engine version (CEV). RDS Custom applies the patches in the order in which they're listed in the manifest. You can set the Oracle home, Oracle base, and UNIX/Linux user and group using the installation parameters. For more information, see [JSON fields in the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.preparing.html#custom-cev.preparing.manifest.fields) in the *Amazon RDS User Guide*.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 51000.  
Pattern: `[\s\S]*`   
Required: No

 ** DatabaseInstallationFiles.member.N **   
The database installation files (ISO and EXE) that were uploaded to Amazon S3 and used to import the database engine version to Amazon RDS. Returned for RDS for SQL Server engine versions (`sqlserver-ee`, `sqlserver-se`, and `sqlserver-dev-ee`) created from customer-supplied installation media.  
Type: Array of strings  
Required: No

 ** DatabaseInstallationFilesS3BucketName **   
The name of the Amazon S3 bucket that contains your database installation files.  
Type: String  
Required: No

 ** DatabaseInstallationFilesS3Prefix **   
The Amazon S3 directory that contains the database installation files. If not specified, then no prefix is assumed.  
Type: String  
Required: No

 ** DBEngineDescription **   
The description of the database engine.  
Type: String  
Required: No

 ** DBEngineMediaType **   
The source of the installation media for this engine version. A value of `Customer Provided` indicates that the engine version was created from customer-supplied installation media using `CreateCustomDBEngineVersion`. Applicable to RDS Custom for SQL Server and to RDS for SQL Server engine versions (`sqlserver-ee` and `sqlserver-se` with the `bring-your-own-media` license model, and `sqlserver-dev-ee`).  
Type: String  
Required: No

 ** DBEngineVersionArn **   
The ARN of the custom engine version.  
Type: String  
Required: No

 ** DBEngineVersionDescription **   
The description of the database engine version.  
Type: String  
Required: No

 ** DBParameterGroupFamily **   
The name of the DB parameter group family for the database engine.  
Type: String  
Required: No

 ** DefaultCharacterSet **   
The default character set for new instances of this engine version, if the `CharacterSetName` parameter of the CreateDBInstance API isn't specified.  
Type: [CharacterSet](API_CharacterSet.md) object  
Required: No

 ** Engine **   
The name of the database engine.  
Type: String  
Required: No

 ** EngineVersion **   
The version number of the database engine.  
Type: String  
Required: No

 ** ExportableLogTypes.member.N **   
The types of logs that the database engine has available for export to CloudWatch Logs.  
Type: Array of strings  
Required: No

 ** FailureReason **   
The reason that the custom engine version creation failed with an `incompatible-installation-media` status. Applicable to RDS for SQL Server engine versions (`sqlserver-ee`, `sqlserver-se`, and `sqlserver-dev-ee`).  
Type: String  
Required: No

 ** Image **   
The EC2 image  
Type: [CustomDBEngineVersionAMI](API_CustomDBEngineVersionAMI.md) object  
Required: No

 ** KMSKeyId **   
The AWS KMS key identifier for an encrypted CEV. This parameter is required for RDS Custom, but optional for Amazon RDS.  
Type: String  
Required: No

 ** MajorEngineVersion **   
The major engine version of the CEV.  
Type: String  
Required: No

 ** ServerlessV2FeaturesSupport **   
Specifies any Aurora Serverless v2 properties or limits that differ between Aurora engine versions. You can test the values of this attribute when deciding which Aurora version to use in a new or upgraded DB cluster. You can also retrieve the version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.   
Type: [ServerlessV2FeaturesSupport](API_ServerlessV2FeaturesSupport.md) object  
Required: No

 ** Status **   
The status of the DB engine version, either `available` or `deprecated`.  
Type: String  
Required: No

 ** SupportedCACertificateIdentifiers.member.N **   
A list of the supported CA certificate identifiers.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: Array of strings  
Required: No

 ** SupportedCharacterSets.CharacterSet.N **   
A list of the character sets supported by this engine for the `CharacterSetName` parameter of the `CreateDBInstance` operation.  
Type: Array of [CharacterSet](API_CharacterSet.md) objects  
Required: No

 ** SupportedEngineModes.member.N **   
A list of the supported DB engine modes.  
Type: Array of strings  
Required: No

 ** SupportedFeatureNames.member.N **   
A list of features supported by the DB engine.  
The supported features vary by DB engine and DB engine version.  
To determine the supported features for a specific DB engine and DB engine version using the AWS CLI, use the following command:  
 `aws rds describe-db-engine-versions --engine <engine_name> --engine-version <engine_version>`   
For example, to determine the supported features for RDS for PostgreSQL version 13.3 using the AWS CLI, use the following command:  
 `aws rds describe-db-engine-versions --engine postgres --engine-version 13.3`   
The supported features are listed under `SupportedFeatureNames` in the output.  
Type: Array of strings  
Required: No

 ** SupportedNcharCharacterSets.CharacterSet.N **   
A list of the character sets supported by the Oracle DB engine for the `NcharCharacterSetName` parameter of the `CreateDBInstance` operation.  
Type: Array of [CharacterSet](API_CharacterSet.md) objects  
Required: No

 ** SupportedTimezones.Timezone.N **   
A list of the time zones supported by this engine for the `Timezone` parameter of the `CreateDBInstance` action.  
Type: Array of [Timezone](API_Timezone.md) objects  
Required: No

 ** SupportsBabelfish **   
Indicates whether the engine version supports Babelfish for Aurora PostgreSQL.  
Type: Boolean  
Required: No

 ** SupportsCertificateRotationWithoutRestart **   
Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.  
Type: Boolean  
Required: No

 ** SupportsGlobalDatabases **   
Indicates whether you can use Aurora global databases with a specific DB engine version.  
Type: Boolean  
Required: No

 ** SupportsIntegrations **   
Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.  
Type: Boolean  
Required: No

 ** SupportsLimitlessDatabase **   
Indicates whether the DB engine version supports Aurora Limitless Database.  
Type: Boolean  
Required: No

 ** SupportsLocalWriteForwarding **   
Indicates whether the DB engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.  
Valid for: Aurora DB clusters only  
Type: Boolean  
Required: No

 ** SupportsLogExportsToCloudwatchLogs **   
Indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.  
Type: Boolean  
Required: No

 ** SupportsParallelQuery **   
Indicates whether you can use Aurora parallel query with a specific DB engine version.  
Type: Boolean  
Required: No

 ** SupportsReadReplica **   
Indicates whether the database engine version supports read replicas.  
Type: Boolean  
Required: No

 ** TagList.Tag.N **   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** ValidUpgradeTarget.UpgradeTarget.N **   
A list of engine versions that this database engine version can be upgraded to.  
Type: Array of [UpgradeTarget](API_UpgradeTarget.md) objects  
Required: No

## See Also
<a name="API_DBEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBEngineVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBEngineVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBEngineVersion) 