---
id: "@specs/aws/docdb/docs/API_ModifyDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ModifyDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ModifyDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBCluster
<a name="API_ModifyDBCluster"></a>

Modifies a setting for an Amazon DocumentDB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. 

## Request Parameters
<a name="API_ModifyDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The cluster identifier for the cluster that is being modified. This parameter is not case sensitive.  
Constraints:  
+ Must match the identifier of an existing `DBCluster`.
Type: String  
Required: Yes

 ** AllowMajorVersionUpgrade **   
A value that indicates whether major version upgrades are allowed.  
Constraints:  
+ You must allow major version upgrades when specifying a value for the `EngineVersion` parameter that is a different major version than the cluster's current version.
+ Since some parameters are version specific, changing them requires executing a new `ModifyDBCluster` API call after the in-place MVU completes.
Performing an MVU directly impacts the following parameters:  
+  `MasterUserPassword` 
+  `NewDBClusterIdentifier` 
+  `VpcSecurityGroupIds` 
+  `Port` 
Type: Boolean  
Required: No

 ** ApplyImmediately **   
A value that specifies whether the changes in this request and any pending changes are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the cluster. If this parameter is set to `false`, changes to the cluster are applied during the next maintenance window.  
The `ApplyImmediately` parameter affects only the `NewDBClusterIdentifier` and `MasterUserPassword` values. If you set this parameter value to `false`, the changes to the `NewDBClusterIdentifier` and `MasterUserPassword` values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the `ApplyImmediately` parameter.  
Default: `false`   
Type: Boolean  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. You must specify a minimum value of 1.  
Default: 1  
Constraints:  
+ Must be a value from 1 to 35.
Type: Integer  
Required: No

 ** CloudwatchLogsExportConfiguration **   
The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster. The `EnableLogTypes` and `DisableLogTypes` arrays determine which logs are exported (or not exported) to CloudWatch Logs.  
Type: [CloudwatchLogsExportConfiguration](API_CloudwatchLogsExportConfiguration.md) object  
Required: No

 ** DBClusterParameterGroupName **   
The name of the cluster parameter group to use for the cluster.  
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether this cluster can be deleted. If `DeletionProtection` is enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled. `DeletionProtection` protects clusters from being accidentally deleted.  
Type: Boolean  
Required: No

 ** EngineVersion **   
The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless `ApplyImmediately` is enabled.  
To list all of the available engine versions for Amazon DocumentDB use the following command:  
 `aws docdb describe-db-engine-versions --engine docdb --query "DBEngineVersions[].EngineVersion"`   
Type: String  
Required: No

 ** ManageMasterUserPassword **   
Specifies whether to manage the master user password with Amazon Web Services Secrets Manager. If the cluster doesn't manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you can't specify `MasterUserPassword`. If the cluster already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify `MasterUserPassword`. In this case, Amazon DocumentDB deletes the secret and uses the new password for the master user specified by `MasterUserPassword`.  
Type: Boolean  
Required: No

 ** MasterUserPassword **   
The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).  
Constraints: Must contain from 8 to 100 characters.  
Type: String  
Required: No

 ** MasterUserSecretKmsKeyId **   
The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.  
This setting is valid only if both of the following conditions are met:  
+ The cluster doesn't manage the master user password in Amazon Web Services Secrets Manager. If the cluster already manages the master user password in Amazon Web Services Secrets Manager, you can't change the KMS key that is used to encrypt the secret.
+ You are enabling `ManageMasterUserPassword` to manage the master user password in Amazon Web Services Secrets Manager. If you are turning on `ManageMasterUserPassword` and don't specify `MasterUserSecretKmsKeyId`, then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.
The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.  
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

 ** NewDBClusterIdentifier **   
The new cluster identifier for the cluster when renaming a cluster. This value is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster2`   
Type: String  
Required: No

 ** Port **   
The port number on which the cluster accepts connections.  
Constraints: Must be a value from `1150` to `65535`.   
Default: The same port as the original cluster.  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter.   
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

 ** RotateMasterUserPassword **   
Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.  
This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the cluster. The secret value contains the updated password.  
Constraint: You must apply the change immediately when rotating the master user password.  
Type: Boolean  
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

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of virtual private cloud (VPC) security groups that the cluster will belong to.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_ModifyDBCluster_Errors"></a>

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

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

 ** InvalidDBSecurityGroupState **   
The state of the security group doesn't allow deletion.  
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **   
The subnet group can't be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.  
HTTP Status Code: 400

 ** NetworkTypeNotSupported **   
The network type is not supported by either `DBSubnetGroup` or the DB engine version.  
HTTP Status Code: 400

 ** StorageQuotaExceeded **   
The request would cause you to exceed the allowed amount of storage available across all instances.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/ModifyDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBCluster) 