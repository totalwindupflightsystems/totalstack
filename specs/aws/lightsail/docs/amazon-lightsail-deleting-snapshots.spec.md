---
id: "@specs/aws/lightsail/docs/amazon-lightsail-deleting-snapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete snapshots"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete snapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-deleting-snapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete unused Lightsail snapshots to avoid monthly charges
<a name="amazon-lightsail-deleting-snapshots"></a>

Delete instance, database, and disk snapshots in Amazon Lightsail if you no longer need them to avoid incurring a monthly charge.

**Delete an individual snapshot**
**Important**  
This is a permanent operation and can't be undone. You will lose all data on the snapshots when you delete them.

1. On the [Lightsail console](https://lightsail.aws.amazon.com/), choose **Snapshots** tab.

1. Find the Lightsail resource whose snapshot you want to delete, and choose the right-arrow to expand the list of available snapshots for that resource.

1. Choose the actions menu icon (⋮) next to the snapshot you want to delete, and choose **Delete snapshot**.  
![Delete a snapshot in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-delete-snapshot-menu-option.png)

1. Choose **Yes** to confirm that you want to delete the snapshot.

**Delete multiple snapshots**
**Important**  
This is a permanent operation and can't be undone. You will lose all data on the snapshots when you delete them.

1. From the Lightsail home page, choose **Snapshots**.

1. Find the Lightsail resource whose snapshots you want to delete and expand the snapshots section for the resource.

1. Select the snapshots for the resource to delete, then choose **Delete**.  
![Use the shortcut menu to show your disk snapshots and delete multiple disk snapshots](http://docs.aws.amazon.com/lightsail/latest/userguide/images/delete-disk-snapshot-multiple.png)

1. Choose **Yes** to confirm that you want to delete the snapshots.