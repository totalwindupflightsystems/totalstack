---
id: "@specs/aws/opensearchserverless/docs/snapshot-based-migration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using a snapshot to migrate data"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Using a snapshot to migrate data

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/snapshot-based-migration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using a snapshot to migrate data
<a name="snapshot-based-migration"></a>

In-place upgrades are the easier, faster, and more reliable way to upgrade a domain to a later OpenSearch or Elasticsearch version. Snapshots are a good option if you need to migrate from a pre-5.1 version of Elasticsearch or want to migrate to an entirely new cluster.

The following table shows how to use snapshots to migrate data to a domain that uses a different OpenSearch or Elasticsearch version. For more information about taking and restoring snapshots, see [Creating index snapshots in Amazon OpenSearch Service](managedomains-snapshots.md).


| From version | To version | Migration process | 
| --- | --- | --- | 
| OpenSearch 1.3 or 2.x | OpenSearch 2.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| OpenSearch 1.x | OpenSearch 1.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 6.x or 7.x | OpenSearch 1.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 6.x | Elasticsearch 7.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 6.x | Elasticsearch 6.8 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 5.x | Elasticsearch 6.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 5.x | Elasticsearch 5.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 2.3 | Elasticsearch 6.x | Elasticsearch 2.3 snapshots are not compatible with 6.*x*. To migrate your data directly from 2.3 to 6.*x*, you must manually recreate your indexes in the new domain.<br />Alternately, you can follow the 2.3 to 5.*x* steps in this table, perform `_reindex` operations in the new 5.*x* domain to convert your 2.3 indexes to 5.*x* indexes, and then follow the 5.*x* to 6.*x* steps. | 
| Elasticsearch 2.3 | Elasticsearch 5.x |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 
| Elasticsearch 1.5 | Elasticsearch 5.x | Elasticsearch 1.5 snapshots are not compatible with 5.*x*. To migrate your data from 1.5 to 5.*x*, you must manually recreate your indexes in the new domain. 1.5 snapshots *are* compatible with 2.3, but OpenSearch Service 2.3 domains do not support the `_reindex` operation. Because you cannot reindex them, indexes that originated in a 1.5 domain still fail to restore from 2.3 snapshots to 5.*x* domains.  | 
| Elasticsearch 1.5 | Elasticsearch 2.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/snapshot-based-migration.html)  | 