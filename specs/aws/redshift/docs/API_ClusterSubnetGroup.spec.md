---
id: "@specs/aws/redshift/docs/API_ClusterSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterSubnetGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterSubnetGroup
<a name="API_ClusterSubnetGroup"></a>

Describes a subnet group.

## Contents
<a name="API_ClusterSubnetGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ClusterSubnetGroupName **   
The name of the cluster subnet group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Description **   
The description of the cluster subnet group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SubnetGroupStatus **   
The status of the cluster subnet group. Possible values are `Complete`, `Incomplete` and `Invalid`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Subnets.Subnet.N **   
A list of the VPC [Subnet](API_Subnet.md) elements.   
Type: Array of [Subnet](API_Subnet.md) objects  
Required: No

 ** SupportedClusterIpAddressTypes.item.N **   
The IP address types supported by this cluster subnet group. Possible values are `ipv4` and `dualstack`.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Tags.Tag.N **   
The list of tags for the cluster subnet group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** VpcId **   
The VPC ID of the cluster subnet group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterSubnetGroup) 