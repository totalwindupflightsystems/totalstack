---
id: "@specs/aws/appconfig/docs/appconfig-creating-experiment-definition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step 2: Creating an experiment definition"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Step 2: Creating an experiment definition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-experiment-definition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 2: Creating an experiment definition
<a name="appconfig-creating-experiment-definition"></a>

An experiment definition describes the purpose, scope, and operational configuration of an experiment. It captures information about what is being tested, the expected outcome, and the business or technical objective so that stakeholders can quickly understand the intent of the experiment and interpret the results consistently.

The experiment definition also includes the operational details required to run the experiment in AWS AppConfig. This includes the application and feature flag associated with the experiment, the configuration profile used to store experiment settings, and the treatment configurations that define the experiences being evaluated. The experiment definition acts as the central configuration for experiment runs, audience exposure settings, and treatment assignment logic. For more detailed information about the concepts described here, see [About experiments in AWS AppConfig](appconfig-experimentation-about.md).

**Topics**
+ [Creating an experiment definition (console)](#appconfig-creating-experiment-definition-console)

## Creating an experiment definition (console)
<a name="appconfig-creating-experiment-definition-console"></a>

Use the following procedure to create an experiment definition using AWS AppConfig experimentation in the AWS Management Console.

**To create an experiment definition**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose **Create experiment**.

1. For **Experiment Name**, enter a descriptive name to distinguish this experiment from other experiments.

1. For **Experiment hypothesis**, describe the goal or hypothesis you want to validate.

1. For **Launch criteria**, enter information about metrics or data essential to deploying a winning treatment. This information is helpful for long-running experiments.

1. For **Experiment application**, select the application where this experiment will run.

1. Choose **Next**.

1. On the **Specify target audience** page, for **Audience description**, enter information about the intended audience for the experiment.

1. In the **Audience rule** section, choose either the **Rule builder** tab or the **Editor** tab to create a rule that identifies or filters the audience. Choose **Rule blueprints** to view and select a pre-constructed rule for your experiment. When building a rule:
   + Add a condition

     Choose an attribute, select an operator, and specify a value.
   + Group conditions

     Use `AND` to require all conditions in a group to be true, or `OR` to match any condition.
   + Nest groups

     Combine multiple groups to create more advanced targeting logic.
   + Refine the rule

     Add or remove conditions and groups as needed to match your targeting requirements.

   For more information about building rules, including expression formats, supported operators, and rule examples, see [Creating audience rules](appconfig-experimentation-about-specifying-audience-rule-section.md).

1. Choose **Next**.

1. On the **Select experiment feature flag** page, for **Environment**, select the environment where this experiment will run. For **Configuration profile**, select the configuration profile associated with the feature flag.

1. For **Feature flag**, select an existing feature flag to use with the experiment. For more information about experiment feature flags, see [Selecting the experiment feature flag](appconfig-experimentation-about-experiment-feature-flag.md).

1. Choose **Next**.

1. On the **Add treatments** page, review the **Default flag value** section. When audience exposure is set between 0% and 99%, users not assigned to a treatment receive the default flag value. This value is always off and cannot be changed.

1. On the **Add treatments** page, in the **Control** section, enter a description and verify the flag value is toggled **ON**.
**Note**  
The control treatment represents the baseline experience used for comparison during the experiment. It is typically the current default behavior, but can be any stable, well-understood configuration. The *default feature flag value* (which is toggled off by default) defines the fallback behavior for users who are not assigned to a treatment. Although the control treatment and default flag value often deliver the same user experience, only users assigned to the control treatment participate in experiment measurement and analysis.

   If one or more keys are listed in the **Attribute values** section, specify their values in the corresponding **Value** field.

1. In the **Treatment 1** section, enter a description and verify the flag value is toggled **ON**. If one or more keys are listed in the **Attribute values** section, specify their values in the corresponding **Value** field. Repeat this process for any additional treatments.

1. AWS AppConfig experimentation automatically allocates traffic to all treatments based on the total number of treatments. If you want to allocate traffic to different treatments, you can expand **Advanced settings**, and choose **Use custom allocation weights** (not recommended).
**Note**  
Treatment traffic allocation determines how traffic is split among treatments. Audience exposure, which controls what percentage of the eligible audience enters the experiment, is configured separately when you start the experiment run.

1. Choose **Next**.

1. Review the details, and then choose **Save experiment definition**. AWS AppConfig displays the completed definition page for the experiment.