---
id: "@specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.correlation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Correlation"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Correlation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.correlation
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Correlation functions
<a name="timeseries-specific-constructs.functions.correlation"></a>

Given two similar length time series, correlation functions provide a correlation coefficient, which explains how the two time series trend over time. The correlation coefficient ranges from `-1.0` to `1.0`. `-1.0` indicates that the two time series trend in opposite directions at the same rate. whereas `1.0` indicates that the two timeseries trend in the same direction at the same rate. A value of `0` indicates no correlation between the two time series. For example, if the price of oil increases, and the stock price of an oil company increases, the trend of the price increase of oil and the price increase of the oil company will have a positive correlation coefficient. A high positive correlation coefficient would indicate that the two prices trend at a similar rate. Similarly, the correlation coefficient between bond prices and bond yields is negative, indicating that these two values trends in the opposite direction over time.

Amazon Timestream supports two variants of correlation functions. This section provides usage information for the Timestream for LiveAnalytics correlation functions, as well as sample queries. 



## Usage information
<a name="w2aab7c59c13c13c19c11"></a>


| Function | Output data type | Description | 
| --- | --- | --- | 
| `correlate_pearson(timeseries, timeseries)` | double | Calculates [Pearson's correlation coefficient](https://wikipedia.org/wiki/Pearson_correlation_coefficient) for the two `timeseries`. The timeseries must have the same timestamps. | 
| `correlate_spearman(timeseries, timeseries)` | double | Calculates [Spearman's correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) for the two `timeseries`. The timeseries must have the same timestamps. | 

## Query examples
<a name="w2aab7c59c13c13c19c13"></a>

**Example**  

```
WITH cte_1 AS (
    SELECT INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(time, measure_value::double), 
        SEQUENCE(min(time), max(time), 10m)) AS result 
    FROM sample.DevOps 
    WHERE measure_name = 'cpu_utilization' 
    AND hostname = 'host-Hovjv' AND time > ago(1h) 
    GROUP BY hostname, measure_name
), 
cte_2 AS (
    SELECT INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(time, measure_value::double), 
        SEQUENCE(min(time), max(time), 10m)) AS result 
    FROM sample.DevOps 
    WHERE measure_name = 'cpu_utilization' 
    AND hostname = 'host-Hovjv' AND time > ago(1h) 
    GROUP BY hostname, measure_name
) 
SELECT correlate_pearson(cte_1.result, cte_2.result) AS result 
FROM cte_1, cte_2
```