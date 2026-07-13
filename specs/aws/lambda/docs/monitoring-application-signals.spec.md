---
id: "@specs/aws/lambda/docs/monitoring-application-signals"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Application Signals"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Application Signals

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/monitoring-application-signals
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitor application performance with Amazon CloudWatch Application Signals
<a name="monitoring-application-signals"></a>

Amazon CloudWatch Application Signals is an application performance monitoring (APM) solution that enables developers and operators to monitor the health and performance of their serverless applications built using Lambda. You can enable Application Signals in one-click from the Lambda console, and you don't need to add any instrumentation code or external dependencies to your Lambda function. After you enable Application Signals, you can view all collected metrics and traces in the CloudWatch console. This page describes how to enable and view Application Signals telemetry data for your applications.

**Topics**
+ [How Application Signals integrates with Lambda](#monitoring-application-signals-how)
+ [Pricing](#monitoring-application-signals-pricing)
+ [Supported runtimes](#monitoring-application-signals-runtimes)
+ [Enabling Application Signals in the Lambda console](#monitoring-application-signals-console)
+ [Using the Application Signals dashboard](#monitoring-application-signals-dashboard)

## How Application Signals integrates with Lambda
<a name="monitoring-application-signals-how"></a>

Application Signals automatically instruments your Lambda functions using enhanced [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/) libraries, provided via a [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html). Application Signals reads data collected by the layer and generates dashboards with key performance metrics for your applications.

You can attach this layer in one-click by [ enabling Application Signals](#monitoring-application-signals-console) in the Lambda console. When you enable Application Signals from the console, Lambda does the following on your behalf:
+ Updates your function's execution role to include the `CloudWatchLambdaApplicationSignalsExecutionRolePolicy`. [ This policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchLambdaApplicationSignalsExecutionRolePolicy.html) provides write access to AWS X-Ray and CloudWatch log groups used for Application Signals.
+ Adds a layer to your function which automatically instruments the function to capture telemetry data such as requests, availability, latency, errors, and faults. To ensure that Application Signals works properly, remove any existing X-Ray SDK instrumentation code from your function. Custom X-Ray SDK instrumentation code can interfere with the layer-provided instrumentation.
+ Adds the `AWS_LAMBDA_EXEC_WRAPPER` environment variable to your function, and sets its value to `/opt/otel-instrument`. This environment variable modifies your function's startup behavior to utilize the Application Signals layer, and is required for proper instrumentation. If this environment variable already exists, ensure that it's set to the required value.

## Pricing
<a name="monitoring-application-signals-pricing"></a>

Using Application Signals for your Lambda functions incurs costs. For pricing information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Supported runtimes
<a name="monitoring-application-signals-runtimes"></a>

The Application Signals integration with Lambda works with the following runtimes:
+ .NET 8
+ Java 11
+ Java 17
+ Java 21
+ Python 3.10
+ Python 3.11
+ Python 3.12
+ Python 3.13
+ Node.js 18.x
+ Node.js 20.x
+ Node.js 22.x

## Enabling Application Signals in the Lambda console
<a name="monitoring-application-signals-console"></a>

You can enable Application Signals on any existing Lambda function using a [supported runtime](#monitoring-application-signals-runtimes). The following steps describe how to enable Application Signals in one-click in the Lambda console.

**To enable Application Signals in the Lambda console**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function.

1. Choose the **Configuration** tab.

1. On the left menu, choose **Monitoring and operations tools**.

1. On the **Additional monitoring tools** pane, choose **Edit**.

1. Under **CloudWatch Application Signals and AWS X-Ray**, and under **Application Signals**, choose **Enable**.

1. Choose **Save**.

If this is your first time enabling Application Signals for your function, you must also do a one-time service discovery setup for Application Signals in the CloudWatch console. After you complete this one-time service discovery setup, Application Signals automatically discovers any additional Lambda functions that you enable Application Signals for, across all Regions.

**Note**  
After you invoke your updated function, it can take up to 10 minutes for service data to start appearing in the Application Signals dashboard in the CloudWatch console.

## Using the Application Signals dashboard
<a name="monitoring-application-signals-dashboard"></a>

After you enable Application Signals for your function, you can visualize your application metrics in the CloudWatch console. You can quickly view the associated Application Signals dashboard from the Lambda console with the following steps:

**To view the Application Signals dashboard for your function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function.

1. Choose the **Monitor** tab.

1. Choose the **View Application Signals** button. This takes you directly to the Application Signals overview for your service in the CloudWatch console.

For example, the following screenshot shows metrics for latency, number of requests, availability, fault rate, and error rate for a function across a 10 minute time window.

![An example of an Application Signals dashboard for a Lambda function, depicting latency, number of requests, availability, fault rate, and error rate.](http://docs.aws.amazon.com/lambda/latest/dg/images/monitoring-application-signals-dashboard.png)


To make the most out of your integration with Application Signals, you can create service-level objectives (SLOs) for your aplication. For example, you can create latency SLOs to ensure your application responds quickly to user requests, and availability SLOs to track uptime. SLOs can help you detect performance degradation or outages before they impact your users. For more information, see [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) in the Amazon CloudWatch User Guide.