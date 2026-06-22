---
id: "@specs/aws/kafka/docs/migration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Migrate to MSK cluster"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Migrate to MSK cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/migration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Migrate Kafka workloads to an Amazon MSK cluster
<a name="migration"></a>

Amazon MSK Replicator supports replication between Amazon MSK clusters in the same AWS account. It also supports migrations between non-MSK Apache Kafka clusters and Amazon MSK clusters. For cross-account replication between Amazon MSK clusters, you must use Apache MirrorMaker 2.0.

[MSK Replicator](msk-replicator.md) is a fully managed, serverless solution that automates data migration to Amazon MSK. MSK Replicator handles scaling, monitoring, and maintenance tasks without requiring infrastructure management. It also maintains topic configurations and consumer group offsets during migration, and integrates with other AWS services.

[Apache MirrorMaker 2.0](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330) is an open-source tool that requires manual setup and management, but provides detailed control over the migration process. You can define custom replication rules and migrate between any Apache Kafka clusters regardless of the hosting platform or across different AWS accounts. For information about using MirrorMaker to migrate your clusters, see [Geo-Replication (Cross-Cluster Data Mirroring)](https://kafka.apache.org/40/documentation.html#georeplication). We recommend setting up MirrorMaker in a highly available configuration.

For more information about migrating to Amazon MSK with MSK Replicator, see [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/).