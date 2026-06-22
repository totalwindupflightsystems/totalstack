---
id: "@specs/aws/docdb/docs/API_RestoreDBClusterFromSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreDBClusterFromSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RestoreDBClusterFromSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_RestoreDBClusterFromSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreDBClusterFromSnapshot
<a name="API_RestoreDBClusterFromSnapshot"></a>

Creates a new cluster from a snapshot or cluster snapshot.

If a snapshot is specified, the target cluster is created from the source DB snapshot with a default configuration and default security group.

If a cluster snapshot is specified, the target cluster is created from the source cluster restore point with the same configuration as the original source DB cluster, except that the new cluster is created with the default security group.

## Request Parameters
<a name="API_RestoreDBClusterFromSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The name of the cluster to create from the snapshot or cluster snapshot. This parameter isn't case sensitive.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-snapshot-id`   
Type: String  
Required: Yes

 ** Engine **   
The database engine to use for the new cluster.  
Default: The same as source.  
Constraint: Must be compatible with the engine of the source.  
Type: String  
Required: Yes

 ** SnapshotIdentifier **   
The identifier for the snapshot or cluster snapshot to restore from.  
You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.  
Constraints:  
+ Must match the identifier of an existing snapshot.
Type: String  
Required: Yes

 **AvailabilityZones.AvailabilityZone.N**   
Provides the list of Amazon EC2 Availability Zones that instances in the restored DB cluster can be created in.  
Type: Array of strings  
Required: No

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group to associate with this DB cluster.  
 *Type:* String.       *Required:* No.  
If this argument is omitted, the default DB cluster parameter group is used. If supplied, must match the name of an existing default DB cluster parameter group. The string must consist of from 1 to 255 letters, numbers or hyphens. Its first character must be a letter, and it cannot end with a hyphen or contain two consecutive hyphens.  
Type: String  
Required: No

 ** DBSubnetGroupName **   
The name of the subnet group to use for the new cluster.  
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

 ** EngineVersion **   
The version of the database engine to use for the new cluster.  
Type: String  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier to use when restoring an encrypted cluster from a DB snapshot or cluster snapshot.  
The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.  
If you do not specify a value for the `KmsKeyId` parameter, then the following occurs:  
+ If the snapshot or cluster snapshot in `SnapshotIdentifier` is encrypted, then the restored cluster is encrypted using the AWS KMS key that was used to encrypt the snapshot or the cluster snapshot.
+ If the snapshot or the cluster snapshot in `SnapshotIdentifier` is not encrypted, then the restored DB cluster is not encrypted.
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
Default: The same port as the original cluster.  
Type: Integer  
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

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of virtual private cloud (VPC) security groups that the new cluster will belong to.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_RestoreDBClusterFromSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_RestoreDBClusterFromSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **   
You already have a cluster with the given identifier.  
HTTP Status Code: 400

 ** DBClusterQuotaExceededFault **   
The cluster can't be created because you have reached the maximum allowed quota of clusters.  
HTTP Status Code: 403

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.   
HTTP Status Code: 404

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing snapshot.   
HTTP Status Code: 404

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
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

 ** StorageQuotaExceeded **   
The request would cause you to exceed the allowed amount of storage available across all instances.  
HTTP Status Code: 400

## See Also
<a name="API_RestoreDBClusterFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/RestoreDBClusterFromSnapshot) 