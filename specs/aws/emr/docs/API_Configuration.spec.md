---
id: "@specs/aws/emr/docs/API_Configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuration
<a name="API_Configuration"></a>

**Note**  
Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Contents
<a name="API_Configuration_Contents"></a>

 ** Classification **   <a name="EMR-Type-Configuration-Classification"></a>
The classification within a configuration.  
Type: String  
Required: No

 ** Configurations **   <a name="EMR-Type-Configuration-Configurations"></a>
A list of additional configurations to apply within a configuration object.  
Type: Array of [Configuration](#API_Configuration) objects  
Required: No

 ** Properties **   <a name="EMR-Type-Configuration-Properties"></a>
A set of properties specified within a configuration classification.  
Type: String to string map  
Required: No

## See Also
<a name="API_Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Configuration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Configuration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Configuration) 