---
id: "@specs/aws/rds/docs/API_CreateTenantDatabase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTenantDatabase"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateTenantDatabase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateTenantDatabase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTenantDatabase
<a name="API_CreateTenantDatabase"></a>

Creates a tenant database in a DB instance that uses the multi-tenant configuration. Only RDS for Oracle container database (CDB) instances are supported.

## Request Parameters
<a name="API_CreateTenantDatabase_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The user-supplied DB instance identifier. RDS creates your tenant database in this DB instance. This parameter isn't case-sensitive.  
Type: String  
Required: Yes

 ** MasterUsername **   
The name for the master user account in your tenant database. RDS creates this user account in the tenant database and grants privileges to the master user. This parameter is case-sensitive.  
Constraints:  
+ Must be 1 to 16 letters, numbers, or underscores.
+ First character must be a letter.
+ Can't be a reserved word for the chosen database engine.
Type: String  
Required: Yes

 ** TenantDBName **   
The user-supplied name of the tenant database that you want to create in your DB instance. This parameter has the same constraints as `DBName` in `CreateDBInstance`.  
Type: String  
Required: Yes

 ** CharacterSetName **   
The character set for your tenant database. If you don't specify a value, the character set name defaults to `AL32UTF8`.  
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
Type: Boolean  
Required: No

 ** MasterUserPassword **   
The password for the master user in your tenant database.  
Constraints:  
+ Must be 8 to 30 characters.
+ Can include any printable ASCII character except forward slash (`/`), double quote (`"`), at symbol (`@`), ampersand (`&`), or single quote (`'`).
+ Can't be specified when `ManageMasterUserPassword` is enabled.
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB instance.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.  
There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** NcharCharacterSetName **   
The `NCHAR` value for the tenant database.  
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateTenantDatabase_ResponseElements"></a>

The following element is returned by the service.

 ** TenantDatabase **   
A tenant database in the DB instance. This data type is an element in the response to the `DescribeTenantDatabases` action.  
Type: [TenantDatabase](API_TenantDatabase.md) object

## Errors
<a name="API_CreateTenantDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** TenantDatabaseAlreadyExists **   
You attempted to either create a tenant database that already exists or modify a tenant database to use the name of an existing tenant database.  
HTTP Status Code: 400

 ** TenantDatabaseQuotaExceeded **   
You attempted to create more tenant databases than are permitted in your AWS account.  
HTTP Status Code: 400

## See Also
<a name="API_CreateTenantDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateTenantDatabase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateTenantDatabase) 