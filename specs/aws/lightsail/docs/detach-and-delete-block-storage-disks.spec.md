---
id: "@specs/aws/lightsail/docs/detach-and-delete-block-storage-disks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Detach and delete disks"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Detach and delete disks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/detach-and-delete-block-storage-disks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Detach and delete Lightsail block storage disks
<a name="detach-and-delete-block-storage-disks"></a>

If you no longer need a block storage disk, you can detach it from your stopped Amazon Lightsail instance, and then delete it. This topic describes how to back up your data and safely delete a disk.

## Prerequisites
<a name="delete-block-storage-disk-prerequisites"></a>
+ Stop your instance from running. You have to do this before you can detach and then delete your disk. [Learn how to stop your instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md)
+ (Optional) We recommend that you create a snapshot of your disk. That way, you have a backup in case you change your mind. For more information, see [Create a snapshot of your database](create-block-storage-disk-snapshot.md)

## Detach and delete your disk
<a name="delete-block-storage-disk-detach-and-delete"></a>

Once you stop your Lightsail instance, you can safely detach and delete your disk.

1. On the home page, choose **Storage**.

1. Choose the name of your attached disk to manage it.  
![Example of a block storage disk that is still attached to a Lightsail instance](http://docs.aws.amazon.com/lightsail/latest/userguide/images/example-disk-still-attached-home-page-storage-tab.png)

   

1. On the disk management page, choose **Detach**.

   After a few seconds, the disk is detached and ready to be deleted or reattached.

1. Choose the **Delete** tab.

1. Choose **Delete disk**, and then confirm by choosing **Yes, delete**.
**Important**  
This is a permanent operation and can't be undone. You will lose all data on the disk when you delete it.