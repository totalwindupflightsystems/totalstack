---
id: "@specs/aws/lightsail/docs/amazon-lightsail-choosing-a-database"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Select a database engine"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Select a database engine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-choosing-a-database
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Select the right Lightsail database engine for your project
<a name="amazon-lightsail-choosing-a-database"></a>

Amazon Lightsail provides the latest major versions of the MySQL and PostgreSQL databases. This guide helps you decide which database is right for your project.

Lightsail also offers a Windows Server 2022 instance with SQL Server. For more information, see [Choose an Amazon Lightsail instance image](compare-options-choose-lightsail-instance-image.md).

## Compare managed databases in Lightsail
<a name="lightsail-compare-databases"></a>

**MySQL**

MySQL 5.7, and 8.0 are available in Lightsail. MySQL is the most widely adopted open source relational database. It serves as the primary relational data store for many popular websites, applications, and commercial products. MySQL is a reliable, stable, and secure SQL-based database management system, with more than 20 years of community-backed development and support. The MySQL database is suitable for a wide variety of use cases, including mission-critical apps and dynamic websites. It also functions as an embedded database for software, hardware, and appliances.

**Important**  
Starting June 30, 2024, Lightsail will no longer support MySQL 5.7, and you will not be able to create new databases with this blueprint. To learn how you can upgrade major versions of your database instance, see [Upgrade the major version of a Lightsail database](amazon-lightsail-upgrade-database-major-version.md).

For more information, see the following MySQL documentation:
+ [MySQL 5.7 documentation](https://dev.mysql.com/doc/refman/5.7/en/)
+ [MySQL 8.0 documentation](https://dev.mysql.com/doc/refman/8.0/en/)

**PostgreSQL**

PostgreSQL 12, 13, 14, 15, and 16 are available in Lightsail. PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

There is a wealth of information to be found describing how to install and use PostgreSQL through the [official documentation](https://www.postgresql.org/docs/). The [PostgreSQL community](https://www.postgresql.org/community/) provides many helpful places to become familiar with the technology, discover how it works, and find career opportunities.

**Important**  
Starting June 30, 2024, Lightsail will no longer support PostgreSQL 11, and you will not be able to create new databases with this blueprint. To learn how you can upgrade major versions of your database instance, see [Upgrade the major version of a Lightsail database](amazon-lightsail-upgrade-database-major-version.md).
The PostgreSQL community plans to deprecate PostgreSQL 12 on November 14, 2024, and Lightsail instances launched from this blueprint won't receive security patches after this date. Therefore, Amazon Lightsail will end standard support of PostgreSQL 12 on February 28, 2025. You will not be able to create new Lightsail databases using PostgreSQL 12 on or after February 28, 2025. For more information, see the [PostgreSQL website](https://www.postgresql.org/support/versioning/).

For more information, see the following PostgreSQL documentation:
+ [PostgreSQL 11 documentation](https://www.postgresql.org/docs/11/index.html)
+ [PostgreSQL 12 documentation](https://www.postgresql.org/docs/12/index.html)
+ [PostgreSQL 13 documentation](https://www.postgresql.org/docs/13/index.html)
+ [PostgreSQL 14 documentation](https://www.postgresql.org/docs/14/index.html)
+ [PostgreSQL 15 documentation](https://www.postgresql.org/docs/15/index.html)
+ [PostgreSQL 16 documentation](https://www.postgresql.org/docs/16/index.html)

## Optimize data import
<a name="optimizing-your-data-import"></a>

Several database plans are available in Lightsail, each with specific memory, vCPU, storage, and data transfer allowance specifications. Because each database plan has these specifications, it is important that you choose an appropriately-sized database plan for the amount of data that you want to import into your new Lightsail database. Your data import may be slowed if you choose a plan that is under your size requirements. Use the following guidelines to select the appropriate database plan for your data import requirement:
+ **Micro $15 USD/month database plan** — Data import may be slowed if you transfer more than 10 GB of data.
+ **Small $30 USD/month database plan** — Data import may be slowed if you transfer more than 20 GB of data.
+ **Medium $60 USD/month database plan** — Data import may be slowed if you transfer more than 85 GB of data.
+ **Large $115 USD/month database plan** — Data import may be slowed if you transfer more than 156 GB of data.
+ **Xlarge $230 USD/month database plan** — Data import may be slowed if you transfer more than 156 GB of data.
+ **2Xlarge $460 USD/month database plan** — Data import may be slowed if you transfer more than 156 GB of data.

**Note**  
For more information about importing data into your database, see [Import data into your MySQL database](amazon-lightsail-importing-data-into-your-mysql-database.md) or [Import data into your PostgreSQL database](amazon-lightsail-importing-data-into-your-postgres-database.md).