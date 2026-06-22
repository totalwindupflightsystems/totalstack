---
id: "@specs/aws/batch/docs/API_LinuxParameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LinuxParameters"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# LinuxParameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_LinuxParameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LinuxParameters
<a name="API_LinuxParameters"></a>

Linux-specific modifications that are applied to the container, such as details for device mappings.

## Contents
<a name="API_LinuxParameters_Contents"></a>

 ** devices **   <a name="Batch-Type-LinuxParameters-devices"></a>
Any of the host devices to expose to the container. This parameter maps to `Devices` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--device` option to [docker run](https://docs.docker.com/engine/reference/run/).  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
Type: Array of [Device](API_Device.md) objects  
Required: No

 ** initProcessEnabled **   <a name="Batch-Type-LinuxParameters-initProcessEnabled"></a>
If true, run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to [docker run](https://docs.docker.com/engine/reference/run/). This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`   
Type: Boolean  
Required: No

 ** maxSwap **   <a name="Batch-Type-LinuxParameters-maxSwap"></a>
The total amount of swap memory (in MiB) a container can use. This parameter is translated to the `--memory-swap` option to [docker run](https://docs.docker.com/engine/reference/run/) where the value is the sum of the container memory plus the `maxSwap` value. For more information, see [`--memory-swap` details](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details) in the Docker documentation.  
If a `maxSwap` value of `0` is specified, the container doesn't use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container doesn't use the swap configuration for the container instance on which it runs. A `maxSwap` value must be set for the `swappiness` parameter to be used.  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
Type: Integer  
Required: No

 ** sharedMemorySize **   <a name="Batch-Type-LinuxParameters-sharedMemorySize"></a>
The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to [docker run](https://docs.docker.com/engine/reference/run/).  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
Type: Integer  
Required: No

 ** swappiness **   <a name="Batch-Type-LinuxParameters-swappiness"></a>
You can use this parameter to tune a container's memory swappiness behavior. A `swappiness` value of `0` causes swapping to not occur unless absolutely necessary. A `swappiness` value of `100` causes pages to be swapped aggressively. Valid values are whole numbers between `0` and `100`. If the `swappiness` parameter isn't specified, a default value of `60` is used. If a value isn't specified for `maxSwap`, then this parameter is ignored. If `maxSwap` is set to 0, the container doesn't use swap. This parameter maps to the `--memory-swappiness` option to [docker run](https://docs.docker.com/engine/reference/run/).  
Consider the following when you use a per-container swap configuration.  
+ Swap space must be enabled and allocated on the container instance for the containers to use.
**Note**  
By default, the Amazon ECS optimized AMIs don't have swap enabled. You must enable swap on the instance to use this feature. For more information, see [Instance store swap volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html) in the *Amazon EC2 User Guide for Linux Instances* or [How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?](http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/) 
+ The swap space parameters are only supported for job definitions using EC2 resources.
+ If the `maxSwap` and `swappiness` parameters are omitted from a job definition, each container has a default `swappiness` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide it for these jobs.
Type: Integer  
Required: No

 ** tmpfs **   <a name="Batch-Type-LinuxParameters-tmpfs"></a>
The container path, mount options, and size (in MiB) of the `tmpfs` mount. This parameter maps to the `--tmpfs` option to [docker run](https://docs.docker.com/engine/reference/run/).  
This parameter isn't applicable to jobs that are running on Fargate resources. Don't provide this parameter for this resource type.
Type: Array of [Tmpfs](API_Tmpfs.md) objects  
Required: No

## See Also
<a name="API_LinuxParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LinuxParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LinuxParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LinuxParameters) 