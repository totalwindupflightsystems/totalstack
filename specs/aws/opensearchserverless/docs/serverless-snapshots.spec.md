---
id: "@specs/aws/opensearchserverless/docs/serverless-snapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Backing up collections using snapshots"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Backing up collections using snapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-snapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Backing up collections using snapshots
<a name="serverless-snapshots"></a>

Snapshots are point-in-time backups of your Amazon OpenSearch Serverless collections that provide disaster recovery capabilities. OpenSearch Serverless automatically creates and manages snapshots of your collections, ensuring business continuity and data protection. Each snapshot contains index metadata (settings and mappings for your indexes), cluster metadata (index templates and aliases), and index data (all documents and data stored in your indexes).

OpenSearch Serverless provides automatic hourly backups with no manual configuration, zero maintenance overhead, no additional storage costs, quick recovery from accidental data loss, and the ability to restore specific indexes from a snapshot.

Before working with snapshots, understand these important considerations. Creating a snapshot takes time to complete and isn't instantaneous. New documents or updates during snapshot creation will not be included in the snapshot. You can restore snapshots only to their original collection and not to a new one. When restored, indexes receive new UUIDs that differ from their original versions. Restoring to an existing open index in OpenSearch Serverless will overwrite the data of that index provided a new index name or a prefix pattern is not provided.This differs from OpenSearch core behavior. You can run only one restore operation at a time, and you can't start multiple restore operations on the same collection simultaneously. Attempting to restore indexes during an active restore operation causes the operation to fail. During a restore operation, your requests to the indexes fail.

## Required permissions
<a name="serverless-snapshots-permissions"></a>

To work with snapshots, configure the following permissions in your data access policy. For more information about data access policies, see [Data access policies versus IAM policies](serverless-data-access.md#serverless-data-access-vs-iam).


****  

| Data Access Policy | APIs | 
| --- | --- | 
| aoss:DescribeSnapshot | GET /\_cat/snapshots/aoss-automated<br />GET \_snapshot/aoss-automated/{{snapshot\_id}}/ | 
| aoss:RestoreSnapshot | POST /\_snapshot/aoss-automated/{{snapshot\_id}}/\_restore | 
| aoss:DescribeCollectionItems | GET /\_cat/recovery | 

**Note**  
Replace `<snapshot_id>` with the actual snapshot ID retrieved from `GET /_cat/snapshots/aoss-automated`.

You can configure policies using the following AWS CLI commands:

1.  [ create-access-policy](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/create-access-policy.html) 

1.  [ delete-access-policy ](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/delete-access-policy.html) 

1. [ get-access-policy ](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/get-access-policy.html)

1. [ update-access-policy ](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/update-access-policy.html)

1. [ list-access-policies ](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/list-access-policies.html)

Here is a sample CLI command for creating an access policy. In the command, replace the {{example}} content with your specific information.

```
aws opensearchserverless create-access-policy \
--type data \
--name {{Example-data-access-policy}} \
--region {{aws-region}} \
--policy '[
  {
    "Rules": [
      {
        "Resource": [
          "collection/{{Example-collection}}"
        ],
        "Permission": [
          "aoss:DescribeSnapshot",
          "aoss:RestoreSnapshot",
          "aoss:DescribeCollectionItems"
        ],
        "ResourceType": "collection"
      }
    ],
    "Principal": [
      "arn:aws:iam::{{111122223333}}:user/{{UserName}}"
    ],
    "Description": "{{Data policy to support snapshot operations.}}"
  }
]'
```

## Working with snapshots
<a name="serverless-snapshots-working-with"></a>

By default, when you create a new collection, OpenSearch Serverless automatically creates snapshots every hour. You don't need to take any action. Each snapshot includes all indexes in the collection. After OpenSearch Serverless creates snapshots, you can list them and review the details of the snapshot using the following procedures.

### List snapshots
<a name="serverless-snapshots-listing"></a>

Use the following procedures to list all snapshots in a collection and review their details.

------
#### [ Console ]

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Serverless**, then choose **Collections**.

1. Choose the name of your collection to open its details page.

1. Choose the **Snapshots** tab to display all generated snapshots.

1. Review the snapshot information including:
   + **Snapshot ID** - Unique identifier for the snapshot
   + **Status** - Current state (Available, In Progress)
   + **Created time** - When the snapshot was taken

------
#### [ OpenSearch API ]
+ Use the following command to list all snapshots in a collection:

  ```
  GET /_cat/snapshots/aoss-automated
  ```
**Note**  
Do not include a trailing slash in this API call. Using `GET /_cat/snapshots/aoss-automated/` (with trailing slash) will return a 404 error.

  ```
  id                                 status  start_epoch start_time end_epoch  end_time    duration    indexes successful_shards failed_shards total_shards
  snapshot-ExampleSnapshotID1     SUCCESS 1737964331  07:52:11   1737964382 07:53:02    50.4s       1                                             
  snapshot-ExampleSnapshotID2     SUCCESS 1737967931  08:52:11   1737967979 08:52:59    47.7s       2                                             
  snapshot-ExampleSnapshotID3     SUCCESS 1737971531  09:52:11   1737971581 09:53:01    49.1s       3                                             
  snapshot-ExampleSnapshotID4 IN_PROGRESS 1737975131  10:52:11   -          -            4.8d       3
  ```

------

### Get snapshot details
<a name="serverless-snapshots-get-details"></a>

Use the following procedures to retrieve detailed information about a specific snapshot.

------
#### [ Console ]

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Serverless**, then choose **Collections**.

1. Choose the name of your collection to open its details page.

1. Choose the **Snapshots** tab.

1. Choose the snapshot job ID to display detailed information about the snapshot, including metadata, indexes included, and timing information.

------
#### [ OpenSearch API ]
+ Use the following command to retrieve information about a snapshot. In the command, replace the {{example}} content with your specific information.

  ```
  GET _snapshot/aoss-automated/{{snapshot_id}}/
  ```
**Note**  
Replace `<snapshot_id>` with the actual snapshot ID retrieved from `GET /_cat/snapshots/aoss-automated`.

  Example Request:

  ```
  GET _snapshot/aoss-automated/{{snapshot-ExampleSnapshotID1}}/
  ```

  Example Response:

  ```
  {
      "snapshots": [
          {
              "snapshot": "{{snapshot-ExampleSnapshotID1-5e01-4423-9833Example}}",
              "uuid": "{{Example-5e01-4423-9833-9e9eb757Example}}",
              "version_id": 136327827,
              "version": "2.11.0",
              "remote_store_index_shallow_copy": true,
              "indexes": [
                  "{{Example-index-0117}}"
              ],
              "data_streams": [],
              "include_global_state": true,
              "metadata": {},
              "state": "SUCCESS",
              "start_time": "2025-01-27T09:52:11.953Z",
              "start_time_in_millis": 1737971531953,
              "end_time": "2025-01-27T09:53:01.062Z",
              "end_time_in_millis": 1737971581062,
              "duration_in_millis": 49109,
              "failures": [],
              "shards": {
                  "total": 0,
                  "failed": 0,
                  "successful": 0
              }
          }
      ]
  }
  ```

------

The snapshot response includes several key fields: `id` provides a unique identifier for the snapshot operation, `status` returns the current state `SUCCESS` or `IN_PROGRESS`, `duration` indicates the time taken to complete the snapshot operation, and `indexes` returns the number of indexes included in the snapshot.

## Restoring from a snapshot
<a name="serverless-snapshots-restoring"></a>

Restoring from a snapshot recovers data from a previously taken backup. This process is crucial for disaster recovery and data management in OpenSearch Serverless. Before restoring, understand that restored indexes will have different UUIDs than their original versions, restoring to an existing open index in OpenSearch Serverless will overwrite the data of that index provided a new index name or a prefix pattern is not provided, snapshots can only be restored to their original collection (cross-collection restoration is not supported), and restore operations will impact cluster performance so plan accordingly.

Use the following procedures to restore backed up indexes from a snapshot.

------
#### [ Console ]

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Serverless**, then choose **Collections**.

1. Choose the name of your collection to open its details page.

1. Choose the **Snapshots** tab to display available snapshots.

1. Choose the snapshot you want to restore from, then choose **Restore from snapshot**.

1. In the **Restore from snapshot** dialog:
   + For **Snapshot name**, verify the selected snapshot ID.
   + For **Snapshot scope**, choose either:
     + **All indexes in collection** - Restore all indexes from the snapshot
     + **Specific indexes** - Select individual indexes to restore
   + For **Destination**, choose the collection to restore to.
   + (Optional) Configure **Rename settings** to rename restored indexes:
     + **Do not rename** - Keep original index names
     + **Add prefix to restored index names** - Add a prefix to avoid conflicts
     + **Rename using regular expression** - Use advanced renaming patterns
   + (Optional) Configure **Notification** settings to be notified when the restore completes or encounters errors.

1. Choose **Save** to start the restore operation.

------
#### [ OpenSearch API ]

1. Run the following command to identify the appropriate snapshot.

   ```
   GET /_snapshot/aoss-automated/_all
   ```

   For a smaller list of snapshots, run the following command.

   ```
   GET /_cat/snapshots/aoss-automated
   ```

1. Run the following command to verify the details of the snapshot before restoring. In the command, replace the {{example}} content with your specific information.

   ```
   GET _snapshot/aoss-automated/{{snapshot-ExampleSnapshotID1}}/
   ```

1. Run the following command to restore from a specific snapshot.

   ```
   POST /_snapshot/aoss-automated/{{snapshot-ID}}/_restore
   ```

   You can customize the restore operation by including a request body. Here's an example.

   ```
   POST /_snapshot/aoss-automated/{{snapshot-ExampleSnapshotID1-5e01-4423-9833Example}}/_restore
   {
     "indices": "opensearch-dashboards*,my-index*",
     "ignore_unavailable": true,
     "include_global_state": false,
     "include_aliases": false,
     "rename_pattern": "opensearch-dashboards(.+)",
     "rename_replacement": "restored-opensearch-dashboards$1"
   }
   ```

1. Run the following command to view the restore progress.

   ```
   GET /_cat/recovery
   ```

------

**Note**  
When restoring a snapshot with a command that includes a request body, you can use several parameters to control the restore behavior. The `indices` parameter specifies which indices to restore and supports wildcard patterns. Set `ignore_unavailable` to continue the restore operation even if an index in the snapshot is missing. Use `include_global_state` to determine whether to restore the cluster state, and `include_aliases` to control whether to restore associated aliases. The `rename_pattern` and `rename_replacement` parameters rename indexes during the restore operation.