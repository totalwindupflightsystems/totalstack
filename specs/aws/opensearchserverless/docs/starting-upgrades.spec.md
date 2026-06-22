---
id: "@specs/aws/opensearchserverless/docs/starting-upgrades"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Upgrading a domain (console)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Upgrading a domain (console)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/starting-upgrades
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Upgrading a domain (console)
<a name="starting-upgrades"></a>

The upgrade process is irreversible and can't be paused or cancelled. During an upgrade, you can't make configuration changes to the domain. Before starting an upgrade, double-check that you want to proceed. You can use these same steps to perform the pre-upgrade check without actually starting an upgrade.

If the cluster has dedicated master nodes, OpenSearch upgrades complete without downtime. However, a brief sub-second interruption (approximately 300ms) may occur during master node re-election. Otherwise, the cluster might be unresponsive for several seconds post-upgrade while it elects a master node.

**To upgrade a domain to a later version of OpenSearch or Elasticsearch**

1. [Take a manual snapshot](managedomains-snapshots.md) of your domain. This snapshot serves as a backup that you can [restore on a new domain](managedomains-snapshot-restore.md) if you want to return to using the prior OpenSearch version.

1. Go to [https://aws.amazon.com](https://console.aws.amazon.com/) and choose **Sign In to the Console**.

1. Under **Analytics**, choose **Amazon OpenSearch Service**.

1. In the navigation pane, under **Domains**, choose the domain that you want to upgrade.

1. Choose **Actions** and **Upgrade**.

1. Select the version to upgrade to. If you're upgrading to an OpenSearch version, the **Enable compatibility mode** option appears. If you enable this setting, OpenSearch reports its version as 7.10 to allow Elasticsearch OSS clients and plugins like Logstash to continue working with Amazon OpenSearch Service. You can disable this setting later

1. Choose **Upgrade**.

1. Check the **Status** on the domain dashboard to monitor the status of the upgrade.