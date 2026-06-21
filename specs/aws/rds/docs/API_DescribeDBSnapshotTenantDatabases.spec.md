---
id: "@specs/aws/rds/docs/API_DescribeDBSnapshotTenantDatabases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBSnapshotTenantDatabases"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBSnapshotTenantDatabases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBSnapshotTenantDatabases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBSnapshotTenantDatabases
<a name="API_DescribeDBSnapshotTenantDatabases"></a>

Describes the tenant databases that exist in a DB snapshot. This command only applies to RDS for Oracle DB instances in the multi-tenant configuration.

You can use this command to inspect the tenant databases within a snapshot before restoring it. You can't directly interact with the tenant databases in a DB snapshot. If you restore a snapshot that was taken from DB instance using the multi-tenant configuration, you restore all its tenant databases.

## Request Parameters
<a name="API_DescribeDBSnapshotTenantDatabases_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The ID of the DB instance used to create the DB snapshots. This parameter isn't case-sensitive.  
Constraints:  
+ If supplied, must match the identifier of an existing `DBInstance`.
Type: String  
Required: No

 ** DbiResourceId **   
A specific DB resource identifier to describe.  
Type: String  
Required: No

 ** DBSnapshotIdentifier **   
The ID of a DB snapshot that contains the tenant databases to describe. This value is stored as a lowercase string.  
Constraints:  
+ If you specify this parameter, the value must match the ID of an existing DB snapshot.
+ If you specify an automatic snapshot, you must also specify `SnapshotType`.
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more tenant databases to describe.  
Supported filters:  
+  `tenant-db-name` - Tenant database names. The results list only includes information about the tenant databases that match these tenant DB names.
+  `tenant-database-resource-id` - Tenant database resource identifiers. The results list only includes information about the tenant databases contained within the DB snapshots.
+  `dbi-resource-id` - DB instance resource identifiers. The results list only includes information about snapshots containing tenant databases contained within the DB instances identified by these resource identifiers.
+  `db-instance-id` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).
+  `db-snapshot-id` - Accepts DB snapshot identifiers.
+  `snapshot-type` - Accepts types of DB snapshots.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBSnapshotTenantDatabases` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Type: Integer  
Required: No

 ** SnapshotType **   
The type of DB snapshots to be returned. You can specify one of the following values:  
+  `automated` – All DB snapshots that have been automatically taken by Amazon RDS for my Amazon Web Services account.
+  `manual` – All DB snapshots that have been taken by my Amazon Web Services account.
+  `shared` – All manual DB snapshots that have been shared to my Amazon Web Services account.
+  `public` – All DB snapshots that have been marked as public.
+  `awsbackup` – All DB snapshots managed by the AWS Backup service.
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBSnapshotTenantDatabases_ResponseElements"></a>

The following elements are returned by the service.

 **DBSnapshotTenantDatabases.DBSnapshotTenantDatabase.N**   
A list of DB snapshot tenant databases.  
Type: Array of [DBSnapshotTenantDatabase](API_DBSnapshotTenantDatabase.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBSnapshotTenantDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBSnapshotTenantDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBSnapshotTenantDatabases) 