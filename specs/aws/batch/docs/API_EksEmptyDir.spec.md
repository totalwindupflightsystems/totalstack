---
id: "@specs/aws/batch/docs/API_EksEmptyDir"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksEmptyDir"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksEmptyDir

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksEmptyDir
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksEmptyDir
<a name="API_EksEmptyDir"></a>

Specifies the configuration of a Kubernetes `emptyDir` volume. An `emptyDir` volume is first created when a pod is assigned to a node. It exists as long as that pod is running on that node. The `emptyDir` volume is initially empty. All containers in the pod can read and write the files in the `emptyDir` volume. However, the `emptyDir` volume can be mounted at the same or different paths in each container. When a pod is removed from a node for any reason, the data in the `emptyDir` is deleted permanently. For more information, see [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) in the *Kubernetes documentation*.

## Contents
<a name="API_EksEmptyDir_Contents"></a>

 ** medium **   <a name="Batch-Type-EksEmptyDir-medium"></a>
The medium to store the volume. The default value is an empty string, which uses the storage of the node.    
""  
 **(Default)** Use the disk storage of the node.  
"Memory"  
Use the `tmpfs` volume that's backed by the RAM of the node. Contents of the volume are lost when the node reboots, and any storage on the volume counts against the container's memory limit.
Type: String  
Required: No

 ** sizeLimit **   <a name="Batch-Type-EksEmptyDir-sizeLimit"></a>
The maximum size of the volume. By default, there's no maximum size defined.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## See Also
<a name="API_EksEmptyDir_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksEmptyDir) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksEmptyDir) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksEmptyDir) 