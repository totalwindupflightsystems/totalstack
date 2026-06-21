---
id: "@specs/aws/lightsail/docs/baseline-cpu-performance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CPU performance"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# CPU performance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/baseline-cpu-performance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understand baseline CPU performance and burst capacity accrual for Lightsail instances
<a name="baseline-cpu-performance"></a>

**Did you know?**  
 You can change your instance bundle to a larger size when you create an instance from an instance snapshot. For more information, see [ Upsize a Lightsail instance, storage, or database from snapshots ](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html) . 

Lightsail instances continuously earn (at a millisecond-level resolution) a set rate of CPU burst capacity per hour, which is also consumed when your instance's CPU utilization is greater than 0%. The accounting process for whether burst capacity is accrued or consumed also happens at a millisecond-level resolution, so you don't have to worry about overspending CPU burst capacity; a short burst of CPU uses a small fraction of burst capacity.

If your instance uses fewer CPU resources than is required for baseline performance (such as when it is idle), the unspent CPU burst capacity is accrued in the form of CPU burst capacity percentage and minutes. If your instance needs to burst above the baseline performance level, it spends the accrued CPU burst capacity. The more CPU burst capacity that your instance has accrued, the more time it can burst beyond its baseline when more performance is needed.

## Baseline CPU performance
<a name="baseline-cpu-instance-plans"></a>

The following table outlines the performance baselines for dual-stack instance plans in Lightsail. While the price for an IPv6-only plan is different, the performance baselines are the same.


|  Instance plan  |  vCPUs  |  Memory  |  Storage  |  Performance baseline  | 
| --- | --- | --- | --- | --- | 
| Linux or Unix $5 and Windows $9.50 | 2 | 512 MB | 20 GB | 5% | 
| Linux or Unix $7 and Windows $14 | 2 | 1 GB | 40 GB | 10% | 
| Linux or Unix $12 and Windows $22 | 2 | 2 GB | 60 GB | 20% | 
| Linux or Unix $24 and Windows $44 | 2 | 4 GB | 80 GB | 20% | 
| Linux or Unix $44 and Windows $74 | 2 | 8 GB | 160 GB | 30% | 
| Linux or Unix $84 and Windows $124 | 4 | 16 GB | 320 GB | 40% | 
| Linux or Unix $164 and Windows $244 | 8 | 32 GB | 640 GB | 40% | 
| \* Linux or Unix $384 and Windows $574 | 16 | 64 GB | 1,280 GB | 40% | 
| \* Linux or Unix $884 and Windows $1,254 | 32 | 128 GB | 1,280 GB | 40% | 
| \* Linux or Unix $1,324 and Windows $1,884 | 48 | 192 GB | 1,280 GB | 40% | 
| \* Linux or Unix $1,764 and Windows $2,504 | 64 | 256 GB | 1,280 GB | 40% | 


|  | 
| --- |
| \* These instance plans burst automatically as needed and don't utilize burst capacity. | 

These performance baselines are per vCPU. The CPU utilization metric graph in the Lightsail console averages the CPU utilization and baseline for instances with more than one vCPU. For example, a Linux or Unix-based $44 USD/month instance has two vCPUs and an averaged CPU utilization baseline of 30%. Therefore, if:
+ One vCPU operates at 50% and the other at 0%, a 25% averaged CPU utilization is displayed on the graph. This puts the instance's CPU utilization below its 30% baseline, and in the sustainable zone.
+ One vCPU operates at 30%, and the other at 20%, a 25% averaged CPU utilization is displayed on the graph. This puts the instance's CPU utilization below its 30% baseline, and in the sustainable zone.
+ One vCPU operates at 35% and the other at 25%, a 30% averaged CPU utilization is displayed on the graph. This puts the instance's CPU utilization at the 30% baseline.
+ One vCPU operates at 100% and the other at 90%, a 95% averaged CPU utilization is displayed on the graph. This puts the instance's CPU utilization above its 30% baseline, and in the burstable zone.

For more information about the sustainable and burstable zones, see [Identify when your instance bursts](identifying-instance-burst.md) later in this guide.

## Previous generation CPU performance
<a name="baseline-previous-instance-plans"></a>

The following table outlines the performance baselines for Lightsail instances that were created prior to **June 29, 2023**. These performance baselines are per vCPU.


|  Instance plan  |  vCPUs  |  Memory  |  Storage  |  Performance baseline  | 
| --- | --- | --- | --- | --- | 
| Linux or Unix $5 and Windows $9.50 | 1 | 512 MB | 20 GB | 5% | 
| Linux or Unix $7 and Windows $14 | 1 | 1 GB | 40 GB | 10% | 
| Linux or Unix $12 and Windows $22 | 1 | 2 GB | 60 GB | 20% | 
| Linux or Unix $24 and Windows $44 | 2 | 4 GB | 80 GB | 20% | 
| Linux or Unix $44 and Windows $74 | 2 | 8 GB | 160 GB | 30% | 
| Linux or Unix $84 and Windows $124 | 4 | 16 GB | 320 GB | 22.5% | 
| Linux or Unix $164 and Windows $244 | 8 | 32 GB | 640 GB | 17% | 