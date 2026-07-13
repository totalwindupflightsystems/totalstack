---
id: "@specs/aws/lambda/docs/go-image"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deploy container images"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Deploy container images

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/go-image
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deploy Go Lambda functions with container images
<a name="go-image"></a>

There are two ways to build a container image for a Go Lambda function:
+ [Using an AWS OS-only base image](#go-image-provided)

  Go is implemented differently than other managed runtimes. Because Go compiles natively to an executable binary, it doesn't require a dedicated language runtime. Use an [OS-only base image](images-create.md#runtimes-images-provided) to build Go images for Lambda. To make the image compatible with Lambda, you must include the `aws-lambda-go/lambda` package in the image.
+ [Using a non-AWS base image](#go-image-other)

  You can use an alternative base image from another container registry, such as Alpine Linux or Debian. You can also use a custom image created by your organization. To make the image compatible with Lambda, you must include the `aws-lambda-go/lambda` package in the image.

**Tip**  
To reduce the time it takes for Lambda container functions to become active, see [Use multi-stage builds](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#use-multi-stage-builds) in the Docker documentation. To build efficient container images, follow the [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

This page explains how to build, test, and deploy container images for Lambda.

## AWS base images for deploying Go functions
<a name="go-image-base"></a>

Go is implemented differently than other managed runtimes. Because Go compiles natively to an executable binary, it doesn't require a dedicated language runtime. Use an [OS-only base image](images-create.md#runtimes-images-provided) to deploy Go functions to Lambda.


| Name | Identifier | Operating system | Deprecation date | Block function create | Block function update | 
| --- | --- | --- | --- | --- | --- | 
| OS-only Runtime | `provided.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| OS-only Runtime | `provided.al2` | Amazon Linux 2 |  Jul 31, 2026  |  Feb 1, 2027  |  Mar 3, 2027  | 

Amazon Elastic Container Registry Public Gallery: [gallery.ecr.aws/lambda/provided](https://gallery.ecr.aws/lambda/provided)

## Go runtime interface client
<a name="go-image-clients"></a>

The `aws-lambda-go/lambda` package includes an implementation of the runtime interface. For examples of how to use `aws-lambda-go/lambda` in your image, see [Using an AWS OS-only base image](#go-image-provided) or [Using a non-AWS base image](#go-image-other).

## Using an AWS OS-only base image
<a name="go-image-provided"></a>

Go is implemented differently than other managed runtimes. Because Go compiles natively to an executable binary, it doesn't require a dedicated language runtime. Use an [OS-only base image](images-create.md#runtimes-images-provided) to build container images for Go functions.


| Tags | Runtime | Operating system | Dockerfile | Deprecation | 
| --- | --- | --- | --- | --- | 
| al2023 | OS-only Runtime | Amazon Linux 2023 | [Dockerfile for OS-only Runtime on GitHub](https://github.com/aws/aws-lambda-base-images/blob/provided.al2023/Dockerfile.provided.al2023) |  Jun 30, 2029  | 
| al2 | OS-only Runtime | Amazon Linux 2 | [Dockerfile for OS-only Runtime on GitHub](https://github.com/aws/aws-lambda-base-images/blob/provided.al2/Dockerfile.provided.al2) |  Jul 31, 2026  | 

For more information about these base images, see [provided](https://gallery.ecr.aws/lambda/provided) in the Amazon ECR public gallery.

You must include the [aws-lambda-go/lambda](https://github.com/aws/aws-lambda-go) package with your Go handler. This package implements the programming model for Go, including the runtime interface.

### Prerequisites
<a name="go-custom-prerequisites"></a>

To complete the steps in this section, you must have the following:
+ [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [Docker](https://docs.docker.com/get-docker) (minimum version 25.0.0)
+ The Docker [buildx plugin](https://github.com/docker/buildx/blob/master/README.md).
+ Go

### Creating an image from the provided.al2023 base image
<a name="go-custom-create"></a>

**To build and deploy a Go function with the `provided.al2023` base image**

1. Create a directory for the project, and then switch to that directory.

   ```
   mkdir hello
   cd hello
   ```

1. Initialize a new Go module.

   ```
   go mod init {{example.com/hello-world}}
   ```

1. Add the **lambda** library as a dependency of your new module.

   ```
   go get github.com/aws/aws-lambda-go/lambda
   ```

1. Create a file named `main.go` and then open it in a text editor. This is the code for the Lambda function. You can use the following sample code for testing, or replace it with your own.

   ```
   package main
   
   import (
   	"context"
   	"github.com/aws/aws-lambda-go/events"
   	"github.com/aws/aws-lambda-go/lambda"
   )
   
   func handler(ctx context.Context, event events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
   	response := events.APIGatewayProxyResponse{
   		StatusCode: 200,
   		Body:       "\"Hello from Lambda!\"",
   	}
   	return response, nil
   }
   
   func main() {
   	lambda.Start(handler)
   }
   ```

1. Use a text editor to create a Dockerfile in your project directory.
   + The following example Dockerfile uses a [multi-stage build](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#use-multi-stage-builds). This allows you to use a different base image in each step. You can use one image, such as a [Go base image](https://hub.docker.com/_/golang), to compile your code and build the executable binary. You can then use a different image, such as `provided.al2023`, in the final `FROM` statement to define the image that you deploy to Lambda. The build process is separated from the final deployment image, so the final image only contains the files needed to run the application.
   + You can use the optional `lambda.norpc` tag to exclude the Remote Procedure Call (RPC) component of the [lambda](https://github.com/aws/aws-lambda-go/tree/master/lambda) library. The RPC component is only required if you are using the deprecated Go 1.x runtime. Excluding the RPC reduces the size of the deployment package.
   + Note that the example Dockerfile does not include a [USER instruction](https://docs.docker.com/reference/dockerfile/#user). When you deploy a container image to Lambda, Lambda automatically defines a default Linux user with least-privileged permissions. This is different from standard Docker behavior which defaults to the `root` user when no `USER` instruction is provided.  
**Example — Multi-stage build Dockerfile**  
**Note**  
Make sure that the version of Go that you specify in your Dockerfile (for example, `golang:1.20`) is the same version of Go that you used to create your application.

   ```
   FROM {{golang:1.20}} as build
   WORKDIR /helloworld
   # Copy dependencies list
   COPY go.mod go.sum ./
   # Build with optional lambda.norpc tag
   COPY main.go .
   RUN go build {{-tags lambda.norpc}} -o main main.go
   # Copy artifacts to a clean image
   FROM {{public.ecr.aws/lambda/provided:al2023}}
   COPY --from=build /helloworld/main ./main
   ENTRYPOINT [ "./main" ]
   ```

1. Build the Docker image with the [docker build](https://docs.docker.com/engine/reference/commandline/build/) command. The following example names the image `docker-image` and gives it the `test` [tag](https://docs.docker.com/engine/reference/commandline/build/#tag). To make your image compatible with Lambda, you must use the `--provenance=false` option.

   ```
   docker buildx build --platform linux/amd64 --provenance=false -t {{docker-image}}:{{test}} .
   ```
**Note**  
The command specifies the `--platform linux/amd64` option to ensure that your container is compatible with the Lambda execution environment regardless of the architecture of your build machine. If you intend to create a Lambda function using the ARM64 instruction set architecture, be sure to change the command to use the `--platform linux/arm64` option instead.

### (Optional) Test the image locally
<a name="go-custom-test"></a>

Use the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/) to locally test your image. The runtime interface emulator is included in the `provided.al2023` base image.

**To run the runtime interface emulator on your local machine**

1. Start the Docker image with the **docker run** command. Note the following:
   + `docker-image` is the image name and `test` is the tag.
   + `./main` is the `ENTRYPOINT` from your Dockerfile.

   ```
   docker run -d -p 9000:8080 \
   --entrypoint /usr/local/bin/aws-lambda-rie \
   {{docker-image:test ./main}}
   ```

   This command runs the image as a container and creates a local endpoint at `localhost:9000/2015-03-31/functions/function/invocations`.

1. From a new terminal window, post an event to the following endpoint using a **curl** command:

   ```
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
   ```

   This command invokes the function with an empty event and returns a response. Some functions might require a JSON payload. Example:

   ```
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{{{"payload":"hello world!"}}}'
   ```

1. Get the container ID.

   ```
   docker ps
   ```

1. Use the [docker kill](https://docs.docker.com/engine/reference/commandline/kill/) command to stop the container. In this command, replace `3766c4ab331c` with the container ID from the previous step.

   ```
   docker kill {{3766c4ab331c}}
   ```

### Deploying the image
<a name="go-custom-deploy"></a>

**To upload the image to Amazon ECR and create the Lambda function**

1. Run the [get-login-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html) command to authenticate the Docker CLI to your Amazon ECR registry.
   + Set the `--region` value to the AWS Region where you want to create the Amazon ECR repository.
   + Replace `111122223333` with your AWS account ID.

   ```
   aws ecr get-login-password --region {{us-east-1}} | docker login --username AWS --password-stdin {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com
   ```

1. Create a repository in Amazon ECR using the [create-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html) command.

   ```
   aws ecr create-repository --repository-name {{hello-world}} --region {{us-east-1}} --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
   ```
**Note**  
The Amazon ECR repository must be in the same AWS Region as the Lambda function.

   If successful, you see a response like this:

   ```
   {
       "repository": {
           "repositoryArn": "arn:aws:ecr:us-east-1:111122223333:repository/hello-world",
           "registryId": "111122223333",
           "repositoryName": "hello-world",
           "repositoryUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world",
           "createdAt": "2023-03-09T10:39:01+00:00",
           "imageTagMutability": "MUTABLE",
           "imageScanningConfiguration": {
               "scanOnPush": true
           },
           "encryptionConfiguration": {
               "encryptionType": "AES256"
           }
       }
   }
   ```

1. Copy the `repositoryUri` from the output in the previous step.

1. Run the [docker tag](https://docs.docker.com/engine/reference/commandline/tag/) command to tag your local image into your Amazon ECR repository as the latest version. In this command:
   + `docker-image:test` is the name and [tag](https://docs.docker.com/engine/reference/commandline/build/#tag) of your Docker image. This is the image name and tag that you specified in the `docker build` command.
   + Replace `<ECRrepositoryUri>` with the `repositoryUri` that you copied. Make sure to include `:latest` at the end of the URI.

   ```
   docker tag docker-image:test {{<ECRrepositoryUri>}}:latest
   ```

   Example:

   ```
   docker tag {{docker-image}}:{{test}} {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest
   ```

1. Run the [docker push](https://docs.docker.com/engine/reference/commandline/push/) command to deploy your local image to the Amazon ECR repository. Make sure to include `:latest` at the end of the repository URI.

   ```
   docker push {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest
   ```

1. [Create an execution role](lambda-intro-execution-role.md#permissions-executionrole-api) for the function, if you don't already have one. You need the Amazon Resource Name (ARN) of the role in the next step.

1. Create the Lambda function. For `ImageUri`, specify the repository URI from earlier. Make sure to include `:latest` at the end of the URI.

   ```
   aws lambda create-function \
     --function-name {{hello-world}} \
     --package-type Image \
     --code ImageUri={{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest \
     --role {{arn:aws:iam::111122223333:role/lambda-ex}}
   ```
**Note**  
You can create a function using an image in a different AWS account, as long as the image is in the same Region as the Lambda function. For more information, see [Amazon ECR cross-account permissions](images-create.md#configuration-images-xaccount-permissions).

1. Invoke the function.

   ```
   aws lambda invoke --function-name {{hello-world}} response.json
   ```

   You should see a response like this:

   ```
   {
     "ExecutedVersion": "$LATEST", 
     "StatusCode": 200
   }
   ```

1. To see the output of the function, check the `response.json` file.

To update the function code, you must build the image again, upload the new image to the Amazon ECR repository, and then use the [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html) command to deploy the image to the Lambda function.

Lambda resolves the image tag to a specific image digest. This means that if you point the image tag that was used to deploy the function to a new image in Amazon ECR, Lambda doesn't automatically update the function to use the new image.

To deploy the new image to the same Lambda function, you must use the [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html) command, even if the image tag in Amazon ECR remains the same. In the following example, the `--publish` option creates a new version of the function using the updated container image.

```
aws lambda update-function-code \
  --function-name {{hello-world}} \
  --image-uri {{111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest}} \
  --publish
```

## Using a non-AWS base image
<a name="go-image-other"></a>

You can build a container image for Go from a non-AWS base image. The example Dockerfile in the following steps uses an [Alpine base image](https://hub.docker.com/_/golang/).

You must include the [aws-lambda-go/lambda](https://github.com/aws/aws-lambda-go) package with your Go handler. This package implements the programming model for Go, including the runtime interface.

### Prerequisites
<a name="go-alt-prerequisites"></a>

To complete the steps in this section, you must have the following:
+ [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [Docker](https://docs.docker.com/get-docker) (minimum version 25.0.0)
+ The Docker [buildx plugin](https://github.com/docker/buildx/blob/master/README.md).
+ Go

### Creating an image from an alternative base image
<a name="go-alt-create"></a>

**To build and deploy a Go function with an Alpine base image**

1. Create a directory for the project, and then switch to that directory.

   ```
   mkdir hello
   cd hello
   ```

1. Initialize a new Go module.

   ```
   go mod init {{example.com/hello-world}}
   ```

1. Add the **lambda** library as a dependency of your new module.

   ```
   go get github.com/aws/aws-lambda-go/lambda
   ```

1. Create a file named `main.go` and then open it in a text editor. This is the code for the Lambda function. You can use the following sample code for testing, or replace it with your own.

   ```
   package main
   
   import (
   	"context"
   	"github.com/aws/aws-lambda-go/events"
   	"github.com/aws/aws-lambda-go/lambda"
   )
   
   func handler(ctx context.Context, event events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
   	response := events.APIGatewayProxyResponse{
   		StatusCode: 200,
   		Body:       "\"Hello from Lambda!\"",
   	}
   	return response, nil
   }
   
   func main() {
   	lambda.Start(handler)
   }
   ```

1. Use a text editor to create a Dockerfile in your project directory. The following example Dockerfile uses an [Alpine base image](https://hub.docker.com/_/golang/). Note that the example Dockerfile does not include a [USER instruction](https://docs.docker.com/reference/dockerfile/#user). When you deploy a container image to Lambda, Lambda automatically defines a default Linux user with least-privileged permissions. This is different from standard Docker behavior which defaults to the `root` user when no `USER` instruction is provided.  
**Example Dockerfile**  
**Note**  
Make sure that the version of Go that you specify in your Dockerfile (for example, `golang:1.20`) is the same version of Go that you used to create your application.

   ```
   FROM golang:1.20.2-alpine3.16 as build
   WORKDIR /helloworld
   # Copy dependencies list
   COPY go.mod go.sum ./
   # Build
   COPY main.go .
   RUN go build -o main main.go
   # Copy artifacts to a clean image
   FROM alpine:3.16
   COPY --from=build /helloworld/main /main
   ENTRYPOINT [ "/main" ]
   ```

1. Build the Docker image with the [docker build](https://docs.docker.com/engine/reference/commandline/build/) command. The following example names the image `docker-image` and gives it the `test` [tag](https://docs.docker.com/engine/reference/commandline/build/#tag). To make your image compatible with Lambda, you must use the `--provenance=false` option.

   ```
   docker buildx build --platform linux/amd64 --provenance=false -t {{docker-image}}:{{test}} .
   ```
**Note**  
The command specifies the `--platform linux/amd64` option to ensure that your container is compatible with the Lambda execution environment regardless of the architecture of your build machine. If you intend to create a Lambda function using the ARM64 instruction set architecture, be sure to change the command to use the `--platform linux/arm64` option instead.

### (Optional) Test the image locally
<a name="go-alt-test"></a>

Use the [runtime interface emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator/) to locally test the image. You can [build the emulator into your image](https://github.com/aws/aws-lambda-runtime-interface-emulator/?tab=readme-ov-file#build-rie-into-your-base-image) or use the following procedure to install it on your local machine.

**To install and run the runtime interface emulator on your local machine**

1. From your project directory, run the following command to download the runtime interface emulator (x86-64 architecture) from GitHub and install it on your local machine.

------
#### [ Linux/macOS ]

   ```
   mkdir -p ~/.aws-lambda-rie && \
       curl -Lo ~/.aws-lambda-rie/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
       chmod +x ~/.aws-lambda-rie/aws-lambda-rie
   ```

   To install the arm64 emulator, replace the GitHub repository URL in the previous command with the following:

   ```
   https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie-arm64
   ```

------
#### [ PowerShell ]

   ```
   $dirPath = "$HOME\.aws-lambda-rie"
   if (-not (Test-Path $dirPath)) {
       New-Item -Path $dirPath -ItemType Directory
   }
         
   $downloadLink = "https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie"
   $destinationPath = "$HOME\.aws-lambda-rie\aws-lambda-rie"
   Invoke-WebRequest -Uri $downloadLink -OutFile $destinationPath
   ```

   To install the arm64 emulator, replace the `$downloadLink` with the following:

   ```
   https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie-arm64
   ```

------

1. Start the Docker image with the **docker run** command. Note the following:
   + `docker-image` is the image name and `test` is the tag.
   + `/main` is the `ENTRYPOINT` from your Dockerfile.

------
#### [ Linux/macOS ]

   ```
   docker run --platform linux/amd64 -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
       --entrypoint /aws-lambda/aws-lambda-rie \
       {{docker-image:test}} \
           {{/main}}
   ```

------
#### [ PowerShell ]

   ```
   docker run --platform linux/amd64 -d -v "$HOME\.aws-lambda-rie:/aws-lambda" -p 9000:8080 `
   --entrypoint /aws-lambda/aws-lambda-rie `
   {{docker-image:test}} `
       {{/main}}
   ```

------

   This command runs the image as a container and creates a local endpoint at `localhost:9000/2015-03-31/functions/function/invocations`.
**Note**  
If you built the Docker image for the ARM64 instruction set architecture, be sure to use the `--platform linux/{{arm64}}` option instead of `--platform linux/{{amd64}}`.

1. Post an event to the local endpoint.

------
#### [ Linux/macOS ]

   In Linux and macOS, run the following `curl` command:

   ```
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
   ```

   This command invokes the function with an empty event and returns a response. If you're using your own function code rather than the sample function code, you might want to invoke the function with a JSON payload. Example:

   ```
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{{{"payload":"hello world!"}}}'
   ```

------
#### [ PowerShell ]

   In PowerShell, run the following `Invoke-WebRequest` command:

   ```
   Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post -Body '{}' -ContentType "application/json"
   ```

   This command invokes the function with an empty event and returns a response. If you're using your own function code rather than the sample function code, you might want to invoke the function with a JSON payload. Example:

   ```
   Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post -Body '{{{"payload":"hello world!"}}}' -ContentType "application/json"
   ```

------

1. Get the container ID.

   ```
   docker ps
   ```

1. Use the [docker kill](https://docs.docker.com/engine/reference/commandline/kill/) command to stop the container. In this command, replace `3766c4ab331c` with the container ID from the previous step.

   ```
   docker kill {{3766c4ab331c}}
   ```

### Deploying the image
<a name="go-alt-deploy"></a>

**To upload the image to Amazon ECR and create the Lambda function**

1. Run the [get-login-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html) command to authenticate the Docker CLI to your Amazon ECR registry.
   + Set the `--region` value to the AWS Region where you want to create the Amazon ECR repository.
   + Replace `111122223333` with your AWS account ID.

   ```
   aws ecr get-login-password --region {{us-east-1}} | docker login --username AWS --password-stdin {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com
   ```

1. Create a repository in Amazon ECR using the [create-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html) command.

   ```
   aws ecr create-repository --repository-name {{hello-world}} --region {{us-east-1}} --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
   ```
**Note**  
The Amazon ECR repository must be in the same AWS Region as the Lambda function.

   If successful, you see a response like this:

   ```
   {
       "repository": {
           "repositoryArn": "arn:aws:ecr:us-east-1:111122223333:repository/hello-world",
           "registryId": "111122223333",
           "repositoryName": "hello-world",
           "repositoryUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world",
           "createdAt": "2023-03-09T10:39:01+00:00",
           "imageTagMutability": "MUTABLE",
           "imageScanningConfiguration": {
               "scanOnPush": true
           },
           "encryptionConfiguration": {
               "encryptionType": "AES256"
           }
       }
   }
   ```

1. Copy the `repositoryUri` from the output in the previous step.

1. Run the [docker tag](https://docs.docker.com/engine/reference/commandline/tag/) command to tag your local image into your Amazon ECR repository as the latest version. In this command:
   + `docker-image:test` is the name and [tag](https://docs.docker.com/engine/reference/commandline/build/#tag) of your Docker image. This is the image name and tag that you specified in the `docker build` command.
   + Replace `<ECRrepositoryUri>` with the `repositoryUri` that you copied. Make sure to include `:latest` at the end of the URI.

   ```
   docker tag docker-image:test {{<ECRrepositoryUri>}}:latest
   ```

   Example:

   ```
   docker tag {{docker-image}}:{{test}} {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest
   ```

1. Run the [docker push](https://docs.docker.com/engine/reference/commandline/push/) command to deploy your local image to the Amazon ECR repository. Make sure to include `:latest` at the end of the repository URI.

   ```
   docker push {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest
   ```

1. [Create an execution role](lambda-intro-execution-role.md#permissions-executionrole-api) for the function, if you don't already have one. You need the Amazon Resource Name (ARN) of the role in the next step.

1. Create the Lambda function. For `ImageUri`, specify the repository URI from earlier. Make sure to include `:latest` at the end of the URI.

   ```
   aws lambda create-function \
     --function-name {{hello-world}} \
     --package-type Image \
     --code ImageUri={{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{hello-world}}:latest \
     --role {{arn:aws:iam::111122223333:role/lambda-ex}}
   ```
**Note**  
You can create a function using an image in a different AWS account, as long as the image is in the same Region as the Lambda function. For more information, see [Amazon ECR cross-account permissions](images-create.md#configuration-images-xaccount-permissions).

1. Invoke the function.

   ```
   aws lambda invoke --function-name {{hello-world}} response.json
   ```

   You should see a response like this:

   ```
   {
     "ExecutedVersion": "$LATEST", 
     "StatusCode": 200
   }
   ```

1. To see the output of the function, check the `response.json` file.

To update the function code, you must build the image again, upload the new image to the Amazon ECR repository, and then use the [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html) command to deploy the image to the Lambda function.

Lambda resolves the image tag to a specific image digest. This means that if you point the image tag that was used to deploy the function to a new image in Amazon ECR, Lambda doesn't automatically update the function to use the new image.

To deploy the new image to the same Lambda function, you must use the [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html) command, even if the image tag in Amazon ECR remains the same. In the following example, the `--publish` option creates a new version of the function using the updated container image.

```
aws lambda update-function-code \
  --function-name {{hello-world}} \
  --image-uri {{111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest}} \
  --publish
```