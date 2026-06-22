---
id: "@specs/aws/eks/docs/API_RemoteAccessConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoteAccessConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RemoteAccessConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RemoteAccessConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoteAccessConfig
<a name="API_RemoteAccessConfig"></a>

An object representing the remote access configuration for the managed node group.

## Contents
<a name="API_RemoteAccessConfig_Contents"></a>

 ** ec2SshKey **   <a name="AmazonEKS-Type-RemoteAccessConfig-ec2SshKey"></a>
The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group. For more information, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*. For Windows, an Amazon EC2 SSH key is used to obtain the RDP password. For more information, see [Amazon EC2 key pairs and Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances*.  
Type: String  
Required: No

 ** sourceSecurityGroups **   <a name="AmazonEKS-Type-RemoteAccessConfig-sourceSecurityGroups"></a>
The security group IDs that are allowed SSH access (port 22) to the nodes. For Windows, the port is 3389. If you specify an Amazon EC2 SSH key but don't specify a source security group when you create a managed node group, then the port on the nodes is opened to the internet (`0.0.0.0/0`). For more information, see [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon Virtual Private Cloud User Guide*.  
Type: Array of strings  
Required: No

## See Also
<a name="API_RemoteAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RemoteAccessConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RemoteAccessConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RemoteAccessConfig) 