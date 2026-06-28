---
id: "@specs/aws/fsx/docs/API_CreateAndAttachS3AccessPointS3Configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAndAttachS3AccessPointS3Configuration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateAndAttachS3AccessPointS3Configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateAndAttachS3AccessPointS3Configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAndAttachS3AccessPointS3Configuration
<a name="API_CreateAndAttachS3AccessPointS3Configuration"></a>

Used to create an S3 access point that accepts requests only from a virtual private cloud (VPC) to restrict data access to a private network.

## Contents
<a name="API_CreateAndAttachS3AccessPointS3Configuration_Contents"></a>

 ** Policy **   <a name="FSx-Type-CreateAndAttachS3AccessPointS3Configuration-Policy"></a>
Specifies an access policy to associate with the S3 access point configuration. For more information, see [Configuring IAM policies for using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html) in the Amazon Simple Storage Service User Guide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200000.  
Required: No

 ** VpcConfiguration **   <a name="FSx-Type-CreateAndAttachS3AccessPointS3Configuration-VpcConfiguration"></a>
If included, Amazon S3 restricts access to this S3 access point to requests made from the specified virtual private cloud (VPC).  
Type: [S3AccessPointVpcConfiguration](API_S3AccessPointVpcConfiguration.md) object  
Required: No

## See Also
<a name="API_CreateAndAttachS3AccessPointS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateAndAttachS3AccessPointS3Configuration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateAndAttachS3AccessPointS3Configuration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateAndAttachS3AccessPointS3Configuration) 