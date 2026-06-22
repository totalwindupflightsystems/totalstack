---
id: "@specs/aws/docdb/docs/API_ModifyGlobalCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyGlobalCluster"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ModifyGlobalCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ModifyGlobalCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyGlobalCluster
<a name="API_ModifyGlobalCluster"></a>

Modify a setting for an Amazon DocumentDB global cluster. You can change one or more configuration parameters (for example: deletion protection), or the global cluster identifier by specifying these parameters and the new values in the request.

**Note**  
This action only applies to Amazon DocumentDB clusters.

## Request Parameters
<a name="API_ModifyGlobalCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GlobalClusterIdentifier **   
The identifier for the global cluster being modified. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing global cluster.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: Yes

 ** DeletionProtection **   
Indicates if the global cluster has deletion protection enabled. The global cluster can't be deleted when deletion protection is enabled.   
Type: Boolean  
Required: No

 ** NewGlobalClusterIdentifier **   
The new identifier for a global cluster when you modify a global cluster. This value is stored as a lowercase string.  
+ Must contain from 1 to 63 letters, numbers, or hyphens

  The first character must be a letter

  Can't end with a hyphen or contain two consecutive hyphens
Example: `my-cluster2`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`   
Required: No

## Response Elements
<a name="API_ModifyGlobalCluster_ResponseElements"></a>

The following element is returned by the service.

 ** GlobalCluster **   
A data type representing an Amazon DocumentDB global cluster.  
Type: [GlobalCluster](API_GlobalCluster.md) object

## Errors
<a name="API_ModifyGlobalCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalClusterNotFoundFault **   
The `GlobalClusterIdentifier` doesn't refer to an existing global cluster.  
HTTP Status Code: 404

 ** InvalidGlobalClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyGlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/ModifyGlobalCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ModifyGlobalCluster) 