---
id: "@specs/aws/rds/docs/API_FailoverGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailoverGlobalCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# FailoverGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_FailoverGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailoverGlobalCluster
<a name="API_FailoverGlobalCluster"></a>

Promotes the specified secondary DB cluster to be the primary DB cluster in the global database cluster to fail over or switch over a global database. Switchover operations were previously called "managed planned failovers."

**Note**  
Although this operation can be used either to fail over or to switch over a global database cluster, its intended use is for global database failover. To switch over a global database cluster, we recommend that you use the [SwitchoverGlobalCluster](API_SwitchoverGlobalCluster.md) operation instead.

How you use this operation depends on whether you are failing over or switching over your global database cluster:
+ Failing over - Specify the `AllowDataLoss` parameter and don't specify the `Switchover` parameter.
+ Switching over - Specify the `Switchover` parameter or omit it, but don't specify the `AllowDataLoss` parameter.

 **About failing over and switching over** 

While failing over and switching over a global database cluster both change the primary DB cluster, you use these operations for different reasons:
+  *Failing over* - Use this operation to respond to an unplanned event, such as a Regional disaster in the primary Region. Failing over can result in a loss of write transaction data that wasn't replicated to the chosen secondary before the failover event occurred. However, the recovery process that promotes a DB instance on the chosen seconday DB cluster to be the primary writer DB instance guarantees that the data is in a transactionally consistent state.

  For more information about failing over an Amazon Aurora global database, see [Performing managed failovers for Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover.managed-unplanned) in the *Amazon Aurora User Guide*.
+  *Switching over* - Use this operation on a healthy global database cluster for planned events, such as Regional rotation or to fail back to the original primary DB cluster after a failover operation. With this operation, there is no data loss.

  For more information about switching over an Amazon Aurora global database, see [Performing switchovers for Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_FailoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The identifier of the global database cluster (Aurora global database) this operation should apply to. The identifier is the unique key assigned by the user when the Aurora global database is created. In other words, it's the name of the Aurora global database.  
Constraints:  
+ Must match the identifier of an existing global database cluster.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** TargetDbClusterIdentifier **   
The identifier of the secondary Aurora DB cluster that you want to promote to the primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Aurora can locate the cluster in its AWS Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** AllowDataLoss **   
Specifies whether to allow data loss for this global database cluster operation. Allowing data loss triggers a global failover operation.  
If you don't specify `AllowDataLoss`, the global database cluster operation defaults to a switchover.  
Constraints:  
+ Can't be specified together with the `Switchover` parameter.
Type: Boolean  
Required: No

 ** Switchover **   
Specifies whether to switch over this global database cluster.  
Constraints:  
+ Can't be specified together with the `AllowDataLoss` parameter.
Type: Boolean  
Required: No

## Response Elements
<a name="API_FailoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Aurora global database.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_FailoverGlobalCluster_Errors"></a>

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
<a name="API_FailoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/FailoverGlobalCluster) 