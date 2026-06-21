---
id: "@specs/aws/lightsail/docs/create-block-storage-disk-snapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create block storage disk snapshots"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Create block storage disk snapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/create-block-storage-disk-snapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create Lightsail block storage disk snapshots for backup or baseline
<a name="create-block-storage-disk-snapshot"></a>

You can create disk snapshots in Amazon Lightsail as backups of your additional block storage disks.

You can use the snapshot of a disk as a baseline for new disks or for data backup. If you make periodic snapshots of a disk, the snapshots are incremental. Only the blocks on the device that have changed after your last snapshot are saved in the new snapshot. Even though snapshots are saved incrementally, the snapshot deletion process is designed so that you need to retain only the most recent snapshot to restore the entire disk.

For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).

1. In the left navigation pane, choose **Storage**.

1. Choose the name of the block storage disk for which you want to create a snapshot.

1. Choose the **Snapshots** tab.

1. Under the **Manual snapshots** section of the page, choose **Create snapshot**, then enter a name for your snapshot.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose **Create**.

   You can see the snapshot you just created with a status of **Snapshotting...**.

   After the snapshot is finished, you can [create another disk from the snapshot](create-new-block-storage-disk-from-snapshot.md).