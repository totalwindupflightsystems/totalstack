---
id: "@specs/aws/rds/docs/API_StartDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StartDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StartDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartDBInstance
<a name="API_StartDBInstance"></a>

Starts an Amazon RDS DB instance that was stopped using the AWS console, the stop-db-instance AWS CLI command, or the `StopDBInstance` operation.

For more information, see [ Starting an Amazon RDS DB instance That Was Previously Stopped](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StartInstance.html) in the *Amazon RDS User Guide.* 

**Note**  
This command doesn't apply to RDS Custom, Aurora MySQL, and Aurora PostgreSQL. For Aurora DB clusters, use `StartDBCluster` instead.

## Request Parameters
<a name="API_StartDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The user-supplied instance identifier.  
Type: String  
Required: Yes

## Response Elements
<a name="API_StartDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Contains the details of an Amazon RDS DB instance.  
This data type is used as a response element in the operations `CreateDBInstance`, `CreateDBInstanceReadReplica`, `DeleteDBInstance`, `DescribeDBInstances`, `ModifyDBInstance`, `PromoteReadReplica`, `RebootDBInstance`, `RestoreDBInstanceFromDBSnapshot`, `RestoreDBInstanceFromS3`, `RestoreDBInstanceToPointInTime`, `StartDBInstance`, and `StopDBInstance`.  
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_StartDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **   
The specified CIDR IP range or Amazon EC2 security group might not be authorized for the specified DB security group.  
Or, RDS might not be authorized to perform necessary actions using IAM on your behalf.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** InsufficientDBInstanceCapacity **   
The specified DB instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
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

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_StartDBInstance_Examples"></a>

### Example
<a name="API_StartDBInstance_Example_1"></a>

This example illustrates one usage of StartDBInstance.

#### Sample Request
<a name="API_StartDBInstance_Example_1_Request"></a>

```
https://rds.amazonaws.com/
    ?Action=StartDBInstance
    &DBInstanceIdentifier=mydbinstance
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4EXAMPLE/20131016/us-west-1/rds/aws4_request
    &X-Amz-Date=20131016T233051Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=6e25c542bf96fe24b28c12976ec92d2f856ab1d2a158e21c35441a736e4fde2b
```

#### Sample Response
<a name="API_StartDBInstance_Example_1_Response"></a>

```
<StartDBInstanceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <StartDBInstanceResult>
    <DBInstance>
      <AllocatedStorage>100</AllocatedStorage>
      <EnabledCloudwatchLogsExports>
        <member>alert</member>
        <member>audit</member>
        <member>listener</member>
        <member>trace</member>
      </EnabledCloudwatchLogsExports>
      <AssociatedRoles/>
      <DBParameterGroups>
        <DBParameterGroup>
          <DBParameterGroupName>default.oracle-ee-19</DBParameterGroupName>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
        </DBParameterGroup>
      </DBParameterGroups>
      <AvailabilityZone>us-east-1b</AvailabilityZone>
      <DBSecurityGroups/>
      <Iops>1000</Iops>
      <PerformanceInsightsKMSKeyId>arn:aws:kms:us-east-1:123456789012:key/87c22544-4cac-4640-99de-cfdaa8760ad0</PerformanceInsightsKMSKeyId>
      <EnhancedMonitoringResourceArn>arn:aws:logs:us-east-1:123456789012:log-group:RDSOSMetrics:log-stream:db-LENX3LYCR6OKTGWZZEXAMPLE</EnhancedMonitoringResourceArn>
      <PerformanceInsightsRetentionPeriod>7</PerformanceInsightsRetentionPeriod>
      <EngineVersion>19.0.0.0.ru-2019-10.rur-2019-10.r1</EngineVersion>
      <MasterUsername>admin</MasterUsername>
      <InstanceCreateTime>2019-11-23T17:27:58.540Z</InstanceCreateTime>
      <DBInstanceClass>db.t3.medium</DBInstanceClass>
      <HttpEndpointEnabled>false</HttpEndpointEnabled>
      <ReadReplicaDBInstanceIdentifiers/>
      <CustomerOwnedIpEnabled>false</CustomerOwnedIpEnabled>
      <MonitoringInterval>60</MonitoringInterval>
      <DBInstanceStatus>starting</DBInstanceStatus>
      <BackupRetentionPeriod>0</BackupRetentionPeriod>
      <OptionGroupMemberships>
        <OptionGroupMembership>
          <OptionGroupName>default:oracle-ee-19</OptionGroupName>
          <Status>in-sync</Status>
        </OptionGroupMembership>
      </OptionGroupMemberships>
      <CACertificateIdentifier>rds-ca-2019</CACertificateIdentifier>
      <DbInstancePort>0</DbInstancePort>
      <DbiResourceId>db-LENX3LYCR6OKTGWZEXAMPLE</DbiResourceId>
      <PreferredBackupWindow>08:31-09:01</PreferredBackupWindow>
      <DeletionProtection>false</DeletionProtection>
      <DBInstanceIdentifier>mydbinstance</DBInstanceIdentifier>
      <DBInstanceArn>arn:aws:rds:us-east-1:123456789012:db:mydbinstance</DBInstanceArn>
      <Endpoint>
        <HostedZoneId>Z2R2ITUGPM61AM</HostedZoneId>
        <Address>mydbinstance.123example.us-east-1.rds.amazonaws.com</Address>
        <Port>1521</Port>
      </Endpoint>
      <Engine>oracle-ee</Engine>
      <MaxAllocatedStorage>1000</MaxAllocatedStorage>
      <PubliclyAccessible>true</PubliclyAccessible>
      <IAMDatabaseAuthenticationEnabled>false</IAMDatabaseAuthenticationEnabled>
      <PerformanceInsightsEnabled>true</PerformanceInsightsEnabled>
      <DBName>DBOR</DBName>
      <MultiAZ>false</MultiAZ>
      <DomainMemberships/>
      <CharacterSetName>AL32UTF8</CharacterSetName>
      <MonitoringRoleArn>arn:aws:iam::123456789012:role/rds-monitoring-role</MonitoringRoleArn>
      <StorageEncrypted>false</StorageEncrypted>
      <DBSubnetGroup>
        <VpcId>vpc-67a0bc1c</VpcId>
        <Subnets>
          <Subnet>
            <SubnetIdentifier>subnet-example1</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1a</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetIdentifier>subnet-example12</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1e</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetIdentifier>subnet-example3</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1f</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetIdentifier>subnet-example4</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1d</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetIdentifier>subnet-example5</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1b</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetIdentifier>subnet-example6</SubnetIdentifier>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetOutpost/>
            <SubnetAvailabilityZone>
              <Name>us-east-1c</Name>
            </SubnetAvailabilityZone>
          </Subnet>
        </Subnets>
        <SubnetGroupStatus>Complete</SubnetGroupStatus>
        <DBSubnetGroupDescription>Created from the RDS Management Console</DBSubnetGroupDescription>
        <DBSubnetGroupName>default-vpc-67a0bc1c</DBSubnetGroupName>
      </DBSubnetGroup>
      <TagList>
        <Tag>
          <Value>hr</Value>
          <Key>department</Key>
        </Tag>
        <Tag>
          <Value>rds</Value>
          <Key>type</Key>
        </Tag>
      </TagList>
      <VpcSecurityGroups>
        <VpcSecurityGroupMembership>
          <VpcSecurityGroupId>sg-0417e54f</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroupMembership>
      </VpcSecurityGroups>
      <NcharCharacterSetName>AL16UTF16</NcharCharacterSetName>
      <LicenseModel>bring-your-own-license</LicenseModel>
      <PendingModifiedValues/>
      <PreferredMaintenanceWindow>sun:05:12-sun:05:42</PreferredMaintenanceWindow>
      <StorageType>io1</StorageType>
      <AutoMinorVersionUpgrade>false</AutoMinorVersionUpgrade>
      <CopyTagsToSnapshot>false</CopyTagsToSnapshot>
    </DBInstance>
  </StartDBInstanceResult>
  <ResponseMetadata>
    <RequestId>9d4d8c94-7b81-4a64-8518-EXAMPLE</RequestId>
  </ResponseMetadata>
</StartDBInstanceResponse>
```

## See Also
<a name="API_StartDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StartDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StartDBInstance) 