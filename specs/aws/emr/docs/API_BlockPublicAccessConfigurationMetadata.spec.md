---
id: "@specs/aws/emr/docs/API_BlockPublicAccessConfigurationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlockPublicAccessConfigurationMetadata"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# BlockPublicAccessConfigurationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_BlockPublicAccessConfigurationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlockPublicAccessConfigurationMetadata
<a name="API_BlockPublicAccessConfigurationMetadata"></a>

Properties that describe the AWS principal that created the `BlockPublicAccessConfiguration` using the `PutBlockPublicAccessConfiguration` action as well as the date and time that the configuration was created. Each time a configuration for block public access is updated, Amazon EMR updates this metadata.

## Contents
<a name="API_BlockPublicAccessConfigurationMetadata_Contents"></a>

 ** CreatedByArn **   <a name="EMR-Type-BlockPublicAccessConfigurationMetadata-CreatedByArn"></a>
The Amazon Resource Name that created or last modified the configuration.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** CreationDateTime **   <a name="EMR-Type-BlockPublicAccessConfigurationMetadata-CreationDateTime"></a>
The date and time that the configuration was created.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_BlockPublicAccessConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/BlockPublicAccessConfigurationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/BlockPublicAccessConfigurationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/BlockPublicAccessConfigurationMetadata) 