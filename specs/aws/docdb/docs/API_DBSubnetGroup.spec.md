---
id: "@specs/aws/docdb/docs/API_DBSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBSubnetGroup"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBSubnetGroup
<a name="API_DBSubnetGroup"></a>

Detailed information about a subnet group. 

## Contents
<a name="API_DBSubnetGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBSubnetGroupArn **   
The Amazon Resource Name (ARN) for the DB subnet group.  
Type: String  
Required: No

 ** DBSubnetGroupDescription **   
Provides the description of the subnet group.  
Type: String  
Required: No

 ** DBSubnetGroupName **   
The name of the subnet group.  
Type: String  
Required: No

 ** SubnetGroupStatus **   
Provides the status of the subnet group.  
Type: String  
Required: No

 ** Subnets.Subnet.N **   
Detailed information about one or more subnets within a subnet group.  
Type: Array of [Subnet](API_Subnet.md) objects  
Required: No

 ** SupportedNetworkTypes.member.N **   
The network type of the DB subnet group.  
Valid Values: `IPV4` \| `DUAL`   
A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (DUAL).  
Type: Array of strings  
Required: No

 ** VpcId **   
Provides the virtual private cloud (VPC) ID of the subnet group.  
Type: String  
Required: No

## See Also
<a name="API_DBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBSubnetGroup) 