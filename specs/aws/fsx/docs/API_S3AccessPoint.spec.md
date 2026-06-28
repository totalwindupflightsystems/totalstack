---
id: "@specs/aws/fsx/docs/API_S3AccessPoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3AccessPoint"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# S3AccessPoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_S3AccessPoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3AccessPoint
<a name="API_S3AccessPoint"></a>

Describes the S3 access point configuration of the S3 access point attachment.

## Contents
<a name="API_S3AccessPoint_Contents"></a>

 ** Alias **   <a name="FSx-Type-S3AccessPoint-Alias"></a>
The S3 access point's alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[0-9a-z\\-]{1,63}`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-S3AccessPoint-ResourceARN"></a>
he S3 access point's ARN.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`   
Required: No

 ** VpcConfiguration **   <a name="FSx-Type-S3AccessPoint-VpcConfiguration"></a>
The S3 access point's virtual private cloud (VPC) configuration.  
Type: [S3AccessPointVpcConfiguration](API_S3AccessPointVpcConfiguration.md) object  
Required: No

## See Also
<a name="API_S3AccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPoint) 