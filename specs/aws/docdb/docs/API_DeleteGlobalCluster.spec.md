---
id: "@specs/aws/docdb/docs/API_DeleteGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteGlobalCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteGlobalCluster
<a name="API_DeleteGlobalCluster"></a>

Deletes a global cluster. The primary and secondary clusters must already be detached or deleted before attempting to delete a global cluster.

**Note**  
This action only applies to Amazon DocumentDB clusters.

## Request Parameters
<a name="API_DeleteGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The cluster identifier of the global cluster being deleted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

## Response Elements
<a name="API_DeleteGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Amazon DocumentDB global cluster.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_DeleteGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.  
HTTP Status Code: 404

 ** InvalidGlobalClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteGlobalCluster) 