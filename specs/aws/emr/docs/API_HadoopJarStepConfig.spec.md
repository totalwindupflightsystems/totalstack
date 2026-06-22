---
id: "@specs/aws/emr/docs/API_HadoopJarStepConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HadoopJarStepConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# HadoopJarStepConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_HadoopJarStepConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HadoopJarStepConfig
<a name="API_HadoopJarStepConfig"></a>

A job flow step consisting of a JAR file whose main function will be executed. The main function submits a job for Hadoop to execute and waits for the job to finish or fail.

## Contents
<a name="API_HadoopJarStepConfig_Contents"></a>

 ** Jar **   <a name="EMR-Type-HadoopJarStepConfig-Jar"></a>
A path to a JAR file run during the step.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Args **   <a name="EMR-Type-HadoopJarStepConfig-Args"></a>
A list of command line arguments passed to the JAR file's main function when executed.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** MainClass **   <a name="EMR-Type-HadoopJarStepConfig-MainClass"></a>
The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Properties **   <a name="EMR-Type-HadoopJarStepConfig-Properties"></a>
A list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.  
Type: Array of [KeyValue](API_KeyValue.md) objects  
Required: No

## See Also
<a name="API_HadoopJarStepConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/HadoopJarStepConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/HadoopJarStepConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/HadoopJarStepConfig) 