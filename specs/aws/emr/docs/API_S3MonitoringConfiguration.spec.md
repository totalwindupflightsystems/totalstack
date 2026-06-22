---
id: "@specs/aws/emr/docs/API_S3MonitoringConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3MonitoringConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# S3MonitoringConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_S3MonitoringConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3MonitoringConfiguration
<a name="API_S3MonitoringConfiguration"></a>

The Amazon S3 configuration for monitoring log publishing. You can configure your step to send log information to Amazon S3. When it's specified, it takes precedence over the cluster's logging configuration. If you don't specify this configuration entirely, or omit individual fields, EMR falls back to cluster-level logging behavior.

## Contents
<a name="API_S3MonitoringConfiguration_Contents"></a>

 ** EncryptionKeyArn **   <a name="EMR-Type-S3MonitoringConfiguration-EncryptionKeyArn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogUri **   <a name="EMR-Type-S3MonitoringConfiguration-LogUri"></a>
The Amazon S3 destination URI for log publishing.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_S3MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/S3MonitoringConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/S3MonitoringConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/S3MonitoringConfiguration) 