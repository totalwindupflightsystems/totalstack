---
id: "@specs/aws/fsx/docs/API_S3AccessPointVpcConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3AccessPointVpcConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# S3AccessPointVpcConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_S3AccessPointVpcConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3AccessPointVpcConfiguration
<a name="API_S3AccessPointVpcConfiguration"></a>

If included, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).

## Contents
<a name="API_S3AccessPointVpcConfiguration_Contents"></a>

 ** VpcId **   <a name="FSx-Type-S3AccessPointVpcConfiguration-VpcId"></a>
Specifies the virtual private cloud (VPC) for the S3 access point VPC configuration, if one exists.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(vpc-[0-9a-f]{8,})$`   
Required: No

## See Also
<a name="API_S3AccessPointVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPointVpcConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPointVpcConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPointVpcConfiguration) 