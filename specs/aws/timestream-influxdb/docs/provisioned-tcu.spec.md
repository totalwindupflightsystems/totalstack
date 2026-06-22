---
id: "@specs/aws/timestream-influxdb/docs/provisioned-tcu"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Provisioned Timestream Compute Units"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Provisioned Timestream Compute Units

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/provisioned-tcu
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Provisioned Timestream Compute Units
<a name="provisioned-tcu"></a>

**Note**  
Provisioned TCU is available only in the Asia Pacific (Mumbai) region.

With provisioned Timestream Compute Units (TCUs), you can allocate a fixed number of TCUs to your account, ensuring predictable performance and cost for your queries. By provisioning TCUs, you gain greater control over compute capacity, enabling you to optimize both performance and query costs based on your application's specific needs.

**Topics**
+ [Benefits of Provisioning TCU](#provisioned-tcu.benefits)
+ [How Provisioned TCU Works](#provisioned-tcu.how-provisioned-tcu-works)
+ [Monitoring Provisioned TCU usage](#provisioned-tcu.monitoring)
+ [Modifying your Provisioned TCUs](#provisioned-tcu.modifying)
+ [Pricing for Provisioned TCUs](#provisioned-tcu.pricing)

## Benefits of Provisioning TCU
<a name="provisioned-tcu.benefits"></a>

Provisioning TCU provides several benefits for customers with dedicated workloads, including:

1. **Predictable Performance:** By allocating a fixed number of TCUs, you ensure consistent performance for your queries.

1. **Cost Control:** With provisioned TCU, you can better predict and manage your costs, as you are only charged for the duration of the provisioned TCUs.

1. **Flexibility:** Provisioned TCU ensures that your workload has dedicated compute resources and you can adjust the number of provisioned TCUs to match your workload requirements, providing the required scalability as your application’s needs change. 

## How Provisioned TCU Works
<a name="provisioned-tcu.how-provisioned-tcu-works"></a>

Each Timestream Compute Unit (TCU) is comprised of 4 vCPUs and 16GB of memory. To provision TCUs, use the AWS Management Console or the UpdateAccountSettings API operation to allocate a fixed number of TCUs to your account, which are then dedicated to your workload. This ensures predictable performance and cost for your queries. The minimum number of provisioned TCUs is 4, with subsequent increments also in multiples of 4 (e.g., 4, 8, 12, 16). Once provisioned, you can run your query workloads uninterrupted. As your workload demands change, you can adjust the provisioned TCUs using the AWS Management Console or the UpdateAccountSettings API operation at any time. However, you can only decrease the number of TCUs after a minimum of 1 hour has passed since provisioning them.

For example, if you provision 8 TCUs at 10:00 AM, you will be charged for a minimum of 1 hour, until 11:00 AM. During this time, you can increment the TCUs to 12 or more, but you cannot decrement them until 11:00 AM. 

The time it takes to provision the requested Timestream Compute Units (TCUs) in your account varies depending on the number of TCUs requested. For example, provisioning 100 TCUs could take up to 30 minutes. However, you will only be charged for the resources once they are provisioned and available to serve your query workload. To ensure a smooth experience during planned increases in usage, we recommend provisioning the required resources in advance. This allows sufficient time for the resources to become available and ensures that your workload can be handled without interruption.

## Monitoring Provisioned TCU usage
<a name="provisioned-tcu.monitoring"></a>

To monitor your provisioned TCU usage, you can use the following CloudWatch metrics:
+ **Provisioned QueryTCU:** This metric specifies the number of TCUs provisioned in your account.
+ **QueryTCU:** This metric specifies the number of TCUs used by your workload.
+ **InsufficientTCUThrottles:** This metric specifies the number of queries throttled due to insufficient compute capacity.

## Modifying your Provisioned TCUs
<a name="provisioned-tcu.modifying"></a>

You can adjust the number of provisioned Timestream Compute Units (TCUs) to match your changing workload demands using the AWS Management Console, AWS Command Line Interface (CLI), or AWS SDKs. 

To view the current number of provisioned TCUs in your account, navigate to the "Admin Dashboard" section in the AWS Management Console. From there, you can easily monitor and manage your provisioned TCUs.

In the Query Compute Settings, you can verify that the compute mode is set to "Provisioned" and view the current number of provisioned Timestream Compute Units (TCUs) in your account, which is displayed as "Active Query TCU". The default value is 0. You need to provision TCUs before you run your query workload. 

To modify the query compute settings, click the "Modify" button. For instance, if you want to increase the provisioned TCUs from 32 to 64, simply enter your desired target value (64) in the "Target Query TCU" field. Additionally, you can specify an Amazon Simple Notification Service (SNS) topic to receive a notification when the provisioning process is complete.

![Image of console view of modifying settings for provisioned TCUs.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/modify-prov-tcu-settings.png)


After confirming your desired configuration by selecting "Save settings", you will see that the current request status is updated to "Pending". The "Target Query TCU" field will now reflect the desired number of compute units, which is 64 in this case, indicating that the provisioning process has been initiated and is awaiting completion.

![Image of console view of saving settings for provisioned TCUs.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/query-compute-save-settings.png)


Once provisioned, the "Active Query TCU" field will be updated to reflect the new provisioned capacity of 64 Timestream Compute Units, indicating that the provisioning process is complete and the additional resources are now available for use in your account.

![Image of console view of new updated settings for provisioned TCUs.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/query-compute-updated-settings.png)


To reduce the number of provisioned Timestream Compute Units (TCUs) in your account, follow the same steps as before and enter your desired target value. For example, if you want to decrease the provisioned TCUs to 16, simply set the "Target Query TCU" field to 16. Please note that you can only decrease the number of provisioned TCUs after a minimum of 1 hour has passed since the last provisioning request. This means that if you provisioned or modified your TCUs within the last hour, you will need to wait until the 1-hour window has elapsed before you can decrement the TCUs.

![Image of console view of reducing the number of provisioned TCUs.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/query-modify-reduce-tcu-settings.png)


After requesting a decrease in provisioned Timestream Compute Units (TCUs), the service will decrement the TCUs when it determines it is safe to do so, which may take up to a few minutes. During this time, the "Target Query TCU" field will continue to display the desired target value, in this case, 16 TCUs, indicating the pending change. Once the decrement is complete, the "Active Query TCU" field will be updated to reflect the new provisioned capacity of 16 TCUs.

![Image of console view of updated reduced number of provisioned TCUs.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/query-modify-updated-reduce-tcu-settings.png)


Once the request is successfully completed, the "Active Query TCU" field will be updated to reflect the new provisioned capacity of 16 Timestream Compute Units (TCUs). If you no longer anticipate any query workload, you can further decrement the provisioned TCUs to 0, effectively releasing all provisioned resources and stopping any associated charges.

## Pricing for Provisioned TCUs
<a name="provisioned-tcu.pricing"></a>

You are charged for the duration of the Timestream Compute Units (TCUs) provisioned in your account, with a minimum charge of 1 hour. After the first hour, the TCUs are metered per second. 

To calculate the total metered hours, multiply the number of provisioned TCUs by the duration of use. For example: If you provision 16 TCUs for 2 hours, the total metered hours are 16 TCU \* 2 hours = 32 TCU-hours. If you provision 16 TCUs for 4 hours, then decrement to 8 TCUs and use them for 6 hours, the total metered hours are 16 TCU \* 4 hours \+ 8 TCU \* 6 hours = 112 TCU-hours. 

Your total spend will depend on the prevailing TCU-hour cost in your region. Please refer to the Amazon Timestream Pricing page for detailed information. 

**Best Practices for managing Provisioned TCU**

To get the most out of the Provisioned TCU feature, follow these best practices:
+ **Monitor your workload:** Monitor your workload's performance, [QueryTCU used](monitoring-cloudwatch.md) and view `InsufficientTCUThrottles` to understand your usage patterns and adjust your provisioned TCUs accordingly.
+ **Pro-active adjustment:** Increase or decrease provisioned TCUs based on observed trends and anticipated workload changes. Make adjustments for your peak and off-peak periods. 
+ **Maintain Headroom:** Maintain your consumed QueryTCU to within 80% - 90% of your ProvisionedQueryTCU to handle unexpected spikes. 
+ **Optimize Queries:** Leverage features such as Query Insights and follow Timestream Query best practices to optimize queries for reduced compute usage.
+ **Implement Retries:**Timestream for LiveAnalytics Query SDK supports a retry mechanism with a default of 3 retries. Adjust the value accordingly to handle occasional and unanticipated bursts.