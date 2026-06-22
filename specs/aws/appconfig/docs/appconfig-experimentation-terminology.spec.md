---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-terminology"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Experimentation terminology"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Experimentation terminology

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-terminology
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Experimentation terminology
<a name="appconfig-experimentation-terminology"></a>

Familiarize yourself with the following terminology and concepts before you begin working with AWS AppConfig experimentation.

**Experiment**  
A configured test in which a control and one or more treatments are deployed to defined targets, and their performance is measured to evaluate the impact of changes.

**Exposure**  
The event in which an assigned user actually encounters an experiment treatment or control in their application experience. The *audience exposure* setting controls the percentage of eligible users who receive this experience.

**Experiment run**  
A single execution of an experiment in which treatments are delivered to the target audience and metrics are collected. You can start multiple experiment runs from the same experiment definition. AWS AppConfig experimentation have priced calls, and you will be charged per hour per experiment run from when the experiment starts until it is ended. [Learn more about pricing](https://aws.amazon.com/systems-manager/pricing/).

**Treatments**  
The alternative configurations, features, or experiences evaluated in an experiment, each representing a distinct variation compared to a baseline (control). For example, the control could be the current version of an LLM model, or an existing add-to-cart button experience. A treatment could be a new LLM version or model, or an experience with a different color button.

**Control**  
A stable, well-understood configuration or experience against which treatments are compared. The control is often the current default behavior of the application, but it can be any known-good baseline suitable for measuring the impact of changes.

**Overrides**  
Configuration rules that supersede experiment assignments by forcing specific targets or conditions to receive a designated configuration instead of their assigned control or treatment. Overrides are often used for internal testing.

**Testing**  
The stage of an experiment in which assigned targets are exposed to a control and one or more treatments. During the test, outcome metrics need to be collected and evaluated to determine the experiment result. Note the following about the testing phase:  
+ Testing begins when traffic is first exposed to the experiment.
+ Testing ends when you stop data collection to make a decision.
+ Testing may include gradual traffic increases.
+ Test results determine whether to:
  + Promote a treatment
  + Start another experiment run
  + Abort the experiment