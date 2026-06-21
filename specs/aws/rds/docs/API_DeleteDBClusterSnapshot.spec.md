---
id: "@specs/aws/rds/docs/API_DeleteDBClusterSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBClusterSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBClusterSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBClusterSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBClusterSnapshot
<a name="API_DeleteDBClusterSnapshot"></a>

Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.

**Note**  
The DB cluster snapshot must be in the `available` state to be deleted.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DeleteDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **   
The identifier of the DB cluster snapshot to delete.  
Constraints: Must be the name of an existing DB cluster snapshot in the `available` state.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **   
Contains the details for an Amazon RDS DB cluster snapshot  
This data type is used as a response element in the `DescribeDBClusterSnapshots` action.  
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_DeleteDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **   
The supplied value isn't a valid DB cluster snapshot state.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBClusterSnapshot_Examples"></a>

### Example
<a name="API_DeleteDBClusterSnapshot_Example_1"></a>

This example illustrates one usage of DeleteDBClusterSnapshot.

#### Sample Request
<a name="API_DeleteDBClusterSnapshot_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=DeleteDBClusterSnapshot
    &DBClusterSnapshotIdentifier=sample-cluster-snapshot
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20150318/us-east-1/rds/aws4_request
    &X-Amz-Date=20150318T215614Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=7aaab0a295151051bc4723f5b1f7b6b535615b8db9256bd56993c4dc6df4c2c4
```

#### Sample Response
<a name="API_DeleteDBClusterSnapshot_Example_1_Response"></a>

```
<DeleteDBClusterSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteDBClusterSnapshotResult>
    <DBClusterSnapshot>
      <Port>0</Port>
      <Status>available</Status>
      <Engine>aurora</Engine>
      <SnapshotType>manual</SnapshotType>
      <LicenseModel>aurora</LicenseModel>
      <DBClusterSnapshotIdentifier>sample-cluster-snapshot</DBClusterSnapshotIdentifier>
      <SnapshotCreateTime>2015-03-18T20:53:22.523Z</SnapshotCreateTime>
      <DBClusterIdentifier>sample-cluster</DBClusterIdentifier>
      <VpcId>vpc-3fabee54</VpcId>
      <ClusterCreateTime>2015-03-06T22:11:13.826Z</ClusterCreateTime>
      <PercentProgress>100</PercentProgress>
      <AllocatedStorage>1</AllocatedStorage>
      <MasterUsername>awsuser</MasterUsername>
    </DBClusterSnapshot>
  </DeleteDBClusterSnapshotResult>
  <ResponseMetadata>
    <RequestId>994ab08d-cdb9-2ce4-abf9-7528e6348483</RequestId>
  </ResponseMetadata>
</DeleteDBClusterSnapshotResponse>
```

## See Also
<a name="API_DeleteDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBClusterSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBClusterSnapshot) 