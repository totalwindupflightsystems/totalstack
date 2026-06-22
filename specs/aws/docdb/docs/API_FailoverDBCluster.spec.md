---
id: "@specs/aws/docdb/docs/API_FailoverDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailoverDBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# FailoverDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_FailoverDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailoverDBCluster
<a name="API_FailoverDBCluster"></a>

Forces a failover for a cluster.

A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).

If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.

## Request Parameters
<a name="API_FailoverDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
A cluster identifier to force a failover for. This parameter is not case sensitive.  
Constraints:  
+ Must match the identifier of an existing `DBCluster`.
Type: String  
Required: No

 ** TargetDBInstanceIdentifier **   
The name of the instance to promote to the primary instance.  
You must specify the instance identifier for an Amazon DocumentDB replica in the cluster. For example, `mydbcluster-replica1`.  
Type: String  
Required: No

## Response Elements
<a name="API_FailoverDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_FailoverDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

## See Also
<a name="API_FailoverDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/FailoverDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/FailoverDBCluster) 