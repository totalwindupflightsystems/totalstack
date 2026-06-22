---
id: "@specs/aws/sesv2/docs/API_CloudWatchDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudWatchDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CloudWatchDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CloudWatchDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CloudWatchDestination
<a name="API_CloudWatchDestination"></a>

An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

## Contents
<a name="API_CloudWatchDestination_Contents"></a>

 ** DimensionConfigurations **   <a name="SES-Type-CloudWatchDestination-DimensionConfigurations"></a>
An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.  
Type: Array of [CloudWatchDimensionConfiguration](API_CloudWatchDimensionConfiguration.md) objects  
Required: Yes

## See Also
<a name="API_CloudWatchDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CloudWatchDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CloudWatchDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CloudWatchDestination) 