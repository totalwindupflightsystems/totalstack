---
id: "@specs/aws/batch/docs/API_EksContainerResourceRequirements"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksContainerResourceRequirements"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksContainerResourceRequirements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksContainerResourceRequirements
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksContainerResourceRequirements
<a name="API_EksContainerResourceRequirements"></a>

The type and amount of resources to assign to a container. The supported resources include `memory`, `cpu`, and `nvidia.com/gpu`. For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksContainerResourceRequirements_Contents"></a>

 ** limits **   <a name="Batch-Type-EksContainerResourceRequirements-limits"></a>
The type and quantity of the resources to reserve for the container. The values vary based on the `name` that's specified. Resources can be requested using either the `limits` or the `requests` objects.    
memory  
The memory hard limit (in MiB) for the container, using whole integers, with a "Mi" suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits`, `requests`, or both. If `memory` is specified in both places, then the value that's specified in `limits` must be equal to the value that's specified in `requests`.  
To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the * AWS Batch User Guide*.  
cpu  
The number of CPUs that's reserved for the container. Values must be an even multiple of `0.25`. `cpu` can be specified in `limits`, `requests`, or both. If `cpu` is specified in both places, then the value that's specified in `limits` must be at least as large as the value that's specified in `requests`.  
nvidia.com/gpu  
The number of GPUs that's reserved for the container. Values must be a whole integer. `memory` can be specified in `limits`, `requests`, or both. If `memory` is specified in both places, then the value that's specified in `limits` must be equal to the value that's specified in `requests`.
Type: String to string map  
Value Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** requests **   <a name="Batch-Type-EksContainerResourceRequirements-requests"></a>
The type and quantity of the resources to request for the container. The values vary based on the `name` that's specified. Resources can be requested by using either the `limits` or the `requests` objects.    
memory  
The memory hard limit (in MiB) for the container, using whole integers, with a "Mi" suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits`, `requests`, or both. If `memory` is specified in both, then the value that's specified in `limits` must be equal to the value that's specified in `requests`.  
If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the * AWS Batch User Guide*.  
cpu  
The number of CPUs that are reserved for the container. Values must be an even multiple of `0.25`. `cpu` can be specified in `limits`, `requests`, or both. If `cpu` is specified in both, then the value that's specified in `limits` must be at least as large as the value that's specified in `requests`.  
nvidia.com/gpu  
The number of GPUs that are reserved for the container. Values must be a whole integer. `nvidia.com/gpu` can be specified in `limits`, `requests`, or both. If `nvidia.com/gpu` is specified in both, then the value that's specified in `limits` must be equal to the value that's specified in `requests`.
Type: String to string map  
Value Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

## See Also
<a name="API_EksContainerResourceRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainerResourceRequirements) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainerResourceRequirements) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainerResourceRequirements) 