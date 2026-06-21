---
id: "@specs/aws/lightsail/docs/amazon-lightsail-upgrade-database-major-version"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Upgrade major version"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Upgrade major version

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-upgrade-database-major-version
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Upgrade the major version of a Lightsail database
<a name="amazon-lightsail-upgrade-database-major-version"></a>

When Amazon Lightsail supports a new version of a database engine, you can upgrade your database to the new version. Lightsail offers two database blueprints, MySQL and PostgreSQL. This guide describes how to upgrade the major version for your MySQL or PostgreSQL database instance. You can upgrade the database major version only by using the [https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html) API action.

We will use AWS CloudShell to perform the upgrade. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. With CloudShell, you can run AWS Command Line Interface (AWS CLI) commands using your preferred shell, such as Bash, PowerShell, or Z shell. You can do this without downloading or installing command line tools. For more information about how to set up and use CloudShell, see [AWS CloudShell in Lightsail](amazon-lightsail-cloudshell.md).

**Understand the changes**  
Major version upgrades can introduce a number of incompatibilities with the previous version. These incompatibilities can cause problems during an upgrade. You might need to prepare your database for the upgrade to be successful. For information about upgrading major versions of a database, see the following topics on the MySQL and PostgreSQL websites.
+ [Preparing Your Installation for Upgrade](https://dev.mysql.com/doc/refman/8.0/en/upgrade-prerequisites.html)
+ [MySQL Upgrade Checker Utility](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-upgrade.html)
+ [Upgrading a PostgreSQL Cluster](https://www.postgresql.org/docs/current/upgrading.html)

## Prerequisites
<a name="upgrade-database-major-version-prerequisites"></a>

1. Verify that your application supports both major versions of the database.

1. We recommend that you create a snapshot of your database instance before making any changes. For more information, see [Create a snapshot of your Lightsail database](amazon-lightsail-creating-a-database-snapshot.md).

1. (Optional) Create a new database instance from the snapshot that you just created. Because database updates require downtime, you can test the upgrade on the new database before you upgrade the database that's currently active. For more information about making a copy of your database, see [Create a snapshot of your Lightsail database](amazon-lightsail-creating-a-database-snapshot.md).

## Update the database major version
<a name="upgrade-database-major-version-update-procedure"></a>

Lightsail supports major version upgrades for MySQL and PostgreSQL database instances. A MySQL database is used as an example in the following procedure. However, the process and commands are the same for a PostgreSQL database.

Complete the following procedure to upgrade the database major version for your Lightsail database.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Databases**.

1. Note of the name and AWS Region for the database instance that you want to upgrade.  
![The name and Region of the new database instance in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/mysql80-upgrade-dbname-endpoint.png)

1. In the lower left corner of the Lightsail console, choose **CloudShell**. A CloudShell terminal will open in the same browser tab. When the command prompt displays, the shell is ready for interaction.

1. Enter the following command at the CloudShell prompt to get a list of database blueprint IDs that are available.

   ```
   aws lightsail get-relational-database-blueprints
   ```

1. Note of the blueprint ID for the major version that you're upgrading to. For example, `mysql_8_0`.  
![The response of the get-relational-database-blueprints command in the CloudShell window.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/mysql80-upgrade-get-blueprints.png)

1. Enter the following command to upgrade the major version of your database. The upgrade will take place during the next maintenance window for your database. In the command, replace {{DatabaseName}} with the name of your database, {{blueprintId}} with the blueprint id of the major version that you are upgrading to, and {{DatabaseRegion}} with the AWS Region that your database is in.

   ```
   aws lightsail update-relational-database \
    --relational-database-name {{DatabaseName}} \
    --relational-database-blueprint-id {{blueprintId}} \
    --region {{DatabaseRegion}}
   ```

   (Optional) To apply the upgrade immediately, include the `--apply-immediately` parameter in the command. You will see a response similar to the following example, and your database will become unavailable while the upgrade is being applied. For more information, see [https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html) in the Lightsail API Reference.   
![The successful result of the update-relational-database --apply-immediately command in the CloudShell window.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/mysql80-upgrade-successful.png)

1. Enter the following command to verify that the major version upgrade is scheduled for the next database maintenance window. In the command, replace {{DatabaseName}} with the name of your database, and {{DatabaseRegion}} with the AWS Region that your database is in.

   ```
   aws lightsail get-relational-database \
    --relational-database-name {{DatabaseName}} \
    --region {{DatabaseRegion}}
   ```

   In the `get-relational-database` response, the database [https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html#Lightsail-Type-RelationalDatabase-state](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html#Lightsail-Type-RelationalDatabase-state) informs you of a pending major version upgrade during the next maintenance window. You can locate the date and time of the next maintenance window in the [https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html#Lightsail-Type-RelationalDatabase-preferredMaintenanceWindow](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateRelationalDatabase.html#Lightsail-Type-RelationalDatabase-preferredMaintenanceWindow) section of the response.

   **Database instance state**

   ```
   "state": "upgrading",
     "backupRetentionEnabled": true, 
     "pendingModifiedValues": {
     "engineVersion": "8.0.36"
   ```

   **Maintenance window**

   ```
   "preferredMaintenanceWindow": "wed: 09:22-wed: 09:52"
   ```

## Next steps
<a name="upgrade-database-major-version-next-steps"></a>

If you created a test database, you can delete it after you have verified that your application will work with the upgraded database. Keep the snapshot that you created of your previous database in case you need to go back to it. You should also create a snapshot of your upgraded database so that you have a new point-in-time copy of it.