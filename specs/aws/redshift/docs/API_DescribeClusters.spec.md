---
id: "@specs/aws/redshift/docs/API_DescribeClusters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusters"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusters
<a name="API_DescribeClusters"></a>

Returns properties of provisioned clusters including general cluster properties, cluster database properties, maintenance and backup properties, and security and access properties. This operation supports pagination. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all clusters that have any combination of those values are returned.

If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeClusters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.  
The default is that all clusters defined for an account are returned.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusters](#API_DescribeClusters) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Constraints: You can specify either the **ClusterIdentifier** parameter or the **Marker** parameter, but not both.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusters_ResponseElements"></a>

The following elements are returned by the service.

 **Clusters.Cluster.N**   
A list of `Cluster` objects, where each object describes one cluster.   
Type: Array of [Cluster](API_Cluster.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusters_Examples"></a>

### Example
<a name="API_DescribeClusters_Example_1"></a>

This example illustrates one usage of DescribeClusters.

#### Sample Request
<a name="API_DescribeClusters_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusters
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusters_Example_1_Response"></a>

```
<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClustersResult>
    <Clusters>
      <Cluster>
        <AllowVersionUpgrade>true</AllowVersionUpgrade>
        <ClusterIdentifier>mycluster</ClusterIdentifier>
        <ClusterRevisionNumber>11978</ClusterRevisionNumber>
        <NumberOfNodes>1</NumberOfNodes>
        <ClusterPublicKey>ssh-rsa AAAABexamplepublickey...LzrwzEXAMPLE Amazon-Redshift</ClusterPublicKey>
        <AvailabilityZone>us-east-2f</AvailabilityZone>
        <ClusterVersion>1.0</ClusterVersion>
        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
        <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>
        <Endpoint>
          <Port>5439</Port>
          <Address>mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com</Address>
        </Endpoint>
        <VpcId>vpc-a1abc1a1</VpcId>
        <PubliclyAccessible>false</PubliclyAccessible>
        <ClusterCreateTime>2019-12-23T23:21:27.977Z</ClusterCreateTime>
        <ClusterSnapshotCopyStatus>
          <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>
          <DestinationRegion>us-east-1</DestinationRegion>
          <RetentionPeriod>15</RetentionPeriod>
        </ClusterSnapshotCopyStatus>
        <MasterUsername>adminuser</MasterUsername>
        <DBName>dev</DBName>
        <EnhancedVpcRouting>false</EnhancedVpcRouting>
        <IamRoles/>
        <ClusterSecurityGroups/>
        <NodeType>dc2.large</NodeType>
        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
        <NextMaintenanceWindowStartTime>2020-01-12T23:15:00Z</NextMaintenanceWindowStartTime>
        <DeferredMaintenanceWindows>
          <DeferredMaintenanceWindow>
            <DeferMaintenanceEndTime>2020-01-09T18:18:39.354Z</DeferMaintenanceEndTime>
            <DeferMaintenanceIdentifier>dfm-MuEIBOA9bi0aZ1Vjh0cy</DeferMaintenanceIdentifier>
            <DeferMaintenanceStartTime>2019-12-10T18:18:39.354Z</DeferMaintenanceStartTime>
          </DeferredMaintenanceWindow>
        </DeferredMaintenanceWindows>
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
        <Encrypted>false</Encrypted>
        <ClusterNodes>
          <member>
            <PrivateIPAddress>172.31.64.51</PrivateIPAddress>
            <NodeRole>SHARED</NodeRole>
            <PublicIPAddress>54.162.164.238</PublicIPAddress>
          </member>
        </ClusterNodes>
        <MaintenanceTrackName>current</MaintenanceTrackName>
        <PendingModifiedValues/>
        <PreferredMaintenanceWindow>sun:23:15-sun:23:45</PreferredMaintenanceWindow>
        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>
        <ClusterStatus>available</ClusterStatus>
      </Cluster>
    </Clusters>
  </DescribeClustersResult>
  <ResponseMetadata>
    <RequestId>e47f901c-283e-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</DescribeClustersResponse>
```

## See Also
<a name="API_DescribeClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusters) 