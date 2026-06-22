---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-stopping-an-experiment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Stopping an experiment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Stopping an experiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-stopping-an-experiment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Stopping an experiment
<a name="appconfig-experimentation-stopping-an-experiment"></a>

You can stop an experiment run at any time. Common reasons for stopping include:
+ **Operational issues, invalid experiment behavior, or unexpected treatment performance**: Stopping the experiment run prevents additional users from being exposed to treatments and returns users to the currently deployed feature flag configuration.
+ **A clear treatment winner**: Results consistently meet the success criteria and operational metrics remain within acceptable thresholds. Before promoting a winner, verify that the treatment performs better than the control for the intended outcome. For information about rolling out the winning treatment, see [Promoting a winning treatment](appconfig-experimentation-promoting-a-treatment.md).
+ **Inconclusive results or changing priorities**: The experiment is no longer relevant, the hypothesis needs revising, or you want to restart with a different configuration.

Use the following procedure to stop an experiment.

**To stop an experiment**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose a running experiment. The experiment dashboard opens.

1. Choose **Stop**.

1. (Optional) In the **Experiment results summary** section, document the experiment outcome to help your team make an informed launch decision. This summary is saved with the experiment run for future reference. You can provide:
   + **Executive summary** – Summarize the experiment outcome and key findings.
   + **Reasons to launch** – Evidence in favor of launching the treatment.
   + **Reasons not to launch** – Evidence against launching the treatment.

1. In the **Confirmation** section, type **confirm**, and then choose **Stop experiment run**.