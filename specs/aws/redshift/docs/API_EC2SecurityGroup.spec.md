---
id: "@specs/aws/redshift/docs/API_EC2SecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EC2SecurityGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EC2SecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EC2SecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EC2SecurityGroup
<a name="API_EC2SecurityGroup"></a>

Describes an Amazon EC2 security group.

## Contents
<a name="API_EC2SecurityGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** EC2SecurityGroupName **   
The name of the EC2 Security Group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroupOwnerId **   
The AWS account ID of the owner of the EC2 security group specified in the `EC2SecurityGroupName` field.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
The status of the EC2 security group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Tags.Tag.N **   
The list of tags for the EC2 security group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_EC2SecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EC2SecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EC2SecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EC2SecurityGroup) 