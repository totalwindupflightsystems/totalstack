---
id: "@specs/aws/docdb/docs/API_CreateDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CreateDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CreateDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBCluster
<a name="API_CreateDBCluster"></a>

Creates a new Amazon DocumentDB cluster.

## Request Parameters
<a name="API_CreateDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The cluster identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens. 
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens. 
Example: `my-cluster`   
Type: String  
Required: Yes

 ** Engine **   
The name of the database engine to be used for this cluster.  
Valid values: `docdb`   
Type: String  
Required: Yes

 **AvailabilityZones.AvailabilityZone.N**   
A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.  
Type: Array of strings  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. You must specify a minimum value of 1.  
Default: 1  
Constraints:  
+ Must be a value from 1 to 35.
Type: Integer  
Required: No

 ** DBClusterParameterGroupName **   
The name of the cluster parameter group to associate with this cluster.  
Type: String  
Required: No

 ** DBSubnetGroupName **   
A subnet group to associate with this cluster.  
Constraints: Must match the name of an existing `DBSubnetGroup`. Must not be default.  
Example: `mySubnetgroup`   
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether this cluster can be deleted. If `DeletionProtection` is enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled. `DeletionProtection` protects clusters from being accidentally deleted.  
Type: Boolean  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see [ Auditing Amazon DocumentDB Events](https://docs.aws.amazon.com/documentdb/latest/devguide/event-auditing.html) and [ Profiling Amazon DocumentDB Operations](https://docs.aws.amazon.com/documentdb/latest/devguide/profiling.html).   
Type: Array of strings  
Required: No

 ** EngineVersion **   
The version number of the database engine to use. The `--engine-version` will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.  
Type: String  
Required: No

 ** GlobalClusterIdentifier **   
The cluster identifier of the new global cluster.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier for an encrypted cluster.  
The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.  
If an encryption key is not specified in `KmsKeyId`:   
+ If the `StorageEncrypted` parameter is `true`, Amazon DocumentDB uses your default encryption key. 
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Regions.  
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.  
Constraint: You can't manage the master user password with Amazon Web Services Secrets Manager if `MasterUserPassword` is specified.  
Type: Boolean  
Required: No

 ** MasterUsername **   
The name of the master user for the cluster.  
Constraints:  
+ Must be from 1 to 63 letters or numbers.
+ The first character must be a letter.
+ Cannot be a reserved word for the chosen database engine. 
Type: String  
Required: No

 ** MasterUserPassword **   
The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).  
Constraints: Must contain from 8 to 100 characters.  
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager. This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the DB cluster.  
The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.  
If you don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.  
There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.  
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
The port number on which the instances in the cluster accept connections.  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled using the `BackupRetentionPeriod` parameter.   
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.   
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window. 
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).  
Format: `ddd:hh24:mi-ddd:hh24:mi`   
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.  
Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun  
Constraints: Minimum 30-minute window.  
Type: String  
Required: No

 ** PreSignedUrl **   
Not currently supported.   
Type: String  
Required: No

 ** ServerlessV2ScalingConfiguration **   
Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.  
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object  
Required: No

 ** StorageEncrypted **   
Specifies whether the cluster is encrypted.  
Type: Boolean  
Required: No

 ** StorageType **   
The storage type to associate with the DB cluster.  
For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide*.  
Valid values for storage type - `standard | iopt1`   
Default value is `standard `   
When you create an Amazon DocumentDB cluster with the storage type set to `iopt1`, the storage type is returned in the response. The storage type isn't returned when you set it to `standard`.
Type: String  
Required: No

 **Tags.Tag.N**   
The tags to be assigned to the cluster.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of EC2 VPC security groups to associate with this cluster.   
Type: Array of strings  
Required: No

## Response Elements
<a name="API_CreateDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_CreateDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **   
You already have a cluster with the given identifier.  
HTTP Status Code: 400

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** DBClusterParameterGroupNotFound **   
 `DBClusterParameterGroupName` doesn't refer to an existing cluster parameter group.   
HTTP Status Code: 404

 ** DBClusterQuotaExceededFault **   
The cluster can't be created because you have reached the maximum allowed quota of clusters.  
HTTP Status Code: 403

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing instance.   
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.  
HTTP Status Code: 404

 ** InsufficientStorageClusterCapacity **   
There is not enough storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.   
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **   
The subnet group can't be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
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
<a name="API_CreateDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/CreateDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CreateDBCluster) 