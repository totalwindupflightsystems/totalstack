---
id: "@specs/aws/batch/docs/API_EksMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksMetadata"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksMetadata
<a name="API_EksMetadata"></a>

Describes and uniquely identifies Kubernetes resources. For example, the compute environment that a pod runs in or the `jobID` for a job running in the pod. For more information, see [ Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksMetadata_Contents"></a>

 ** annotations **   <a name="Batch-Type-EksMetadata-annotations"></a>
Key-value pairs used to attach arbitrary, non-identifying metadata to Kubernetes objects. Valid annotation keys have two segments: an optional prefix and a name, separated by a slash (/).   
+ The prefix is optional and must be 253 characters or less. If specified, the prefix must be a DNS subdomain− a series of DNS labels separated by dots (.), and it must end with a slash (/).
+ The name segment is required and must be 63 characters or less. It can include alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (\_), and dots (.), but must begin and end with an alphanumeric character.
Annotation values must be 255 characters or less.
Annotations can be added or modified at any time. Each resource can have multiple annotations.   
Type: String to string map  
Required: No

 ** labels **   <a name="Batch-Type-EksMetadata-labels"></a>
Key-value pairs used to identify, sort, and organize cube resources. Can contain up to 63 uppercase letters, lowercase letters, numbers, hyphens (-), and underscores (\_). Labels can be added or modified at any time. Each resource can have multiple labels, but each key must be unique for a given object.  
Type: String to string map  
Required: No

 ** namespace **   <a name="Batch-Type-EksMetadata-namespace"></a>
The namespace of the Amazon EKS cluster. In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. AWS Batch places Batch Job pods in this namespace. If this field is provided, the value can't be empty or null. It must meet the following requirements:  
+ 1-63 characters long
+ Can't be set to default
+ Can't start with `kube` 
+ Must match the following regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$` 
 For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the *Kubernetes documentation*. This namespace can be different from the `kubernetesNamespace` set in the compute environment's `EksConfiguration`, but must have identical role-based access control (RBAC) roles as the compute environment's `kubernetesNamespace`. For multi-node parallel jobs, the same value must be provided across all the node ranges.  
Type: String  
Required: No

## See Also
<a name="API_EksMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksMetadata) 