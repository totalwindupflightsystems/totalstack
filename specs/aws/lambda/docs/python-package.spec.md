---
id: "@specs/aws/lambda/docs/python-package"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Deploy .zip file archives"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Deploy .zip file archives

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/python-package
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Working with .zip file archives for Python Lambda functions
<a name="python-package"></a>

 Your AWS Lambda function’s code comprises a .py file containing your function’s handler code, together with any additional packages and modules your code depends on. To deploy this function code to Lambda, you use a *deployment package*. This package may either be a .zip file archive or a container image. For more information about using container images with Python, see [Deploy Python Lambda functions with container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html). 

 To create your deployment package as .zip file archive, you can use your command-line tool’s built-in .zip file archive utility, or any other .zip file utility such as [7zip](https://www.7-zip.org/download.html). The examples shown in the following sections assume you’re using a command-line `zip` tool in a Linux or MacOS environment. To use the same commands in Windows, you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash. 

 Note that Lambda uses POSIX file permissions, so you may need to [set permissions for the deployment package folder](http://aws.amazon.com/premiumsupport/knowledge-center/lambda-deployment-package-errors/) before you create the .zip file archive. 

**Topics**
+ [Runtime dependencies in Python](#python-package-dependencies)
+ [Creating a .zip deployment package with no dependencies](#python-package-create-no-dependencies)
+ [Creating a .zip deployment package with dependencies](#python-package-create-dependencies)
+ [Dependency search path and runtime-included libraries](#python-package-searchpath)
+ [Using \_\_pycache\_\_ folders](#python-package-pycache)
+ [Creating .zip deployment packages with native libraries](#python-package-native-libraries)
+ [Creating and updating Python Lambda functions using .zip files](#python-package-create-update)

## Runtime dependencies in Python
<a name="python-package-dependencies"></a>

For Lambda functions that use the Python runtime, a dependency can be any Python package or module. When you deploy your function using a .zip archive, you can either add these dependencies to your .zip file with your function code or use a [Lambda layer](chapter-layers.md). A layer is a separate .zip file that can contain additional code and other content. To learn more about using Lambda layers in Python, see [Working with layers for Python Lambda functions](python-layers.md).

The Lambda Python runtimes include the AWS SDK for Python (Boto3) and its dependencies. Lambda provides the SDK in the runtime for deployment scenarios where you are unable to add your own dependencies. These scenarios include creating functions in the console using the built-in code editor or using inline functions in AWS Serverless Application Model (AWS SAM) or CloudFormation templates.

Lambda periodically updates the libraries in the Python runtime to include the latest updates and security patches. If your function uses the version of the Boto3 SDK included in the runtime but your deployment package includes SDK dependencies, this can cause version misalignment issues. For example, your deployment package could include the SDK dependency urllib3. When Lambda updates the SDK in the runtime, compatibility issues between the new version of the runtime and the version of urllib3 in your deployment package can cause your function to fail.

**Important**  
To maintain full control over your dependencies and to avoid possible version misalignment issues, we recommend you add all of your function’s dependencies to your deployment package, even if versions of them are included in the Lambda runtime. This includes the Boto3 SDK.

To find out which version of the SDK for Python (Boto3) is included in the runtime you're using, see [Runtime-included SDK versions](lambda-python.md#python-sdk-included).

 Under the [AWS shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html), you are responsible for the management of any dependencies in your functions' deployment packages. This includes applying updates and security patches. To update dependencies in your function's deployment package, first create a new .zip file and then upload it to Lambda. See [Creating a .zip deployment package with dependencies](#python-package-create-dependencies) and [Creating and updating Python Lambda functions using .zip files](#python-package-create-update) for more information.

## Creating a .zip deployment package with no dependencies
<a name="python-package-create-no-dependencies"></a>

 If your function code has no dependencies, your .zip file contains only the .py file with your function’s handler code. Use your preferred zip utility to create a .zip file with your .py file at the root. If the .py file is not at the root of your .zip file, Lambda won’t be able to run your code. 

 To learn how to deploy your .zip file to create a new Lambda function or update an existing one, see [Creating and updating Python Lambda functions using .zip files](#python-package-create-update). 

## Creating a .zip deployment package with dependencies
<a name="python-package-create-dependencies"></a>

 If your function code depends on additional packages or modules, you can either add these dependencies to your .zip file with your function code or [use a Lambda layer](python-layers.md). The instructions in this section show you how to include your dependencies in your .zip deployment package. For Lambda to run your code, the .py file containing your handler code and all of your function's dependencies must be installed at the root of the .zip file.

 Suppose your function code is saved in a file named `lambda_function.py`. The following example CLI commands create a .zip file named `my_deployment_package.zip` containing your function code and its dependencies. You can either install your dependencies directly to a folder in your project directory or use a Python virtual environment. 

**To create the deployment package (project directory)**

1. Navigate to the project directory containing your `lambda_function.py` source code file. In this example, the directory is named `my_function`.

   ```
   cd my_function
   ```

1. Create a new directory named package into which you will install your dependencies.

   ```
   mkdir package
   ```

   Note that for a .zip deployment package, Lambda expects your source code and its dependencies all to be at the root of the .zip file. However, installing dependencies directly in your project directory can introduce a large number of new files and folders and make navigating around your IDE difficult. You create a separate `package` directory here to keep your dependencies separate from your source code.

1. Install your dependencies in the `package` directory. The example below installs the Boto3 SDK from the Python Package Index using pip. If your function code uses Python packages you have created yourself, save them in the `package` directory.

   ```
   pip install --target ./package boto3
   ```

1. Create a .zip file with the installed libraries at the root.

   ```
   cd package
   zip -r ../my_deployment_package.zip .
   ```

   This generates a `my_deployment_package.zip` file in your project directory.

1. Add the lambda\_function.py file to the root of the .zip file

   ```
   cd ..
   zip my_deployment_package.zip lambda_function.py
   ```

   Your .zip file should have a flat directory structure, with your function's handler code and all your dependency folders installed at the root as follows.

   ```
   my_deployment_package.zip
   |- bin
   |  |-jp.py
   |- boto3
   |  |-compat.py
   |  |-data
   |  |-docs
   ...
   |- lambda_function.py
   ```

   If the .py file containing your function’s handler code is not at the root of your .zip file, Lambda will not be able to run your code.

**To create the deployment package (virtual environment)**

1. Create and activate a virtual environment in your project directory. In this example the project directory is named `my_function`.

   ```
   ~$ cd my_function
   ~/my_function$ python3.14 -m venv my_virtual_env
   ~/my_function$ source ./my_virtual_env/bin/activate
   ```

1. Install your required libraries using pip. The following example installs the Boto3 SDK

   ```
   (my_virtual_env) ~/my_function$ pip install boto3
   ```

1. Use `pip show` to find the location in your virtual environment where pip has installed your dependencies.

   ```
   (my_virtual_env) ~/my_function$ pip show <package_name>
   ```

   The folder in which pip installs your libraries may be named `site-packages` or `dist-packages`. This folder may be located in either the `lib/python3.x` or `lib64/python3.x` directory (where python3.x represents the version of Python you are using).

1. Deactivate the virtual environment

   ```
   (my_virtual_env) ~/my_function$ deactivate
   ```

1. Navigate into the directory containing the dependencies you installed with pip and create a .zip file in your project directory with the installed dependencies at the root. In this example, pip has installed your dependencies in the `my_virtual_env/lib/python3.14/site-packages` directory.

   ```
   ~/my_function$ cd my_virtual_env/lib/python3.14/site-packages
   ~/my_function/my_virtual_env/lib/python3.14/site-packages$ zip -r ../../../../my_deployment_package.zip .
   ```

1. Navigate to the root of your project directory where the .py file containing your handler code is located and add that file to the root of your .zip package. In this example, your function code file is named `lambda_function.py`.

   ```
   ~/my_function/my_virtual_env/lib/python3.14/site-packages$ cd ../../../../
   ~/my_function$ zip my_deployment_package.zip lambda_function.py
   ```

## Dependency search path and runtime-included libraries
<a name="python-package-searchpath"></a>

 When you use an `import` statement in your code, the Python runtime searches the directories in its search path until it finds the module or package. By default, the first location the runtime searches is the directory into which your .zip deployment package is decompressed and mounted (`/var/task`). If you include a version of a runtime-included library in your deployment package, your version will take precedence over the version that's included in the runtime. Dependencies in your deployment package also have precedence over dependencies in layers. 

 When you add a dependency to a layer, Lambda extracts this to `/opt/python/lib/python3.x/site-packages` (where `python3.x` represents the version of the runtime you're using) or `/opt/python`. In the search path, these directories have precedence over the directories containing the runtime-included libraries and pip-installed libraries (`/var/runtime` and `/var/lang/lib/python3.x/site-packages`). Libraries in function layers therefore have precedence over versions included in the runtime. 

**Note**  
In the Python 3.11 managed runtime and base image, the AWS SDK and its dependencies are installed in the `/var/lang/lib/python3.11/site-packages` directory.

 You can see the full search path for your Lambda function by adding the following code snippet. 

```
import sys
      
search_path = sys.path
print(search_path)
```

**Note**  
Because dependencies in your deployment package or layers take precedence over runtime-included libraries, this can cause version misalignment problems if you include an SDK dependency such as urllib3 in your package without including the SDK as well. If you deploy your own version of a Boto3 dependency, you must also deploy Boto3 as a dependency in your deployment package. We recommend that you package all of your function’s dependencies, even if versions of them are included in the runtime.

 You can also add dependencies in a separate folder inside your .zip package. For example, you might add a version of the Boto3 SDK to a folder in your .zip package called `common`. When your .zip package is decompressed and mounted, this folder is placed inside the `/var/task` directory. To use a dependency from a folder in your .zip deployment package in your code, use an `import from` statement. For example, to use a version of Boto3 from a folder named `common` in your .zip package, use the following statement. 

```
from common import boto3
```

## Using \_\_pycache\_\_ folders
<a name="python-package-pycache"></a>

 We recommend that you don't include `__pycache__` folders in your function's deployment package. Python bytecode that's compiled on a build machine with a different architecture or operating system might not be compatible with the Lambda execution environment. 

## Creating .zip deployment packages with native libraries
<a name="python-package-native-libraries"></a>

 If your function uses only pure Python packages and modules, you can use the `pip install` command to install your dependencies on any local build machine and create your .zip file. Many popular Python libraries, including NumPy and Pandas, are not pure Python and contain code written in C or C\+\+. When you add libraries containing C/C\+\+ code to your deployment package, you must build your package correctly to ensure that it’s compatible with the Lambda execution environment. 

 Most packages available on the Python Package Index ([PyPI](https://pypi.org/)) are available as “wheels” (.whl files). A .whl file is a type of ZIP file which contains a built distribution with pre-compiled binaries for a particular operating system and instruction set architecture. To make your deployment package compatible with Lambda, you install the wheel for Linux operating systems and your function’s instruction set architecture. 

 Some packages may only be available as source distributions. For these packages, you need to compile and build the C/C\+\+ components yourself. 

 To see what distributions are available for your required package, do the following: 

1. Search for the name of the package on the [Python Package Index main page](https://pypi.org/).

1. Choose the version of the package you want to use.

1. Choose **Download files**.

### Working with built distributions (wheels)
<a name="python-package-wheels"></a>

 To download a wheel that’s compatible with Lambda, you use the pip `--platform` option. 

 If your Lambda function uses the **x86\_64** instruction set architecture, run the following `pip install` command to install a compatible wheel in your `package` directory. Replace `--python 3.x` with the version of the Python runtime you are using. 

```
pip install \
--platform manylinux2014_x86_64 \
--target=package \
--implementation cp \
--python-version {{3.x}} \
--only-binary=:all: --upgrade \
<package_name>
```

 If your function uses the **arm64** instruction set architecture, run the following command. Replace `--python 3.x` with the version of the Python runtime you are using. 

```
pip install \
--platform manylinux2014_aarch64 \
--target=package \
--implementation cp \
--python-version {{3.x}} \
--only-binary=:all: --upgrade \
<package_name>
```

### Working with source distributions
<a name="python-package-source-dist"></a>

 If your package is only available as a source distribution, you need to build the C/C\+\+ libraries yourself. To make your package compatible with the Lambda execution environment, you need to build it in an environment that uses the same Amazon Linux operating system. You can do this by building your package in an Amazon Elastic Compute Cloud (Amazon EC2) Linux instance. 

 To learn how to launch and connect to an Amazon EC2 Linux instance, see [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*. 

## Creating and updating Python Lambda functions using .zip files
<a name="python-package-create-update"></a>

 After you have created your .zip deployment package, you can use it to create a new Lambda function or update an existing one. You can deploy your .zip package using the Lambda console, the AWS Command Line Interface, and the Lambda API. You can also create and update Lambda functions using AWS Serverless Application Model (AWS SAM) and CloudFormation. 

The maximum size for a .zip deployment package for Lambda is 250 MB (unzipped). Note that this limit applies to the combined size of all the files you upload, including any Lambda layers.

The Lambda runtime needs permission to read the files in your deployment package. In Linux permissions octal notation, Lambda needs 644 permissions for non-executable files (rw-r--r--) and 755 permissions (rwxr-xr-x) for directories and executable files.

In Linux and MacOS, use the `chmod` command to change file permissions on files and directories in your deployment package. For example, to give a non-executable file the correct permissions, run the following command.

```
chmod 644 <filepath>
```

To change file permissions in Windows, see [Set, View, Change, or Remove Permissions on an Object](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731667(v=ws.10)) in the Microsoft Windows documentation.

**Note**  
If you don't grant Lambda the permissions it needs to access directories in your deployment package, Lambda sets the permissions for those directories to 755 (rwxr-xr-x).

### Creating and updating functions with .zip files using the console
<a name="python-package-create-console"></a>

 To create a new function, you must first create the function in the console, then upload your .zip archive. To update an existing function, open the page for your function, then follow the same procedure to add your updated .zip file. 

 If your .zip file is less than 50MB, you can create or update a function by uploading the file directly from your local machine. For .zip files greater than 50MB, you must upload your package to an Amazon S3 bucket first. For instructions on how to upload a file to an Amazon S3 bucket using the AWS Management Console, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html). To upload files using the AWS CLI, see [Move objects](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-move) in the *AWS CLI User Guide*. 

**Note**  
You cannot change the [deployment package type](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html#lambda-CreateFunction-request-PackageType) (.zip or container image) for an existing function. For example, you cannot convert a container image function to use a .zip file archive. You must create a new function.

**To create a new function (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and choose **Create Function**.

1. Choose **Author from scratch**.

1. Under **Basic information**, do the following:

   1. For **Function name**, enter the name for your function.

   1. For **Runtime**, select the runtime you want to use.

   1. (Optional) For **Architecture**, choose the instruction set architecture for your function. The default architecture is x86\_64. Ensure that the .zip deployment package for your function is compatible with the instruction set architecture you select.

1. (Optional) Under **Permissions**, expand **Change default execution role**. You can create a new **Execution role** or use an existing one.

1. Choose **Create function**. Lambda creates a basic 'Hello world' function using your chosen runtime.

**To upload a .zip archive from your local machine (console)**

1. In the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console, choose the function you want to upload the .zip file for.

1. Select the **Code** tab.

1. In the **Code source** pane, choose **Upload from**.

1. Choose **.zip file**.

1. To upload the .zip file, do the following:

   1. Select **Upload**, then select your .zip file in the file chooser.

   1. Choose **Open**.

   1. Choose **Save**.

**To upload a .zip archive from an Amazon S3 bucket (console)**

1. In the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console, choose the function you want to upload a new .zip file for.

1. Select the **Code** tab.

1. In the **Code source** pane, choose **Upload from**.

1. Choose **Amazon S3 location**.

1. Paste the Amazon S3 link URL of your .zip file and choose **Save**.

### Updating .zip file functions using the console code editor
<a name="python-package-console-edit"></a>

 For some functions with .zip deployment packages, you can use the Lambda console’s built-in code editor to update your function code directly. To use this feature, your function must meet the following criteria: 
+ Your function must use one of the interpreted language runtimes (Python, Node.js, or Ruby)
+ Your function’s deployment package must be smaller than 50 MB (unzipped).

Function code for functions with container image deployment packages cannot be edited directly in the console.

**To update function code using the console code editor**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and select your function.

1. Select the **Code** tab.

1. In the **Code source** pane, select your source code file and edit it in the integrated code editor.

1. In the **DEPLOY** section, choose **Deploy** to update your function's code:  
![Deploy button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/deploy-console.png)

### Creating and updating functions with .zip files using the AWS CLI
<a name="python-package-create-cli"></a>

 You can can use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to create a new function or to update an existing one using a .zip file. Use the [create-function](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html) and [update-function-code](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html) commands to deploy your .zip package. If your .zip file is smaller than 50MB, you can upload the .zip package from a file location on your local build machine. For larger files, you must upload your .zip package from an Amazon S3 bucket. For instructions on how to upload a file to an Amazon S3 bucket using the AWS CLI, see [Move objects](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-move) in the *AWS CLI User Guide*. 

**Note**  
If you upload your .zip file from an Amazon S3 bucket using the AWS CLI, the bucket must be located in the same AWS Region as your function.

 To create a new function using a .zip file with the AWS CLI, you must specify the following: 
+ The name of your function (`--function-name`)
+ Your function’s runtime (`--runtime`)
+ The Amazon Resource Name (ARN) of your function’s [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) (`--role`)
+ The name of the handler method in your function code (`--handler`)

 You must also specify the location of your .zip file. If your .zip file is located in a folder on your local build machine, use the `--zip-file` option to specify the file path, as shown in the following example command. 

```
aws lambda create-function --function-name myFunction \
--runtime python3.14 --handler lambda_function.lambda_handler \
--role arn:aws:iam::111122223333:role/service-role/my-lambda-role \
--zip-file fileb://myFunction.zip
```

 To specify the location of .zip file in an Amazon S3 bucket, use the `--code` option as shown in the following example command. You only need to use the `S3ObjectVersion` parameter for versioned objects. 

```
aws lambda create-function --function-name myFunction \
--runtime python3.14 --handler lambda_function.lambda_handler \
--role arn:aws:iam::111122223333:role/service-role/my-lambda-role \
--code S3Bucket=amzn-s3-demo-bucket,S3Key=myFileName.zip,S3ObjectVersion=myObjectVersion
```

 To update an existing function using the CLI, you specify the the name of your function using the `--function-name` parameter. You must also specify the location of the .zip file you want to use to update your function code. If your .zip file is located in a folder on your local build machine, use the `--zip-file` option to specify the file path, as shown in the following example command. 

```
aws lambda update-function-code --function-name myFunction \
--zip-file fileb://myFunction.zip
```

 To specify the location of .zip file in an Amazon S3 bucket, use the `--s3-bucket` and `--s3-key` options as shown in the following example command. You only need to use the `--s3-object-version` parameter for versioned objects. 

```
aws lambda update-function-code --function-name myFunction \
--s3-bucket amzn-s3-demo-bucket --s3-key myFileName.zip --s3-object-version myObject Version
```

### Creating and updating functions with .zip files using the Lambda API
<a name="python-package-create-api"></a>

 To create and update functions using a .zip file archive, use the following API operations: 
+ [CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html)
+ [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html)

### Creating and updating functions with .zip files using AWS SAM
<a name="python-package-create-sam"></a>

 The AWS Serverless Application Model (AWS SAM) is a toolkit that helps streamline the process of building and running serverless applications on AWS. You define the resources for your application in a YAML or JSON template and use the AWS SAM command line interface (AWS SAM CLI) to build, package, and deploy your applications. When you build a Lambda function from an AWS SAM template, AWS SAM automatically creates a .zip deployment package or container image with your function code and any dependencies you specify. To learn more about using AWS SAM to build and deploy Lambda functions, see [Getting started with AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html) in the *AWS Serverless Application Model Developer Guide*.

You can also use AWS SAM to create a Lambda function using an existing .zip file archive. To create a Lambda function using AWS SAM, you can save your .zip file in an Amazon S3 bucket or in a local folder on your build machine. For instructions on how to upload a file to an Amazon S3 bucket using the AWS CLI, see [Move objects](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-move) in the *AWS CLI User Guide*. 

 In your AWS SAM template, the `AWS::Serverless::Function` resource specifies your Lambda function. In this resource, set the following properties to create a function using a .zip file archive: 
+ `PackageType` - set to `Zip`
+ `CodeUri` - set to the function code's Amazon S3 URI, path to local folder, or [FunctionCode](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functioncode.html) object
+ `Runtime` - Set to your chosen runtime

 With AWS SAM, if your .zip file is larger than 50MB, you don’t need to upload it to an Amazon S3 bucket first. AWS SAM can upload .zip packages up to the maximum allowed size of 250MB (unzipped) from a location on your local build machine. 

 To learn more about deploying functions using .zip file in AWS SAM, see [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html) in the *AWS SAM Developer Guide*. 

### Creating and updating functions with .zip files using CloudFormation
<a name="python-package-create-cfn"></a>

 You can use CloudFormation to create a Lambda function using a .zip file archive. To create a Lambda function from a .zip file, you must first upload your file to an Amazon S3 bucket. For instructions on how to upload a file to an Amazon S3 bucket using the AWS CLI, see [Move objects](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-move) in the *AWS CLI User Guide. *

For Node.js and Python runtimes, you can also provide inline source code in your CloudFormation template. CloudFormation then creates a .zip file containing your code when you build your function. 

**Using an existing .zip file**

In your CloudFormation template, the `AWS::Lambda::Function` resource specifies your Lambda function. In this resource, set the following properties to create a function using a .zip file archive:
+ `PackageType` - Set to `Zip`
+ `Code` - Enter the Amazon S3 bucket name and the .zip file name in the `S3Bucket` and `S3Key` fields
+ `Runtime` - Set to your chosen runtime

**Creating a .zip file from inline code**

You can declare simple functions written in Python or Node.js inline in an CloudFormation template. Because the code is embedded in YAML or JSON, you can't add any external dependenices to your deployment package. This means your function has to use the version of the AWS SDK that's included in the runtime. The requirements of the template, such as having to escape certain characters, also make it harder to use your IDE's syntax checking and code completion features. This means that your template might require additional testing. Because of these limitations, declaring functions inline is best suited for very simple code that does not change frequently. 

To create a .zip file from inline code for Node.js and Python runtimes, set the following properties in your template’s `AWS::Lambda::Function` resource:
+ `PackageType` - Set to `Zip`
+ `Code` - Enter your function code in the `ZipFile` field
+ `Runtime` - Set to your chosen runtime

 The .zip file that CloudFormation generates cannot exceed 4MB. To learn more about deploying functions using .zip file in CloudFormation, see [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html) in the *CloudFormation User Guide*. 