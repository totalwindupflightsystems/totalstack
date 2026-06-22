---
id: "@specs/aws/kafka/docs/broker-instance-sizes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Broker sizes"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Broker sizes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/broker-instance-sizes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK broker sizes
<a name="broker-instance-sizes"></a>

When you create an Amazon MSK Provisioned cluster you specify the size of brokers that you want it to have. Depending on the [broker type](broker-instance-types.md), Amazon MSK supports the following broker sizes.

**Standard broker sizes**
+ kafka.t3.small
+ kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, kafka.m5.24xlarge
+ kafka.m7g.large, kafka.m7g.xlarge, kafka.m7g.2xlarge, kafka.m7g.4xlarge, kafka.m7g.8xlarge, kafka.m7g.12xlarge, kafka.m7g.16xlarge

**Express broker sizes**
+ express.m7g.large, express.m7g.xlarge, express.m7g.2xlarge, express.m7g.4xlarge, express.m7g.8xlarge, express.m7g.12xlarge, express.m7g.16xlarge

**Note**  
Some broker sizes may not be available in certian AWS Regions. See the updated Broker Instance Pricing Tables on the [Amazon MSK pricing page](https://aws.amazon.com/msk/pricing/) for the latest list of available instances by Region.

## Other notes on broker sizes
<a name="broker-instance-sizes-other-notes"></a>
+ M7g brokers use AWS Graviton processors (custom Arm-based processors built by Amazon Web Services). M7g brokers offer improved price performance relative to comparable M5 instances. M7g brokers consume less power than comparable M5 instances.
+ Amazon MSK supports M7g brokers on MSK Provisioned clusters running 2.8.2 and 3.3.2 and higher Kafka versions.
+ M7g and M5 brokers have higher baseline throughput performance than T3 brokers and are recommended for production workloads. M7g and M5 brokers can also have more partitions per broker than T3 brokers. Use M7g or M5 brokers if you are running larger production-grade workloads or require a greater number of partitions. To learn more about M7g and M5 instance sizes, see [Amazon EC2 General Purpose Instances](https://aws.amazon.com/ec2/instance-types/).
+ T3 brokers have the ability to use CPU credits to temporarily burst performance. Use T3 brokers for low-cost development, if you are testing small to medium streaming workloads, or if you have low-throughput streaming workloads that experience temporary spikes in throughput. We recommend that you run a proof-of-concept test to determine if T3 brokers are sufficient for production or critical workload. To learn more about T3 broker sizes, see [Amazon EC2 T3 Instances](https://aws.amazon.com/ec2/instance-types/t3/).

For more information on how to choose broker sizes, see [Best practices for Standard and Express brokers](bestpractices-intro.md).