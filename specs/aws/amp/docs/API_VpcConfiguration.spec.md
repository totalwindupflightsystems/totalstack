---
id: "@specs/aws/amp/docs/API_VpcConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# VpcConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_VpcConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The Amazon VPC configuration that specifies the network settings for a Prometheus collector to securely connect to Amazon MSK clusters. This configuration includes the security groups and subnets that control network access and placement for the collector.

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="prometheus-Type-VpcConfiguration-securityGroupIds"></a>
The security group IDs that control network access for the Prometheus collector. These security groups must allow the collector to communicate with your Amazon MSK cluster on the required ports.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `sg-[0-9a-z]+`   
Required: Yes

 ** subnetIds **   <a name="prometheus-Type-VpcConfiguration-subnetIds"></a>
The subnet IDs where the Prometheus collector will be deployed. The subnets must be in the same Amazon VPC as your Amazon MSK cluster and have network connectivity to the cluster.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `subnet-[0-9a-z]+`   
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/VpcConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/VpcConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/VpcConfiguration) 