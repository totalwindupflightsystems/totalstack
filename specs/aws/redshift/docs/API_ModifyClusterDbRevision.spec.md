---
id: "@specs/aws/redshift/docs/API_ModifyClusterDbRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterDbRevision"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterDbRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterDbRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterDbRevision
<a name="API_ModifyClusterDbRevision"></a>

Modifies the database revision of a cluster. The database revision is a unique revision of the database running in a cluster.

## Request Parameters
<a name="API_ModifyClusterDbRevision_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of a cluster whose database revision you want to modify.   
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** RevisionTarget **   
The identifier of the database revision. You can retrieve this value from the response to the [DescribeClusterDbRevisions](API_DescribeClusterDbRevisions.md) request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_ModifyClusterDbRevision_ResponseElements"></a>

The following element is returned by the service.

 ** Cluster **   
Describes a cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_ModifyClusterDbRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterOnLatestRevision **   
Cluster is already on the latest database revision.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyClusterDbRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterDbRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterDbRevision) 