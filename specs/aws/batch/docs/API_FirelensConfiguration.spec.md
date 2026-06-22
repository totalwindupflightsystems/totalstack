---
id: "@specs/aws/batch/docs/API_FirelensConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirelensConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# FirelensConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_FirelensConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirelensConfiguration
<a name="API_FirelensConfiguration"></a>

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) routing in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_FirelensConfiguration_Contents"></a>

 ** type **   <a name="Batch-Type-FirelensConfiguration-type"></a>
The log router to use. The valid values are `fluentd` or `fluentbit`.  
Type: String  
Valid Values: `fluentd | fluentbit`   
Required: Yes

 ** options **   <a name="Batch-Type-FirelensConfiguration-options"></a>
The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}`. For more information, see [Creating a task definition that uses a FireLens configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef) in the *Amazon Elastic Container Service Developer Guide*.  
Type: String to string map  
Required: No

## See Also
<a name="API_FirelensConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FirelensConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FirelensConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FirelensConfiguration) 