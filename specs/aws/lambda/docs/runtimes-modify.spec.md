---
id: "@specs/aws/lambda/docs/runtimes-modify"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Runtime modifications"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Runtime modifications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtimes-modify
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Modifying the runtime environment
<a name="runtimes-modify"></a>

You can use [internal extensions](lambda-extensions.md) to modify the runtime process. Internal extensions are not separate processes—they run as part of the runtime process.

Lambda provides language-specific [environment variables](configuration-envvars.md) that you can set to add options and tools to the runtime. Lambda also provides [wrapper scripts](#runtime-wrapper), which allow Lambda to delegate the runtime startup to your script. You can create a wrapper script to customize the runtime startup behavior.

## Language-specific environment variables
<a name="runtimes-envvars"></a>

Lambda supports configuration-only ways to enable code to be pre-loaded during function initialization through the following language-specific environment variables:
+ `JAVA_TOOL_OPTIONS` – On Java, Lambda supports this environment variable to set additional command-line variables in Lambda. This environment variable allows you to specify the initialization of tools, specifically the launching of native or Java programming language agents using the `agentlib` or `javaagent` options. For more information, see [`JAVA_TOOL_OPTIONS` environment variable](https://docs.aws.amazon.com/lambda/latest/dg/java-customization.html#java-tool-options).
+ `NODE_OPTIONS` – Available in [Node.js runtimes](lambda-nodejs.md).
+ `DOTNET_STARTUP_HOOKS` – On .NET Core 3.1 and above, this environment variable specifies a path to an assembly (dll) that Lambda can use.

Using language-specific environment variables is the preferred way to set startup properties.

## Wrapper scripts
<a name="runtime-wrapper"></a>

You can create a *wrapper script* to customize the runtime startup behavior of your Lambda function. A wrapper script enables you to set configuration parameters that cannot be set through language-specific environment variables.

**Note**  
Invocations may fail if the wrapper script does not successfully start the runtime process.

Wrapper scripts are supported on all native [Lambda runtimes](lambda-runtimes.md). Wrapper scripts are not supported on [OS-only runtimes](runtimes-provided.md) (the `provided` runtime family).

When you use a wrapper script for your function, Lambda starts the runtime using your script. Lambda sends to your script the path to the interpreter and all of the original arguments for the standard runtime startup. Your script can extend or transform the startup behavior of the program. For example, the script can inject and alter arguments, set environment variables, or capture metrics, errors, and other diagnostic information.

You specify the script by setting the value of the `AWS_LAMBDA_EXEC_WRAPPER` environment variable as the file system path of an executable binary or script.

### Example: Create and use a wrapper script as a Lambda layer
<a name="runtime-wrapper-example"></a>

In the following example, you create a wrapper script to start the Python interpreter with the `-X importtime` option. When you run the function, Lambda generates a log entry to show the duration of the import time for each import.

**To create and use a wrapper script as a layer**

1. Create a directory for the layer:

   ```
   mkdir -p {{python-wrapper-layer/bin}}
   cd {{python-wrapper-layer/bin}}
   ```

1. In the `bin` directory, paste the following code into a new file named `importtime_wrapper`. This is the wrapper script.

   ```
   #!/bin/bash
   
   # the path to the interpreter and all of the originally intended arguments
   args=("$@")
   
   # the extra options to pass to the interpreter
   extra_args=("-X" "importtime")
   
   # insert the extra options
   args=("${args[@]:0:$#-1}" "${extra_args[@]}" "${args[@]: -1}")
   
   # start the runtime with the extra options
   exec "${args[@]}"
   ```

1. Give the script executable permissions:

   ```
   chmod +x {{importtime_wrapper}}
   ```

1. Create a .zip file for the layer:

   ```
   cd ..
   zip -r ../{{python-wrapper-layer.zip}} .
   ```

1. Confirm that your .zip file has the following directory structure:

   ```
   python-wrapper-layer.zip
   └ bin
       └ importtime_wrapper
   ```

1. [Create a layer](creating-deleting-layers.md#layers-create) using the .zip package.

1. Create a function using the Lambda console.

   1. Open the [Lambda console](https://console.aws.amazon.com/lambda).

   1. Choose **Create function**.

   1. Enter a **Function name**.

   1. For **Runtime**, choose the **Latest supported** Python runtime.

   1. Choose **Create function**.

1. Add the layer to your function.

   1. Choose your function, and then choose the **Code** tab if it's not already selected.

   1. Scroll down to the **Layers** section, and then choose **Add a layer**.

   1. For **Layer source**, select **Custom layers**, and then choose your layer from the **Custom layers** dropdown list.

   1.  For **Version**, choose **1**.

   1. Choose **Add**.

1. Add the wrapper environment variable.

   1. Choose the **Configuration** tab, then choose **Environment variables**.

   1. Under **Environment variables**, choose **Edit**.

   1. Choose **Add environment variable**.

   1. For **Key**, enter `AWS_LAMBDA_EXEC_WRAPPER`.

   1. For **Value**, enter `/opt/bin/importtime_wrapper` (`/opt/` \+ your .zip layer's folder structure).

   1. Choose **Save**.

1. Test the wrapper script.

   1. Choose the **Test** tab.

   1. Under **Test event**, choose **Test**. You don't need to create a test event—the default event will work.

   1. Scroll down to **Log output**. Because your wrapper script started the Python interpreter with the `-X importtime` option, the logs show the time required for each import. For example:

      ```
      532 |           collections
      import time:        63 |         63 |           _functools
      import time:      1053 |       3646 |         functools
      import time:      2163 |       7499 |       enum
      import time:       100 |        100 |         _sre
      import time:       446 |        446 |           re._constants
      import time:       691 |       1136 |         re._parser
      import time:       378 |        378 |         re._casefix
      import time:       670 |       2283 |       re._compiler
      import time:       416 |        416 |       copyreg
      ```