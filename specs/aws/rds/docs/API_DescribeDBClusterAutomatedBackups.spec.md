---
id: "@specs/aws/rds/docs/API_DescribeDBClusterAutomatedBackups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterAutomatedBackups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterAutomatedBackups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterAutomatedBackups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterAutomatedBackups
<a name="API_DescribeDBClusterAutomatedBackups"></a>

Displays backups for both current and deleted DB clusters. For example, use this operation to find details about automated backups for previously deleted clusters. Current clusters are returned for both the `DescribeDBClusterAutomatedBackups` and `DescribeDBClusters` operations.

All parameters are optional.

## Request Parameters
<a name="API_DescribeDBClusterAutomatedBackups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
(Optional) The user-supplied DB cluster identifier. If this parameter is specified, it must match the identifier of an existing DB cluster. It returns information from the specific DB cluster's automated backup. This parameter isn't case-sensitive.  
Type: String  
Required: No

 ** DbClusterResourceId **   
The resource ID of the DB cluster that is the source of the automated backup. This parameter isn't case-sensitive.  
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies which resources to return based on status.  
Supported filters are the following:  
+  `status` 
  +  `retained` - Automated backups for deleted clusters and after backup replication is stopped.
+  `db-cluster-id` - Accepts DB cluster identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB cluster automated backups identified by these ARNs.
+  `db-cluster-resource-id` - Accepts DB resource identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB cluster resources identified by these ARNs.
Returns all resources by default. The status for each resource is specified in the response.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBClusterAutomatedBackups_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterAutomatedBackups.DBClusterAutomatedBackup.N**   
A list of `DBClusterAutomatedBackup` backups.  
Type: Array of [DBClusterAutomatedBackup](API_DBClusterAutomatedBackup.md) objects

 ** Marker **   
The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBClusterAutomatedBackups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAutomatedBackupNotFoundFault **   
No automated backup for this DB cluster was found.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterAutomatedBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterAutomatedBackups) 