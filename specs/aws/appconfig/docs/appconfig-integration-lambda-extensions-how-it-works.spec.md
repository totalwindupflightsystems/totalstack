---
id: "@specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-how-it-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding how the AWS AppConfig Agent Lambda extension works"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding how the AWS AppConfig Agent Lambda extension works

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-lambda-extensions-how-it-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding how the AWS AppConfig Agent Lambda extension works
<a name="appconfig-integration-lambda-extensions-how-it-works"></a>

If you use AWS AppConfig to manage configurations for a Lambda function *without* Lambda extensions, then you must configure your Lambda function to receive configuration updates by integrating with the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html) and [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) API actions.

Integrating the AWS AppConfig Agent Lambda extension with your Lambda function simplifies this process. The extension takes care of calling the AWS AppConfig service, managing a local cache of retrieved data, tracking the configuration tokens needed for the next service calls, and periodically checking for configuration updates in the background. The following diagram shows how it works.

![A diagram of how the AWS AppConfig Agent Lambda extension works](http://docs.aws.amazon.com/appconfig/latest/userguide/images/AppConfigLambdaExtension.png)


1. You configure the AWS AppConfig Agent Lambda extension as a layer of your Lambda function. 

1. To access its configuration data, your function calls the AWS AppConfig extension at an HTTP endpoint running on `localhost:2772`.

1. The extension maintains a local cache of the configuration data. If the data isn't in the cache, the extension calls AWS AppConfig to get the configuration data.

1. Upon receiving the configuration from the service, the extension stores it in the local cache and passes it to the Lambda function. 

1. AWS AppConfig Agent Lambda extension periodically checks for updates to your configuration data in the background. Each time your Lambda function is invoked, the extension checks the elapsed time since it retrieved a configuration. If the elapsed time is greater than the configured poll interval, the extension calls AWS AppConfig to check for newly deployed data, updates the local cache if there has been a change, and resets the elapsed time. 

**Note**  
Lambda instantiates separate instances corresponding to the concurrency level that your function requires. Each instance is isolated and maintains its own local cache of your configuration data. For more information about Lambda instances and concurrency, see [Managing concurrency for a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).
The amount of time it takes for a configuration change to appear in a Lambda function, after you deploy an updated configuration from AWS AppConfig, depends on the deployment strategy you used for the deployment and the polling interval you configured for the extension. 