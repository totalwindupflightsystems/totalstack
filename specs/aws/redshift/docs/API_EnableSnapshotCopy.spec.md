---
id: "@specs/aws/redshift/docs/API_EnableSnapshotCopy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableSnapshotCopy"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EnableSnapshotCopy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EnableSnapshotCopy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableSnapshotCopy
<a name="API_EnableSnapshotCopy"></a>

Enables the automatic copy of snapshots from one region to another region for a specified cluster.

## Request Parameters
<a name="API_EnableSnapshotCopy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the source cluster to copy snapshots from.  
Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** DestinationRegion **   
The destination AWS Region that you want to copy snapshots to.  
Constraints: Must be the name of a valid AWS Region. For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region) in the Amazon Web Services General Reference.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ManualSnapshotRetentionPeriod **   
The number of days to retain newly copied snapshots in the destination AWS Region after they are copied from the source AWS Region. If the value is -1, the manual snapshot is retained indefinitely.   
The value must be either -1 or an integer between 1 and 3,653.  
Type: Integer  
Required: No

 ** RetentionPeriod **   
The number of days to retain automated snapshots in the destination region after they are copied from the source region.  
Default: 7.  
Constraints: Must be at least 1 and no more than 35.  
Type: Integer  
Required: No

 ** SnapshotCopyGrantName **   
The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_EnableSnapshotCopy_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_EnableSnapshotCopy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** CopyToRegionDisabledFault **   
Cross-region snapshot copy was temporarily disabled. Try your request again.  
HTTP Status Code: 400

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** IncompatibleOrderableOptions **   
The specified options are incompatible.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

 ** LimitExceededFault **   
The encryption key has exceeded its grant limit in AWS KMS.  
HTTP Status Code: 400

 ** SnapshotCopyAlreadyEnabledFault **   
The cluster already has cross-region snapshot copy enabled.  
HTTP Status Code: 400

 ** SnapshotCopyGrantNotFoundFault **   
The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnknownSnapshotCopyRegionFault **   
The specified region is incorrect or does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_EnableSnapshotCopy_Examples"></a>

### Example
<a name="API_EnableSnapshotCopy_Example_1"></a>

This example illustrates one usage of EnableSnapshotCopy.

#### Sample Request
<a name="API_EnableSnapshotCopy_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=EnableSnapshotCopy
&ClusterIdentifier=mycluster
&DestinationRegion=us-east-1
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_EnableSnapshotCopy_Example_1_Response"></a>

```
<EnableSnapshotCopyResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <EnableSnapshotCopyResult>
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
      <ClusterSnapshotCopyStatus>
        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
        <DestinationRegion>us-east-1</DestinationRegion>
        <RetentionPeriod>7</RetentionPeriod>
      </ClusterSnapshotCopyStatus>
      <MasterUsername>adminuser</MasterUsername>
      <DBName>dev</DBName>
      <EnhancedVpcRouting>false</EnhancedVpcRouting>
      <IamRoles/>
      <ClusterSecurityGroups/>
      <ExpectedNextSnapshotScheduleTime>2019-12-28T05:48:20.939Z</ExpectedNextSnapshotScheduleTime>
      <NodeType>dc2.large</NodeType>
      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
      <NextMaintenanceWindowStartTime>2019-12-29T05:30:00Z</NextMaintenanceWindowStartTime>
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
      <PreferredMaintenanceWindow>sun:05:30-sun:06:00</PreferredMaintenanceWindow>
      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
      <ClusterStatus>available</ClusterStatus>
    </Cluster>
  </EnableSnapshotCopyResult>
  <ResponseMetadata>
    <RequestId>76c22d87-28da-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</EnableSnapshotCopyResponse>
```

## See Also
<a name="API_EnableSnapshotCopy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/EnableSnapshotCopy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EnableSnapshotCopy) 