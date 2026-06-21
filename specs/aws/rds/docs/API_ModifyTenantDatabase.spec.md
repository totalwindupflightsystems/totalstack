---
id: "@specs/aws/rds/docs/API_ModifyTenantDatabase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyTenantDatabase"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyTenantDatabase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyTenantDatabase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyTenantDatabase
<a name="API_ModifyTenantDatabase"></a>

Modifies an existing tenant database in a DB instance. You can change the tenant database name or the master user password. This operation is supported only for RDS for Oracle CDB instances using the multi-tenant configuration.

## Request Parameters
<a name="API_ModifyTenantDatabase_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The identifier of the DB instance that contains the tenant database that you are modifying. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing DB instance.
Type: String  
Required: Yes

 ** TenantDBName **   
The user-supplied name of the tenant database that you want to modify. This parameter isn’t case-sensitive.  
Constraints:  
+ Must match the identifier of an existing tenant database.
Type: String  
Required: Yes

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with AWS Secrets Manager.  
If the tenant database doesn't manage the master user password with AWS Secrets Manager, you can turn on this management. In this case, you can't specify `MasterUserPassword`.  
If the tenant database already manages the master user password with AWS Secrets Manager, and you specify that the master user password is not managed with AWS Secrets Manager, then you must specify `MasterUserPassword`. In this case, Amazon RDS deletes the secret and uses the new password for the master user specified by `MasterUserPassword`.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ Can't manage the master user password with AWS Secrets Manager if `MasterUserPassword` is specified.
Type: Boolean  
Required: No

 ** MasterUserPassword **   
The new password for the master user of the specified tenant database in your DB instance.  
Amazon RDS operations never return the password, so this action provides a way to regain access to a tenant database user if the password is lost. This includes restoring privileges that might have been accidentally revoked.
Constraints:  
+ Can include any printable ASCII character except `/`, `"` (double quote), `@`, `&` (ampersand), and `'` (single quote).
Length constraints:  
+ Must contain between 8 and 30 characters. 
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The AWS KMS key identifier to encrypt a secret that is automatically generated and managed in AWS Secrets Manager.  
This setting is valid only if both of the following conditions are met:  
+ The tenant database doesn't manage the master user password in AWS Secrets Manager.

  If the tenant database already manages the master user password in AWS Secrets Manager, you can't change the KMS key used to encrypt the secret.
+ You're turning on `ManageMasterUserPassword` to manage the master user password in AWS Secrets Manager.

  If you're turning on `ManageMasterUserPassword` and don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different AWS account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a self-managed KMS key.
The AWS KMS key identifier is any of the following:  
+ Key ARN
+ Key ID
+ Alias ARN
+ Alias name for the KMS key
To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
A default KMS key exists for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** NewTenantDBName **   
The new name of the tenant database when renaming a tenant database. This parameter isn’t case-sensitive.  
Constraints:  
+ Can't be the string null or any other reserved word.
+ Can't be longer than 8 characters.
Type: String  
Required: No

 ** RotateMasterUserPassword **   
Specifies whether to rotate the secret managed by AWS Secrets Manager for the master user password.  
This setting is valid only if the master user password is managed by RDS in AWS Secrets Manager for the DB instance. The secret value contains the updated password.  
For more information, see [Password management with AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*   
Constraints:  
+ You must apply the change immediately when rotating the master user password.
Type: Boolean  
Required: No

## Response Elements
<a name="API_ModifyTenantDatabase_ResponseElements"></a>

The following element is returned by the service.

 ** TenantDatabase **   
A tenant database in the DB instance. This data type is an element in the response to the `DescribeTenantDatabases` action.  
Type: [TenantDatabase](API_TenantDatabase.md) object

## Errors
<a name="API_ModifyTenantDatabase_Errors"></a>

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

 ** TenantDatabaseNotFound **   
The specified tenant database wasn't found in the DB instance.  
HTTP Status Code: 404

## See Also
<a name="API_ModifyTenantDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyTenantDatabase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyTenantDatabase) 