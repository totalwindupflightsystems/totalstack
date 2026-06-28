---
id: "@specs/aws/amp/docs/API_RoleConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RoleConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# RoleConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_RoleConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RoleConfiguration
<a name="API_RoleConfiguration"></a>

Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.

## Contents
<a name="API_RoleConfiguration_Contents"></a>

 ** sourceRoleArn **   <a name="prometheus-Type-RoleConfiguration-sourceRoleArn"></a>
The Amazon Resource Name (ARN) of the role used in the source account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write).  
Type: String  
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`   
Required: No

 ** targetRoleArn **   <a name="prometheus-Type-RoleConfiguration-targetRoleArn"></a>
The Amazon Resource Name (ARN) of the role used in the target account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write).  
Type: String  
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`   
Required: No

## See Also
<a name="API_RoleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/RoleConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/RoleConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/RoleConfiguration) 