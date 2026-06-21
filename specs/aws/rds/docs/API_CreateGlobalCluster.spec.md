---
id: "@specs/aws/rds/docs/API_CreateGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateGlobalCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateGlobalCluster
<a name="API_CreateGlobalCluster"></a>

Creates an Aurora global database spread across multiple AWS Regions. The global database contains a single primary cluster with read-write capability, and a read-only secondary cluster that receives data from the primary cluster through high-speed replication performed by the Aurora storage subsystem.

You can create a global database that is initially empty, and then create the primary and secondary DB clusters in the global database. Or you can specify an existing Aurora cluster during the create operation, and this cluster becomes the primary cluster of the global database.

**Note**  
This operation applies only to Aurora DB clusters.

## Request Parameters
<a name="API_CreateGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The cluster identifier for this global database cluster. This parameter is stored as a lowercase string.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** DatabaseName **   
The name for your database of up to 64 alphanumeric characters. If you don't specify a name, Amazon Aurora doesn't create a database in the global database cluster.  
Constraints:  
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the database name from the source DB cluster.
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether to enable deletion protection for the new global database cluster. The global database can't be deleted when deletion protection is enabled.  
Type: Boolean  
Required: No

 ** Engine **   
The database engine to use for this global database cluster.  
Valid Values: `aurora-mysql | aurora-postgresql`   
Constraints:  
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the engine of the source DB cluster.
Type: String  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this global database cluster.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your global cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, creating the global cluster will fail if the DB major version is past its end of standard support date.
This setting only applies to Aurora PostgreSQL-based global databases.  
You can use this setting to enroll your global cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your global cluster past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide*.  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** EngineVersion **   
The engine version to use for this global database cluster.  
Constraints:  
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the engine version of the source DB cluster.
Type: String  
Required: No

 ** SourceDBClusterIdentifier **   
The Amazon Resource Name (ARN) to use as the primary cluster of the global database.  
If you provide a value for this parameter, don't specify values for the following settings because Amazon Aurora uses the values from the specified source DB cluster:  
+  `DatabaseName` 
+  `Engine` 
+  `EngineVersion` 
+  `StorageEncrypted` 
Type: String  
Required: No

 ** StorageEncrypted **   
Specifies whether to enable storage encryption for the new global database cluster.  
Constraints:  
+ Can't be specified if `SourceDBClusterIdentifier` is specified. In this case, Amazon Aurora uses the setting from the source DB cluster.
Type: Boolean  
Required: No

 **Tags.Tag.N**   
Tags to assign to the global cluster.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Aurora global database.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_CreateGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** GlobalClusterAlreadyExistsFault **   
The `GlobalClusterIdentifier` already exists. Specify a new global database identifier (unique name) to create a new global database cluster or to rename an existing one.  
HTTP Status Code: 400

 ** GlobalClusterQuotaExceededFault **   
The number of global database clusters for this account is already at the maximum allowed.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBShardGroupState **   
The DB shard group must be in the available state.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_CreateGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateGlobalCluster) 