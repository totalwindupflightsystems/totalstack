---
id: "@specs/aws/docdb/docs/API_StopDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopDBCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# StopDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_StopDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopDBCluster
<a name="API_StopDBCluster"></a>

Stops the running cluster that is specified by `DBClusterIdentifier`. The cluster must be in the *available* state. For more information, see [Stopping and Starting an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-stop-start.html).

## Request Parameters
<a name="API_StopDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier of the cluster to stop. Example: `docdb-2019-05-28-15-24-52`   
Type: String  
Required: Yes

## Response Elements
<a name="API_StopDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **   
Detailed information about a cluster.   
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_StopDBCluster_Errors"></a>

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
<a name="API_StopDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/StopDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/StopDBCluster) 