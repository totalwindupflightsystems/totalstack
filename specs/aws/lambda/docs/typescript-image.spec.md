---
id: "@specs/aws/lambda/docs/typescript-image"
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
> **spec:id:** @specs/aws/lambda/docs/typescript-image
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Deploy transpiled TypeScript code in Lambda with container images
<a name="typescript-image"></a>

You can deploy your TypeScript code to an AWS Lambda function as a Node.js [container image](images-create.md). AWS provides [base images](nodejs-image.md#nodejs-image-base) for Node.js to help you build the container image. These base images are preloaded with a language runtime and other components that are required to run the image on Lambda. AWS provides a Dockerfile for each of the base images to help with building your container image.

If you use a community or private enterprise base image, you must [add the Node.js runtime interface client (RIC)](nodejs-image.md#nodejs-image-clients) to the base image to make it compatible with Lambda.

Lambda provides a runtime interface emulator for local testing. The AWS base images for Node.js include the runtime interface emulator. If you use an alternative base image, such as an Alpine Linux or Debian image, you can [build the emulator into your image](https://github.com/aws/aws-lambda-runtime-interface-emulator/?tab=readme-ov-file#build-rie-into-your-base-image) or [install it on your local machine](https://github.com/aws/aws-lambda-runtime-interface-emulator/?tab=readme-ov-file#test-an-image-without-adding-rie-to-the-image).

## Using a Node.js base image to build and package TypeScript function code
<a name="base-image-typescript"></a>

### Prerequisites
<a name="typescript-image-prerequisites"></a>

To complete the steps in this section, you must have the following:
+ [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [Docker](https://docs.docker.com/get-docker) (minimum version 25.0.0)
+ The Docker [buildx plugin](https://github.com/docker/buildx/blob/master/README.md).
+ Node.js 22.x

### Creating an image from a base image
<a name="typescript-image-create"></a>

**To create an image from an AWS base image for Lambda**

1. On your local machine, create a project directory for your new function.

1. Create a new Node.js project with `npm` or a package manager of your choice.

   ```
   npm init
   ```

1. Add the [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda) and [esbuild](https://esbuild.github.io/) packages as development dependencies. The `@types/aws-lambda` package contains the type definitions for Lambda.

   ```
   npm install -D @types/aws-lambda esbuild
   ```

1. Add a [build script](https://esbuild.github.io/getting-started/#build-scripts) to the `package.json` file.

   ```
     "scripts": {
     "build": "esbuild index.ts --bundle --minify --sourcemap --platform=node --target=es2020 --outfile=dist/index.js"
   }
   ```

1. Create a new file called `index.ts`. Add the following sample code to the new file. This is the code for the Lambda function. The function returns a `hello world` message.
**Note**  
The `import` statement imports the type definitions from [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda). It does not import the `aws-lambda` NPM package, which is an unrelated third-party tool. For more information, see [aws-lambda](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda) in the DefinitelyTyped GitHub repository.

   ```
   import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';
   
   export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {
       console.log(`Event: ${JSON.stringify(event, null, 2)}`);
       console.log(`Context: ${JSON.stringify(context, null, 2)}`);
       return {
           statusCode: 200,
           body: JSON.stringify({
               message: 'hello world',
           }),
       };
   };
   ```

1. Create a new Dockerfile with the following configuration:
   + Set the `FROM` property to the URI of the base image.
   + Set the `CMD` argument to specify the Lambda function handler.

   The following example Dockerfile uses a multi-stage build. The first step transpiles the TypeScript code into JavaScript. The second step produces a container image that contains only JavaScript files and production dependencies.

   Note that the example Dockerfile does not include a [USER instruction](https://docs.docker.com/reference/dockerfile/#user). When you deploy a container image to Lambda, Lambda automatically defines a default Linux user with least-privileged permissions. This is different from standard Docker behavior which defaults to the `root` user when no `USER` instruction is provided.  
**Example Dockerfile**  

   ```
   FROM public.ecr.aws/lambda/nodejs:22 as builder
   WORKDIR /usr/app
   COPY package.json index.ts  ./
   RUN npm install
   RUN npm run build
       
   FROM public.ecr.aws/lambda/nodejs:22
   WORKDIR ${LAMBDA_TASK_ROOT}
   COPY --from=builder /usr/app/dist/* ./
   CMD ["index.handler"]
   ```

1. Build the Docker image with the [docker build](https://docs.docker.com/engine/reference/commandline/build/) command. The following example names the image `docker-image` and gives it the `test` [tag](https://docs.docker.com/engine/reference/commandline/build/#tag). To make your image compatible with Lambda, you must use the `--provenance=false` option.

   ```
   docker buildx build --platform linux/amd64 --provenance=false -t {{docker-image}}:{{test}} .
   ```
**Note**  
The command specifies the `--platform linux/amd64` option to ensure that your container is compatible with the Lambda execution environment regardless of the architecture of your build machine. If you intend to create a Lambda function using the ARM64 instruction set architecture, be sure to change the command to use the `--platform linux/arm64` option instead.

### (Optional) Test the image locally
<a name="typescript-image-test"></a>

1. Start the Docker image with the **docker run** command. In this example, `docker-image` is the image name and `test` is the tag.

   ```
   docker run --platform linux/amd64 -p 9000:8080 {{docker-image}}:{{test}}
   ```

   This command runs the image as a container and creates a local endpoint at `localhost:9000/2015-03-31/functions/function/invocations`.
**Note**  
If you built the Docker image for the ARM64 instruction set architecture, be sure to use the `--platform linux/{{arm64}}` option instead of `--platform linux/{{amd64}}`.

1. From a new terminal window, post an event to the local endpoint.

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
<a name="typescript-image-deploy"></a>

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