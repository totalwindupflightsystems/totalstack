---
id: "@specs/aws/opensearchserverless/docs/restart-node"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Rebooting a data node"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Rebooting a data node

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/restart-node
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Rebooting a data node in Amazon OpenSearch Service
<a name="restart-node"></a>

**To reboot a data node**

1. Navigate to the OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Domains**. Choose the name of the domain that you want to work with.

1. After the domain details page opens, navigate to the **Instance health** tab.

1. Under **Data nodes**, select the button next to the node that you want to restart the process on. 

1. Select the **Actions** dropdown and choose **Reboot node**.

1. Choose **Confirm** on the modal.

1. To see the status of the action that you initiated, select the name of the node. After the node details page opens, choose the **Events** tab under the name of the node to see a list of events associated with that node.