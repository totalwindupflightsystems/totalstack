---
id: "@specs/aws/redshift/docs/API_ClusterParameterGroupStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterParameterGroupStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterParameterGroupStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterParameterGroupStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterParameterGroupStatus
<a name="API_ClusterParameterGroupStatus"></a>

Describes the status of a parameter group.

## Contents
<a name="API_ClusterParameterGroupStatus_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ClusterParameterStatusList.member.N **   
The list of parameter statuses.  
 For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.  
Type: Array of [ClusterParameterStatus](API_ClusterParameterStatus.md) objects  
Required: No

 ** ParameterApplyStatus **   
The status of parameter updates.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterGroupName **   
The name of the cluster parameter group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterParameterGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterParameterGroupStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterParameterGroupStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterParameterGroupStatus) 