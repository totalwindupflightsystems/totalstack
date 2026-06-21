---
id: "@specs/aws/lightsail/docs/monitoring-cpu-burst-capacity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Monitor burst capacity"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Monitor burst capacity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/monitoring-cpu-burst-capacity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Monitor CPU burst capacity for your Lightsail instance
<a name="monitoring-cpu-burst-capacity"></a>

**Did you know?**  
 You can change your instance bundle to a larger size when you create an instance from an instance snapshot. For more information, see [ Upsize a Lightsail instance, storage, or database from snapshots ](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html) . 

The CPU overview page in the Lightsail console displays your instance's CPU utilization in comparison to its available CPU burst capacity. In the following CPU overview example, the CPU burst capacity percentage has increased because the instance has continuously operated below its baseline in the sustainable zone.

![CPU overview page in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/cpu-overview-page.png)


The remaining CPU burst capacity graph view can be switched between CPU burst capacity percentage and minutes. Your instance consumes more CPU burst capacity when operating in the bursting zone. The CPU burst capacity minutes metric is the amount of time available for your instance to burst at 100% CPU utilization, It is consumed at the same rate as your instance's current CPU utilization percentage when operating in the burstable zone. For example, a Linux or Unix-based $7 USD/month instance has a CPU utilization baseline of 10%, and accrues 6 minutes of CPU burst capacity minutes per hour. Therefore, if the instance operates at:
+ 100% CPU utilization in the burstable zone for a 60-minute period, then it consumes CPU burst capacity minutes at a 100% rate in that period. The instance consumes 60 minutes of CPU burst capacity, and accrues 6 minutes, for a net consumption of 54 minutes.
+ 50% CPU utilization in the burstable zone for a 60-minute period, then it consumes CPU burst capacity minutes at a 50% rate in that period. The instance consumes 30 minutes of CPU burst capacity, and accrues 6 minutes, for a net consumption of 24 minutes.
+ 10% CPU utilization at the instance's baseline for a 60-minute period, then it consumes CPU burst capacity minutes at a 10% rate in that period. The instance consumes 6 minutes of CPU burst capacity, and accrues 6 minutes. When an instance operates at its baseline, the CPU burst capacity minutes doesn't increase or decrease.
+ 5% CPU utilization in the sustainable zone for a 60-minute period, then it consumes CPU burst capacity minutes at a 5% rate in that period. The instance consumed 3 minutes of CPU burst capacity, and accrued 6 minutes, for a net accrual of 3 minutes.

Alternately, if the instance has accrued 60 minutes of CPU burst capacity, then it can operate at 100% CPU utilization for 60 minutes, at 50% for 120 minutes, or at 25% at 150 minutes.