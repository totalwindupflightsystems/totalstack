---
id: "@specs/aws/rds/docs/API_RestoreDBClusterToPointInTime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreDBClusterToPointInTime"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RestoreDBClusterToPointInTime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RestoreDBClusterToPointInTime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreDBClusterToPointInTime
<a name="API_RestoreDBClusterToPointInTime"></a>

Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before `LatestRestorableTime` for up to `BackupRetentionPeriod` days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group. Unless the `RestoreType` is set to `copy-on-write`, the restore may occur in a different Availability Zone (AZ) from the original DB cluster. The AZ where RDS restores the DB cluster depends on the AZs in the specified subnet group.

You can use the `EnableVPCNetworking` and `EnableInternetAccessGateway` parameters together to restore an Aurora PostgreSQL cluster without VPC networking and with internet-based connectivity. These two parameters must always be specified together. Set `EnableVPCNetworking` to `false` to disable the VPC network interface (ENI) for the cluster. `EnableInternetAccessGateway` enables internet-based connectivity through an internet access gateway. IAM database authentication is required and must be enabled using `EnableIAMDatabaseAuthentication`. Once the cluster is restored, you need to modify the DB cluster to update `MasterUserAuthenticationType` to `iam-db-auth`. 

**Note**  
For Aurora, this operation only restores the DB cluster, not the DB instances for that DB cluster. You must invoke the `CreateDBInstance` operation to create DB instances for the restored DB cluster, specifying the identifier of the restored DB cluster in `DBClusterIdentifier`. You can create DB instances only after the `RestoreDBClusterToPointInTime` operation has completed and the DB cluster is available.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_RestoreDBClusterToPointInTime_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The name of the new DB cluster to be created.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: Yes

 ** BacktrackWindow **   
The target backtrack window, in seconds. To disable backtracking, set this value to 0.  
Default: 0  
Constraints:  
+ If specified, this value must be set to a number from 0 to 259,200 (72 hours).
Valid for: Aurora MySQL DB clusters only  
Type: Long  
Required: No

 ** BackupRetentionPeriod **   
The number of days for which automated backups are retained. Specify a minimum value of `1`.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Default: Uses existing setting  
Constraints:  
+ Must be a value from 1 to 35.
Type: Integer  
Required: No

 ** CopyTagsToSnapshot **   
Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** DBClusterInstanceClass **   
The compute and memory capacity of the each DB instance in the Multi-AZ DB cluster, for example db.m6gd.xlarge. Not all DB instance classes are available in all AWS Regions, or for all database engines.  
For the full list of DB instance classes, and availability for your engine, see [DB instance class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.  
Valid for: Multi-AZ DB clusters only  
Type: String  
Required: No

 ** DBClusterParameterGroupName **   
The name of the custom DB cluster parameter group to associate with this DB cluster.  
If the `DBClusterParameterGroupName` parameter is omitted, the default DB cluster parameter group for the specified engine is used.  
Constraints:  
+ If supplied, must match the name of an existing DB cluster parameter group.
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** DBSubnetGroupName **   
The DB subnet group name to use for the new DB cluster.  
Constraints: If supplied, must match the name of an existing DBSubnetGroup.  
Example: `mydbsubnetgroup`   
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** DeletionProtection **   
Specifies whether to enable deletion protection for the DB cluster. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** Domain **   
The Active Directory directory ID to restore the DB cluster in. The domain must be created prior to this operation.  
For Amazon Aurora DB clusters, Amazon RDS can use Kerberos Authentication to authenticate users that connect to the DB cluster. For more information, see [Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html) in the *Amazon Aurora User Guide*.  
Valid for: Aurora DB clusters only  
Type: String  
Required: No

 ** DomainIAMRoleName **   
The name of the IAM role to be used when making API calls to the Directory Service.  
Valid for: Aurora DB clusters only  
Type: String  
Required: No

 **EnableCloudwatchLogsExports.member.N**   
The list of logs that the restored DB cluster is to export to CloudWatch Logs. The values in the list depend on the DB engine being used.  
 **RDS for MySQL**   
Possible values are `error`, `general`, `slowquery`, and `iam-db-auth-error`.  
 **RDS for PostgreSQL**   
Possible values are `postgresql`, `upgrade`, and `iam-db-auth-error`.  
 **Aurora MySQL**   
Possible values are `audit`, `error`, `general`, `instance`, `slowquery`, and `iam-db-auth-error`.  
 **Aurora PostgreSQL**   
Possible value are `instance`, `postgresql`, and `iam-db-auth-error`.  
For more information about exporting CloudWatch Logs for Amazon RDS, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide*.  
For more information about exporting CloudWatch Logs for Amazon Aurora, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Array of strings  
Required: No

 ** EnableIAMDatabaseAuthentication **   
Specifies whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.  
For more information, see [ IAM Database Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon Aurora User Guide* or [ IAM database authentication for MariaDB, MySQL, and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide*.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 ** EnableInternetAccessGateway **   
Specifies that the restored DB cluster should use internet-based connectivity through an internet access gateway. This allows clients to connect to the cluster over the internet without requiring a VPC.  
This parameter must be used together with `EnableVPCNetworking` set to `false`. When both parameters are specified, IAM database authentication is required. You must also specify `EnableIAMDatabaseAuthentication`.  
Valid for Cluster Type: Aurora PostgreSQL clusters  
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
Specifies whether to turn on Performance Insights for the DB cluster.  
Type: Boolean  
Required: No

 ** EnableVPCNetworking **   
Specifies whether to enable VPC networking for the restored DB cluster. Set this parameter to `false` to create a cluster without the VPC network interface (ENI).  
This parameter must be used together with `EnableInternetAccessGateway`. When both parameters are specified, IAM database authentication is required. You must also specify `EnableIAMDatabaseAuthentication`.  
Valid for Cluster Type: Aurora PostgreSQL clusters  
Type: Boolean  
Required: No

 ** EngineLifecycleSupport **   
The life cycle type for this DB cluster.  
By default, this value is set to `open-source-rds-extended-support`, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled`. In this case, RDS automatically upgrades your restored DB cluster to a higher engine version, if the major engine version is past its end of standard support date.
You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:  
+ Amazon Aurora - [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide* 
+ Amazon RDS - [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* 
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`   
Default: `open-source-rds-extended-support`   
Type: String  
Required: No

 ** EngineMode **   
The engine mode of the new cluster. Specify `provisioned` or `serverless`, depending on the type of the cluster you are creating. You can create an Aurora Serverless v1 clone from a provisioned cluster, or a provisioned clone from an Aurora Serverless v1 cluster. To create a clone that is an Aurora Serverless v1 cluster, the original cluster must be an Aurora Serverless v1 cluster or an encrypted provisioned cluster. To create a full copy that is an Aurora Serverless v1 cluster, specify the engine mode `serverless`.  
Valid for: Aurora DB clusters only  
Type: String  
Required: No

 ** Iops **   
The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.  
For information about valid IOPS values, see [Amazon RDS Provisioned IOPS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.  
Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB instance.  
Valid for: Multi-AZ DB clusters only  
Type: Integer  
Required: No

 ** KmsKeyId **   
The AWS KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different AWS account, specify the key ARN or alias ARN.  
You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different from the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the `KmsKeyId` parameter.  
If you don't specify a value for the `KmsKeyId` parameter, then the following occurs:  
+ If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.
+ If the DB cluster isn't encrypted, then the restored DB cluster isn't encrypted.
If `DBClusterIdentifier` refers to a DB cluster that isn't encrypted, then the restore request is rejected.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** MonitoringInterval **   
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify `0`.  
If `MonitoringRoleArn` is specified, also set `MonitoringInterval` to a value other than `0`.  
Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`   
Default: `0`   
Type: Integer  
Required: No

 ** MonitoringRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is `arn:aws:iam:123456789012:role/emaccess`.  
If `MonitoringInterval` is set to a value other than `0`, supply a `MonitoringRoleArn` value.  
Type: String  
Required: No

 ** NetworkType **   
The network type of the DB cluster.  
Valid Values:  
+  `IPV4` 
+  `DUAL` 
The network type is determined by the `DBSubnetGroup` specified for the DB cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL`).  
For more information, see [ Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*   
Valid for: Aurora DB clusters only  
Type: String  
Required: No

 ** OptionGroupName **   
The name of the option group for the new DB cluster.  
DB clusters are associated with a default option group that can't be modified.  
Type: String  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you don't specify a value for `PerformanceInsightsKMSKeyId`, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.  
Type: String  
Required: No

 ** PerformanceInsightsRetentionPeriod **   
The number of days to retain Performance Insights data.  
Valid Values:  
+  `7` 
+  *month* \* 31, where *month* is a number of months from 1-23. Examples: `93` (3 months \* 31), `341` (11 months \* 31), `589` (19 months \* 31)
+  `731` 
Default: `7` days  
If you specify a retention period that isn't valid, such as `94`, Amazon RDS issues an error.  
Type: Integer  
Required: No

 ** Port **   
The port number on which the new DB cluster accepts connections.  
Constraints: A value from `1150-65535`.  
Default: The default port for the engine.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Integer  
Required: No

 ** PreferredBackupWindow **   
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter.  
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To view the time blocks available, see [ Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow) in the *Amazon Aurora User Guide*.  
Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters  
Constraints:  
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String  
Required: No

 ** PubliclyAccessible **   
Specifies whether the DB cluster is publicly accessible.  
When the DB cluster is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB cluster's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB cluster's VPC. Access to the DB cluster is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB cluster doesn't permit it.  
When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.  
Default: The default behavior varies depending on whether `DBSubnetGroupName` is specified.  
If `DBSubnetGroupName` isn't specified, and `PubliclyAccessible` isn't specified, the following applies:  
+ If the default VPC in the target Region doesn’t have an internet gateway attached to it, the DB cluster is private.
+ If the default VPC in the target Region has an internet gateway attached to it, the DB cluster is public.
If `DBSubnetGroupName` is specified, and `PubliclyAccessible` isn't specified, the following applies:  
+ If the subnets are part of a VPC that doesn’t have an internet gateway attached to it, the DB cluster is private.
+ If the subnets are part of a VPC that has an internet gateway attached to it, the DB cluster is public.
Valid for: Multi-AZ DB clusters only  
Type: Boolean  
Required: No

 ** RdsCustomClusterConfiguration **   
Reserved for future use.  
Type: [RdsCustomClusterConfiguration](API_RdsCustomClusterConfiguration.md) object  
Required: No

 ** RestoreToTime **   
The date and time to restore the DB cluster to.  
Valid Values: Value must be a time in Universal Coordinated Time (UTC) format  
Constraints:  
+ Must be before the latest restorable time for the DB instance
+ Must be specified if `UseLatestRestorableTime` parameter isn't provided
+ Can't be specified if the `UseLatestRestorableTime` parameter is enabled
+ Can't be specified if the `RestoreType` parameter is `copy-on-write` 
Example: `2015-03-07T23:45:00Z`   
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Timestamp  
Required: No

 ** RestoreType **   
The type of restore to be performed. You can specify one of the following values:  
+  `full-copy` - The new DB cluster is restored as a full copy of the source DB cluster.
+  `copy-on-write` - The new DB cluster is restored as a clone of the source DB cluster.
If you don't specify a `RestoreType` value, then the new DB cluster is restored as a full copy of the source DB cluster.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** ScalingConfiguration **   
For DB clusters in `serverless` DB engine mode, the scaling properties of the DB cluster.  
Valid for: Aurora DB clusters only  
Type: [ScalingConfiguration](API_ScalingConfiguration.md) object  
Required: No

 ** ServerlessV2ScalingConfiguration **   
Contains the scaling configuration of an Aurora Serverless v2 DB cluster.  
For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.  
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object  
Required: No

 ** SourceDBClusterIdentifier **   
The identifier of the source DB cluster from which to restore.  
Constraints:  
+ Must match the identifier of an existing DBCluster.
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 ** SourceDbClusterResourceId **   
The resource ID of the source DB cluster from which to restore.  
Type: String  
Required: No

 ** StorageType **   
Specifies the storage type to be associated with the DB cluster.  
When specified for a Multi-AZ DB cluster, a value for the `Iops` parameter is required.  
Valid Values: `aurora`, `aurora-iopt1` (Aurora DB clusters); `io1` (Multi-AZ DB clusters)  
Default: `aurora` (Aurora DB clusters); `io1` (Multi-AZ DB clusters)  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 **TagSpecifications.item.N**   
Tags to assign to resources associated with the DB cluster.  
Valid Values:   
+  `cluster-auto-backup` - The DB cluster's automated backup.
Type: Array of [TagSpecification](API_TagSpecification.md) objects  
Required: No

 ** UseLatestRestorableTime **   
Specifies whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster isn't restored to the latest restorable backup time.  
Constraints: Can't be specified if `RestoreToTime` parameter is provided.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Boolean  
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**   
A list of VPC security groups that the new DB cluster belongs to.  
Valid for: Aurora DB clusters and Multi-AZ DB clusters  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_RestoreDBClusterToPointInTime_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_RestoreDBClusterToPointInTime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **   
The user already has a DB cluster with the given identifier.  
HTTP Status Code: 400

 ** DBClusterAutomatedBackupNotFoundFault **   
No automated backup for this DB cluster was found.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterParameterGroupNotFound **   
 `DBClusterParameterGroupName` doesn't refer to an existing DB cluster parameter group.  
HTTP Status Code: 404

 ** DBClusterQuotaExceededFault **   
The user attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.  
HTTP Status Code: 403

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** DomainNotFoundFault **   
 `Domain` doesn't refer to an existing Active Directory domain.  
HTTP Status Code: 404

 ** InsufficientDBClusterCapacityFault **   
The DB cluster doesn't have enough capacity for the current operation.  
HTTP Status Code: 403

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InsufficientStorageClusterCapacity **   
There is insufficient storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.  
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **   
The supplied value isn't a valid DB cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBSnapshotState **   
The state of the DB snapshot doesn't allow deletion.  
HTTP Status Code: 400

 ** InvalidRestoreFault **   
Cannot restore from VPC backup to non-VPC DB instance.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The DB subnet group doesn't cover all Availability Zones after it's created because of users' change.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** NetworkTypeNotSupported **   
The network type is invalid for the DB instance. Valid nework type values are `IPV4` and `DUAL`.  
HTTP Status Code: 400

 ** OptionGroupNotFoundFault **   
The specified option group could not be found.  
HTTP Status Code: 404

 ** StorageQuotaExceeded **   
The request would result in the user exceeding the allowed amount of storage available across all DB instances.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
The specified `StorageType` can't be associated with the DB instance.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_RestoreDBClusterToPointInTime_Examples"></a>

### Restoring an Aurora DB cluster to a point in time
<a name="API_RestoreDBClusterToPointInTime_Example_1"></a>

This example illustrates one usage of RestoreDBClusterToPointInTime.

#### Sample Request
<a name="API_RestoreDBClusterToPointInTime_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=RestoreDBClusterToPointInTime
    &DBClusterIdentifier=sample-restored-1
    &RestoreToTime=2023-02-13T18%3A45%3A00Z
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &SourceDBClusterIdentifier=sample-cluster
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20230213/us-west-2/rds/aws4_request
    &X-Amz-Date=20230213T224930Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=e3b88945052247e82eaeaca6e269e7f6e18a36147b45c3b077bc600472e70de6
```

#### Sample Response
<a name="API_RestoreDBClusterToPointInTime_Example_1_Response"></a>

```
<RestoreDBClusterToPointInTimeResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RestoreDBClusterToPointInTimeResult>
    <DBCluster>
      <AllocatedStorage>1</AllocatedStorage>
      <DatabaseName>sample</DatabaseName>
      <AvailabilityZones>
        <AvailabilityZone>us-west-2a</AvailabilityZone>
        <AvailabilityZone>us-west-2b</AvailabilityZone>
        <AvailabilityZone>us-west-2c</AvailabilityZone>
      </AvailabilityZones>
      <PreferredBackupWindow>10:37-11:07</PreferredBackupWindow>
      <Endpoint>sample-restored-1.cluster-cnubrrfwfkg6.us-west-2.rds.amazonaws.com</Endpoint>
      <Engine>aurora-mysql</Engine>
      <ReaderEndpoint>sample-restored-1.cluster-ro-cnubrrfwfkg6.us-west-2.rds.amazonaws.com</ReaderEndpoint>
      <ReadReplicaIdentifiers/>
      <EngineVersion>8.0.mysql_aurora.3.01.0</EngineVersion>
      <MasterUsername>mymasteruser</MasterUsername>
      <DBClusterMembers/>
      <StorageEncrypted>false</StorageEncrypted>
      <DBSubnetGroup>default</DBSubnetGroup>
      <HostedZoneId>Z1PVIF0B622C1W</HostedZoneId>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <VpcSecurityGroupId>sg-187c1671</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <Port>3306</Port>
      <PreferredMaintenanceWindow>tue:11:51-tue:12:21</PreferredMaintenanceWindow>
      <DBClusterParameterGroup>default.aurora5.6</DBClusterParameterGroup>
      <BackupRetentionPeriod>1</BackupRetentionPeriod>
      <DBClusterIdentifier>sample-restored-1</DBClusterIdentifier>
      <DbClusterResourceId>cluster-U5ZXU3237H7YVCVKISDIXSQKUQ</DbClusterResourceId>
      <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:sample-restored-1</DBClusterArn>
      <Status>creating</Status>
    </DBCluster>
  </RestoreDBClusterToPointInTimeResult>
  <ResponseMetadata>
    <RequestId>54b75eef-7a04-15b6-aaa0-75ef834084a0</RequestId>
  </ResponseMetadata>
</RestoreDBClusterToPointInTimeResponse>
```

### Restoring a Multi-AZ DB cluster to a point in time
<a name="API_RestoreDBClusterToPointInTime_Example_2"></a>

This example illustrates one usage of RestoreDBClusterToPointInTime.

#### Sample Request
<a name="API_RestoreDBClusterToPointInTime_Example_2_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=RestoreDBClusterToPointInTime
    &DBClusterIdentifier=my-multi-az-cluster-pit
    &SourceDBClusterIdentifier=my-multi-az-cluster
    &UseLatestRestorableTime=true
    &DBClusterInstanceClass=db.r6gd.large
    &StorageType=io1
    &Iops=1000
    &PubliclyAccessible=true
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20221026/us-west-2/rds/aws4_request
    &X-Amz-Date=20221027T000601Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=e3b88945052247e82eaeaca6e269e7f6e18a36147b45c3b077bc600472e70de6
```

#### Sample Response
<a name="API_RestoreDBClusterToPointInTime_Example_2_Response"></a>

```
<RestoreDBClusterToPointInTimeResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/"> 
  <RestoreDBClusterToPointInTimeResult> 
    <DBCluster> 
      <CrossAccountClone>false</CrossAccountClone> 
      <AllocatedStorage>100</AllocatedStorage> 
      <DatabaseName>mydb</DatabaseName> 
      <AssociatedRoles /> 
      <AvailabilityZones> 
        <AvailabilityZone>us-west-2a</AvailabilityZone> 
        <AvailabilityZone>us-west-2b</AvailabilityZone> 
        <AvailabilityZone>us-west-2d</AvailabilityZone> 
      </AvailabilityZones> 
      <ReadReplicaIdentifiers /> 
      <Iops>1000</Iops> 
      <EngineVersion>8.0.26</EngineVersion> 
      <MasterUsername>admin</MasterUsername> 
      <DBClusterMembers> 
        <DBClusterMember> 
          <DBInstanceIdentifier>my-multi-az-cluster-instance-3</DBInstanceIdentifier> 
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus> 
          <PromotionTier>1</PromotionTier> 
          <IsClusterWriter>false</IsClusterWriter> 
        </DBClusterMember> 
        <DBClusterMember> 
          <DBInstanceIdentifier>my-multi-az-cluster-instance-2</DBInstanceIdentifier> 
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus> 
          <PromotionTier>1</PromotionTier> 
          <IsClusterWriter>false</IsClusterWriter> 
        </DBClusterMember> 
        <DBClusterMember> 
          <DBInstanceIdentifier>my-multi-az-cluster-instance-1</DBInstanceIdentifier> 
          <DBClusterParameterGroupStatus>in-sync</DBClusterParameterGroupStatus> 
          <PromotionTier>1</PromotionTier> 
          <IsClusterWriter>false</IsClusterWriter> 
        </DBClusterMember> 
      </DBClusterMembers> 
      <HttpEndpointEnabled>false</HttpEndpointEnabled> 
      <Port>3306</Port> 
      <BackupRetentionPeriod>2</BackupRetentionPeriod> 
      <KmsKeyId>arn:aws:kms:us-west-2:123456789012:key/123EXAMPLE-abcd-4567-efgEXAMPLE</KmsKeyId> 
      <DBClusterIdentifier>my-multi-az-cluster-pit</DBClusterIdentifier> 
      <DbClusterResourceId>cluster-SA2CL64NMV4KTUP6PI4TJWLOM4</DbClusterResourceId> 
      <Status>creating</Status> 
      <PreferredBackupWindow>11:34-12:04</PreferredBackupWindow> 
      <DeletionProtection>false</DeletionProtection> 
      <Endpoint>my-multi-az-cluster.cluster-123456789012.us-west-2.rds.amazonaws.com</Endpoint> 
      <EngineMode>provisioned</EngineMode> 
      <Engine>mysql</Engine> 
      <ReaderEndpoint>my-multi-az-cluster.cluster-ro-123456789012.us-west-2.rds.amazonaws.com</ReaderEndpoint> 
      <PubliclyAccessible>true</PubliclyAccessible> 
      <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled> 
      <ClusterCreateTime>2021-10-27T00:06:04.033Z</ClusterCreateTime> 
      <MultiAZ>true</MultiAZ> 
      <DomainMemberships /> 
      <StorageEncrypted>true</StorageEncrypted> 
      <DBSubnetGroup>default</DBSubnetGroup> 
      <VpcSecurityGroups> 
        <VpcSecurityGroupMembership> 
          <VpcSecurityGroupId>sg-6921cc28</VpcSecurityGroupId> 
          <Status>active</Status> 
        </VpcSecurityGroupMembership> 
      </VpcSecurityGroups> 
      <HostedZoneId>Z3GZ3VYA3PGHTQ</HostedZoneId> 
      <TagList /> 
      <PreferredMaintenanceWindow>sat:07:05-sat:07:35</PreferredMaintenanceWindow> 
      <DBClusterParameterGroup>my-cluster-param-1</DBClusterParameterGroup> 
      <StorageType>io1</StorageType> 
      <DBClusterInstanceClass>db.r6gd.large</DBClusterInstanceClass> 
      <CopyTagsToSnapshot>false</CopyTagsToSnapshot> 
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade> 
      <DBClusterArn>arn:aws:rds:us-west-2:123456789012:cluster:my-multi-az-cluster</DBClusterArn> 
    </DBCluster> 
  </RestoreDBClusterToPointInTimeResult> 
  <ResponseMetadata> 
    <RequestId>ec5c848f-3f6a-4c98-9b45-2da58c4e4a96</RequestId> 
  </ResponseMetadata> 
</RestoreDBClusterToPointInTimeResponse>
```

## See Also
<a name="API_RestoreDBClusterToPointInTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RestoreDBClusterToPointInTime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RestoreDBClusterToPointInTime) 