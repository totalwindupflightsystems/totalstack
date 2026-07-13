---
id: "@specs/aws/lambda/docs/configuring-alias-routing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Weighted aliases"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Weighted aliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuring-alias-routing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Implement Lambda canary deployments using a weighted alias
<a name="configuring-alias-routing"></a>

You can use a weighted alias to split traffic between two different [versions](configuration-versions.md) of the same function. With this approach, you can test new versions of your functions with a small percentage of traffic and quickly roll back if necessary. This is known as a [canary deployment](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html). Canary deployments differ from blue/green deployments by exposing the new version to only a portion of requests rather than switching all traffic at once.

You can point an alias to a maximum of two Lambda function versions. The versions must meet the following criteria:
+ Both versions must have the same [execution role](lambda-intro-execution-role.md).
+ Both versions must have the same [dead-letter queue](invocation-async-retain-records.md#invocation-dlq) configuration, or no dead-letter queue configuration.
+ Both versions must be published. The alias cannot point to `$LATEST`.

**Note**  
Lambda uses a simple probabilistic model to distribute the traffic between the two function versions. At low traffic levels, you might see a high variance between the configured and actual percentage of traffic on each version. If your function uses provisioned concurrency, you can avoid [spillover invocations](monitoring-metrics-types.md#invocation-metrics) by configuring a higher number of provisioned concurrency instances during the time that alias routing is active. 

## Create a weighted alias
<a name="create-weighted-alias"></a>

------
#### [ Console ]

**To configure routing on an alias using the console**
**Note**  
Verify that the function has at least two published versions. To create additional versions, follow the instructions in [Creating function versions](configuration-versions.md#configuration-versions-config).

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose **Aliases** and then choose **Create alias**.

1. On the **Create alias** page, do the following:

   1. Enter a **Name** for the alias.

   1. (Optional) Enter a **Description** for the alias.

   1. For **Version**, choose the first function version that you want the alias to point to.

   1. Expand **Weighted alias**.

   1. For **Additional version**, choose the second function version that you want the alias to point to.

   1. For **Weight (%)**, enter a weight value for the function. *Weight* is the percentage of traffic that is assigned to that version when the alias is invoked. The first version receives the residual weight. For example, if you specify 10 percent to **Additional version**, the first version is assigned 90 percent automatically.

   1. Choose **Save**.

------
#### [ AWS CLI ]

Use the [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html) and [update-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-alias.html) AWS CLI commands to configure the traffic weights between two function versions. When you create or update the alias, you specify the traffic weight in the `routing-config` parameter.

The following example creates a Lambda function alias named **routing-alias** that points to version 1 of the function. Version 2 of the function receives 3 percent of the traffic. The remaining 97 percent of traffic is routed to version 1.

```
aws lambda create-alias \
  --name routing-alias \
  --function-name my-function \
  --function-version 1  \
  --routing-config AdditionalVersionWeights={"2"=0.03}
```

Use the `update-alias` command to increase the percentage of incoming traffic to version 2. In the following example, you increase the traffic to 5 percent.

```
aws lambda update-alias \
  --name routing-alias \
  --function-name my-function \
  --routing-config AdditionalVersionWeights={"2"=0.05}
```

To route all traffic to version 2, use the `update-alias` command to change the `function-version` property to point the alias to version 2. The command also resets the routing configuration.

```
aws lambda update-alias \
  --name routing-alias \
  --function-name my-function  \
  --function-version 2 \
  --routing-config AdditionalVersionWeights={}
```

 The AWS CLI commands in the preceding steps correspond to the following Lambda API operations:
+ [CreateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_CreateAlias.html)
+ [UpdateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateAlias.html)

------

## Determining which version was invoked
<a name="determining-routing-version"></a>

When you configure traffic weights between two function versions, there are two ways to determine the Lambda function version that has been invoked:
+ **CloudWatch Logs** – Lambda automatically emits a `START` log entry that contains the invoked version ID for every function invocation. Example:

  `START RequestId: 1dh194d3759ed-4v8b-a7b4-1e541f60235f Version: {{2}}` 

  For alias invocations, Lambda uses the `ExecutedVersion` dimension to filter the metric data by the invoked version. For more information, see [Viewing metrics for Lambda functions](monitoring-metrics-view.md).
+ **Response payload (synchronous invocations)** – Responses to synchronous function invocations include an `x-amz-executed-version` header to indicate which function version has been invoked.

## Create a rolling deployment with weighted aliases
<a name="lambda-rolling-deployments"></a>

Use AWS CodeDeploy and AWS Serverless Application Model (AWS SAM) to create a rolling deployment that automatically detects changes to your function code, deploys a new version of your function, and gradually increase the amount of traffic flowing to the new version. The amount of traffic and rate of increase are parameters that you can configure.

In a rolling deployment, AWS SAM performs these tasks:
+ Configures your Lambda function and creates an alias. The weighted alias routing configuration is the underlying capability that implements the rolling deployment.
+ Creates a CodeDeploy application and deployment group. The deployment group manages the rolling deployment and the rollback, if needed.
+ Detects when you create a new version of your Lambda function.
+ Triggers CodeDeploy to start the deployment of the new version.

### Example AWS SAM template
<a name="sam-template"></a>

The following example shows an [AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-basics.html) for a simple rolling deployment. 

```
AWSTemplateFormatVersion : '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: A sample SAM template for deploying Lambda functions

Resources:
# Details about the myDateTimeFunction Lambda function
  myDateTimeFunction:
    Type: [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
    Properties:
      Handler: myDateTimeFunction.handler
      Runtime: nodejs24.x
# Creates an alias named "live" for the function, and automatically publishes when you update the function.
      AutoPublishAlias: live
      DeploymentPreference:
# Specifies the deployment configuration
          Type: Linear10PercentEvery2Minutes
```

This template defines a Lambda function named `myDateTimeFunction` with the following properties. 

**AutoPublishAlias **  
The `AutoPublishAlias` property creates an alias named `live`. In addition, the AWS SAM framework automatically detects when you save new code for the function. The framework then publishes a new function version and updates the `live` alias to point to the new version.

**DeploymentPreference**  
The `DeploymentPreference` property determines the rate at which the CodeDeploy application shifts traffic from the original version of the Lambda function to the new version. The value `Linear10PercentEvery2Minutes` shifts an additional ten percent of the traffic to the new version every two minutes.   
For a list of the predefined deployment configurations, see [Deployment configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html). 

For more information on how to create rolling deployments with CodeDeploy and AWS SAM, see the following:
+ [Tutorial: Deploy an updated Lambda function with CodeDeploy and the AWS Serverless Application Model](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam.html)
+ [Deploying serverless applications gradually with AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html)