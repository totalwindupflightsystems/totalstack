---
id: "@specs/aws/docdb/docs/API_FailoverGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailoverGlobalCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# FailoverGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_FailoverGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailoverGlobalCluster
<a name="API_FailoverGlobalCluster"></a>

Promotes the specified secondary DB cluster to be the primary DB cluster in the global cluster when failing over a global cluster occurs.

Use this operation to respond to an unplanned event, such as a regional disaster in the primary region. Failing over can result in a loss of write transaction data that wasn't replicated to the chosen secondary before the failover event occurred. However, the recovery process that promotes a DB instance on the chosen seconday DB cluster to be the primary writer DB instance guarantees that the data is in a transactionally consistent state.

## Request Parameters
<a name="API_FailoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The identifier of the Amazon DocumentDB global cluster to apply this operation. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster.  
Constraints:  
+ Must match the identifier of an existing global cluster.
+ Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** TargetDbClusterIdentifier **   
The identifier of the secondary Amazon DocumentDB cluster that you want to promote to the primary for the global cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its AWS region.  
Constraints:  
+ Must match the identifier of an existing secondary cluster.
+ Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** AllowDataLoss **   
Specifies whether to allow data loss for this global cluster operation. Allowing data loss triggers a global failover operation.  
If you don't specify `AllowDataLoss`, the global cluster operation defaults to a switchover.  
Constraints:  
+ Can't be specified together with the `Switchover` parameter.
Type: Boolean  
Required: No

 ** Switchover **   
Specifies whether to switch over this global database cluster.  
Constraints:  
+ Can't be specified together with the `AllowDataLoss` parameter.
Type: Boolean  
Required: No

## Response Elements
<a name="API_FailoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Amazon DocumentDB global cluster.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_FailoverGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_FailoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/FailoverGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/FailoverGlobalCluster) 