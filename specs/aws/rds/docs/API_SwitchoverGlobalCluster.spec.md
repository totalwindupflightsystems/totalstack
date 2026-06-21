---
id: "@specs/aws/rds/docs/API_SwitchoverGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SwitchoverGlobalCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# SwitchoverGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_SwitchoverGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SwitchoverGlobalCluster
<a name="API_SwitchoverGlobalCluster"></a>

Switches over the specified secondary DB cluster to be the new primary DB cluster in the global database cluster. Switchover operations were previously called "managed planned failovers."

Aurora promotes the specified secondary cluster to assume full read/write capabilities and demotes the current primary cluster to a secondary (read-only) cluster, maintaining the orginal replication topology. All secondary clusters are synchronized with the primary at the beginning of the process so the new primary continues operations for the Aurora global database without losing any data. Your database is unavailable for a short time while the primary and selected secondary clusters are assuming their new roles. For more information about switching over an Aurora global database, see [Performing switchovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover) in the *Amazon Aurora User Guide*.

**Note**  
This operation is intended for controlled environments, for operations such as "regional rotation" or to fall back to the original primary after a global database failover.

## Request Parameters
<a name="API_SwitchoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The identifier of the global database cluster to switch over. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing global database cluster (Aurora global database).
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** TargetDbClusterIdentifier **   
The identifier of the secondary Aurora DB cluster to promote to the new primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Aurora can locate the cluster in its AWS Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

## Response Elements
<a name="API_SwitchoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Aurora global database.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_SwitchoverGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The global cluster is in an invalid state and can't perform the requested operation.  
HTTP Status Code: 400

## See Also
<a name="API_SwitchoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/SwitchoverGlobalCluster) 