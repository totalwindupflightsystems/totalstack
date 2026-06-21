---
id: "@specs/aws/lightsail/docs/amazon-lightsail-deleting-your-database"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete a database"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Delete a database

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-deleting-your-database
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete a Lightsail database and create a final snapshot
<a name="amazon-lightsail-deleting-your-database"></a>

Delete your managed database in Amazon Lightsail if you no longer need it. You stop incurring charges for the database as soon as it’s deleted.

**Note**  
You can’t recover a deleted database. You can create a final snapshot of your database as part of the steps covered in this guide, or you can create a snapshot separately from the deletion process. For more information, see [Create a snapshot of your database](amazon-lightsail-creating-a-database-snapshot.md).

**To delete your database**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Databases**.

1. Choose the name of the database that you want to delete.

1. Choose the **Delete** tab.

1. Add a check mark next to **Create snapshot before deletion** to create a final snapshot before deleting the database. Then enter a name for your snapshot.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose **Delete database**.

1. Choose **Yes, delete** to confirm the deletion.  
![Creating a database snapshot before deleting a database](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-delete-database-with-snapshot.png)

   If you opted to create a snapshot before deleting, you can view it on the **Snapshots** section of the Lightsail home page.