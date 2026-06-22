---
id: "@specs/aws/opensearchserverless/docs/managedomains-snapshot-restore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Restoring data from snapshots"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Restoring data from snapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/managedomains-snapshot-restore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Restoring data from snapshots
<a name="managedomains-snapshot-restore"></a>

Before you restore a snapshot, note that restoring to a domain with [Multi-AZ with Standby](managedomains-multiaz.md#managedomains-za-standby) requires that restored indices have replica settings compatible with the standby configuration. If the snapshot contains indices with incompatible replica counts, the restore will fail unless you override the settings during restore. To avoid failures, ensure that the replica count for restored indices is compatible with your domain's standby configuration, or use the `index_settings` parameter to override replica settings during the restore operation.

**Warning**  
If you use index aliases, you should either cease write requests to an alias or switch the alias to another index prior to deleting its index. Halting write requests helps avoid the following scenario:  
You delete an index, which also deletes its alias.
An errant write request to the now-deleted alias creates a new index with the same name as the alias.
You can no longer use the alias due to a naming conflict with the new index. If you switched the alias to another index, specify `"include_aliases": false` when you restore from a snapshot.

To restore a snapshot

1. Identify the snapshot you want to restore. Ensure that all settings for this index, such as custom analyzer packages or allocation requirement settings, are compatible with the domain. To see all snapshot repositories, run the following command:

   ```
   curl -XGET '{{domain-endpoint}}/_snapshot?pretty'
   ```

   After you identify the repository, run the following command to see all snapshots:

   ```
   curl -XGET '{{domain-endpoint}}/_snapshot/{{repository-name}}/_all?pretty'
   ```
**Note**  
Most automated snapshots are stored in the `cs-automated` repository. If your domain encrypts data at rest, they're stored in the `cs-automated-enc` repository. If you don't see the manual snapshot repository you're looking for, make sure you [registered it](managedomains-snapshot-registerdirectory.md) to the domain.

1. (Optional) Delete or rename one or more indexes in the OpenSearch Service domain if you have naming conflicts between indexes on the cluster and indexes in the snapshot. You can't restore a snapshot of your indexes to an OpenSearch cluster that already contains indexes with the same names.

   You have the following options if you have index naming conflicts:
   + Delete the indexes on the existing OpenSearch Service domain and then restore the snapshot.
   + Rename the indexes as you restore them from the snapshot and reindex them later. To learn how to rename indexes, see [this example request](https://opensearch.org/docs/latest/api-reference/snapshots/restore-snapshot/#example-request) in the OpenSearch documentation.
   + Restore the snapshot to a different OpenSearch Service domain (only possible with manual snapshots).

   The following command deletes all existing indexes in a domain:

   ```
   curl -XDELETE '{{domain-endpoint}}/_all'
   ```

   However, if you don't plan to restore all indexes, you can just delete one:

   ```
   curl -XDELETE '{{domain-endpoint}}/{{index-name}}'
   ```

1. To restore a snapshot, run the following command:

   ```
   curl -XPOST '{{domain-endpoint}}/_snapshot/{{repository-name}}/{{snapshot-name}}/_restore'
   ```

   Due to special permissions on the OpenSearch Dashboards and fine-grained access control indexes, attempts to restore all indexes might fail, especially if you try to restore from an automated snapshot. The following example restores just one index, `my-index`, from `2020-snapshot` in the `cs-automated` snapshot repository:

   ```
   curl -XPOST '{{domain-endpoint}}/_snapshot/cs-automated/2020-snapshot/_restore' \
   -d '{"indices": "my-index"}' \
   -H 'Content-Type: application/json'
   ```

   Alternately, you might want to restore all indexes *except* the Dashboards and fine-grained access control indexes:

   ```
   curl -XPOST '{{domain-endpoint}}/_snapshot/cs-automated/2020-snapshot/_restore' \
   -d '{"indices": "-.kibana*,-.opendistro*"}' \
   -H 'Content-Type: application/json'
   ```
**Note**  
Depending on your OpenSearch version, additional system indexes may also need to be excluded, such as `-.opensearch-observability*` and `-.plugins-ml-config*`. The restore operation may fail if these indexes already exist on the target domain. To exclude them, add them to the `indices` exclusion list. For example: `"indices": "-.kibana*,-.opendistro*,-.opensearch-observability*,-.plugins-ml-config*"`.

   You can restore a snapshot without deleting its data by using the `rename_pattern` and `rename_replacement` parameters. For more information on these parameters, see the Restore Snapshot API [request fields](https://opensearch.org/docs/latest/api-reference/snapshots/restore-snapshot/#request-fields) and [example request](https://opensearch.org/docs/latest/api-reference/snapshots/restore-snapshot/#example-request) in the OpenSearch documentation.

**Note**  
If not all primary shards were available for the indexes involved, a snapshot might have a `state` of `PARTIAL`. This value indicates that data from at least one shard wasn't stored successfully. You can still restore from a partial snapshot, but you might need to use older snapshots to restore any missing indexes.