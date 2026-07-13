---
id: "@specs/aws/lambda/docs/runtime-management-configure-settings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring runtime management"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Configuring runtime management

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/runtime-management-configure-settings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring Lambda runtime management settings
<a name="runtime-management-configure-settings"></a>

You can configure runtime management settings using the Lambda console or the AWS Command Line Interface (AWS CLI).

**Note**  
You can configure runtime management settings separately for each [function version](configuration-versions.md).

**To configure how Lambda updates your runtime version (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. On the **Code** tab, under **Runtime settings**, choose **Edit runtime management configuration**.

1. Under **Runtime management configuration**, choose one of the following:
   + To have your function update to the latest runtime version automatically, choose **Auto**.
   + To have your function update to the latest runtime version when you change the function, choose **Function update**.
   + To have your function update to the latest runtime version only when you change the runtime version ARN, choose **Manual**. You can find the runtime version ARN under **Runtime management configuration**. You can also find the ARN in the `INIT_START` line of your function logs.

   For more information about these options, see [Runtime update modes](runtimes-update.md#runtime-management-controls).

1. Choose **Save**.

**To configure how Lambda updates your runtime version (AWS CLI)**

To configure runtime management for a function, run the [put-runtime-management-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-runtime-management-config.html) AWS CLI command. When using `Manual` mode, you must also provide the runtime version ARN.

```
aws lambda put-runtime-management-config \
  --function-name {{my-function}} \
  --update-runtime-on Manual \
  --runtime-version-arn {{arn:aws:lambda:us-east-2::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1}}
```

You should see output similar to the following:

```
{
  "UpdateRuntimeOn": "Manual",
  "FunctionArn": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
  "RuntimeVersionArn": "arn:aws:lambda:us-east-2::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1"
}
```