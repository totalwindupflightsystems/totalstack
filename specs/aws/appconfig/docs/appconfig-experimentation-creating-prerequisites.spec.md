---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-creating-prerequisites"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step 1: Configuring prerequisites"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Step 1: Configuring prerequisites

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-creating-prerequisites
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 1: Configuring prerequisites
<a name="appconfig-experimentation-creating-prerequisites"></a>

Before you begin, complete the following tasks:
+ **[Install and configure AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent.html)**: AWS AppConfig experimentation requires AWS AppConfig Agent to deliver treatments to users. The agent retrieves feature flag and other configuration data from AWS AppConfig, caches it locally, and asynchronously polls the AWS AppConfig data plane for updates. This approach keeps feature flag and other configuration data readily available to your application while reducing latency and cost. The following topics describe how to install and configure AWS AppConfig Agent for each supported compute environment:
  + [Using AWS AppConfig Agent with AWS Lambda](appconfig-integration-lambda-extensions.md)
  + [Using AWS AppConfig Agent with Amazon EC2 and on-premises machines](appconfig-integration-ec2.md)
  + [Using AWS AppConfig Agent with Amazon ECS and Amazon EKS](appconfig-integration-containers-agent.md)

  Note that each section includes information about configuring IAM permissions so the agent can retrieve feature flags and other configuration data.
+ **Configure experiment assignment logging**: To capture treatment assignment data during an experiment run, set the `EXPERIMENT_ASSIGNMENT_LOG_DESTINATION` agent configuration option to a file path on disk (for example, `file:/var/log/appconfig/experiments/`). For more information about assignment log format and export, see [About data collection](appconfig-experimentation-about-data-collection.md).