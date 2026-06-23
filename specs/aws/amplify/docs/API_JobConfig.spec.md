---
id: "@specs/aws/amplify/docs/API_JobConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobConfig"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# JobConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_JobConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobConfig
<a name="API_JobConfig"></a>

Describes the configuration details that apply to the jobs for an Amplify app.

Use `JobConfig` to apply configuration to jobs, such as customizing the build instance size when you create or update an Amplify app. For more information about customizable build instances, see [Custom build instances](https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-instance.html) in the *Amplify User Guide*.

## Contents
<a name="API_JobConfig_Contents"></a>

 ** buildComputeType **   <a name="amplify-Type-JobConfig-buildComputeType"></a>
Specifies the size of the build instance. Amplify supports three instance sizes: `STANDARD_8GB`, `LARGE_16GB`, and `XLARGE_72GB`. If you don't specify a value, Amplify uses the `STANDARD_8GB` default.  
The following list describes the CPU, memory, and storage capacity for each build instance type:    
STANDARD\_8GB  
+ vCPUs: 4
+ Memory: 8 GiB
+ Disk space: 128 GB  
LARGE\_16GB  
+ vCPUs: 8
+ Memory: 16 GiB
+ Disk space: 128 GB  
XLARGE\_72GB  
+ vCPUs: 36
+ Memory: 72 GiB
+ Disk space: 256 GB
Type: String  
Valid Values: `STANDARD_8GB | LARGE_16GB | XLARGE_72GB`   
Required: Yes

## See Also
<a name="API_JobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/JobConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/JobConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/JobConfig) 