---
id: "@specs/aws/batch/docs/API_EksPodProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksPodProperties"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksPodProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksPodProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksPodProperties
<a name="API_EksPodProperties"></a>

The properties for the pod.

## Contents
<a name="API_EksPodProperties_Contents"></a>

 ** containers **   <a name="Batch-Type-EksPodProperties-containers"></a>
The properties of the container that's used on the Amazon EKS pod.  
This object is limited to 10 elements.
Type: Array of [EksContainer](API_EksContainer.md) objects  
Required: No

 ** dnsPolicy **   <a name="Batch-Type-EksPodProperties-dnsPolicy"></a>
The DNS policy for the pod. The default value is `ClusterFirst`. If the `hostNetwork` parameter is not specified, the default is `ClusterFirstWithHostNet`. `ClusterFirst` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. For more information, see [Pod's DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation*.  
Valid values: `Default` \| `ClusterFirst` \| `ClusterFirstWithHostNet`   
Type: String  
Required: No

 ** hostNetwork **   <a name="Batch-Type-EksPodProperties-hostNetwork"></a>
Indicates if the pod uses the hosts' network IP address. The default value is `true`. Setting this to `false` enables the Kubernetes pod networking model. Most AWS Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see [Host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces) and [Pod networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

 ** imagePullSecrets **   <a name="Batch-Type-EksPodProperties-imagePullSecrets"></a>
References a Kubernetes secret resource. It holds a list of secrets. These secrets help to gain access to pull an images from a private registry.  
 `ImagePullSecret$name` is required when this object is used.  
Type: Array of [ImagePullSecret](API_ImagePullSecret.md) objects  
Required: No

 ** initContainers **   <a name="Batch-Type-EksPodProperties-initContainers"></a>
These containers run before application containers, always runs to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation*.  
This object is limited to 10 elements.
Type: Array of [EksContainer](API_EksContainer.md) objects  
Required: No

 ** metadata **   <a name="Batch-Type-EksPodProperties-metadata"></a>
Metadata about the Kubernetes pod. For more information, see [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation*.  
Type: [EksMetadata](API_EksMetadata.md) object  
Required: No

 ** serviceAccountName **   <a name="Batch-Type-EksPodProperties-serviceAccountName"></a>
The name of the service account that's used to run the pod. For more information, see [Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) and [Configure a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) in the *Amazon EKS User Guide* and [Configure service accounts for pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the *Kubernetes documentation*.  
Type: String  
Required: No

 ** shareProcessNamespace **   <a name="Batch-Type-EksPodProperties-shareProcessNamespace"></a>
Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/).  
Type: Boolean  
Required: No

 ** volumes **   <a name="Batch-Type-EksPodProperties-volumes"></a>
Specifies the volumes for a job definition that uses Amazon EKS resources.  
Type: Array of [EksVolume](API_EksVolume.md) objects  
Required: No

## See Also
<a name="API_EksPodProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPodProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPodProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPodProperties) 