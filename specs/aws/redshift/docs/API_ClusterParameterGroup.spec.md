---
id: "@specs/aws/redshift/docs/API_ClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterParameterGroup
<a name="API_ClusterParameterGroup"></a>

Describes a parameter group.

## Contents
<a name="API_ClusterParameterGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Description **   
The description of the parameter group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterGroupFamily **   
The name of the cluster parameter group family that this cluster parameter group is compatible with.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterGroupName **   
The name of the cluster parameter group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Tags.Tag.N **   
The list of tags for the cluster parameter group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_ClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterParameterGroup) 