---
id: "@specs/aws/opensearchserverless/docs/setting-up"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Setting up"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Setting up

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/setting-up
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Setting up Amazon OpenSearch Service
<a name="setting-up"></a>

## Grant permissions
<a name="setting-up-iam"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Install and configure the AWS CLI
<a name="setting-up-cli"></a>

If you want to use OpenSearch Service APIs, you must install the latest version of the AWS Command Line Interface (AWS CLI). You don't need the AWS CLI to use OpenSearch Service from the console, and you can get started without the CLI by following the steps in [Getting started with Amazon OpenSearch Service](gsg.md).

**To set up the AWS CLI**

1. To install the latest version of the AWS CLI for macOS, Linux, or Windows, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. To configure the AWS CLI and secure setup of your access to AWS services, including OpenSearch Service, see [Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config).

1. To verify the setup, enter the following DataBrew command at the command prompt.

   ```
   aws opensearch help
   ```

   AWS CLI commands use the default AWS Region from your configuration, unless you set it with a parameter or a profile. To set your AWS Region with a parameter, you can add the `--region` parameter to each command.

   To set your AWS Region with a profile, first add a named profile in the `~/.aws/config` file or the `%UserProfile%/.aws/config` file (for Microsoft Windows). Follow the steps in [Named profiles for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html). Next, set your AWS Region and other settings with a command similar to the one in the following example.

   ```
   [profile opensearch]
   aws_access_key_id = ACCESS-KEY-ID-OF-IAM-USER
   aws_secret_access_key = SECRET-ACCESS-KEY-ID-OF-IAM-USER
   region = us-east-1
   output = text
   ```

## Open the console
<a name="opening-console"></a>

Most of the console-oriented topics in this section start from the [OpenSearch Service console](https://console.aws.amazon.com/aos/home). If you aren't already signed in to your AWS account, sign in, then open the [OpenSearch Service console](https://console.aws.amazon.com/aos/home) and continue to the next section to continue getting started with OpenSearch Service.