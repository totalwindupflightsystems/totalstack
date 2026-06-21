---
id: "@specs/aws/lightsail/docs/amazon-lightsail-high-availability-databases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS High availability databases"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# High availability databases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-high-availability-databases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# High availability databases in Lightsail
<a name="amazon-lightsail-high-availability-databases"></a>

A Lightsail high availability managed database provides failover support with a primary database in one Availability Zone, and a secondary standby database in another. We recommend high availability databases for production workloads that experience heavy use and require data redundancy. For development and test purposes, you can use a standard database that isn't high availability.

To create a high availability database, select one of the high availability database plans available in Lightsail when creating your managed database. For more information, see [Create a database](amazon-lightsail-creating-a-database.md) . You can also change your standard database to a high availability database. Create a snapshot of your standard database, create a new database from the snapshot, and choose a high availability plan. For more information, see [Create a database from a snapshot](amazon-lightsail-creating-a-database-from-snapshot.md).