---
id: "@specs/aws/redshift/docs/API_ClusterVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterVersion"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterVersion
<a name="API_ClusterVersion"></a>

Describes a cluster version, including the parameter group family and description of the version.

## Contents
<a name="API_ClusterVersion_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ClusterParameterGroupFamily **   
The name of the cluster parameter group family for the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The version number used by the cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Description **   
The description of the cluster version.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterVersion) 