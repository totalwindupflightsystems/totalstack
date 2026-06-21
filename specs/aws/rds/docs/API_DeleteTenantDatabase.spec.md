---
id: "@specs/aws/rds/docs/API_DeleteTenantDatabase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTenantDatabase"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteTenantDatabase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteTenantDatabase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTenantDatabase
<a name="API_DeleteTenantDatabase"></a>

Deletes a tenant database from your DB instance. This command only applies to RDS for Oracle container database (CDB) instances.

You can't delete a tenant database when it is the only tenant in the DB instance.

## Request Parameters
<a name="API_DeleteTenantDatabase_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The user-supplied identifier for the DB instance that contains the tenant database that you want to delete.  
Type: String  
Required: Yes

 ** TenantDBName **   
The user-supplied name of the tenant database that you want to remove from your DB instance. Amazon RDS deletes the tenant database with this name. This parameter isn’t case-sensitive.  
Type: String  
Required: Yes

 ** FinalDBSnapshotIdentifier **   
The `DBSnapshotIdentifier` of the new `DBSnapshot` created when the `SkipFinalSnapshot` parameter is disabled.  
If you enable this parameter and also enable `SkipFinalShapshot`, the command results in an error.
Type: String  
Required: No

 ** SkipFinalSnapshot **   
Specifies whether to skip the creation of a final DB snapshot before removing the tenant database from your DB instance. If you enable this parameter, RDS doesn't create a DB snapshot. If you don't enable this parameter, RDS creates a DB snapshot before it deletes the tenant database. By default, RDS doesn't skip the final snapshot. If you don't enable this parameter, you must specify the `FinalDBSnapshotIdentifier` parameter.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DeleteTenantDatabase_ResponseElements"></a>

The following element is returned by the service.

 ** TenantDatabase **   
A tenant database in the DB instance. This data type is an element in the response to the `DescribeTenantDatabases` action.  
Type: [TenantDatabase](API_TenantDatabase.md) object

## Errors
<a name="API_DeleteTenantDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **   
 `DBSnapshotIdentifier` is already used by an existing snapshot.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** TenantDatabaseNotFound **   
The specified tenant database wasn't found in the DB instance.  
HTTP Status Code: 404

## See Also
<a name="API_DeleteTenantDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteTenantDatabase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteTenantDatabase) 