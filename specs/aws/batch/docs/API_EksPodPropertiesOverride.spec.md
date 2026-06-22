---
id: "@specs/aws/batch/docs/API_EksPodPropertiesOverride"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksPodPropertiesOverride"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksPodPropertiesOverride

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksPodPropertiesOverride
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksPodPropertiesOverride
<a name="API_EksPodPropertiesOverride"></a>

An object that contains overrides for the Kubernetes pod properties of a job.

## Contents
<a name="API_EksPodPropertiesOverride_Contents"></a>

 ** containers **   <a name="Batch-Type-EksPodPropertiesOverride-containers"></a>
The overrides for the container that's used on the Amazon EKS pod.  
Type: Array of [EksContainerOverride](API_EksContainerOverride.md) objects  
Required: No

 ** initContainers **   <a name="Batch-Type-EksPodPropertiesOverride-initContainers"></a>
The overrides for the `initContainers` defined in the Amazon EKS pod. These containers run before application containers, always run to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation*.  
Type: Array of [EksContainerOverride](API_EksContainerOverride.md) objects  
Required: No

 ** metadata **   <a name="Batch-Type-EksPodPropertiesOverride-metadata"></a>
Metadata about the overrides for the container that's used on the Amazon EKS pod.  
Type: [EksMetadata](API_EksMetadata.md) object  
Required: No

## See Also
<a name="API_EksPodPropertiesOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPodPropertiesOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPodPropertiesOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPodPropertiesOverride) 