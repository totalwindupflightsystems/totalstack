---
id: "@specs/aws/lightsail/docs/amazon-lightsail-configuring-database-public-mode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Public mode"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Public mode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-configuring-database-public-mode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure public access for your Lightsail database
<a name="amazon-lightsail-configuring-database-public-mode"></a>

Your managed database in Amazon Lightsail is accessible only by your Lightsail resources (instances, load balancers, etc.) that are in the same Lightsail account. One common scenario is to create both a Lightsail instance with a public-facing web application and a Lightsail database that is not publicly accessible, and then connect the two.

Enable the public mode feature to make your database publicly accessible. This way, anyone with the database endpoint, port, user name, and password can connect to your database. For more information, see [Connect to your MySQL database](amazon-lightsail-connecting-to-your-mysql-database.md) or [Connect to your PostgreSQL database](amazon-lightsail-connecting-to-your-postgres-database.md).

**To configure the public mode for your database**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Databases**.

1. Choose the name of the database for which you want to configure public mode.

1. Choose the **Networking** tab.

1. Under the **Public mode** section, use the toggle to turn it on. Likewise, use the toggle to turn it off.  
![The database public mode toggle in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-database-public-mode-toggle.png)

   The public accessibility setting begins applying immediately but may require a few minutes to complete. During this time, the status of your database changes to **Modifying**. The status of your database changes to **Available** after the public accessibility setting is applied.

## Next steps
<a name="configuring-database-public-mode-next-steps"></a>

Here are a few guides to help you manage your database:
+ [Configure the data import mode for your database](amazon-lightsail-configuring-database-data-import-mode.md)
+ [Manage your database password](amazon-lightsail-managing-database-password.md)
+ [Connect to your MySQL database](amazon-lightsail-connecting-to-your-mysql-database.md)
+ [Connect to your PostgreSQL database](amazon-lightsail-connecting-to-your-postgres-database.md)
+ [Import data into your MySQL database](amazon-lightsail-importing-data-into-your-mysql-database.md)
+ [Import data into your PostgreSQL database](amazon-lightsail-importing-data-into-your-postgres-database.md)
+ [Create a snapshot of your database](amazon-lightsail-creating-a-database-snapshot.md)