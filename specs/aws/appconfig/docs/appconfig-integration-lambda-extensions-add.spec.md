---
id: "@specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-add"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Adding the AWS AppConfig Agent Lambda extension"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Adding the AWS AppConfig Agent Lambda extension

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-add
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Adding the AWS AppConfig Agent Lambda extension
<a name="appconfig-integration-lambda-extensions-add"></a>

To use the AWS AppConfig Agent Lambda extension, you need to add the extension to your Lambda. This can be done by adding the AWS AppConfig Agent Lambda extension to your Lambda function as a layer or by enabling the extension on a Lambda function as a container image.

**Note**  
The AWS AppConfig extension is runtime agnostic and supports all runtimes.

**Before you begin**  
Before you enable the AWS AppConfig Agent Lambda extension, do the following:
+ Organize the configurations in your Lambda function so that you can externalize them into AWS AppConfig.
+ Create AWS AppConfig artifacts and configuration data, including feature flags or freeform configuration data. For more information, see [Creating feature flags and free form configuration data in AWS AppConfig](creating-feature-flags-and-configuration-data.md).
+ Add `appconfig:StartConfigurationSession` and `appconfig:GetLatestConfiguration` to the AWS Identity and Access Management (IAM) policy used by the Lambda function execution role. For more information, see [AWS Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) in the *AWS Lambda Developer Guide*. For more information about AWS AppConfig permissions, see [Actions, resources, and condition keys for AWS AppConfig](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappconfig.html) in the *Service Authorization Reference*. 

## Adding the AWS AppConfig Agent Lambda extension by using a layer and an ARN
<a name="appconfig-integration-lambda-extensions-enabling"></a>

To use the AWS AppConfig Agent Lambda extension, you add the extension to your Lambda function as a layer. For information about how to add a layer to your function, see [Configuring extensions](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html#using-extensions-config) in the *AWS Lambda Developer Guide*. The name of the extension in the AWS Lambda console is **AWS-AppConfig-Extension**. Also note that when you add the extension as a layer to your Lambda, you must specify an Amazon Resource Name (ARN). Choose an ARN from one of the following lists that corresponds with the platform and AWS Region where you created the Lambda.
+ [x86-64 platform](appconfig-integration-lambda-extensions-versions.md#appconfig-integration-lambda-extensions-enabling-x86-64)
+ [ARM64 platform](appconfig-integration-lambda-extensions-versions.md#appconfig-integration-lambda-extensions-enabling-ARM64)

If you want to test the extension before you add it to your function, you can verify that it works by using the following code example.

```
import urllib.request
                

def lambda_handler(event, context):
    url = f'http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}'
    config = urllib.request.urlopen(url).read()
    return config
```

To test it, create a new Lambda function for Python, add the extension, and then run the Lambda function. After you run the Lambda function, the AWS AppConfig Lambda function returns the configuration you specified for the http://localhost:2772 path. For information about creating a Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the *AWS Lambda Developer Guide*. 

**Important**  
You can view log data for the AWS AppConfig Agent Lambda extension in the AWS Lambda logs. Log entries are prefaced with `appconfig agent`. Here's an example.  

```
[appconfig agent] 2024/05/07 04:19:01 ERROR retrieve failure for 'SourceEventConfig:SourceEventConfigEnvironment:SourceEventConfigProfile': StartConfigurationSession: api error AccessDenied: User: arn:aws:sts::0123456789:assumed-role/us-east-1-LambdaRole/extension1 is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::0123456789:role/test1 (retry in 60s)
```