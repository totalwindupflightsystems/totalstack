---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-creating-starting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step 3: Starting an experiment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Step 3: Starting an experiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-creating-starting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 3: Starting an experiment
<a name="appconfig-experimentation-creating-starting"></a>

Before you start an experiment, verify you completed the prerequisites. For more information, see [Step 1: Configuring prerequisites](appconfig-experimentation-creating-prerequisites.md). Before running an experiment in production, read [About running and monitoring an experiment](appconfig-experimentation-about-running-an-experiment.md) to familiarize yourself with recommended practices for safely starting and monitoring the experiment.

**To start an experiment**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose an experiment to run. The experiment definition page opens.

1. Choose **Start experiment run**.

1. (Optional) In the **Description** field, enter information about this particular experiment run.

1. For an initial experiment run, verify that **Test first at 0% exposure on start** is selected.

1. If you plan to use treatment assignment overrides, choose **Add entity ID**. For more information, see [About treatment assignment overrides](appconfig-experimentation-about-controls-and-treatments.md#appconfig-experimentation-about-treatment-overrides).

1. (Optional) Expand **Tags** to assign one or more key-value pairs to the experiment run.

1. (Optional) Expand **Deployment parameters** to assign a AWS Key Management Service (AWS KMS) key and tags to the experiment run.

1. For an initial experiment run, leave audience exposure set to 0%.

1. Choose **Start experiment run**. AWS AppConfig experimentation opens the dashboard for the running experiment.

At 0% exposure, no audience traffic is assigned to treatments unless overrides are configured. Use this stage to validate feature flags, treatment logic, metrics, and logging before increasing exposure. For more information, see [Operational considerations](appconfig-experimentation-about-running-an-experiment.md#appconfig-experimentation-about-running-an-experiment-operational-considerations).