---
id: "@specs/aws/batch/docs/API_EksConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksConfiguration
<a name="API_EksConfiguration"></a>

Configuration for the Amazon EKS cluster that supports the AWS Batch compute environment. The cluster must exist before the compute environment can be created.

## Contents
<a name="API_EksConfiguration_Contents"></a>

 ** eksClusterArn **   <a name="Batch-Type-EksConfiguration-eksClusterArn"></a>
The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is `arn:aws:eks:us-east-1:123456789012:cluster/ClusterForBatch `.   
Type: String  
Required: Yes

 ** kubernetesNamespace **   <a name="Batch-Type-EksConfiguration-kubernetesNamespace"></a>
The namespace of the Amazon EKS cluster. AWS Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to `default`, can't start with "`kube-`," and must match this regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`. For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.  
Type: String  
Required: Yes

## See Also
<a name="API_EksConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksConfiguration) 