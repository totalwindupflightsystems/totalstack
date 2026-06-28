---
id: "@specs/aws/datasync/docs/how-discovery-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How it works"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# How it works

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/how-discovery-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



# How AWS DataSync Discovery works
<a name="how-discovery-works"></a>

Learn the key concepts and terminology related to AWS DataSync Discovery.

## DataSync Discovery architecture
<a name="discovery-architecture"></a>

The following diagram illustrates how DataSync Discovery collects information and provides recommendations for migrating data from an on-premises storage system to AWS.

![The first connection is for communicating with the source storage location. The second connection is for transferring between locations. The third and final connection is with the destination storage location.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-discovery-overview-diagram.png)



| Reference | Description | 
| --- | --- | 
| 1 | A DataSync agent connects to your on-premises storage system's management interface (using port 443, for example). You then run a discovery job to collect information about your system. | 
| 2 | The agent sends the information that it collects to DataSync Discovery through a [public service endpoint](choose-service-endpoint.md). | 
| 3 | Using the information that it collects, DataSync Discovery recommends AWS storage services that you can migrate your data to. | 

## Concepts and terminology
<a name="discovery-terminology"></a>

Familiarize yourself with DataSync Discovery features.

**Topics**
+ [Agent](#how-discovery-works-agent)
+ [Discovery job](#how-discovery-works-job)
+ [Storage system resource information](#how-discovery-works-perf)
+ [AWS storage recommendations](#how-discovery-works-recs)

### Agent
<a name="how-discovery-works-agent"></a>

An *agent* is a virtual machine (VM) appliance that DataSync Discovery uses to access the management interface of your on-premises storage system. The agent collects (reads) information about how your storage resources are performing and being used.

You can deploy an agent in your storage environment on VMware ESXi, Linux Kernel-based Virtual Machine (KVM), or Microsoft Hyper-V hypervisors. For storage in a virtual private cloud (VPC) in AWS, you can deploy an agent as an Amazon EC2 instance.

A DataSync Discovery agent is no different than an agent that you can use for DataSync transfers, but we don't recommend using the same agent for these scenarios.

To get started, see [Deploying your AWS DataSync agent](deploy-agents.md).

### Discovery job
<a name="how-discovery-works-job"></a>

You run a *discovery job* to collect information about your on-premises storage system through the storage system's management interface.

You can run a discovery job between 1 hour and 31 days. You'll get more accurate AWS storage recommendations the longer your discovery job runs.

For more information, see [Working with DataSync discovery jobs](discovery-job-create.md).

### Storage system resource information
<a name="how-discovery-works-perf"></a>

DataSync Discovery can give you performance and utilization information about your on-premises storage system's resources. For example, get an idea about how much storage capacity is being used in a specific storage volume compared to how much capacity you originally provisioned.

You can view this information as your discovery job collects it by using the following:
+ The [DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html) operation
+ The [DescribeStorageSystemResourceMetrics](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResourceMetrics.html) operation

For more information, see [Viewing storage resource information collected by AWS DataSync Discovery](discovery-understand-findings.md).

### AWS storage recommendations
<a name="how-discovery-works-recs"></a>

Using the information that it collects about your on-premises storage system's resources, DataSync Discovery recommends AWS storage services to help plan your migration to AWS.

You can view recommendations by using the [DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html) operation.

For more information, see [Getting recommendations from AWS DataSync Discovery](discovery-understand-recommendations.md).

## Limitations
<a name="discovery-limitations"></a>
+ Currently, you can only activate DataSync Discovery agents with [public service endpoints](choose-service-endpoint.md).