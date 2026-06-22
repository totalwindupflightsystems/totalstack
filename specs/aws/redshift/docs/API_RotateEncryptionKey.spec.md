---
id: "@specs/aws/redshift/docs/API_RotateEncryptionKey"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RotateEncryptionKey"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RotateEncryptionKey

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RotateEncryptionKey
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RotateEncryptionKey
<a name="API_RotateEncryptionKey"></a>

Rotates the encryption keys for a cluster.

## Request Parameters
<a name="API_RotateEncryptionKey_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster that you want to rotate the encryption keys for.  
Constraints: Must be the name of valid cluster that has encryption enabled.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_RotateEncryptionKey_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_RotateEncryptionKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_RotateEncryptionKey_Examples"></a>

### Example
<a name="API_RotateEncryptionKey_Example_1"></a>

This example illustrates one usage of RotateEncryptionKey.

#### Sample Request
<a name="API_RotateEncryptionKey_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=RotateEncryptionKey
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_RotateEncryptionKey_Example_1_Response"></a>

```
<RotateEncryptionKeyResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <RotateEncryptionKeyResult>
    <Cluster>
      <AllowVersionUpgrade>true</AllowVersionUpgrade>
      <ClusterIdentifier>mycluster</ClusterIdentifier>
      <NumberOfNodes>1</NumberOfNodes>
      <AvailabilityZone>us-east-2a</AvailabilityZone>
      <ClusterVersion>1.0</ClusterVersion>
      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
      <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>
      <Endpoint>
        <Port>5439</Port>
        <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
      </Endpoint>
      <VpcId>vpc-a1abc1a1</VpcId>
      <PubliclyAccessible>false</PubliclyAccessible>
      <ClusterCreateTime>2019-12-25T11:21:49.458Z</ClusterCreateTime>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles>
        <ClusterIamRole>
          <IamRoleArn>arn:aws:iam::123456789012:role/myRedshiftRole</IamRoleArn>
          <ApplyStatus>in-sync</ApplyStatus>
        </ClusterIamRole>
      </IamRoles>
      <ClusterSecurityGroups/>
      <NodeType>dc2.large</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-28T16:00:00Z</NextMaintenanceWindowStartTime>
      <DeferredMaintenanceWindows/>
      <Tags/>
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
      <Encrypted>true</Encrypted>
      <MaintenanceTrackName>current</MaintenanceTrackName>
      <PendingModifiedValues/>
      <PreferredMaintenanceWindow>sat:16:00-sat:16:30</PreferredMaintenanceWindow>
      <KmsKeyId>arn:aws:kms:us-east-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY</KmsKeyId>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>rotating-keys</ClusterStatus>
    </Cluster>
  </RotateEncryptionKeyResult>
  <ResponseMetadata>
    <RequestId>0cdb408d-28f7-11ea-8a28-2fd1719d0e86</RequestId>
  </ResponseMetadata>
</RotateEncryptionKeyResponse>
```

## See Also
<a name="API_RotateEncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RotateEncryptionKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RotateEncryptionKey) 