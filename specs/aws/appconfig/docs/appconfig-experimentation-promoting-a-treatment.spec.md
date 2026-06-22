---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-promoting-a-treatment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Promoting a winning treatment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Promoting a winning treatment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-promoting-a-treatment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Promoting a winning treatment
<a name="appconfig-experimentation-promoting-a-treatment"></a>

After you identify a winning treatment, you can promote it to all users by updating and deploying the feature flag configuration. The order in which you perform these steps determines whether your users experience a seamless transition.

**Promoting with a seamless transition**

To ensure a seamless transition from your current traffic split to full treatment rollout, update and deploy the feature flag configuration while the experiment is still running:

1. Update the feature flag values in the configuration profile to match the winning treatment.

1. Deploy the updated configuration using a standard AWS AppConfig deployment strategy. While the experiment is active, this deployment does not change what users see because the experiment is still controlling the flag.

1. Stop the experiment run. AWS AppConfig stops managing the flag, and your application begins serving the configuration you deployed in step 2 – the winning treatment – to all users.

This approach provides a seamless transition from your split traffic state (for example, 50/50) to full treatment release (100%) without any users reverting to the default experience.

**Promoting after stopping the experiment**

If you stop the experiment before updating the flag, AWS AppConfig stops managing the flag and your application immediately serves whatever version of the flag is currently deployed – typically the default value. Users see the default experience until you update and redeploy the flag with the winning treatment values. This approach does not provide a seamless transition.

For more information about deploying configurations, see [Deploying a configuration](appconfig-deploying.md).