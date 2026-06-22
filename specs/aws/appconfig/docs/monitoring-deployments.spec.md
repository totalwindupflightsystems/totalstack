---
id: "@specs/aws/appconfig/docs/monitoring-deployments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitoring deployments for automatic rollback"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Monitoring deployments for automatic rollback

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/monitoring-deployments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitoring deployments for automatic rollback
<a name="monitoring-deployments"></a>

During a deployment, you can mitigate situations where malformed or incorrect configuration data causes errors in your application by using a combination of AWS AppConfig [deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html) and automatic rollbacks based on Amazon CloudWatch alarms. Once configured, if one or more CloudWatch alarms go into the `ALARM` or `INSUFFICIENT_DATA`state during a deployment, AWS AppConfig automatically rolls back your configuration data to the previous version, thereby preventing application outages or errors. 

**Note**  
A deployment doesn't automatically roll back if actions have been disabled in an associated CloudWatch alarm.   
You can disable and enable alarms by using the [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html) and [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html) API actions, or the [disable-alarm-actions](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/disable-alarm-actions.html) and [enable-alarm-actions](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/enable-alarm-actions.html) commands in the AWS CLI. 

You can also roll back a configuration by calling the [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html) API operation while a deployment is still in progress.

**Important**  
For deployments that successfully complete, AWS AppConfig also supports reverting configuration data to a previous version by using the `AllowRevert` parameter with the [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html) API operation. For some customers, reverting to a previous configuration after a successful deployment guarantees the data will be the same as it was before the deployment. Reverting also ignores alarm monitors, which may prevent a roll forward from progressing during an application emergency. For more information, see [Reverting a configuration](appconfig-deploying-reverting.md).

To configure automatic rollbacks, you specify the Amazon Resource Name (ARN) of one or more CloudWatch metrics in the **CloudWatch alarms** field when you create (or edit) an AWS AppConfig environment. For more information, see [Creating environments for your application in AWS AppConfig](appconfig-creating-environment.md).

**Note**  
If you use a third-party monitoring solution (for example, Datadog or New Relic), you can create an AWS AppConfig extension that checks for alarms at the `AT_DEPLOYMENT_TICK` action point and, as a safety guardrail, rolls back the deployment if it triggered an alarm. For more information, see the following Datadog and New Relic integration examples on GitHub:   
[Datadog](https://github.com/aws-samples/aws-appconfig-tick-extn-for-datadog)
[New Relic](https://github.com/aws-samples/sample-aws-appconfig-tick-extn-for-newrelic)
For more information about AWS AppConfig extensions, see the following topics:  
[Extending AWS AppConfig workflows using extensions](working-with-appconfig-extensions.md)
[Walkthrough: Creating custom AWS AppConfig extensions](working-with-appconfig-extensions-creating-custom.md)

## Recommended metrics to monitor for automatic rollback
<a name="monitoring-deployments-metrics"></a>

The metrics you choose to monitor will depend on the hardware and software used by your applications. AWS AppConfig customers often monitor the following metrics. For a complete list of recommended metrics grouped by AWS service, see [Recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html) in the *Amazon CloudWatch User Guide*.

After you determine the metrics you want to monitor, use CloudWatch to configure alarms. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).


****  

| Service | Metric | Details | 
| --- | --- | --- | 
| [Amazon API Gateway](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ApiGateway) | 4XXError | This alarm detects a high rate of client-side errors. This can indicate an issue in the authorization or client request parameters. It could also mean that a resource was removed or a client is requesting one that doesn't exist. Consider enabling Amazon CloudWatch Logs and checking for any errors that may be causing the 4XX errors. Moreover, consider enabling detailed CloudWatch metrics to view this metric per resource and method and narrow down the source of the errors. Errors could also be caused by exceeding the configured throttling limit.  | 
| [Amazon API Gateway](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ApiGateway) | 5XXError | This alarm helps to detect a high rate of server-side errors. This can indicate that there is something wrong on the API backend, the network, or the integration between the API gateway and the backend API.  | 
| [Amazon API Gateway](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ApiGateway) | Latency | This alarm detects high latency in a stage. Find the `IntegrationLatency` metric value to check the API backend latency. If the two metrics are mostly aligned, the API backend is the source of higher latency and you should investigate there for issues. Consider also enabling CloudWatch Logs and checking for errors that might be causing the high latency.  | 
| [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#AutoScaling) | GroupInServiceCapacity | This alarm helps to detect when the capacity in the group is below the desired capacity required for your workload. To troubleshoot, check your scaling activities for launch failures and confirm that your desired capacity configuration is correct. | 
| [Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#EC2) | CPUUtilization | This alarm helps to monitor the CPU utilization of an EC2 instance. Depending on the application, consistently high utilization levels might be normal. But if performance is degraded, and the application is not constrained by disk I/O, memory, or network resources, then a maxed-out CPU might indicate a resource bottleneck or application performance problems. | 
| [Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ECS) | CPUReservation | This alarm helps you detect a high CPU reservation of the ECS cluster. High CPU reservation might indicate that the cluster is running out of registered CPUs for the task.  | 
| [Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#ECS) | HTTPCode\_Target\_5XX\_Count | This alarm helps you detect a high server-side error count for the ECS service. This can indicate that there are errors that cause the server to be unable to serve requests.  | 
| [Amazon EKS with Container insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#EKS-ContainerInsights) | node\_cpu\_utilization | This alarm helps to detect high CPU utilization in worker nodes of the Amazon EKS cluster. If the utilization is consistently high, it might indicate a need for replacing your worker nodes with instances that have greater CPU or a need to scale the system horizontally. | 
| [Amazon EKS with Container insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#EKS-ContainerInsights) | node\_memory\_utilization | This alarm helps in detecting high memory utilization in worker nodes of the Amazon EKS cluster. If the utilization is consistently high, it might indicate a need to scale the number of pod replicas, or optimize your application. | 
| [Amazon EKS with Container insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#EKS-ContainerInsights) | pod\_cpu\_utilization\_over\_pod\_limit | This alarm helps in detecting high CPU utilization in pods of the Amazon EKS cluster. If the utilization is consistently high, it might indicate a need to increase the CPU limit for the affected pod. | 
| [Amazon EKS with Container insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#EKS-ContainerInsights) | pod\_memory\_utilization\_over\_pod\_limit | This alarm helps in detecting high CPU utilization in pods of the Amazon EKS cluster. If the utilization is consistently high, it might indicate a need to increase the CPU limit for the affected pod. | 
| [AWS Lambda](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#Lambda) | Errors | This alarm detects high error counts. Errors includes the exceptions thrown by the code as well as exceptions thrown by the Lambda runtime.  | 
| [AWS Lambda](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#Lambda) | Throttles | This alarm detects a high number of throttled invocation requests. Throttling occurs when there is no concurrency is available for scale up.  | 
| [Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#LambdaInsights) | memory\_utilization | This alarm is used to detect if the memory utilization of a lambda function is approaching the configured limit.  | 
| [Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#S3) | 4xxErrors | This alarm helps us report the total number of 4xx error status codes that are made in response to client requests. 403 error codes might indicate an incorrect IAM policy, and 404 error codes might indicate mis-behaving client application, for example. | 
| [Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html#S3) | 5xxErrors | This alarm helps you detect a high number of server-side errors. These errors indicate that a client made a request that the server couldn’t complete. This can help you correlate the issue your application is facing because of S3. | 