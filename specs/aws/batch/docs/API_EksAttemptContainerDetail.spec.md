---
id: "@specs/aws/batch/docs/API_EksAttemptContainerDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksAttemptContainerDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksAttemptContainerDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksAttemptContainerDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksAttemptContainerDetail
<a name="API_EksAttemptContainerDetail"></a>

An object that represents the details for an attempt for a job attempt that an Amazon EKS container runs.

## Contents
<a name="API_EksAttemptContainerDetail_Contents"></a>

 ** containerID **   <a name="Batch-Type-EksAttemptContainerDetail-containerID"></a>
The ID for the container.  
Type: String  
Required: No

 ** exitCode **   <a name="Batch-Type-EksAttemptContainerDetail-exitCode"></a>
The exit code returned for the job attempt. A non-zero exit code is considered failed.  
Type: Integer  
Required: No

 ** name **   <a name="Batch-Type-EksAttemptContainerDetail-name"></a>
The name of a container.  
Type: String  
Required: No

 ** reason **   <a name="Batch-Type-EksAttemptContainerDetail-reason"></a>
A short (255 max characters) human-readable string to provide additional details for a running or stopped container.  
Type: String  
Required: No

## See Also
<a name="API_EksAttemptContainerDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksAttemptContainerDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksAttemptContainerDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksAttemptContainerDetail) 