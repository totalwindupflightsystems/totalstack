---
id: "@specs/aws/opensearchserverless/docs/restart-dashboards"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Restarting the Dashboards process"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Restarting the Dashboards process

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/restart-dashboards
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Restarting the OpenSearch Dashboards process on a node in Amazon OpenSearch Service
<a name="restart-dashboards"></a>

You can restart the OpenSearch Dashboards (previously Kibana) process to recover from issues such as a frozen interface, loading failures, or unresponsive visualizations. The option to restart OpenSearch Dashboards is only available for the node that is actively running the Dashboards process. In most OpenSearch Service domains, this process runs on dedicated coordinator nodes, not data nodes. As a result, when you open the **Actions** dropdown in the console, the option typically appears only for coordinator nodes. For more information, see [Dedicated coordinator nodes in Amazon OpenSearch Service](Dedicated-coordinator-nodes.md).

This behavior depends on how your domain is configured.
+ **Domains with dedicated coordinator nodes** – The Dashboards process runs exclusively on those nodes, and only they show the restart option.
+ **Domains without dedicated coordinator nodes** – In simpler or older setups, Dashboards might run on a data node instead, and the restart option appears there.
+ **Master nodes** – These nodes are solely for managing cluster state and elections. They don't run Dashboards and never show the restart option.

To determine which node is running the Dashboards process, navigate to the **Cluster configuration** section of your domain and review the node roles. The option to restart is only available for the node hosting the Dashboards process.

**To restart the Dashboards process on a node**

1. Navigate to the OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Domains**. Choose the name of the domain that you want to work with.

1. After the domain details page opens, navigate to the **Instance health** tab.

1. In the section for the nodes that are running the Dashboards process, select the button next to the node that you want to restart the process on.

1. Select the **Actions** dropdown and choose **Restart Dashboard/Kibana process**.

1. Choose **Confirm** on the modal.

1. To see the status of the action that you initiated, select the name of the node. After the node details page opens, choose the **Events** tab under the name of the node to see a list of events associated with that node.