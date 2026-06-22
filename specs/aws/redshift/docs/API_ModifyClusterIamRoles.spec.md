---
id: "@specs/aws/redshift/docs/API_ModifyClusterIamRoles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterIamRoles"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterIamRoles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterIamRoles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterIamRoles
<a name="API_ModifyClusterIamRoles"></a>

Modifies the list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to [Quotas and limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_ModifyClusterIamRoles_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster for which you want to associate or disassociate IAM roles.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **AddIamRoles.IamRoleArn.N**   
Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format.   
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DefaultIamRoleArn **   
The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **RemoveIamRoles.IamRoleArn.N**   
Zero or more IAM roles in ARN format to disassociate from the cluster.   
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_ModifyClusterIamRoles_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_ModifyClusterIamRoles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

## Examples
<a name="API_ModifyClusterIamRoles_Examples"></a>

### Example
<a name="API_ModifyClusterIamRoles_Example_1"></a>

This example removes an AWS Identity and Access Management (IAM) role from a cluster.

#### Sample Request
<a name="API_ModifyClusterIamRoles_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyClusterIamRoles
&ClusterIdentifier=mycluster
&RemoveIamRoles.IamRoleArn.1=arn%3Aaws%3Aiam%3A%3A123456789012%3Arole%2FmyRedshiftRole
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyClusterIamRoles_Example_1_Response"></a>

```
<ModifyClusterIamRolesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyClusterIamRolesResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ExpectedNextSnapshotScheduleTimeStatus>OnTrack</ExpectedNextSnapshotScheduleTimeStatus>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>
      <Endpoint>
        <Port>5439</Port>
        <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
      </Endpoint>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <ClusterCreateTime>2019-12-27T17:48:01.504Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ClusterSecurityGroups/>
      <ExpectedNextSnapshotScheduleTime>2019-12-28T05:48:20.939Z</ExpectedNextSnapshotScheduleTime>
      <NodeType>rg.4xlarge</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-29T23:15:00Z</NextMaintenanceWindowStartTime>
      <DeferredMaintenanceWindows/>
      <Tags>
        <Tag>
          <Value>newtag</Value>
          <Key>mytag</Key>
        </Tag>
      </Tags>
      <VpcSecurityGroups>
        <VpcSecurityGroup>
          <VpcSecurityGroupId>sh-a1a123ab</VpcSecurityGroupId>
          <Status>active</Status>
        </VpcSecurityGroup>
      </VpcSecurityGroups>
      <ClusterParameterGroups>
        <ClusterParameterGroup>
          <ParameterGroupName>default.redshift-1.0</ParameterGroupName>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
        </ClusterParameterGroup>
      </ClusterParameterGroups>
      <Encrypted>false</Encrypted>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <PendingModifiedValues/>
      <PreferredMaintenanceWindow>sun:23:15-mon:03:15</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>available</ClusterStatus>
    </Cluster>
  </ModifyClusterIamRolesResult>
  <ResponseMetadata>
    <RequestId>3ca20e36-28e0-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</ModifyClusterIamRolesResponse>
```

## See Also
<a name="API_ModifyClusterIamRoles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterIamRoles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterIamRoles) 