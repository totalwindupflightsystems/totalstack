---
id: "@specs/aws/docdb/docs/API_DBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterSnapshot
<a name="API_DBClusterSnapshot"></a>

Detailed information about a cluster snapshot. 

## Contents
<a name="API_DBClusterSnapshot_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AvailabilityZones.AvailabilityZone.N **   
Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.  
Type: Array of strings  
Required: No

 ** ClusterCreateTime **   
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).  
Type: Timestamp  
Required: No

 ** DBClusterIdentifier **   
Specifies the cluster identifier of the cluster that this cluster snapshot was created from.  
Type: String  
Required: No

 ** DBClusterSnapshotArn **   
The Amazon Resource Name (ARN) for the cluster snapshot.  
Type: String  
Required: No

 ** DBClusterSnapshotIdentifier **   
Specifies the identifier for the cluster snapshot.  
Type: String  
Required: No

 ** Engine **   
Specifies the name of the database engine.  
Type: String  
Required: No

 ** EngineVersion **   
Provides the version of the database engine for this cluster snapshot.  
Type: String  
Required: No

 ** KmsKeyId **   
If `StorageEncrypted` is `true`, the AWS KMS key identifier for the encrypted cluster snapshot.  
Type: String  
Required: No

 ** MasterUsername **   
Provides the master user name for the cluster snapshot.  
Type: String  
Required: No

 ** PercentProgress **   
Specifies the percentage of the estimated data that has been transferred.  
Type: Integer  
Required: No

 ** Port **   
Specifies the port that the cluster was listening on at the time of the snapshot.  
Type: Integer  
Required: No

 ** SnapshotCreateTime **   
Provides the time when the snapshot was taken, in UTC.  
Type: Timestamp  
Required: No

 ** SnapshotType **   
Provides the type of the cluster snapshot.  
Type: String  
Required: No

 ** SourceDBClusterSnapshotArn **   
If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.  
Type: String  
Required: No

 ** Status **   
Specifies the status of this cluster snapshot.  
Type: String  
Required: No

 ** StorageEncrypted **   
Specifies whether the cluster snapshot is encrypted.  
Type: Boolean  
Required: No

 ** StorageType **   
Storage type associated with your cluster snapshot  
For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide*.  
Valid values for storage type - `standard | iopt1`   
Default value is `standard `   
Type: String  
Required: No

 ** VpcId **   
Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBClusterSnapshot) 