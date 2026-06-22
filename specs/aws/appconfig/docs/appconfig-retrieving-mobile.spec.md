---
id: "@specs/aws/appconfig/docs/appconfig-retrieving-mobile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Browser and mobile use considerations"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Browser and mobile use considerations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-retrieving-mobile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS AppConfig browser and mobile use considerations
<a name="appconfig-retrieving-mobile"></a>

Feature flags enable you to update the experience of your web pages and mobile application on the fly, without the overhead, risk, or rigidity of an app store release. Using feature flags, you can gradually release a change to your user base at a time of your choosing. If you encounter an error, you can instantly roll back the change without requiring users to upgrade to a new software version. In short, feature flags provide greater control and flexibility when deploying changes to your application. 

The following sections describe important considerations for using AWS AppConfig feature flags with web pages and mobiles devices.

**Topics**
+ [Configuration data and flag retrieval](#appconfig-retrieving-mobile-configuration-data)
+ [Authentication and Amazon Cognito](#appconfig-retrieving-mobile-authentication)
+ [Caching](#appconfig-retrieving-mobile-caching)
+ [Segmentation](#appconfig-retrieving-mobile-segmentation)
+ [Bandwidth (mobile use cases)](#appconfig-retrieving-mobile-experience-bandwidth)
+ [Additional flag use cases](#appconfig-retrieving-mobile-use-cases)

## Configuration data and flag retrieval
<a name="appconfig-retrieving-mobile-configuration-data"></a>

For browser and mobile use cases, many customers choose to employ a proxy layer between the web or the mobile application and AWS AppConfig. Doing so decouples your AWS AppConfig call volume from the size of your user base, which reduces costs. It also enables you to leverage the [AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html), which optimizes flag-retrieval performance and supports features like [multi-variant flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags.html). AWS AppConfig recommends using AWS Lambda to create the proxy. Instead of retrieving flags directly from AWS AppConfig, configure the [AWS AppConfig Lambda extension](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html) to retrieve your feature flags within a Lambda function. Write the function to accept AWS AppConfig retrieval parameters from the event request and to return the corresponding configuration data in the Lambda response. Expose your proxy to the internet using [Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html). 

After you configure your proxy, consider the frequency in which you retrieve data. Mobile uses cases typically do not require high-frequency polling intervals. Configure AWS AppConfig Agent to refresh data from AWS AppConfig more frequently than your application refreshes from the proxy.

## Authentication and Amazon Cognito
<a name="appconfig-retrieving-mobile-authentication"></a>

Lambda function URLs support [two forms of access control](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html), `AWS_IAM` and `NONE`. Use `NONE` if you prefer to implement your own authentication and authorization in your Lambda function. `NONE` is also the recommended option if your use case allows exposing your endpoint to the public and your configuration data doesn't contain sensitive data. For all other use cases, use `AWS_IAM`. 

**Important**  
If you expose your endpoint to the internet without authentication, ensure that your configuration data does not leak sensitive data, including personally identifiable information (PII), user IDs, or unreleased feature names.

If you choose to use `AWS_IAM`, you’ll need to manage credentials with [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html). To get started with Amazon Cognito, you create an identity pool. An identity pool allows you to vend short-term credentials to your application for authenticated or guest users. You will need to add roles in the identity pool that permit users to use the `InvokeFunctionUrl` for your Lambda function. Doing so enables instances of your application to access the credentials necessary to retrieve your configuration data.

When working with Amazon Cognito in your application, consider using [AWS Amplify](https://docs.aws.amazon.com/amplify/). Amplify simplifies mobile/web application interactions with AWS and provides built-in support for Amazon Cognito. 

## Caching
<a name="appconfig-retrieving-mobile-caching"></a>

When using AWS AppConfig, you should always cache your configuration data locally on the device or in the browser. Caching offers the following advantages:
+ Improves performance by reducing latency and battery drain
+ Offers stability by eliminating dependencies to network access
+ Lowers cost by reducing data retrieval frequency

For mobile use cases, we recommend you implement in-memory and persistent on-device caches. Configure your application to attempt to retrieve the desired configuration from the in-memory cache and fall back to fetching from your proxy, if necessary. Upon successful retrieval from your proxy, update the in-memory cache and then persist the configuration to the device. Use a background process to iterate through the cache and refresh each configuration. When fetching configuration for the first time after application startup, if a retrieval is unsuccessful, defer to the persistent configuration (and use it to seed the in-memory cache).

## Segmentation
<a name="appconfig-retrieving-mobile-segmentation"></a>

When using feature flags, you may want to segment the feature flagging experience across your customer base. To do so, supply context to your flag retrieval calls, and configure rules to return different [variants of your feature flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags.html) based on the provided context. For example, you may have a feature flag variant for iOS 18.X users, a variant for iOS 17.X users, and a default flag for all other versions of iOS. With variants, you can configure every iOS version of your application to target the same configuration in the same environment, but based on the context supplied in the retrieval call (for example, "version": "iOS18.1"), the devices will receive the appropriate variant of the configuration.

**Note**  
If you are using AWS AppConfig feature flag variants for a mobile use case, you must use the AWS AppConfig Agent and a proxy for retrieving feature flags.

If you choose not to use AWS AppConfig Agent to retrieve feature flags, you can leverage AWS AppConfig [environments](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html) for simple, low-cardinality segmentation. An environment is a logical deployment group for your targets. In addition to partitioning your configurations to development, testing, and production environments, you can subdivide your customer base by creating mobile-specific environments, such as device type (tablet vs phone) or OS major versions. With separate environments, you can deploy the same or different sets of configuration data to meet the particular requirements of your customer base.

## Bandwidth (mobile use cases)
<a name="appconfig-retrieving-mobile-experience-bandwidth"></a>

In general, aim to keep the size of each flag set small. Mobile use cases tend to involve low-bandwidth constraints. Minimizing the size of your data will help you maintain a consistent experience across your user base. Also, consider that because mobile devices often operate between low- and no-bandwidth environments, on-device caching is critical. Application code that fails gracefully if no configuration data can be retrieved is also critical.

## Additional flag use cases
<a name="appconfig-retrieving-mobile-use-cases"></a>

The power of feature flags extends beyond feature-release convenience. Long standing operational flags can be used to improve the operational posture of your application. For example, you can create a performance monitoring toggle that emits additional metrics and debug data during an event. Alternatively, you may want to maintain and adjust your application refresh rates for a segment of your customer base. 