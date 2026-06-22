---
id: "@specs/aws/emr/docs/API_HadoopStepConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HadoopStepConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# HadoopStepConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_HadoopStepConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HadoopStepConfig
<a name="API_HadoopStepConfig"></a>

A cluster step consisting of a JAR file whose main function will be executed. The main function submits a job for Hadoop to execute and waits for the job to finish or fail.

## Contents
<a name="API_HadoopStepConfig_Contents"></a>

 ** Args **   <a name="EMR-Type-HadoopStepConfig-Args"></a>
The list of command line arguments to pass to the JAR file's main function for execution.  
Type: Array of strings  
Required: No

 ** Jar **   <a name="EMR-Type-HadoopStepConfig-Jar"></a>
The path to the JAR file that runs during the step.  
Type: String  
Required: No

 ** MainClass **   <a name="EMR-Type-HadoopStepConfig-MainClass"></a>
The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.  
Type: String  
Required: No

 ** Properties **   <a name="EMR-Type-HadoopStepConfig-Properties"></a>
The list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.  
Type: String to string map  
Required: No

## See Also
<a name="API_HadoopStepConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/HadoopStepConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/HadoopStepConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/HadoopStepConfig) 