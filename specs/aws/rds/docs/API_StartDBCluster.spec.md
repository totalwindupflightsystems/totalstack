---
id: "@specs/aws/rds/docs/API_StartDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StartDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StartDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartDBCluster
<a name="API_StartDBCluster"></a>

Starts an Amazon Aurora DB cluster that was stopped using the AWS console, the stop-db-cluster AWS CLI command, or the `StopDBCluster` operation.

For more information, see [ Stopping and Starting an Aurora Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html) in the *Amazon Aurora User Guide*.

**Note**  
This operation only applies to Aurora DB clusters.

## Request Parameters
<a name="API_StartDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier of the Amazon Aurora DB cluster to be started. This parameter is stored as a lowercase string.  
Type: String  
Required: Yes

## Response Elements
<a name="API_StartDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.   
For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `PromoteReadReplicaDBCluster`, `RestoreDBClusterFromS3`, `RestoreDBClusterFromSnapshot`, `RestoreDBClusterToPointInTime`, `StartDBCluster`, and `StopDBCluster`.  
For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster`, `DeleteDBCluster`, `DescribeDBClusters`, `FailoverDBCluster`, `ModifyDBCluster`, `RebootDBCluster`, `RestoreDBClusterFromSnapshot`, and `RestoreDBClusterToPointInTime`.  
For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*   
For more information on Multi-AZ DB clusters, see [ Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_StartDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBShardGroupState **   
The DB shard group must be in the available state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** VpcEncryptionControlViolation **   
The operation violates VPC encryption control settings. Make sure that your DB instance type supports the Nitro encryption-in-transit capability, or modify your VPC's encryption controls to not enforce encryption-in-transit.  
HTTP Status Code: 400

## Examples
<a name="API_StartDBCluster_Examples"></a>

### Example
<a name="API_StartDBCluster_Example_1"></a>

This example illustrates one usage of StartDBCluster.

#### Sample Request
<a name="API_StartDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=StartDBCluster
    &DBClusterIdentifier=mydbcluster
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20131016/us-west-1/rds/aws4_request
    &X-Amz-Date=20131016T233051Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=087a8eb41cb1ab5f99e81575f23e73757ffc6a1e42d7d2b30b9cc0be988cff97
```

## See Also
<a name="API_StartDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StartDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StartDBCluster) 