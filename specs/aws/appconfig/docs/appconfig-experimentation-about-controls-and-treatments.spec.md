---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-about-controls-and-treatments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS About controls and treatments"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# About controls and treatments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-about-controls-and-treatments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# About controls and treatments
<a name="appconfig-experimentation-about-controls-and-treatments"></a>

In AWS AppConfig experimentation:
+ The control treatment represents a stable, well-understood configuration or experience used as the baseline for comparison. This is often the current default behavior, but it can be any known-good state.
+ A treatment represents a variation being evaluated against the control.

Each treatment corresponds to a feature flag configuration or value that your application uses to determine the experience shown to users. Experiment results are evaluated by comparing treatment performance against the control. Treatments can represent:
+ UI changes
+ Feature configurations
+ Recommendation algorithms
+ Application behavior
+ Operational settings

Each treatment should represent a clear and measurable variation from the control.

When you define treatments in AWS AppConfig, provide clear descriptions for controls and treatments. Good descriptions help teams understand experiment intent and results. Descriptions should explain:
+ What changed
+ What users will experience
+ What behavior or outcome is being evaluated

Add screenshots when possible to document the user experience associated with each treatment. Screenshots can help:
+ Validate implementation
+ Clarify visual differences
+ Improve collaboration between teams
+ Simplify experiment review

Screenshots are especially useful for UI experiments.

**Designing effective treatments**

Keep treatments focused and measurable. Change one major variable at a time, and avoid combining unrelated changes into a single treatment. For example, implementing an add-to-cart button beneath all displayed items is a good treatment option. Implementing the add-to-cart button while also changing the page layout and recommendation logic at the same time would return uncertain data. Smaller changes make results easier to interpret.

**Important**  
Don't modify treatment behavior during a run. Changing treatment behavior mid-run can invalidate experiment data and make results difficult to interpret. If you need to make changes:  
Stop the run
Modify the treatment
Start a new experiment run
Use meaningful names that clearly identify the purpose of the new or revised treatment

Ensure that users receive the same treatment assignment throughout an experiment run. Inconsistent assignment can affect both user experience and experiment validity.

## About treatment assignment overrides
<a name="appconfig-experimentation-about-treatment-overrides"></a>

Treatment assignment overrides allow you to assign specific entity IDs to a treatment directly. Overrides bypass random treatment assignment and ensure that selected entities consistently receive the specified treatment. Overrides are commonly used to test treatments before exposing them to your audience. By assigning overrides and setting 0% exposure, you can:
+ Validate that treatments render correctly
+ Verify that metrics and logging work as expected
+ Confirm that feature flag evaluation behaves correctly

Overrides also allow you to preview treatments for stakeholders without affecting the broader audience. You can assign entity IDs to any treatment, including the control, which is useful for verifying that control users receive the expected baseline experience.

Overrides are useful for:
+ Product reviews
+ Design validation
+ Executive demonstrations
+ QA verification
+ Testing specific scenarios

This is one of the safest ways to test an experiment before increasing exposure.

Overrides are configured using entity IDs. An entity ID uniquely identifies the user or system being evaluated during feature flag assignment. An entity ID can be any of the following:
+ User IDs
+ Session IDs
+ Device IDs
+ Account identifiers

**Note**  
Overrides are intended for testing and validation, not long-term audience segmentation. Remove overrides when they are no longer needed, and use audience rules for production targeting logic.

You can add, modify, or remove treatment assignment overrides after an experiment run has started. This allows you to expand testing or grant additional stakeholders access to treatment previews without stopping the run.