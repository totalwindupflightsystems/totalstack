---
id: "@specs/aws/docdb/docs/API_SwitchoverGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SwitchoverGlobalCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# SwitchoverGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_SwitchoverGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SwitchoverGlobalCluster
<a name="API_SwitchoverGlobalCluster"></a>

Switches over the specified secondary Amazon DocumentDB cluster to be the new primary Amazon DocumentDB cluster in the global database cluster.

## Request Parameters
<a name="API_SwitchoverGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The identifier of the Amazon DocumentDB global database cluster to switch over. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster. This parameter isn’t case-sensitive.  
Constraints:  
+ Must match the identifier of an existing global cluster (Amazon DocumentDB global database).
+ Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** TargetDbClusterIdentifier **   
The identifier of the secondary Amazon DocumentDB cluster to promote to the new primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its AWS region.  
Constraints:  
+ Must match the identifier of an existing secondary cluster.
+ Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

## Response Elements
<a name="API_SwitchoverGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Amazon DocumentDB global cluster.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_SwitchoverGlobalCluster_Errors"></a>

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
<a name="API_SwitchoverGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/SwitchoverGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/SwitchoverGlobalCluster) 