---
id: "@specs/aws/redshift/docs/API_ClusterNode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterNode"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterNode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterNode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterNode
<a name="API_ClusterNode"></a>

The identifier of a node in a cluster.

## Contents
<a name="API_ClusterNode_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** NodeRole **   
Whether the node is a leader node or a compute node.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PrivateIPAddress **   
The private IP address of a node within a cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** PublicIPAddress **   
The public IP address of a node within a cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterNode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterNode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterNode) 