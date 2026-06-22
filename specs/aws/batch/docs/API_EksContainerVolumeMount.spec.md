---
id: "@specs/aws/batch/docs/API_EksContainerVolumeMount"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksContainerVolumeMount"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksContainerVolumeMount

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksContainerVolumeMount
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksContainerVolumeMount
<a name="API_EksContainerVolumeMount"></a>

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksContainerVolumeMount_Contents"></a>

 ** mountPath **   <a name="Batch-Type-EksContainerVolumeMount-mountPath"></a>
The path on the container where the volume is mounted.  
Type: String  
Required: No

 ** name **   <a name="Batch-Type-EksContainerVolumeMount-name"></a>
The name the volume mount. This must match the name of one of the volumes in the pod.  
Type: String  
Required: No

 ** readOnly **   <a name="Batch-Type-EksContainerVolumeMount-readOnly"></a>
If this value is `true`, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false`.  
Type: Boolean  
Required: No

 ** subPath **   <a name="Batch-Type-EksContainerVolumeMount-subPath"></a>
A sub-path inside the referenced volume instead of its root.  
Type: String  
Required: No

## See Also
<a name="API_EksContainerVolumeMount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainerVolumeMount) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainerVolumeMount) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainerVolumeMount) 