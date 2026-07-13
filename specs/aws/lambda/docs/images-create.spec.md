---
id: "@specs/aws/lambda/docs/images-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Container images"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Container images

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/images-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Lambda function using a container image
<a name="images-create"></a>

Your AWS Lambda function's code consists of scripts or compiled programs and their dependencies. You use a *deployment package* to deploy your function code to Lambda. Lambda supports two types of deployment packages: container images and .zip file archives. 

There are three ways to build a container image for a Lambda function:
+ [Using an AWS base image for Lambda](#runtimes-images-lp)

  The [AWS base images](#runtimes-images-lp) are preloaded with a language runtime, a runtime interface client to manage the interaction between Lambda and your function code, and a runtime interface emulator for local testing.
+ [Using an AWS OS-only base image](#runtimes-images-provided)

  [AWS OS-only base images](https://gallery.ecr.aws/lambda/provided) contain an Amazon Linux distribution and the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/). These images are commonly used to create container images for compiled languages, such as [Go](go-image.md#go-image-provided) and [Rust](lambda-rust.md), and for a language or language version that Lambda doesn't provide a base image for, such as Node.js 19. You can also use OS-only base images to implement a [custom runtime](runtimes-custom.md). To make the image compatible with Lambda, you must include a [runtime interface client](#images-ric) for your language in the image.
+ [Using a non-AWS base image](#images-types)

  You can use an alternative base image from another container registry, such as Alpine Linux or Debian. You can also use a custom image created by your organization. To make the image compatible with Lambda, you must include a [runtime interface client](#images-ric) for your language in the image.

**Tip**  
To reduce the time it takes for Lambda container functions to become active, see [Use multi-stage builds](https://docs.docker.com/build/building/multi-stage/) in the Docker documentation. To build efficient container images, follow the [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

To create a Lambda function from a container image, build your image locally and upload it to an Amazon Elastic Container Registry (Amazon ECR) repository. If you're using a container image provided by an [AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html) seller, you need to clone the image to your private Amazon ECR repository first. Then, specify the repository URI when you create the function. The Amazon ECR repository must be in the same AWS Region as the Lambda function. You can create a function using an image in a different AWS account, as long as the image is in the same Region as the Lambda function. For more information, see [Amazon ECR cross-account permissions](#configuration-images-xaccount-permissions).

**Note**  
Lambda does not support Amazon ECR FIPS endpoints for container images. If your repository URI includes `ecr-fips`, you are using a FIPS endpoint. Example: `111122223333.dkr.ecr-fips.us-east-1.amazonaws.com`.

This page explains the base image types and requirements for creating Lambda-compatible container images.

**Note**  
You cannot change the [deployment package type](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html#lambda-CreateFunction-request-PackageType) (.zip or container image) for an existing function. For example, you cannot convert a container image function to use a .zip file archive. You must create a new function.

**Topics**
+ [Requirements](#images-reqs)
+ [Using an AWS base image for Lambda](#runtimes-images-lp)
+ [Using an AWS OS-only base image](#runtimes-images-provided)
+ [Using a non-AWS base image](#images-types)
+ [Runtime interface clients](#images-ric)
+ [Amazon ECR permissions](#gettingstarted-images-permissions)
+ [Function lifecycle](#images-lifecycle)

## Requirements
<a name="images-reqs"></a>

Install the [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and the [Docker CLI](https://docs.docker.com/get-docker). Additionally, note the following requirements:
+ The container image must implement the [Using the Lambda runtime API for custom runtimes](runtimes-api.md). The AWS open-source [runtime interface clients](#images-ric) implement the API. You can add a runtime interface client to your preferred base image to make it compatible with Lambda.
+ The container image must be able to run on a read-only file system. Your function code can access a writable `/tmp` directory with between 512 MB and 10,240 MB, in 1-MB increments, of storage. 
+ The default Lambda user must be able to read all the files required to run your function code. Lambda follows security best practices by defining a default Linux user with least-privileged permissions. This means that you don't need to specify a [USER](https://docs.docker.com/reference/dockerfile/#user) in your Dockerfile. Verify that your application code does not rely on files that other Linux users are restricted from running.
+ Lambda supports only Linux-based container images.
+ Lambda provides multi-architecture base images. However, the image you build for your function must target only one of the architectures. Lambda does not support functions that use multi-architecture container images.

## Using an AWS base image for Lambda
<a name="runtimes-images-lp"></a>

You can use one of the [AWS base images](https://gallery.ecr.aws/lambda/) for Lambda to build the container image for your function code. The base images are preloaded with a language runtime and other components required to run a container image on Lambda. You add your function code and dependencies to the base image and then package it as a container image.

AWS periodically provides updates to the AWS base images for Lambda. If your Dockerfile includes the image name in the FROM property, your Docker client pulls the latest version of the image from the [Amazon ECR repository](https://gallery.ecr.aws/lambda/). To use the updated base image, you must rebuild your container image and [update the function code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html).

The Node.js 20, Python 3.12, Java 21, .NET 8, Ruby 3.3, and later base images are based on the [Amazon Linux 2023 minimal container image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html). Earlier base images use Amazon Linux 2. AL2023 provides several advantages over Amazon Linux 2, including a smaller deployment footprint and updated versions of libraries such as `glibc`.

AL2023-based images use `microdnf` (symlinked as `dnf`) as the package manager instead of `yum`, which is the default package manager in Amazon Linux 2. `microdnf` is a standalone implementation of `dnf`. For a list of packages that are included in AL2023-based images, refer to the **Minimal Container** columns in [Comparing packages installed on Amazon Linux 2023 Container Images](https://docs.aws.amazon.com/linux/al2023/ug/al2023-container-image-types.html). For more information about the differences between AL2023 and Amazon Linux 2, see [Introducing the Amazon Linux 2023 runtime for AWS Lambda](https://aws.amazon.com/blogs/compute/introducing-the-amazon-linux-2023-runtime-for-aws-lambda/) on the AWS Compute Blog.

**Note**  
To run AL2023-based images locally, including with AWS Serverless Application Model (AWS SAM), you must use Docker version 20.10.10 or later.

To build a container image using an AWS base image, choose the instructions for your preferred language:
+ [Node.js](nodejs-image.md#nodejs-image-instructions)
+ [TypeScript](typescript-image.md#base-image-typescript) (uses a Node.js base image)
+ [Python](python-image.md#python-image-instructions)
+ [Java](java-image.md#java-image-instructions) 
+ [Go](go-image.md#go-image-provided)
+ [.NET](csharp-image.md#csharp-image-instructions)
+ [Ruby](ruby-image.md#ruby-image-instructions)

## Using an AWS OS-only base image
<a name="runtimes-images-provided"></a>

[AWS OS-only base images](https://gallery.ecr.aws/lambda/provided) contain an Amazon Linux distribution and the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/). These images are commonly used to create container images for compiled languages, such as [Go](go-image.md#go-image-provided) and [Rust](lambda-rust.md), and for a language or language version that Lambda doesn't provide a base image for, such as Node.js 19. You can also use OS-only base images to implement a [custom runtime](runtimes-custom.md). To make the image compatible with Lambda, you must include a [runtime interface client](#images-ric) for your language in the image.


| Tags | Runtime | Operating system | Dockerfile | Deprecation | 
| --- | --- | --- | --- | --- | 
| al2023 | OS-only Runtime | Amazon Linux 2023 | [Dockerfile for OS-only Runtime on GitHub](https://github.com/aws/aws-lambda-base-images/blob/provided.al2023/Dockerfile.provided.al2023) |  Jun 30, 2029  | 
| al2 | OS-only Runtime | Amazon Linux 2 | [Dockerfile for OS-only Runtime on GitHub](https://github.com/aws/aws-lambda-base-images/blob/provided.al2/Dockerfile.provided.al2) |  Jul 31, 2026  | 

Amazon Elastic Container Registry Public Gallery: [gallery.ecr.aws/lambda/provided](https://gallery.ecr.aws/lambda/provided)

## Using a non-AWS base image
<a name="images-types"></a>

Lambda supports any image that conforms to one of the following image manifest formats:
+ Docker image manifest V2, schema 2 (used with Docker version 1.10 and newer)
+ Open Container Initiative (OCI) Specifications (v1.0.0 and up)

Lambda supports a maximum uncompressed image size of 10 GB, including all layers.

**Note**  
To make the image compatible with Lambda, you must include a [runtime interface client](#images-ric) for your language in the image.
For optimal performance, keep your image manifest size under 25,400 bytes. To reduce image manifest size, minimize the number of layers in your image and reduce annotations.

## Runtime interface clients
<a name="images-ric"></a>

If you use an [OS-only base image](#runtimes-images-provided) or an alternative base image, you must include a runtime interface client in your image. The runtime interface client must extend the [Using the Lambda runtime API for custom runtimes](runtimes-api.md), which manages the interaction between Lambda and your function code. AWS provides open-source runtime interface clients for the following languages:
+  [Node.js](nodejs-image.md#nodejs-image-clients) 
+  [Python](python-image.md#python-image-clients) 
+  [Java](java-image.md#java-image-clients) 
+  [.NET](csharp-image.md#csharp-image-clients) 
+  [Go](go-image.md#go-image-clients) 
+  [Ruby](ruby-image.md#ruby-image-clients) 
+  [Rust](lambda-rust.md) – 

If you're using a language that doesn't have an AWS-provided runtime interface client, you must create your own.

## Amazon ECR permissions
<a name="gettingstarted-images-permissions"></a>

Before you create a Lambda function from a container image, you must build the image locally and upload it to an Amazon ECR repository. When you create the function, specify the Amazon ECR repository URI.

Make sure that the permissions for the user or role that creates the function includes `GetRepositoryPolicy`, `SetRepositoryPolicy`, `BatchGetImage`, and `GetDownloadUrlForLayer`.

For example, use the IAM console to create a role with the following policy:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "ecr:SetRepositoryPolicy",
        "ecr:GetRepositoryPolicy",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Resource": "arn:aws:ecr:{{us-east-1}}{{:111122223333}}:repository/{{hello-world}}"
    }
  ]
}
```

------

The permissions that Lambda needs to retrieve your container image depend on whether the Amazon ECR repository is in the same AWS account as the function or in a different account. The following sections explain the requirements for each scenario.

**Note**  
In IAM, same-account access requires only one side to grant permission – either the identity-based policy (on the role) or the resource-based policy (on the Amazon ECR repository). Cross-account access requires both sides to grant permission – the identity-based policy on the role in the consuming account AND the resource-based policy on the Amazon ECR repository in the owning account must both allow the action.

### Same-account Amazon ECR repository policies
<a name="configuration-images-permissions"></a>

For a function in the same account as the container image in Amazon ECR, you can grant Lambda access through either the identity-based policy on the execution role or the resource-based policy on the Amazon ECR repository. Only one side needs to allow access.

If you choose to use an Amazon ECR repository policy, add `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` permissions. The following example shows the minimum policy:

```
{
        "Sid": "LambdaECRImageRetrievalPolicy",
        "Effect": "Allow",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Action": [
          "ecr:BatchGetImage",
          "ecr:GetDownloadUrlForLayer"
        ]
    }
```

For more information about Amazon ECR repository permissions, see [Private repository policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html) in the *Amazon Elastic Container Registry User Guide*.

If the Amazon ECR repository does not include these permissions, Lambda attempts to add them automatically. Lambda can add permissions only if the principal calling Lambda has `ecr:getRepositoryPolicy` and `ecr:setRepositoryPolicy` permissions.

To view or edit your Amazon ECR repository permissions, follow the directions in [Setting a private repository policy statement](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html) in the *Amazon Elastic Container Registry User Guide*.

#### Amazon ECR cross-account permissions
<a name="configuration-images-xaccount-permissions"></a>

When a function in one account uses a container image from an Amazon ECR repository in a different account, both sides must grant access. The identity-based policy on the role in the consuming account must allow `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer`, and the resource-based policy on the Amazon ECR repository in the owning account must also allow these actions.

In the following example, your [Amazon ECR repository permissions policy](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html) needs the following statements to grant access to account number 123456789012.
+ **CrossAccountPermission** – Allows account 123456789012 to create and update Lambda functions that use images from this ECR repository.
+ **LambdaECRImageCrossAccountRetrievalPolicy** – Lambda will eventually set a function's state to inactive if it is not invoked for an extended period. This statement is required so that Lambda can retrieve the container image for optimization and caching on behalf of the function owned by 123456789012. 

**Example — Add cross-account permission to your repository**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CrossAccountPermission",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Principal": {
        "AWS": "arn:aws:iam::{{123456789012}}:root"
      },
      "Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/{{example-lambda-repository}}"
    },
    {
      "Sid": "LambdaECRImageCrossAccountRetrievalPolicy",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Condition": {
        "ArnLike": {
          "aws:sourceARN": "arn:aws:lambda:{{us-east-1}}:{{123456789012}}:function:*"
        }
      },
      "Resource": "arn:aws:ecr:{{us-east-1}}:{{123456789012}}:repository/{{example-lambda-repository}}"
    }
  ]
}
```

To give access to multiple accounts, you add the account IDs to the Principal list in the `CrossAccountPermission` policy and to the Condition evaluation list in the `LambdaECRImageCrossAccountRetrievalPolicy`.

If you are working with multiple accounts in an AWS Organization, we recommend that you enumerate each account ID in the ECR permissions policy. This approach aligns with the AWS security best practice of setting narrow permissions in IAM policies.

In addition to the Amazon ECR repository policy, the user or role that creates the function must also have `BatchGetImage` and `GetDownloadUrlForLayer` permissions in their identity-based policy.

## Function lifecycle
<a name="images-lifecycle"></a>

After you upload a new or updated container image, Lambda optimizes the image before the function can process invocations. The optimization process can take a few seconds. The function remains in the `Pending` state until the process completes, when the state transitions to `Active`. You can't invoke the function until it reaches the `Active` state. 

If a function is not invoked for multiple weeks, Lambda reclaims its optimized version, and the function transitions to the `Inactive` state. To reactivate the function, you must invoke it. Lambda rejects the first invocation and the function enters the `Pending` state until Lambda re-optimizes the image. The function then returns to the `Active` state.

Lambda periodically fetches the associated container image from the Amazon ECR repository. If the corresponding container image no longer exists on Amazon ECR or permissions are revoked, the function enters the `Failed` state, and Lambda returns a failure for any function invocations.

You can use the Lambda API to get information about a function's state. For more information, see [Lambda function states](functions-states.md).