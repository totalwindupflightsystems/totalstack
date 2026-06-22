---
id: "@specs/aws/appconfig/docs/appconfig-experimentation-archiving-or-deleting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cleaning up an experiment"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Cleaning up an experiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-experimentation-archiving-or-deleting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cleaning up an experiment
<a name="appconfig-experimentation-archiving-or-deleting"></a>

After an experiment completes, you can archive or permanently delete the experiment definition.
+ **Archive** – The experiment definition is hidden from the active list but can be restored later. The experiment feature flag remains deployed and continues serving its current configuration. To stop serving the flag, disable it separately in your feature flag configuration.
+ **Delete permanently** – The experiment definition and all associated run history are permanently deleted. This action cannot be undone.

**To archive or delete an experiment**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose an experiment. The experiment dashboard opens.

1. Choose **Actions**, and then choose **Delete experiment definition**.

1. In the **Choose an action** section, choose either **Archive** or **Delete permanently**.

1. In the **Confirmation** section, type **confirm**.

1. Choose the **Archive** or **Delete** button.