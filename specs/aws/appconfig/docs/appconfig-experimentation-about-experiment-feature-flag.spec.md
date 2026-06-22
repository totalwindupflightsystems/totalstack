---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-experiment-feature-flag"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Selecting the experiment feature flag"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Selecting the experiment feature flag

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-experiment-feature-flag
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Selecting the experiment feature flag
<a name="appconfig-experimentation-about-experiment-feature-flag"></a>

AWS AppConfig experiments use feature flags to deliver treatments to users. The feature flag defines the possible experiences that users can receive during an experiment run. Each treatment corresponds to a distinct feature flag configuration or variation.

During the experiment run, AWS AppConfig assigns eligible users to treatments and serves the associated feature flag values. AWS AppConfig experimentation provides the configuration interface for defining experiment parameters, audience rules, and treatment settings.

When you select the feature flag for an experiment, ensure that it includes the flag attributes and constraints needed for the experiment. An *attribute* is a field that you associate with your feature flag to control the feature behavior. Here are a few examples: `buttonColor = "green"` and `layout = "expanded"`. *Constraints* are guardrails. For example, they ensure `buttonColor` must be one of: `"blue" | "green" | "red"`.

The feature flag:
+ Defines the experiences being evaluated
+ Delivers treatments to users at runtime
+ Controls how users are exposed to each treatment
+ Enables gradual rollout of a selected treatment after the experiment

In practice, the feature flag acts as the operational mechanism behind the experiment.

Each treatment should map to a distinct feature flag configuration. For example, the experiment feature flag could include:
+ A flag value that retains the current UI experience (the control)
+ A second flag value that defines the *Implement add-to-cart button for all products displayed* experience
+ A third flag value that defines an alternative add-to-cart button experience, perhaps using a different button color or font

After you've selected the feature flag and configured different flag values for treatments, configure your application to retrieve the flag data from AWS AppConfig Agent running on your compute environment. For more information, see [Using AWS AppConfig Agent to read a specific feature flag](appconfig-code-samples-agent-read-feature-flag.md).