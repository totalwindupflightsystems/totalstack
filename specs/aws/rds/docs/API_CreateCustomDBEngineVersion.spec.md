---
id: "@specs/aws/rds/docs/API_CreateCustomDBEngineVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomDBEngineVersion"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateCustomDBEngineVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateCustomDBEngineVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomDBEngineVersion
<a name="API_CreateCustomDBEngineVersion"></a>

Creates a custom DB engine version (CEV).

## Request Parameters
<a name="API_CreateCustomDBEngineVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **   
The database engine.  
RDS Custom for Oracle supports the following values:  
+  `custom-oracle-ee` 
+  `custom-oracle-ee-cdb` 
+  `custom-oracle-se2` 
+  `custom-oracle-se2-cdb` 
RDS Custom for SQL Server supports the following values:  
+  `custom-sqlserver-ee` 
+  `custom-sqlserver-se` 
+  `custom-sqlserver-web` 
+  `custom-sqlserver-dev` 
RDS for SQL Server supports the following values:  
+  `sqlserver-ee` (Bring Your Own Media)
+  `sqlserver-se` (Bring Your Own Media)
+  `sqlserver-dev-ee` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[A-Za-z0-9-]{1,35}`   
Required: Yes

 ** EngineVersion **   
The name of your custom engine version (CEV).  
For RDS Custom for Oracle, the name format is `19.*customized_string*`. For example, a valid CEV name is `19.my_cev1`.  
For RDS Custom for SQL Server and RDS for SQL Server `sqlserver-dev-ee`, the name format is `*major_engine_version*.*minor_engine_version*.*customized_string*`. For example, a valid CEV name is `16.00.4215.2.my_cev1`.  
For RDS for SQL Server Bring Your Own Media (`sqlserver-ee`, `sqlserver-se`), specify the RDS engine version that you want to use. For example, `16.00.4175.1.v1`.  
The CEV name is unique per customer per AWS Regions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 60.  
Pattern: `[a-z0-9_.-]{1,60}`   
Required: Yes

 **DatabaseInstallationFiles.member.N**   
The database installation files (ISO and EXE) uploaded to Amazon S3 for your database engine version to import to Amazon RDS.  
For RDS for SQL Server Bring Your Own Media (`sqlserver-ee`, `sqlserver-se`), provide the SQL Server RTM ISO file once per major version and edition combination. Minor versions reuse the same file.  
Type: Array of strings  
Required: No

 ** DatabaseInstallationFilesS3BucketName **   
The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `.*`   
Required: No

 ** DatabaseInstallationFilesS3Prefix **   
The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `.*`   
Required: No

 ** Description **   
An optional description of your CEV.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** ImageId **   
The ID of the Amazon Machine Image (AMI). For RDS Custom for SQL Server, an AMI ID is required to create a CEV. For RDS Custom for Oracle, the default is the most recent AMI available, but you can specify an AMI ID that was used in a different Oracle CEV. Find the AMIs used by your CEVs by calling the [DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBEngineVersions.html) operation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `.*`   
Required: No

 ** KMSKeyId **   
The AWS KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.  
If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you don't already have a symmetric encryption KMS key in your account, follow the instructions in [ Creating a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the * AWS Key Management Service Developer Guide*.  
You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9_:\-\/]+`   
Required: No

 ** Manifest **   
The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.  
The following JSON fields are valid:    
MediaImportTemplateVersion  
Version of the CEV manifest. The date is in the format `YYYY-MM-DD`.  
databaseInstallationFileNames  
Ordered list of installation files for the CEV.  
opatchFileNames  
Ordered list of OPatch installers used for the Oracle DB engine.  
psuRuPatchFileNames  
The PSU and RU patches for this CEV.  
OtherPatchFileNames  
The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches.
For more information, see [ Creating the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest) in the *Amazon RDS User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 51000.  
Pattern: `[\s\S]*`   
Required: No

 ** SourceCustomDbEngineVersionIdentifier **   
The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either `Source` or `UseAwsProvidedLatestImage`. You can't specify a different JSON manifest when you specify `SourceCustomDbEngineVersionIdentifier`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `.*`   
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** UseAwsProvidedLatestImage **   
Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify `UseAwsProvidedLatestImage`, you can't also specify `ImageId`.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_CreateCustomDBEngineVersion_ResponseElements"></a>

The following elements are returned by the service.

 ** CreateTime **   
The creation time of the DB engine version.  
Type: Timestamp

 ** CustomDBEngineVersionManifest **   
JSON string that lists the installation files and parameters that RDS Custom uses to create a custom engine version (CEV). RDS Custom applies the patches in the order in which they're listed in the manifest. You can set the Oracle home, Oracle base, and UNIX/Linux user and group using the installation parameters. For more information, see [JSON fields in the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.preparing.html#custom-cev.preparing.manifest.fields) in the *Amazon RDS User Guide*.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 51000.  
Pattern: `[\s\S]*` 

 **DatabaseInstallationFiles.member.N**   
The database installation files (ISO and EXE) that were uploaded to Amazon S3 and used to import the database engine version to Amazon RDS. Returned for RDS for SQL Server engine versions (`sqlserver-ee`, `sqlserver-se`, and `sqlserver-dev-ee`) created from customer-supplied installation media.  
Type: Array of strings

 ** DatabaseInstallationFilesS3BucketName **   
The name of the Amazon S3 bucket that contains your database installation files.  
Type: String

 ** DatabaseInstallationFilesS3Prefix **   
The Amazon S3 directory that contains the database installation files. If not specified, then no prefix is assumed.  
Type: String

 ** DBEngineDescription **   
The description of the database engine.  
Type: String

 ** DBEngineMediaType **   
The source of the installation media for this engine version. A value of `Customer Provided` indicates that the engine version was created from customer-supplied installation media using `CreateCustomDBEngineVersion`. Applicable to RDS Custom for SQL Server and to RDS for SQL Server engine versions (`sqlserver-ee` and `sqlserver-se` with the `bring-your-own-media` license model, and `sqlserver-dev-ee`).  
Type: String

 ** DBEngineVersionArn **   
The ARN of the custom engine version.  
Type: String

 ** DBEngineVersionDescription **   
The description of the database engine version.  
Type: String

 ** DBParameterGroupFamily **   
The name of the DB parameter group family for the database engine.  
Type: String

 ** DefaultCharacterSet **   
The default character set for new instances of this engine version, if the `CharacterSetName` parameter of the CreateDBInstance API isn't specified.  
Type: [CharacterSet](API_CharacterSet.md) object

 ** Engine **   
The name of the database engine.  
Type: String

 ** EngineVersion **   
The version number of the database engine.  
Type: String

 **ExportableLogTypes.member.N**   
The types of logs that the database engine has available for export to CloudWatch Logs.  
Type: Array of strings

 ** FailureReason **   
The reason that the custom engine version creation failed with an `incompatible-installation-media` status. Applicable to RDS for SQL Server engine versions (`sqlserver-ee`, `sqlserver-se`, and `sqlserver-dev-ee`).  
Type: String

 ** Image **   
The EC2 image  
Type: [CustomDBEngineVersionAMI](API_CustomDBEngineVersionAMI.md) object

 ** KMSKeyId **   
The AWS KMS key identifier for an encrypted CEV. This parameter is required for RDS Custom, but optional for Amazon RDS.  
Type: String

 ** MajorEngineVersion **   
The major engine version of the CEV.  
Type: String

 ** ServerlessV2FeaturesSupport **   
Specifies any Aurora Serverless v2 properties or limits that differ between Aurora engine versions. You can test the values of this attribute when deciding which Aurora version to use in a new or upgraded DB cluster. You can also retrieve the version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.   
Type: [ServerlessV2FeaturesSupport](API_ServerlessV2FeaturesSupport.md) object

 ** Status **   
The status of the DB engine version, either `available` or `deprecated`.  
Type: String

 **SupportedCACertificateIdentifiers.member.N**   
A list of the supported CA certificate identifiers.  
For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.  
Type: Array of strings

 **SupportedCharacterSets.CharacterSet.N**   
A list of the character sets supported by this engine for the `CharacterSetName` parameter of the `CreateDBInstance` operation.  
Type: Array of [CharacterSet](API_CharacterSet.md) objects

 **SupportedEngineModes.member.N**   
A list of the supported DB engine modes.  
Type: Array of strings

 **SupportedFeatureNames.member.N**   
A list of features supported by the DB engine.  
The supported features vary by DB engine and DB engine version.  
To determine the supported features for a specific DB engine and DB engine version using the AWS CLI, use the following command:  
 `aws rds describe-db-engine-versions --engine <engine_name> --engine-version <engine_version>`   
For example, to determine the supported features for RDS for PostgreSQL version 13.3 using the AWS CLI, use the following command:  
 `aws rds describe-db-engine-versions --engine postgres --engine-version 13.3`   
The supported features are listed under `SupportedFeatureNames` in the output.  
Type: Array of strings

 **SupportedNcharCharacterSets.CharacterSet.N**   
A list of the character sets supported by the Oracle DB engine for the `NcharCharacterSetName` parameter of the `CreateDBInstance` operation.  
Type: Array of [CharacterSet](API_CharacterSet.md) objects

 **SupportedTimezones.Timezone.N**   
A list of the time zones supported by this engine for the `Timezone` parameter of the `CreateDBInstance` action.  
Type: Array of [Timezone](API_Timezone.md) objects

 ** SupportsBabelfish **   
Indicates whether the engine version supports Babelfish for Aurora PostgreSQL.  
Type: Boolean

 ** SupportsCertificateRotationWithoutRestart **   
Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.  
Type: Boolean

 ** SupportsGlobalDatabases **   
Indicates whether you can use Aurora global databases with a specific DB engine version.  
Type: Boolean

 ** SupportsIntegrations **   
Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.  
Type: Boolean

 ** SupportsLimitlessDatabase **   
Indicates whether the DB engine version supports Aurora Limitless Database.  
Type: Boolean

 ** SupportsLocalWriteForwarding **   
Indicates whether the DB engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.  
Valid for: Aurora DB clusters only  
Type: Boolean

 ** SupportsLogExportsToCloudwatchLogs **   
Indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.  
Type: Boolean

 ** SupportsParallelQuery **   
Indicates whether you can use Aurora parallel query with a specific DB engine version.  
Type: Boolean

 ** SupportsReadReplica **   
Indicates whether the database engine version supports read replicas.  
Type: Boolean

 **TagList.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects

 **ValidUpgradeTarget.UpgradeTarget.N**   
A list of engine versions that this database engine version can be upgraded to.  
Type: Array of [UpgradeTarget](API_UpgradeTarget.md) objects

## Errors
<a name="API_CreateCustomDBEngineVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CreateCustomDBEngineVersionFault **   
An error occurred while trying to create the CEV.  
HTTP Status Code: 400

 ** CustomDBEngineVersionAlreadyExistsFault **   
A CEV with the specified name already exists.  
HTTP Status Code: 400

 ** CustomDBEngineVersionNotFoundFault **   
The specified CEV was not found.  
HTTP Status Code: 404

 ** CustomDBEngineVersionQuotaExceededFault **   
You have exceeded your CEV quota.  
HTTP Status Code: 400

 ** Ec2ImagePropertiesNotSupportedFault **   
The AMI configuration prerequisite has not been met.  
HTTP Status Code: 400

 ** InvalidCustomDBEngineVersionStateFault **   
You can't delete the CEV.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

## Examples
<a name="API_CreateCustomDBEngineVersion_Examples"></a>

### Example
<a name="API_CreateCustomDBEngineVersion_Example_1"></a>

This example illustrates one usage of CreateCustomDBEngineVersion.

#### Sample Request
<a name="API_CreateCustomDBEngineVersion_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Engine=custom-oracle-ee
    &EngineVersion=19.cev1
    &DatabaseInstallationFilesS3BucketName=1-custom-installation-files
    &DatabaseInstallationFilesS3Prefix=123456789012/cev1
    &KMSKeyId=12ab3c4d-5678-90e1-2fg3-45h6ijklmnops
    &Description=cev%20description
    &Manifest=%7B%22mediaImportTemplateVersion%22%3A%222020-08--14%22%2C%22databaseInstallationFileNames%22%3A%5B%22V982063-01.zip%22%5D%2C%22opatchFileNames%22%3A%5B%22p6880880_190000_Linux-x86-64.zip%22%5D%2C%22psuRuPatchFileNames%22%3A%5B%22p31720396_190000_Linux-x86-64.zip%22%2C%22p29213893_199000DBRU_Generic.zip%22%2C%22p28730253_190000_Linux-x86-64.zip%22%2C%22p29374604_199000DBRU_Linux-x86-64.zip%22%2C%22p28852325_190000_Linux-x86-64.zip%22%2C%22p29997937_190000_Linux-x86-64.zip%22%2C%22p31335037_190000_Linux-x86-64.zip%22%2C%22p31335142_190000_Generic.zip%22%5D%7D
```

#### Sample Response
<a name="API_CreateCustomDBEngineVersion_Example_1_Response"></a>

```
<CreateCustomDBEngineVersionResponse xmlns="http://rds.amazonaws.com/doc/1999-01-01/">
  <CreateCustomDBEngineVersionResult>
    <DatabaseInstallationFilesS3Prefix>123456789012/cev1</DatabaseInstallationFilesS3Prefix>
    <MajorEngineVersion>19</MajorEngineVersion>
    <DBEngineVersionArn>arn:aws:rds:us-east-1:123456789012:cev:custom-oracle-ee/19.cev1/123ab45c-abc1-1234-1234-123a45b12345</DBEngineVersionArn>
    <DBEngineVersionDescription>cev description</DBEngineVersionDescription>
    <SupportsGlobalDatabases>false</SupportsGlobalDatabases>
    <SupportsParallelQuery>false</SupportsParallelQuery>
    <Engine>custom-oracle-ee</Engine>
    <KMSKeyId>arn:aws:kms:us-east-1:123456789012:key/12ab3c4d-1234-12a3-1aa2-12a3bcdefghi</KMSKeyId>
    <EngineVersion>19.cev1</EngineVersion>
    <SupportsReadReplica>false</SupportsReadReplica>
    <SupportsCluster>false</SupportsCluster>
    <CreateTime>2021-10-13T22:15:11.157Z</CreateTime>
    <DatabaseInstallationFilesS3BucketName>1-custom-installation-files</DatabaseInstallationFilesS3BucketName>
    <SupportsLogExportsToCloudwatchLogs>false</SupportsLogExportsToCloudwatchLogs>
    <AMIs>
      <member>
        <Id>ami-123a4b5c678901d23</Id>
        <Status>validating</Status>
      </member>
    </AMIs>
    <DBEngineDescription>Oracle Database server EE for RDS Custom</DBEngineDescription>
    <Status>creating</Status>
  </CreateCustomDBEngineVersionResult>
  <ResponseMetadata>
    <RequestId>897d9e88-057a-4695-812c-29cd36ec89d5</RequestId>
  </ResponseMetadata>
</CreateCustomDBEngineVersionResponse>
```

## See Also
<a name="API_CreateCustomDBEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateCustomDBEngineVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateCustomDBEngineVersion) 