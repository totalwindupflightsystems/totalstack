---
id: "@specs/aws/lightsail/docs/identifying-instance-burst"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Identify instance bursts"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Identify instance bursts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/identifying-instance-burst
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Identify when your Lightsail instance bursts
<a name="identifying-instance-burst"></a>

**Did you know?**  
 You can change your instance bundle to a larger size when you create an instance from an instance snapshot. For more information, see [ Upsize a Lightsail instance, storage, or database from snapshots ](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html) . 

On the CPU utilization metric graph for your instances, you will see a sustainable zone, and a burstable zone. In the following CPU utilization metric graph example, the performance baseline is 10% because the instance uses the Linux or Unix-based $7 USD/month instance plan.

![Sustainable and burstable zones on the CPU utilization graph](http://docs.aws.amazon.com/lightsail/latest/userguide/images/cpu-utilization-burstable-zone.png)


Your Lightsail instance can operate in the sustainable zone indefinitely with no impact to the operation of your system. Your instance may begin operating in the burstable zone when under heavy load, such as when compiling code, installing new software, running a batch job, or serving peak load requests. While operating in the burstable zone, your instance is consuming a higher amount of CPU cycles. Therefore, it can only operate in this zone for a limited period of time.

The period of time your instance can operate in the burstable zone is dependent on how far into the burstable zone it is. An instance operating in the lower end of the burstable zone can burst for a longer period of time than an instance operating in the higher end of the burstable zone. However, an instance that is anywhere in the burstable zone for a sustained period of time will eventually use up all the CPU capacity until it operates in the sustainable zone again. Therefore, it is important to also monitor the remaining CPU burst capacity, which is described in the following section of this guide.