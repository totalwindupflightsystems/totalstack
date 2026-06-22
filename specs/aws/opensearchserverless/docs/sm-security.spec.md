---
id: "@specs/aws/opensearchserverless/docs/sm-security"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure permissions"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configure permissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/sm-security
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure permissions
<a name="sm-security"></a>

If you're upgrading to 2.5 from a previous OpenSearch Service domain version, the snapshot management security permissions might not be defined on the domain. Non-admin users must be mapped to this role in order to use snapshot management on domains using fine-grained access control. To manually create the snapshot management role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Permissions**.

1. Choose **Create action group** and configure the following groups:     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/sm-security.html)

1. Choose **Roles** and **Create role**.

1. Name the role **snapshot\_management\_role**.

1. For **Cluster permissions**, select `snapshot_management_full_access` or `snapshot_management_read_access`.

1. Choose **Create**.

1. After you create the role, [map it](fgac.md#fgac-mapping) to any user or backend role that will manage snapshots.