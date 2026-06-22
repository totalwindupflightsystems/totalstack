---
id: "@specs/aws/batch/docs/API_RuntimePlatform"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuntimePlatform"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# RuntimePlatform

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_RuntimePlatform
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuntimePlatform
<a name="API_RuntimePlatform"></a>

 An object that represents the compute environment architecture for AWS Batch jobs on Fargate. 

## Contents
<a name="API_RuntimePlatform_Contents"></a>

 ** cpuArchitecture **   <a name="Batch-Type-RuntimePlatform-cpuArchitecture"></a>
The vCPU architecture. The default value is `X86_64`. Valid values are `X86_64` and `ARM64`.  
This parameter must be set to `X86_64` for Windows containers.
Fargate Spot is not supported on Windows-based containers on Fargate. A job queue will be blocked if a Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.
Type: String  
Required: No

 ** operatingSystemFamily **   <a name="Batch-Type-RuntimePlatform-operatingSystemFamily"></a>
The operating system for the compute environment. Valid values are: `LINUX` (default), `WINDOWS_SERVER_2019_CORE`, `WINDOWS_SERVER_2019_FULL`, `WINDOWS_SERVER_2022_CORE`, and `WINDOWS_SERVER_2022_FULL`.  
The following parameters can’t be set for Windows containers: `linuxParameters`, `privileged`, `user`, `ulimits`, `readonlyRootFilesystem`, and `efsVolumeConfiguration`.
The AWS Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is `LINUX`, the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.
Fargate Spot is not supported on Windows-based containers on Fargate. A job queue will be blocked if a Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.
Type: String  
Required: No

## See Also
<a name="API_RuntimePlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/RuntimePlatform) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/RuntimePlatform) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/RuntimePlatform) 