---
id: "@specs/aws/kafka/docs/msk-connect-max-autoscaling-task-count"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understand maximum autoscaling task count"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Understand maximum autoscaling task count

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-max-autoscaling-task-count
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understand maximum autoscaling task count
<a name="msk-connect-max-autoscaling-task-count"></a>

The `maxAutoscalingTaskCount` parameter is an optional capacity field available for autoscaling connectors in Amazon MSK Connect. This parameter allows you to set an upper limit on the maximum number of tasks that can be created during connector autoscaling operations, providing greater control over resource utilization and performance.

When you use autoscaled capacity mode, Amazon MSK Connect automatically overrides your connector's `tasks.max` property with a value proportional to the number of workers and MCUs per worker. The `maxAutoscalingTaskCount` parameter provides an additional configurable option to limit the maximum number of tasks created for your connector.

This capability is particularly useful when you want to control the level of parallelism in relation to the number of topic partitions in your Kafka cluster. By setting this limit, you can optimize performance and prevent inefficient task distribution that might occur when the automatically calculated task count exceeds your workload requirements.

## Configuration requirements
<a name="msk-connect-max-autoscaling-task-count-requirements"></a>

The `maxAutoscalingTaskCount` parameter must meet the following requirement:

```
maxAutoscalingTaskCount ≥ maxWorkerCount
```

This requirement ensures efficient resource utilization by maintaining at least one task per worker. The system enforces this minimum to optimize connector functionality.

When you specify `maxAutoscalingTaskCount`, the limit is applied immediately upon connector creation and during all subsequent scaling events. As the number of workers increases or decreases during autoscaling operations, the system continues to honor this limit. The `tasks.max` value adjusts proportionally to the number of workers and MCUs per worker but never exceeds the configured `maxAutoscalingTaskCount` value.

If you don't specify this parameter, the connector uses the standard calculation without any limit: `tasks.max = workerCount × mcuCount × tasksPerMcu` (where tasksPerMcu is 2). 

## When to use maxAutoscalingTaskCount
<a name="msk-connect-max-autoscaling-task-count-when-to-use"></a>

Consider using `maxAutoscalingTaskCount` in the following scenarios:
+ *Limited partition count*: When your Kafka topics have a fixed number of partitions that is lower than the automatically calculated task count, setting a limit prevents the creation of idle tasks with no work to perform.
+ *Performance optimization*: When you've identified that a specific task count provides optimal throughput for your workload, you can cap the maximum tasks to maintain consistent performance.
+ *Resource management*: When you want to control the maximum parallelism and resource consumption of your connector regardless of how many workers are running.

## Example
<a name="msk-connect-max-autoscaling-task-count-example"></a>

For a connector with the following configuration:

```
minWorkerCount: 1
maxWorkerCount: 4
mcuCount: 8
maxAutoscalingTaskCount: 15
```

Without `maxAutoscalingTaskCount`, when scaled to 4 workers, the connector would create 64 tasks (4 workers × 8 MCUs × 2 tasks per MCU). With `maxAutoscalingTaskCount` set to 15, the connector creates only 15 tasks, which may be more appropriate if your Kafka topic has 15 or fewer partitions.