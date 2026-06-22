---
id: "@specs/aws/docdb/docs/API_RestoreDBClusterToPointInTime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreDBClusterToPointInTime"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RestoreDBClusterToPointInTime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_RestoreDBClusterToPointInTime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreDBClusterToPointInTime
<a name="API_RestoreDBClusterToPointInTime"></a>

Restores a cluster to an arbitrary point in time. Users can restore to any point in time before `LatestRestorableTime` for up to `BackupRetentionPeriod` days. The target cluster is created from the source cluster with the same configuration as the original cluster, except that the new cluster is created with the default security group. 

## Request Parameters
<a name="API_RestoreDBClusterToPointInTime_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The name of the new cluster to be created.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: Yes

 ** SourceDBClusterIdentifier **   
The identifier of the source cluster from which to restore.  
Constraints:  
+ Must match the identifier of an existing `DBCluster`.
Type: String  
Required: Yes

 ** DBSubnetGroupName **   
The subnet group name to use for the new cluster.  
Constraints: If provided, must match the name of an existing `DBSubnetGroup`.  
Example: `mySubnetgroup`   
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether this cluster can be deleted. If `DeletionProtection` is enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled. `DeletionProtection` protects clusters from being accidentally deleted.  
Type: Boolean  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.  
Type: Array of strings  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier to use when restoring an encrypted cluster from an encrypted cluster.  
The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.  
You can restore to a new cluster and encrypt the new cluster with an AWS KMS key that is different from the AWS KMS key used to encrypt the source cluster. The new DB cluster is encrypted with the AWS KMS key identified by the `KmsKeyId` parameter.  
If you do not specify a value for the `KmsKeyId` parameter, then the following occurs:  
+ If the cluster is encrypted, then the restored cluster is encrypted using the AWS KMS key that was used to encrypt the source cluster.
+ If the cluster is not encrypted, then the restored cluster is not encrypted.
If `DBClusterIdentifier` refers to a cluster that is not encrypted, then the restore request is rejected.  
Type: String  
Required: No

 ** NetworkType **   
The network type of the cluster.  
The network type is determined by the `DBSubnetGroup` specified for the cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [DocumentDB clusters in a VPC](https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html) in the Amazon DocumentDB Developer Guide.  
Valid Values: `IPV4` \| `DUAL`   
Type: String  
Required: No

 ** Port **   
The port number on which the new cluster accepts connections.  
Constraints: Must be a value from `1150` to `65535`.   
Default: The default port for the engine.  
Type: Integer  
Required: No

 ** RestoreToTime **   
The date and time to restore the cluster to.  
Valid values: A time in Universal Coordinated Time (UTC) format.  
Constraints:  
+ Must be before the latest restorable time for the instance.
+ Must be specified if the `UseLatestRestorableTime` parameter is not provided.
+ Cannot be specified if the `UseLatestRestorableTime` parameter is `true`.
+ Cannot be specified if the `RestoreType` parameter is `copy-on-write`.
Example: `2015-03-07T23:45:00Z`   
Type: Timestamp  
Required: No

 ** RestoreType **   
The type of restore to be performed. You can specify one of the following values:  
+  `full-copy` - The new DB cluster is restored as a full copy of the source DB cluster.
+  `copy-on-write` - The new DB cluster is restored as a clone of the source DB cluster.
Constraints: You can't specify `copy-on-write` if the engine version of the source DB cluster is earlier than 1.11.  
If you don't specify a `RestoreType` value, then the new DB cluster is restored as a full copy of the source DB cluster.  
Type: String  
Required: No

 ** ServerlessV2ScalingConfiguration **   
Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.  
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object  
Required: No

 ** StorageType **   
The storage type to associate with the DB cluster.  
For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide*.  
Valid values for storage type - `standard | iopt1`   
Default value is `standard `   
Type: String  
Required: No

 **Tags.Tag.N**   
The tags to be assigned to the restored cluster.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** UseLatestRestorableTime **   
A value that is set to `true` to restore the cluster to the latest restorable backup time, and `false` otherwise.   
Default: `false`   
Constraints: Cannot be specified if the `RestoreToTime` parameter is provided.  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of VPC security groups that the new cluster belongs to.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_RestoreDBClusterToPointInTime_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_RestoreDBClusterToPointInTime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **   
You already have a cluster with the given identifier.  
HTTP Status Code: 400

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** DBClusterQuotaExceededFault **   
The cluster can't be created because you have reached the maximum allowed quota of clusters.  
HTTP Status Code: 403

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** InsufficientDBClusterCapacityFault **   
The cluster doesn't have enough capacity for the current operation.  
HTTP Status Code: 403

 ** InsufficientStorageClusterCapacity **   
There is not enough storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.   
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **   
The provided value isn't a valid cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBSnapshotState **   
The state of the snapshot doesn't allow deletion.  
HTTP Status Code: 400

 ** InvalidRestoreFault **   
You cannot restore from a virtual private cloud (VPC) backup to a non-VPC DB instance.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred when accessing an AWS KMS key.  
HTTP Status Code: 400

 ** NetworkTypeNotSupported **   
The network type is not supported by either `DBSubnetGroup` or the DB engine version.  
HTTP Status Code: 400

 ** StorageQuotaExceeded **   
The request would cause you to exceed the allowed amount of storage available across all instances.  
HTTP Status Code: 400

## See Also
<a name="API_RestoreDBClusterToPointInTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/RestoreDBClusterToPointInTime) 