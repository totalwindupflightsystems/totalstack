---
id: "@specs/aws/lightsail/docs/amazon-lightsail-creating-a-database"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a database"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Create a database

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-creating-a-database
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Lightsail database
<a name="amazon-lightsail-creating-a-database"></a>

Create a managed database in Amazon Lightsail in minutes. You can choose between the latest major versions of MySQL or PostgreSQL, and configure your database with a standard or high availability plan.

**Note**  
For more information about managed databases in Lightsail, see [Choose a database](amazon-lightsail-choosing-a-database.md).

**To create a database**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Databases**.

1. Choose **Create database**.

1. Choose the AWS Region and Availability Zone for your database.

   1. Choose **Change AWS Region and Availability Zone**, then choose a Region.

   1. Choose **Change your Availability Zone**, then choose an Availability Zone.

1. Choose your database type. Under one of the database engine options available, choose the drop-down menu, and then choose one of the latest major database versions supported by Lightsail.  
![Pick a database engine in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-pick-your-database.png)

1. If necessary, choose one of these options:
   + **Specify login credentials** — Specify your own database user name and password. Otherwise, Lightsail specifies the user name, and creates a strong password for you. 
     + To specify your own user name, choose **Specify login credentials**, and enter your user name into the text box. The following constraints apply according to the database engine you select:

       **MySQL**
       + Required for MySQL.
       + Must be 1 to 16 letters or numbers.
       + First character must be a letter.
       + Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html), [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html), or [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).

       **PostgreSQL**
       + Required for PostgreSQL.
       + Must be 1 to 63 letters or numbers.
       + First character must be a letter.
       + Can't be a reserved word for the chosen database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html), [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html), [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html), or [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html).
     + To specify your own password, clear the **Create a strong password for me** check box, and enter your password into the text box. The password can include any printable ASCII character except "/", """, or "@". For MySQL databases, the password can contain from 8 to 41 characters. For PostgreSQL databases, the password can contain from 8 to 128 characters.
   + **Specify the master database name** — Specify your own primary database name, or Lightsail specifies the name for you. To specify your own primary database name, choose **Specify the master database name**, and enter a name into the text box. The following constraints apply according to the database engine you select:

     **MySQL**
     + Must contain 1 to 64 letters or numbers.
     + Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
     + Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html), [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html), or [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).

     **PostgreSQL**
     + Must contain 1 to 63 letters, numbers, or underscores.
     + Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
     + Can't be a reserved word for the chosen database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html), [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html), [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html), or [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html).

1. Choose a high availability or a standard database plan.

   A database created with a high availability plan has a primary database and a secondary standby database in another Availability Zone for failover support. For more information, see [High availability databases](amazon-lightsail-high-availability-databases.md). Differently priced database bundle options are available, each with different levels of memory, processing, storage space, and transfer rates.

1. Enter a name for your database.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose one of the following options to add tags to your database:
   + **Add key-only tags** or **Manage tags** (if tags have already been added). Enter your new tag into the tag key text box, and press **Enter**. Choose **Save** when you’re done entering your tags to add them, or choose **Cancel** to not add them.  
![Key-only tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-only-tags.png)
   + **Create a key-value tag**, then enter a key into the **Key** text box, and a value into the **Value** text box. Choose **Save** when you’re done entering your tags, or choose **Cancel** to not add them.

     Key-value tags can only be added one at a time before saving. To add more than one key-value tag, repeat the previous steps.  
![Key-value tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-value-tag.png)
**Note**  
For more information about key-only and key-value tags, see [Tags](amazon-lightsail-tags.md).

1. Choose **Create database**.

   Within minutes, your Lightsail database is ready. You can begin configuring it for data import, or connect to it by using a database client.

## Next steps
<a name="creating-a-database-next-steps"></a>

Here are a few guides to help you manage your new database in Lightsail after it’s up and running:
+ [Configure the data import mode for your database](amazon-lightsail-configuring-database-data-import-mode.md)
+ [Configure the public mode for your database in Amazon Lightsail](amazon-lightsail-configuring-database-public-mode.md)
+ [Manage your database password](amazon-lightsail-managing-database-password.md)
+ [Connect to your MySQL database](amazon-lightsail-connecting-to-your-mysql-database.md)
+ [Connect to your PostgreSQL database](amazon-lightsail-connecting-to-your-postgres-database.md)
+ [Import data into your MySQL database](amazon-lightsail-importing-data-into-your-mysql-database.md)
+ [Import data into your PostgreSQL database](amazon-lightsail-importing-data-into-your-postgres-database.md)
+ [Create a snapshot of your database](amazon-lightsail-creating-a-database-snapshot.md)