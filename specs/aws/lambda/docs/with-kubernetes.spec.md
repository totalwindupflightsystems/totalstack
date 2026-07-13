---
id: "@specs/aws/lambda/docs/with-kubernetes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Kubernetes"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Kubernetes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-kubernetes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using Lambda with Kubernetes
<a name="with-kubernetes"></a>

You can deploy and manage Lambda functions with the Kubernetes API using [AWS Controllers for Kubernetes (ACK)](https://aws-controllers-k8s.github.io/community/docs/community/overview/) or [Crossplane](https://docs.crossplane.io/latest/packages/providers/).

## AWS Controllers for Kubernetes (ACK)
<a name="kubernetes-ack"></a>

You can use ACK to deploy and manage AWS resources from the Kubernetes API. Through ACK, AWS provides open-source custom controllers for AWS services such as Lambda, Amazon Elastic Container Registry (Amazon ECR), Amazon Simple Storage Service (Amazon S3), and Amazon SageMaker AI. Each supported AWS service has its own custom controller. In your Kubernetes cluster, install a controller for each AWS service that you want to use. Then, create a [Custom Resource Definition (CRD)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) to define the AWS resources.

We recommend that you use [Helm 3.8 or later](https://helm.sh/docs/intro/install/) to install ACK controllers. Every ACK controller comes with its own Helm chart, which installs the controller, CRDs, and Kubernetes RBAC rules. For more information, see [Install an ACK Controller](https://aws-controllers-k8s.github.io/community/docs/user-docs/install/) in the ACK documentation.

After you create the ACK custom resource, you can use it like any other built-in Kubernetes object. For example, you can deploy and manage Lambda functions with your preferred Kubernetes toolchains, including [kubectl](https://kubernetes.io/docs/reference/kubectl/).

Here are some example use cases for provisioning Lambda functions through ACK:
+ Your organization uses [role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) and [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to create permissions boundaries. With ACK, you can reuse this security model for Lambda without having to create new users and policies.
+ Your organization has a DevOps process to deploy resources into an Amazon Elastic Kubernetes Service (Amazon EKS) cluster using Kubernetes manifests. With ACK, you can use a manifest to provision Lambda functions without creating separate infrastructure as code templates.

For more information about using ACK, see the [Lambda tutorial in the ACK documentation](https://aws-controllers-k8s.github.io/community/docs/tutorials/lambda-oci-example/).

## Crossplane
<a name="kubernetes-crossplane"></a>

[Crossplane](https://docs.crossplane.io/latest/packages/providers/) is an open-source Cloud Native Computing Foundation (CNCF) project that uses Kubernetes to manage cloud infrastructure resources. With Crossplane, developers can request infrastructure without needing to understand its complexities. Platform teams retain control over how the infrastructure is provisioned and managed.

Using Crossplane, you can deploy and manage Lambda functions with your preferred Kubernetes toolchains such as [kubectl](https://kubernetes.io/docs/reference/kubectl/), and any CI/CD pipeline that can deploy manifests to Kubernetes. Here are some example use cases for provisioning Lambda functions through Crossplane:
+ Your organization wants to enforce compliance by ensuring that Lambda functions have the correct [tags](configuration-tags.md). Platform teams can use [Crossplane Compositions](https://docs.crossplane.io/latest/get-started/get-started-with-composition/) to define this policy through API abstractions. Developers can then use these abstractions to deploy Lambda functions with tags.
+ Your project uses GitOps with Kubernetes. In this model, Kubernetes continuously reconciles the git repository (desired state) with the resources running inside the cluster (current state). If there are differences, the GitOps process automatically makes changes to the cluster. You can use GitOps with Kubernetes for deploying and managing Lambda functions through Crossplane, using familiar Kubernetes tools and concepts such as [CRDs](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) and [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/).

To learn more about using Crossplane with Lambda, see the following:
+ [AWS Blueprints for Crossplane](https://github.com/awslabs/crossplane-on-eks/blob/main/examples/upbound-aws-provider/README.md#deploy-the-examples): This repository includes examples of how to use Crossplane to deploy AWS resources, including Lambda functions.
**Note**  
AWS Blueprints for Crossplane are under active development and should not be used in production.
+ [Deploying Lambda with Amazon EKS and Crossplane](https://www.youtube.com/watch?v=m-9KLq29K4k): This video demonstrates an advanced example of deploying an AWS serverless architecture with Crossplane, exploring the design from both the developer and platform perspectives.