---
id: "@specs/aws/appconfig/docs/appconfig-creating-deployment-strategy-predefined"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using predefined deployment strategies"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Using predefined deployment strategies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-deployment-strategy-predefined
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using predefined deployment strategies
<a name="appconfig-creating-deployment-strategy-predefined"></a>

AWS AppConfig includes predefined deployment strategies to help you quickly deploy a configuration. Instead of creating your own strategies, you can choose one of the following when you deploy a configuration.


****  

| Deployment strategy | Description | 
| --- | --- | 
| AppConfig.Linear20PercentEvery6Minutes | **AWS recommended**:<br />This strategy deploys the configuration to 20% of all targets every six minutes for a 30 minute deployment. The system monitors for Amazon CloudWatch alarms for 30 minutes. If no alarms are received in this time, the deployment is complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment.<br />We recommend using this strategy for production deployments because it aligns with AWS best practices and includes additional emphasis on deployment safety due to its long duration and bake time. | 
| AppConfig.Canary10Percent20Minutes | **AWS recommended**:<br />This strategy processes the deployment exponentially using a 10% growth factor over 20 minutes. The system monitors for CloudWatch alarms for 10 minutes. If no alarms are received in this time, the deployment is complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment.<br />We recommend using this strategy for production deployments because it aligns with AWS best practices for configuration deployments. | 
| AppConfig.AllAtOnce | **Quick**:<br />This strategy deploys the configuration to all targets immediately. The system monitors for CloudWatch alarms for 10 minutes. If no alarms are received in this time, the deployment is complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment.  | 
| AppConfig.Linear50PercentEvery30Seconds | **Testing/demonstration**:<br />This strategy deploys the configuration to half of all targets every 30 seconds for a one-minute deployment. The system monitors for Amazon CloudWatch alarms for 1 minute. If no alarms are received in this time, the deployment is complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment.<br />We recommend using this strategy only for testing or demonstration purposes because it has a short duration and bake time. | 