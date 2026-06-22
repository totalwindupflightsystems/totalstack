---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-defining"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Documenting your hypothesis"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Documenting your hypothesis

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-defining
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Documenting your hypothesis
<a name="appconfig-experimentation-about-defining"></a>

When you create a new experiment, you specify a name for it and define the goals on the **Document your hypothesis** page in AWS AppConfig experimentation. Enter a name that identifies the experiment goal, for example *Increase add-to-cart rate by adding a button for each product displayed*. If you're creating multiple versions of the same experiment, specify version numbers in the name, for example *V2-Increase add-to-cart rate by adding a button for each product displayed*.

In the **Experiment hypothesis** text box, define the outcome you're trying to achieve and other details so that other users can quickly understand the experiment goals. Focus on a measurable customer or business impact. Here's an example:
+ Goal: Increase add-to-cart rate by adding a button for each product displayed
+ Hypothesis: Implementing 'Add-to-cart' buttons beneath every product displayed on the page will improve clicks
+ Primary metric: Add-to-cart rate
+ Guardrail metrics: Page load time, checkout completion rate

After naming and defining the experiment hypothesis, select the application where you want to run the experiment. An application in AWS AppConfig is simply an organizational construct like a folder that identifies the namespace of your application. 