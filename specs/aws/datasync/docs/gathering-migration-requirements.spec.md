---
id: "@specs/aws/datasync/docs/gathering-migration-requirements"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Gathering requirements"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Gathering requirements

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/gathering-migration-requirements
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Gathering requirements for your migration
<a name="gathering-migration-requirements"></a>

The first step in a large data migration requires collecting a variety of information across your organization.

This information helps you create a migration [process](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/process.html), which for large migrations can include multiple transfers and procedures for cutting over operations (done in [waves](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/wave-planning.html)) from your source to your destination storage.

## Understanding why you want to migrate
<a name="define-migration-goals-why"></a>

Before you can start migrating to AWS, you need to clearly understand why you're migrating your data. This helps address common migration challenges such as meeting deadlines, managing resources, and coordinating across teams.

If you need help determining your motivations for the migration, answer these questions:
+ Are you freeing up on-premises storage space?
+ Are you meeting hardware support contract deadlines?
+ Is this for a data center exit?
+ What's your migration timeline?
+ Are you transferring data from other cloud storage?
+ Are you migrating partial or complete datasets?
+ Is this for data archival?
+ Do applications or users need regular access to this data?

## Figuring out logistics
<a name="define-migration-goals-logistics"></a>

Address some basic logistics about your storage environment, the migration, and your organization:

1. Get a basic understanding of your current data storage infrastructure.

1. Verify whether you need a [DataSync agent](do-i-need-datasync-agent.md). For example, you need an agent if you're transferring from on-premises storage.

1. If you need an agent, make sure that you understand the [agent requirements](agent-requirements.md):
   + An agent can run as a virtual machine (VM) on VMware ESXi, Linux Kernel-based Virtual Machine (KVM), and Microsoft Hyper-V hypervisors. You also can deploy an agent as an Amazon EC2 instance within AWS.
   + Large migrations are typically memory intensive. Make sure that your agent has enough RAM.

1. Identify key stakeholders from your leadership, networking, storage, and IT departments who need to be involved in the migration. This can include:
   + Find a [single-threaded leader](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/people.html) who's dedicated to the project and its results.
   + Determine who's responsible for the ownership and classification of the data that you're migrating.
   + Identify who manages your source and who eventually will manage the AWS storage service that you're migrating to.
   + Find out who will create and manage any other processes for your data once it's in AWS.

1. Establish cross-department communication channels.

1. Create a rollback plan for contingencies.

1. Document the complete migration process, including waves, validation, and cutover procedures. Use this as your runbook for the entire migration. You will update this process as you plan and implement the migration.

## Reviewing the data you're migrating
<a name="review-migration-data"></a>

Work with your storage and application teams to analyze the characteristics of the data you're migrating. This information helps you determine a migration strategy that you can execute with DataSync.

**Contents**
+ [Determining data usage patterns](#review-migration-data-usage)
+ [Identifying data structure and layout](#review-migration-data-structure)
+ [Documenting shares and folders](#review-migration-data-document-shares)
+ [Analyzing file sizes](#review-migration-data-file-sizes)

### Determining data usage patterns
<a name="review-migration-data-usage"></a>
+ For actively used data with frequent modifications, plan for multiple waves of incremental transfers to avoid disrupting business operations.
+ For read-only data that might be considered archival, you might not need to plan for waves.
+ If you have a mix of data usage patterns, plan waves that migrate these different datasets separately. For example, you might have one wave for archive data, with the rest of the waves dedicated to migrating active data.

### Identifying data structure and layout
<a name="review-migration-data-structure"></a>
+ Determine if data is organized by time periods (year, month, day) or other patterns.
+ Use this organization structure to plan your migration waves. For example, you might migrate a year's worth of archive data during one wave.

### Documenting shares and folders
<a name="review-migration-data-document-shares"></a>
+ Create an inventory of shares and folders (including file or object counts for each).
+ Identify shares and folders with active datasets. These might require incremental transfers during the migration.
+ Review the [DataSync quotas](datasync-limits.md). This can help you plan how to partition your dataset when configuring DataSync.

### Analyzing file sizes
<a name="review-migration-data-file-sizes"></a>
+ Expect higher data throughput for transfers with larger files (MB or GB) compared to smaller files (KB).
+ If you're working with a lot of smaller files, expect more metadata operations on your storage system and lower data throughput. DataSync performs these operations when comparing and verifying your source and destination locations.

## Identifying storage requirements
<a name="determine-storage-requirements"></a>

To choose a compatible AWS storage service to migrate your data, you need to evaluate your source storage system's characteristics and performance.

This information can also help you [schedule your transfers](task-scheduling.md) to minimize impact on business operations during the migration.

**Contents**
+ [Determining source storage support](#determine-storage-requirements-protocols)
+ [Reviewing metadata preservation requirements](#determine-storage-requirements-metadata)
+ [Collecting performance metrics from source storage](#determine-storage-requirements-performance)
+ [Choosing a destination AWS storage service](#determine-storage-requirements-destination)

### Determining source storage support
<a name="determine-storage-requirements-protocols"></a>

DataSync can work with a variety of storage systems that allow access through NFS, SMB, HDFS, and S3 compatible object storage clients. 

If you're migrating from other cloud storage, verify that DataSync can work with that provider. For a list of supported source locations, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

### Reviewing metadata preservation requirements
<a name="determine-storage-requirements-metadata"></a>

DataSync can preserve your file or object metadata during a transfer. How your metadata gets preserved depends on your transfer locations and if those locations use similar types of metadata.

DataSync in some cases needs additional permissions to preserve file metadata, such as NTFS discretionary access lists (DACLs).

For more information, see [Understanding how DataSync handles file and object metadata](metadata-copied.md).

### Collecting performance metrics from source storage
<a name="determine-storage-requirements-performance"></a>

Measure baseline IOPS and disk throughput during average and peak workloads for your source storage. Transferring data adds I/O overhead to both your source and destination storage systems.

Compare this performance data against your storage system's specifications to determine available performance resources.

### Choosing a destination AWS storage service
<a name="determine-storage-requirements-destination"></a>

At this point, you might have an idea what AWS storage service makes sense for your data. If not, data usage patterns and storage performance are a couple areas to think about when deciding. For example, you might consider Amazon S3 if you have archive data and Amazon FSx or Amazon EFS for active data.

To help you decide the right object or file-based storage for your data, see [Choosing an AWS storage service](https://docs.aws.amazon.com/decision-guides/latest/storage-on-aws-how-to-choose/choosing-aws-storage-service.html).

## Determining network requirements
<a name="datasync-migration-network-requirements"></a>

To migrate your data with DataSync, you must establish network connections between your source storage, agent, and AWS. You also need to plan for enough network bandwidth and infrastructure.

Work with your network engineers and storage administrators to gather the following network requirements.

**Contents**
+ [Assessing your available network bandwidth](#datasync-migration-network-bandwidth)
+ [Considering options for connecting your network to AWS](#datasync-migration-network-connection-options)
+ [Choosing a service endpoint for agent communication](#datasync-migration-network-service-endpoint)
+ [Planning for enough network infrastructure](#datasync-migration-network-interfaces)

### Assessing your available network bandwidth
<a name="datasync-migration-network-bandwidth"></a>

Your available network bandwidth factors into your transfer speeds and overall migration time. If you're transferring from an on-premises storage system, do the following: 
+ Work with your network team to determine average and peak bandwidth utilization. 
+ Identify windows when you can transfer data and avoid disrupting daily operations. This will inform when your migration waves and cutovers happen.

You can control how much bandwidth DataSync uses. For more information, see [Setting bandwidth limits for your AWS DataSync task](configure-bandwidth.md).

Since transfers from other cloud storage typically happen over the public internet, there usually are less bandwidth restrictions and considerations with these transfers.

### Considering options for connecting your network to AWS
<a name="datasync-migration-network-connection-options"></a>

Consider the following options for establishing network connectivity for your DataSync transfer:
+ **Direct Connect** - Review the [architecture and routing examples](direct-connect-architecture.md) for using Direct Connect with DataSync. You can monitor Direct Connect activity using [Amazon CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html).
+ **VPN** - [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) offers up to 1.25 Gbps throughput per tunnel.
+ **Public internet** - Contact with your internet service provider for network usage data.

### Choosing a service endpoint for agent communication
<a name="datasync-migration-network-service-endpoint"></a>

DataSync agents use [service endpoints](choose-service-endpoint.md) to communicate with the DataSync service. The type of endpoint you use depends on the how you're connecting for your network to AWS. 

### Planning for enough network infrastructure
<a name="datasync-migration-network-interfaces"></a>

For every transfer task that you create, DataSync automatically generates and manages the network infrastructure for your data transfers. This infrastructure is known as *network interfaces* or *elastic network interfaces*, which are logical networking components in an Amazon virtual private cloud (VPC) that represent virtual network cards. For more information, see the [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

Each network interface uses a single IP address in your destination VPC subnet. To make sure that you have enough network infrastructure for your migration, do the following:
+ Note the number of [network interfaces](required-network-interfaces.md) that DataSync will create for your DataSync destination location.
+ Make sure that your subnet has enough IP addresses for your DataSync tasks. For example, a task that uses an agent requires four IP addresses. If you create four tasks for your migration, that means you need 16 available IP addresses in your subnet. 