---
id: "@specs/aws/batch/docs/API_EksContainerSecurityContext"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksContainerSecurityContext"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksContainerSecurityContext

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksContainerSecurityContext
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksContainerSecurityContext
<a name="API_EksContainerSecurityContext"></a>

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksContainerSecurityContext_Contents"></a>

 ** allowPrivilegeEscalation **   <a name="Batch-Type-EksContainerSecurityContext-allowPrivilegeEscalation"></a>
Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false`.  
Type: Boolean  
Required: No

 ** privileged **   <a name="Batch-Type-EksContainerSecurityContext-privileged"></a>
When this parameter is `true`, the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false`. This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

 ** readOnlyRootFilesystem **   <a name="Batch-Type-EksContainerSecurityContext-readOnlyRootFilesystem"></a>
When this parameter is `true`, the container is given read-only access to its root file system. The default value is `false`. This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

 ** runAsGroup **   <a name="Batch-Type-EksContainerSecurityContext-runAsGroup"></a>
When this parameter is specified, the container is run as the specified group ID (`gid`). If this parameter isn't specified, the default is the group that's specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.  
Type: Long  
Required: No

 ** runAsNonRoot **   <a name="Batch-Type-EksContainerSecurityContext-runAsNonRoot"></a>
When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isn't specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

 ** runAsUser **   <a name="Batch-Type-EksContainerSecurityContext-runAsUser"></a>
When this parameter is specified, the container is run as the specified user ID (`uid`). If this parameter isn't specified, the default is the user that's specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation*.  
Type: Long  
Required: No

## See Also
<a name="API_EksContainerSecurityContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainerSecurityContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainerSecurityContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainerSecurityContext) 