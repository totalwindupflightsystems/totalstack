---
id: "@specs/aws/amp/docs/API_EksConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# EksConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_EksConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksConfiguration
<a name="API_EksConfiguration"></a>

The `EksConfiguration` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

## Contents
<a name="API_EksConfiguration_Contents"></a>

 ** clusterArn **   <a name="prometheus-Type-EksConfiguration-clusterArn"></a>
ARN of the Amazon EKS cluster.  
Type: String  
Pattern: `arn:aws[-a-z]*:eks:[-a-z0-9]+:[0-9]{12}:cluster/.+`   
Required: Yes

 ** subnetIds **   <a name="prometheus-Type-EksConfiguration-subnetIds"></a>
A list of subnet IDs for the Amazon EKS cluster VPC configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `subnet-[0-9a-z]+`   
Required: Yes

 ** securityGroupIds **   <a name="prometheus-Type-EksConfiguration-securityGroupIds"></a>
A list of the security group IDs for the Amazon EKS cluster VPC configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `sg-[0-9a-z]+`   
Required: No

## See Also
<a name="API_EksConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/EksConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/EksConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/EksConfiguration) 