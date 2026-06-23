---
id: "@specs/aws/comprehend/docs/API_VpcConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# VpcConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_VpcConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcConfig
<a name="API_VpcConfig"></a>

 Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). 

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="comprehend-Type-VpcConfig-SecurityGroupIds"></a>
The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html).   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[-0-9a-zA-Z]+`   
Required: Yes

 ** Subnets **   <a name="comprehend-Type-VpcConfig-Subnets"></a>
The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[-0-9a-z]+`   
Required: Yes

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/VpcConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/VpcConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/VpcConfig) 