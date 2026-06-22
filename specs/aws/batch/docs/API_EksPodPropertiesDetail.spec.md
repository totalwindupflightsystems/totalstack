---
id: "@specs/aws/batch/docs/API_EksPodPropertiesDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksPodPropertiesDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksPodPropertiesDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksPodPropertiesDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksPodPropertiesDetail
<a name="API_EksPodPropertiesDetail"></a>

The details for the pod.

## Contents
<a name="API_EksPodPropertiesDetail_Contents"></a>

 ** containers **   <a name="Batch-Type-EksPodPropertiesDetail-containers"></a>
The properties of the container that's used on the Amazon EKS pod.  
Type: Array of [EksContainerDetail](API_EksContainerDetail.md) objects  
Required: No

 ** dnsPolicy **   <a name="Batch-Type-EksPodPropertiesDetail-dnsPolicy"></a>
The DNS policy for the pod. The default value is `ClusterFirst`. If the `hostNetwork` parameter is not specified, the default is `ClusterFirstWithHostNet`. `ClusterFirst` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. If no value was specified for `dnsPolicy` in the [RegisterJobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) API operation, then no value will be returned for `dnsPolicy` by either of [DescribeJobDefinitions](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobDefinitions.html) or [DescribeJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html) API operations. The pod spec setting will contain either `ClusterFirst` or `ClusterFirstWithHostNet`, depending on the value of the `hostNetwork` parameter. For more information, see [Pod's DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation*.  
Valid values: `Default` \| `ClusterFirst` \| `ClusterFirstWithHostNet`   
Type: String  
Required: No

 ** hostNetwork **   <a name="Batch-Type-EksPodPropertiesDetail-hostNetwork"></a>
Indicates if the pod uses the hosts' network IP address. The default value is `true`. Setting this to `false` enables the Kubernetes pod networking model. Most AWS Batch workloads are egress-only and don't require the overhead of IP allocation for each pod for incoming connections. For more information, see [Host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces) and [Pod networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

 ** imagePullSecrets **   <a name="Batch-Type-EksPodPropertiesDetail-imagePullSecrets"></a>
Displays the reference pointer to the Kubernetes secret resource. These secrets help to gain access to pull an images from a private registry.  
Type: Array of [ImagePullSecret](API_ImagePullSecret.md) objects  
Required: No

 ** initContainers **   <a name="Batch-Type-EksPodPropertiesDetail-initContainers"></a>
The container registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store.  
Type: Array of [EksContainerDetail](API_EksContainerDetail.md) objects  
Required: No

 ** metadata **   <a name="Batch-Type-EksPodPropertiesDetail-metadata"></a>
Describes and uniquely identifies Kubernetes resources. For example, the compute environment that a pod runs in or the `jobID` for a job running in the pod. For more information, see [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation*.  
Type: [EksMetadata](API_EksMetadata.md) object  
Required: No

 ** nodeName **   <a name="Batch-Type-EksPodPropertiesDetail-nodeName"></a>
The name of the node for this job.  
Type: String  
Required: No

 ** podName **   <a name="Batch-Type-EksPodPropertiesDetail-podName"></a>
The name of the pod for this job.  
Type: String  
Required: No

 ** serviceAccountName **   <a name="Batch-Type-EksPodPropertiesDetail-serviceAccountName"></a>
The name of the service account that's used to run the pod. For more information, see [Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) and [Configure a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) in the *Amazon EKS User Guide* and [Configure service accounts for pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the *Kubernetes documentation*.  
Type: String  
Required: No

 ** shareProcessNamespace **   <a name="Batch-Type-EksPodPropertiesDetail-shareProcessNamespace"></a>
Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/).  
Type: Boolean  
Required: No

 ** volumes **   <a name="Batch-Type-EksPodPropertiesDetail-volumes"></a>
Specifies the volumes for a job definition using Amazon EKS resources.  
Type: Array of [EksVolume](API_EksVolume.md) objects  
Required: No

## See Also
<a name="API_EksPodPropertiesDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPodPropertiesDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPodPropertiesDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPodPropertiesDetail) 