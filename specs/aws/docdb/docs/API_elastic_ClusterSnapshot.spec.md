---
id: "@specs/aws/docdb/docs/API_elastic_ClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterSnapshot
<a name="API_elastic_ClusterSnapshot"></a>

Returns information about a specific elastic cluster snapshot.

## Contents
<a name="API_elastic_ClusterSnapshot_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** adminUserName **   <a name="documentdb-Type-elastic_ClusterSnapshot-adminUserName"></a>
The name of the elastic cluster administrator.  
Type: String  
Required: Yes

 ** clusterArn **   <a name="documentdb-Type-elastic_ClusterSnapshot-clusterArn"></a>
The ARN identifier of the elastic cluster.  
Type: String  
Required: Yes

 ** clusterCreationTime **   <a name="documentdb-Type-elastic_ClusterSnapshot-clusterCreationTime"></a>
The time when the elastic cluster was created in Universal Coordinated Time (UTC).  
Type: String  
Required: Yes

 ** kmsKeyId **   <a name="documentdb-Type-elastic_ClusterSnapshot-kmsKeyId"></a>
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.   
Type: String  
Required: Yes

 ** snapshotArn **   <a name="documentdb-Type-elastic_ClusterSnapshot-snapshotArn"></a>
The ARN identifier of the elastic cluster snapshot.  
Type: String  
Required: Yes

 ** snapshotCreationTime **   <a name="documentdb-Type-elastic_ClusterSnapshot-snapshotCreationTime"></a>
The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).  
Type: String  
Required: Yes

 ** snapshotName **   <a name="documentdb-Type-elastic_ClusterSnapshot-snapshotName"></a>
The name of the elastic cluster snapshot.  
Type: String  
Required: Yes

 ** status **   <a name="documentdb-Type-elastic_ClusterSnapshot-status"></a>
The status of the elastic cluster snapshot.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`   
Required: Yes

 ** subnetIds **   <a name="documentdb-Type-elastic_ClusterSnapshot-subnetIds"></a>
The Amazon EC2 subnet IDs for the elastic cluster.  
Type: Array of strings  
Required: Yes

 ** vpcSecurityGroupIds **   <a name="documentdb-Type-elastic_ClusterSnapshot-vpcSecurityGroupIds"></a>
A list of EC2 VPC security groups to associate with the elastic cluster.  
Type: Array of strings  
Required: Yes

 ** snapshotType **   <a name="documentdb-Type-elastic_ClusterSnapshot-snapshotType"></a>
The type of cluster snapshots to be returned. You can specify one of the following values:  
+  `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
+  `manual` - Return all cluster snapshots that you have manually created for your AWS account.
Type: String  
Valid Values: `MANUAL | AUTOMATED`   
Required: No

## See Also
<a name="API_elastic_ClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterSnapshot) 