---
id: "@specs/aws/lightsail/docs/amazon-lightsail-managing-database-password"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Manage database password"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Manage database password

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-managing-database-password
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Change your Lightsail database password
<a name="amazon-lightsail-managing-database-password"></a>

When you create a new database in Amazon Lightsail, you can let Lightsail create a strong password for you or specify your own. You can view or change the current database password at any time in the Lightsail console.

**To manage your database password**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Databases**.

1. Choose the name of the database for which you want to manage the password.

1. On the **Connect** tab, under the **User name and passwords** section, choose **Show** to view the current database password.  
![Show database password](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-database-show-password.png)

1. To change the database password, choose **Change password**.

   You can opt to have Lightsail create a strong password for you, or you can enter your own password into the text box. The password can include any printable ASCII character except "/", """, or "@". For MySQL databases, the password must contain from 8 to 41 characters. For PostgreSQL, the password must contain from 8 to 128 characters.  
![Changing your database password](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-database-change-password.png)

1. Choose **Save** when you’re done.

   A database password change is applied immediately. If you entered your own password, the password is saved immediately. If Lightsail created the password for you, it is generated within a few seconds. Choose **Show** to view the new password.

## Next steps
<a name="managing-database-password-next-steps"></a>

Here are a few guides to help you manage your database in Lightsail:
+ [Connect to your MySQL database](amazon-lightsail-connecting-to-your-mysql-database.md)
+ [Connect to your PostgreSQL database](amazon-lightsail-connecting-to-your-postgres-database.md)
+ [Create a snapshot of your database](amazon-lightsail-creating-a-database-snapshot.md)