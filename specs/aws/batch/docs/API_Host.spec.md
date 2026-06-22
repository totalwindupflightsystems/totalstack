---
id: "@specs/aws/batch/docs/API_Host"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Host"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# Host

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_Host
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Host
<a name="API_Host"></a>

Determine whether your data volume persists on the host container instance and where it's stored. If this parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.

## Contents
<a name="API_Host_Contents"></a>

 ** sourcePath **   <a name="Batch-Type-Host-sourcePath"></a>
The path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.  
This parameter isn't applicable to jobs that run on Fargate resources. Don't provide this for these jobs.
Type: String  
Required: No

## See Also
<a name="API_Host_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Host) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Host) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Host) 