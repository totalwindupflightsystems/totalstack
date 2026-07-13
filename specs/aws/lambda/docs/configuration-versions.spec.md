---
id: "@specs/aws/lambda/docs/configuration-versions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Versions"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Versions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-versions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Manage Lambda function versions
<a name="configuration-versions"></a>

You can use versions to manage the deployment of your functions. For example, you can publish a new version of a function for beta testing without affecting users of the stable production version. Lambda creates a new version of your function each time that you publish the function. The new version is a copy of the unpublished version of the function. The unpublished version is named `$LATEST`.

Importantly, any time you deploy your function code, you overwrite the current code in `$LATEST`. To save the current iteration of `$LATEST`, create a new function version. If `$LATEST` is identical to a previously published version, you won't be able to create a new version until you deploy changes to `$LATEST`. These changes can include updating the code, or modifying the function configuration settings.

After you publish a function version, its code, runtime, architecture, memory, layers, and most other configuration settings are immutable. This means that you can't change these settings without publishing a new version from `$LATEST`. You can configure the following items for a published function version:
+ [Triggers](lambda-services.md#lambda-invocation-trigger)
+ [Destinations](invocation-async-retain-records.md#create-destination)
+ [Provisioned concurrency](provisioned-concurrency.md)
+ [Asynchronous invocation](invocation-async.md)
+ [Database connections and proxies](services-rds.md#rds-configuration)

**Note**  
When using [runtime management controls](runtimes-update.md#runtime-management-controls) with **Auto** mode, the runtime version used by the function version is updated automatically. When using **Function update** or **Manual** mode, the runtime version is not updated. For more information, see [Understanding how Lambda manages runtime version updates](runtimes-update.md).

**Topics**
+ [Creating function versions](#configuration-versions-config)
+ [Using versions](#versioning-versions-using)
+ [Granting permissions](#versioning-permissions)

## Creating function versions
<a name="configuration-versions-config"></a>

You can change the function code and settings only on the unpublished version of a function. When you publish a version, Lambda locks the code and most of the settings to maintain a consistent experience for users of that version.

You can create a function version using the Lambda console.

**To create a new function version**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function and then choose the **Versions** tab.

1. On the versions configuration page, choose **Publish new version**.

1. (Optional) Enter a version description.

1. Choose **Publish**.

Alternatively, you can publish a version of a function using the [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html) API operation.

The following AWS CLI command publishes a new version of a function. The response returns configuration information about the new version, including the version number and the function ARN with the version suffix.

```
aws lambda publish-version --function-name my-function
```

You should see the following output:

```
{
  "FunctionName": "my-function",
  "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:1",
  "Version": "1",
  "Role": "arn:aws:iam::123456789012:role/lambda-role",
  "Handler": "function.handler",
  "Runtime": "nodejs24.x",
  ...
}
```

**Note**  
Lambda assigns monotonically increasing sequence numbers for versioning. Lambda never reuses version numbers, even after you delete and recreate a function.

## Using versions
<a name="versioning-versions-using"></a>

You can reference your Lambda function using either a qualified ARN or an unqualified ARN.
+ **Qualified ARN** – The function ARN with a version suffix. The following example refers to version 42 of the `helloworld` function.

  ```
  arn:aws:lambda:aws-region:acct-id:function:helloworld:42
  ```
+ **Unqualified ARN** – The function ARN without a version suffix.

  ```
  arn:aws:lambda:aws-region:acct-id:function:helloworld
  ```

You can use a qualified or an unqualified ARN in all relevant API operations. However, you can't use an unqualified ARN to create an alias.

If you decide not to publish function versions, you can invoke the function using either the qualified or unqualified ARN in your [event source mapping](invocation-eventsourcemapping.md). When you invoke a function using an unqualified ARN, Lambda implicitly invokes `$LATEST`. 

The qualified ARN for each Lambda function version is unique. After you publish a version, you can't change the ARN or the function code.

Lambda publishes a new function version only if the code has never been published, or if the code has changed from the last published version. If there is no change, the function version remains at the last published version.

When you publish a version, Lambda creates an immutable snapshot of your function's code and configuration. Not all configuration changes trigger the publication of a new version. The following configuration changes qualify a function for version publication:
+ Function code
+ Environment variables
+ Runtime
+ Handler
+ Layers
+ Memory size
+ Timeout
+ VPC configuration
+ Dead Letter Queue (DLQ) configuration
+ IAM role
+ Description
+ Architecture (x86\_64 or arm64)
+ Ephemeral storage size
+ Package type
+ Logging configuration
+ File system configuration
+ SnapStart
+ Tracing configuration

Operational settings such as [reserved concurrency](configuration-concurrency.md) don't trigger the publication of a new version when changed.

## Granting permissions
<a name="versioning-permissions"></a>

You can use a [resource-based policy](access-control-resource-based.md) or an [identity-based policy](access-control-identity-based.md) to grant access to your function. The scope of the permission depends on whether you apply the policy to a function or to one version of a function. For more information about function resource names in policies, see [Fine-tuning the Resources and Conditions sections of policies](lambda-api-permissions-ref.md). 

You can simplify the management of event sources and AWS Identity and Access Management (IAM) policies by using function aliases. For more information, see [Create an alias for a Lambda function](configuration-aliases.md).