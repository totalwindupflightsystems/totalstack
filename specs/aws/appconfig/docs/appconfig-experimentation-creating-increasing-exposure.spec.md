---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-creating-increasing-exposure"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Step 4: Increasing exposure"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Step 4: Increasing exposure

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-creating-increasing-exposure
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 4: Increasing exposure
<a name="appconfig-experimentation-creating-increasing-exposure"></a>

After validating the experiment at 0% exposure, gradually increase audience exposure while monitoring both experiment metrics and operational health. As exposure increases, verify that treatments continue to behave as expected under production traffic and monitor metrics such as latency, error rates, resource utilization, conversion rates, and user engagement. Increase exposure incrementally to reduce operational risk and allow time to detect unexpected behavior, invalid experiment data, or performance regressions before they affect a larger portion of your audience. Monitor alarms configured in CloudWatch or your preferred monitoring tools throughout the run and be prepared to stop the run if operational or business metrics exceed acceptable thresholds.

**Important**  
If you detect operational issues, invalid experiment behavior, or unexpected treatment performance as you increase exposure, stop the experiment run to prevent additional users from being exposed to treatments. Stopping the run ends audience exposure and returns users to the currently deployed feature flag configuration. For more information, see [Stopping an experiment](appconfig-experimentation-stopping-an-experiment.md).

**To increase exposure**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose a running experiment. The experiment dashboard opens.

1. In the **Audience exposure** section, choose **Increase exposure**.

1. On the **Increase exposure** page, set the new exposure percentage by using the exposure dial or entering a value in the **Increase exposure to** field.

1. Review the exposure change summary. The page displays the percentage of traffic that will be served treatments and the percentage that will receive the default experience.
**Important**  
Once audience exposure is increased, it cannot be decreased within the same experiment run. To reduce exposure, you must stop the experiment run and start a new run at a lower percentage.

1. In the **Confirmation** section, type **confirm**.

1. (Optional) Expand **Deployment parameters** to assign a AWS Key Management Service (AWS KMS) key and tags to the experiment run.

1. Choose **Increase exposure**. AWS AppConfig experimentation opens the experiment dashboard with the increased exposure displayed.

Monitor traffic and metrics as described earlier. When you're ready, repeat this procedure to increase audience exposure further.