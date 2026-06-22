---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-example2"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Drill down"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Drill down

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-example2
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Using scheduled queries and raw data for drill downs
<a name="scheduledqueries-example2"></a>

You can use the aggregated statistics across your fleet to identify areas that need drill downs and then use the raw data to drill down into granular data to get deeper insights.

In this example, you will see how you can use aggregate dashboard to identify any deployment (a deployment is for a given microservice within a given region, cell, silo, and availability zone) which seems to have higher CPU utilization compared to other deployments. You can then drill down to get a better understanding using the raw data. Since these drill downs might be infrequent and only access data relevant to the deployment, you can use the raw data for this analysis and do not need to use scheduled queries. 

**Per deployment drill down**

The dashboard below provides drill down into more granular and server-level statistics within a given deployment. To help you drill down into the different parts of your fleet, this dashboard uses variables such as region, cell, silo, microservice, and availability\_zone. It then shows some aggregate statistics for that deployment.

![Dashboard showing deployment statistics with filters for region, cell, silo, and other parameters.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/sched_query_ex2_img1.png)


![CPU distribution graph showing consistent patterns for avg, p90, p95, and p99 values over 24 hours.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/sched_query_ex2_img2.png)


In the query below, you can see that the values chosen in the drop down of the variables are used as predicates in the `WHERE` clause of the query, which allows you to only focus on the data for the deployment. And then the panel plots the aggregated CPU metrics for instances in that deployment. You can use the raw data to perform this drill down with interactive query latency to derive deeper insights.

```
SELECT bin(time, 5m) as minute,
    ROUND(AVG(cpu_user), 2) AS avg_value,
    ROUND(APPROX_PERCENTILE(cpu_user, 0.9), 2) AS p90_value,
    ROUND(APPROX_PERCENTILE(cpu_user, 0.95), 2) AS p95_value,
    ROUND(APPROX_PERCENTILE(cpu_user, 0.99), 2) AS p99_value
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099476) AND from_milliseconds(1636613499476)
    AND region = 'eu-west-1'
    AND cell = 'eu-west-1-cell-10'
    AND silo = 'eu-west-1-cell-10-silo-1'
    AND microservice_name = 'demeter'
    AND availability_zone = 'eu-west-1-3'
    AND measure_name = 'metrics'
GROUP BY bin(time, 5m)
ORDER BY 1
```

**Instance-level statistics**

This dashboard further computes another variable that also lists the servers/instances with high CPU utilization, sorted in descending order of utilization. The query used to compute this variable is displayed below.

```
WITH microservice_cell_avg AS (
    SELECT AVG(cpu_user) AS microservice_avg_metric
    FROM "raw_data"."devops"
    WHERE $__timeFilter
        AND measure_name = 'metrics'
        AND region = '${region}'
        AND cell = '${cell}'
        AND silo = '${silo}'
        AND availability_zone = '${availability_zone}'
        AND microservice_name = '${microservice}'
), instance_avg AS (
    SELECT instance_name,
        AVG(cpu_user) AS instance_avg_metric
    FROM "raw_data"."devops"
    WHERE $__timeFilter
        AND measure_name = 'metrics'
        AND region = '${region}'
        AND cell = '${cell}'
        AND silo = '${silo}'
        AND microservice_name = '${microservice}'
        AND availability_zone = '${availability_zone}'
    GROUP BY availability_zone, instance_name
) 
SELECT i.instance_name
FROM instance_avg i CROSS JOIN microservice_cell_avg m 
WHERE i.instance_avg_metric > (1 + ${utilization_threshold}) * m.microservice_avg_metric
ORDER BY i.instance_avg_metric DESC
```

In the preceding query, the variable is dynamically recalculated depending on the values chosen for the other variables. Once the variable is populated for a deployment, you can pick individual instances from the list to further visualize the metrics from that instance. You can pick the different instances from the drop down of the instance names as seen from the snapshot below.

![List of AWS instance hostnames in eu-west-1 region with different silo identifiers.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/sched_query_ex2_img3.png)


![Instance statistics dashboard showing CPU at 95%, memory at 100%, 1826 GC pause events, and disk IO metrics.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/sched_query_ex2_img4.png)


Preceding panels show the statistics for the instance that is selected and below are the queries used to fetch these statistics.

```
SELECT BIN(time, 30m) AS time_bin, 
    AVG(cpu_user) AS avg_cpu,
    ROUND(APPROX_PERCENTILE(cpu_user, 0.99), 2) as p99_cpu
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099477) AND from_milliseconds(1636613499477)
    AND measure_name = 'metrics'
    AND region = 'eu-west-1' AND cell = 'eu-west-1-cell-10' AND silo = 'eu-west-1-cell-10-silo-1' 
    AND availability_zone = 'eu-west-1-3' AND microservice_name = 'demeter' 
    AND instance_name = 'i-zaZswmJk-demeter-eu-west-1-cell-10-silo-1-00000272.amazonaws.com'
GROUP BY BIN(time, 30m)
ORDER BY time_bin desc
```

```
SELECT BIN(time, 30m) AS time_bin, 
    AVG(memory_used) AS avg_memory,
    ROUND(APPROX_PERCENTILE(memory_used, 0.99), 2) as p99_memory
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099477) AND from_milliseconds(1636613499477)
    AND measure_name = 'metrics'
    AND region = 'eu-west-1' AND cell = 'eu-west-1-cell-10' AND silo = 'eu-west-1-cell-10-silo-1' 
    AND availability_zone = 'eu-west-1-3' AND microservice_name = 'demeter' 
    AND instance_name = 'i-zaZswmJk-demeter-eu-west-1-cell-10-silo-1-00000272.amazonaws.com'
GROUP BY BIN(time, 30m)
ORDER BY time_bin desc
```

```
SELECT COUNT(gc_pause)
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099477) AND from_milliseconds(1636613499478)
    AND measure_name = 'events'
    AND region = 'eu-west-1' AND cell = 'eu-west-1-cell-10' AND silo = 'eu-west-1-cell-10-silo-1' 
    AND availability_zone = 'eu-west-1-3' AND microservice_name = 'demeter' 
    AND instance_name = 'i-zaZswmJk-demeter-eu-west-1-cell-10-silo-1-00000272.amazonaws.com'
```

```
SELECT avg(gc_pause) as avg, round(approx_percentile(gc_pause, 0.99), 2) as p99
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099478) AND from_milliseconds(1636613499478)
    AND measure_name = 'events'
    AND region = 'eu-west-1' AND cell = 'eu-west-1-cell-10' AND silo = 'eu-west-1-cell-10-silo-1' 
    AND availability_zone = 'eu-west-1-3' AND microservice_name = 'demeter' 
    AND instance_name = 'i-zaZswmJk-demeter-eu-west-1-cell-10-silo-1-00000272.amazonaws.com'
```

```
SELECT BIN(time, 30m) AS time_bin, 
    AVG(disk_io_reads) AS avg,
    ROUND(APPROX_PERCENTILE(disk_io_reads, 0.99), 2) as p99
FROM "raw_data"."devops"
WHERE time BETWEEN from_milliseconds(1636527099478) AND from_milliseconds(1636613499478)
    AND measure_name = 'metrics'
    AND region = 'eu-west-1' AND cell = 'eu-west-1-cell-10' AND silo = 'eu-west-1-cell-10-silo-1' 
    AND availability_zone = 'eu-west-1-3' AND microservice_name = 'demeter' 
    AND instance_name = 'i-zaZswmJk-demeter-eu-west-1-cell-10-silo-1-00000272.amazonaws.com'
GROUP BY BIN(time, 30m)
ORDER BY time_bin desc
```