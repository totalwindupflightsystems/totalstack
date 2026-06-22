---
id: "@specs/aws/docdb/docs/API_elastic_Cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_Cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cluster
<a name="API_elastic_Cluster"></a>

Returns information about a specific elastic cluster.

## Contents
<a name="API_elastic_Cluster_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** adminUserName **   <a name="documentdb-Type-elastic_Cluster-adminUserName"></a>
The name of the elastic cluster administrator.  
Type: String  
Required: Yes

 ** authType **   <a name="documentdb-Type-elastic_Cluster-authType"></a>
The authentication type for the elastic cluster.  
Type: String  
Valid Values: `PLAIN_TEXT | SECRET_ARN`   
Required: Yes

 ** clusterArn **   <a name="documentdb-Type-elastic_Cluster-clusterArn"></a>
The ARN identifier of the elastic cluster.  
Type: String  
Required: Yes

 ** clusterEndpoint **   <a name="documentdb-Type-elastic_Cluster-clusterEndpoint"></a>
The URL used to connect to the elastic cluster.  
Type: String  
Required: Yes

 ** clusterName **   <a name="documentdb-Type-elastic_Cluster-clusterName"></a>
The name of the elastic cluster.  
Type: String  
Required: Yes

 ** createTime **   <a name="documentdb-Type-elastic_Cluster-createTime"></a>
The time when the elastic cluster was created in Universal Coordinated Time (UTC).  
Type: String  
Required: Yes

 ** kmsKeyId **   <a name="documentdb-Type-elastic_Cluster-kmsKeyId"></a>
The KMS key identifier to use to encrypt the elastic cluster.  
Type: String  
Required: Yes

 ** preferredMaintenanceWindow **   <a name="documentdb-Type-elastic_Cluster-preferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).  
 *Format*: `ddd:hh24:mi-ddd:hh24:mi`   
Type: String  
Required: Yes

 ** shardCapacity **   <a name="documentdb-Type-elastic_Cluster-shardCapacity"></a>
The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.  
Type: Integer  
Required: Yes

 ** shardCount **   <a name="documentdb-Type-elastic_Cluster-shardCount"></a>
The number of shards assigned to the elastic cluster. Maximum is 32.  
Type: Integer  
Required: Yes

 ** status **   <a name="documentdb-Type-elastic_Cluster-status"></a>
The status of the elastic cluster.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`   
Required: Yes

 ** subnetIds **   <a name="documentdb-Type-elastic_Cluster-subnetIds"></a>
The Amazon EC2 subnet IDs for the elastic cluster.  
Type: Array of strings  
Required: Yes

 ** vpcSecurityGroupIds **   <a name="documentdb-Type-elastic_Cluster-vpcSecurityGroupIds"></a>
A list of EC2 VPC security groups associated with thie elastic cluster.  
Type: Array of strings  
Required: Yes

 ** backupRetentionPeriod **   <a name="documentdb-Type-elastic_Cluster-backupRetentionPeriod"></a>
The number of days for which automatic snapshots are retained.  
Type: Integer  
Required: No

 ** preferredBackupWindow **   <a name="documentdb-Type-elastic_Cluster-preferredBackupWindow"></a>
The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod`.  
Type: String  
Required: No

 ** shardInstanceCount **   <a name="documentdb-Type-elastic_Cluster-shardInstanceCount"></a>
The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.  
Type: Integer  
Required: No

 ** shards **   <a name="documentdb-Type-elastic_Cluster-shards"></a>
The total number of shards in the cluster.  
Type: Array of [Shard](API_elastic_Shard.md) objects  
Required: No

## See Also
<a name="API_elastic_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/Cluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/Cluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/Cluster) 