---
id: "@specs/aws/redshift/docs/API_ClusterSecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterSecurityGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterSecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterSecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterSecurityGroup
<a name="API_ClusterSecurityGroup"></a>

Describes a security group.

## Contents
<a name="API_ClusterSecurityGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ClusterSecurityGroupName **   
The name of the cluster security group to which the operation was applied.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Description **   
A description of the security group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroups.EC2SecurityGroup.N **   
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.  
Type: Array of [EC2SecurityGroup](API_EC2SecurityGroup.md) objects  
Required: No

 ** IPRanges.IPRange.N **   
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.  
Type: Array of [IPRange](API_IPRange.md) objects  
Required: No

 ** Tags.Tag.N **   
The list of tags for the cluster security group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_ClusterSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterSecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterSecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterSecurityGroup) 