---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-example-flow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Example experiment workflow"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Example experiment workflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-example-flow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Example experiment workflow
<a name="appconfig-experimentation-example-flow"></a>

At a high level, the process of creating, running, and ending an experiment using AWS AppConfig experimentation works as follows:

1. Define the experiment objective, including a name, hypothesis, and launch criteria. For more information, see [Documenting your hypothesis](appconfig-experimentation-about-defining.md). As an Amazon best practice, spend sufficient time on this: the most successful experiments have robust hypotheses and launch criteria.

1. Complete prerequisites, including configuring IAM permissions and installing AWS AppConfig Agent. For more information, see [Step 1: Configuring prerequisites](appconfig-experimentation-creating-prerequisites.md).

1. Configure an analytics platform to capture experiment data. This may be CloudWatch, Snowflake, Datadog, or other.

1. Define the target audience using rules that filter users by attributes such as region, account type, or device. For more information, see [Specifying the target audience for the experiment](appconfig-experimentation-about-specifying-audience.md).

1. Select an existing feature flag to control treatment delivery. For more information, see [Selecting the experiment feature flag](appconfig-experimentation-about-experiment-feature-flag.md).

1. Add treatments that define the control and one or more variations to evaluate. For more information, see [About controls and treatments](appconfig-experimentation-about-controls-and-treatments.md).

1. Start the experiment at 0% exposure, validate with overrides, then gradually increase exposure while monitoring metrics. For more information, see [About running and monitoring an experiment](appconfig-experimentation-about-running-an-experiment.md).

1. In your data warehouse of choice, analyze results, roll out the winning treatment, and clean up the experiment. For more information, see [Promoting a winning treatment](appconfig-experimentation-promoting-a-treatment.md).

For more detailed information about AWS AppConfig experimentation processes and tasks, including screenshots with values for a sample experiment called "Implement add-to-cart button for all products displayed", see [About experiments in AWS AppConfig](appconfig-experimentation-about.md). To get started with an experiment, see [Creating and running an experiment](appconfig-experimentation-creating.md).