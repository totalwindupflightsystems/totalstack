---
id: "@specs/aws/rds/docs/API_CreateDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBClusterSnapshot
<a name="API_CreateDBClusterSnapshot"></a>

Creates a snapshot of a DB cluster.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_CreateDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier of the DB cluster to create a snapshot for. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing DBCluster.
Example: `my-cluster1`   
Type: String  
Required: Yes

 ** DBClusterSnapshotIdentifier **   
The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1-snapshot1`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
The tags to be assigned to the DB cluster snapshot.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Contains the details for an Amazon RDS DB cluster snapshot  
This data type is used as a response element in the `DescribeDBClusterSnapshots` action.  
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CreateDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterSnapshotAlreadyExistsFault **   
The user already has a DB cluster snapshot with the given identifier.  
HTTP Status Code: 400

 ** InvalidDBClusterSnapshotStateFault **   
The supplied value isn't a valid DB cluster snapshot state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB snapshots.  
HTTP Status Code: 400

## Examples
<a name="API_CreateDBClusterSnapshot_Examples"></a>

### Example
<a name="API_CreateDBClusterSnapshot_Example_1"></a>

This example illustrates one usage of CreateDBClusterSnapshot.

#### Sample Request
<a name="API_CreateDBClusterSnapshot_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CreateDBClusterSnapshot
    &DBClusterIdentifier=sample-cluster
    &DBClusterSnapshotIdentifier=sample-cluster-snapshot
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20150318/us-east-1/rds/aws4_request
    &X-Amz-Date=20150318T205321Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=9573ced573a41cdec8e2ef1d9b5235a141f97ae30b4469fc9b0f16149399c4bf
```

#### Sample Response
<a name="API_CreateDBClusterSnapshot_Example_1_Response"></a>

```
<CreateDBClusterSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBClusterSnapshotResult>
    <DBClusterSnapshot>
      <Port>0</Port>
      <Engine>aurora</Engine>
      <Status>creating</Status>
      <SnapshotType>manual</SnapshotType>
      <LicenseModel>aurora</LicenseModel>
      <DBClusterSnapshotIdentifier>sample-cluster-snapshot</DBClusterSnapshotIdentifier>
      <SnapshotCreateTime>2015-03-18T20:53:22.523Z</SnapshotCreateTime>
      <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
      <VpcId>vpc-3faffe54</VpcId>
      <ClusterCreateTime>2015-03-06T22:11:13.826Z</ClusterCreateTime>
      <PercentProgress>0</PercentProgress>
      <AllocatedStorage>1</AllocatedStorage>
      <MasterUsername>awsuser</MasterUsername>
    </DBClusterSnapshot>
  </CreateDBClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>d070d0d2-cea0-11e4-8c88-8351226c8c92</RequestId>
  </ResponseMetadata>
</CreateDBClusterSnapshotResponse>
```

## See Also
<a name="API_CreateDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBClusterSnapshot) 