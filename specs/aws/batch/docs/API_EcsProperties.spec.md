---
id: "@specs/aws/batch/docs/API_EcsProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EcsProperties"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EcsProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EcsProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EcsProperties
<a name="API_EcsProperties"></a>

An object that contains the properties for the Amazon ECS resources of a job.

## Contents
<a name="API_EcsProperties_Contents"></a>

 ** taskProperties **   <a name="Batch-Type-EcsProperties-taskProperties"></a>
An object that contains the properties for the Amazon ECS task definition of a job.  
This object is currently limited to one task element. However, the task element can run up to 10 containers.
Type: Array of [EcsTaskProperties](API_EcsTaskProperties.md) objects  
Required: Yes

## See Also
<a name="API_EcsProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EcsProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EcsProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EcsProperties) 