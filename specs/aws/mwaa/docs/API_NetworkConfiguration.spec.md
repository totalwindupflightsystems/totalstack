---
id: "@specs/aws/mwaa/docs/API_NetworkConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NetworkConfiguration"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# NetworkConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_NetworkConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

Describes the VPC networking components used to secure and enable network traffic between the AWS resources for your environment. For more information, refer to [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** SecurityGroupIds **   <a name="mwaa-Type-NetworkConfiguration-SecurityGroupIds"></a>
A list of security group IDs. For more information, refer to [Security in your VPC on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html).  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `sg-[a-zA-Z0-9\-._]+`   
Required: No

 ** SubnetIds **   <a name="mwaa-Type-NetworkConfiguration-SubnetIds"></a>
A list of subnet IDs. For more information, refer to [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `subnet-[a-zA-Z0-9\-._]+`   
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/NetworkConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/NetworkConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/NetworkConfiguration) 