---
id: "@specs/aws/rds/docs/API_DeleteGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteGlobalCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteGlobalCluster
<a name="API_DeleteGlobalCluster"></a>

Deletes a global database cluster. The primary and secondary clusters must already be detached or destroyed first.

**Note**  
This action only applies to Aurora DB clusters.

## Request Parameters
<a name="API_DeleteGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The cluster identifier of the global database cluster being deleted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

## Response Elements
<a name="API_DeleteGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Aurora global database.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_DeleteGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.  
HTTP Status Code: 404

 ** InvalidGlobalClusterStateFault **   
The global cluster is in an invalid state and can't perform the requested operation.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteGlobalCluster) 