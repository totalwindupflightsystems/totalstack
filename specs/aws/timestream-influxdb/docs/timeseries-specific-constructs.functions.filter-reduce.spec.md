---
id: "@specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.filter-reduce"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Filter and reduce"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Filter and reduce

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.filter-reduce
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Filter and reduce functions
<a name="timeseries-specific-constructs.functions.filter-reduce"></a>

Amazon Timestream supports functions for performing filter and reduce operations on time series data. This section provides usage information for the Timestream for LiveAnalytics filter and reduce functions, as well as sample queries. 



## Usage information
<a name="w2aab7c59c13c13c23b7"></a>


| Function | Output data type | Description | 
| --- | --- | --- | 
| `filter(timeseries(T), function(T, Boolean))` | timeseries(T) | Constructs a time series from an the input time series, using values for which the passed `function` returns `true`. | 
| `reduce(timeseries(T), initialState S, inputFunction(S, T, S), outputFunction(S, R))` | R | Returns a single value, reduced from the time series. The `inputFunction` will be invoked on each element in timeseries in order. In addition to taking the current element, inputFunction takes the current state (initially `initialState`) and returns the new state. The `outputFunction` will be invoked to turn the final state into the result value. The `outputFunction` can be an identity function. | 

## Query examples
<a name="w2aab7c59c13c13c23b9"></a>

**Example**  
Construct a time series of CPU utilization of a host and filter points with measurement greater than 70:  

```
WITH time_series_view AS (
    SELECT INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(time, ROUND(measure_value::double,2)), 
            SEQUENCE(ago(15m), ago(1m), 10s)) AS cpu_user
    FROM sample.DevOps
    WHERE hostname = 'host-Hovjv' and measure_name = 'cpu_utilization'
        AND time > ago(30m)
    GROUP BY hostname
)
SELECT FILTER(cpu_user, x -> x.value > 70.0) AS cpu_above_threshold
from time_series_view
```

**Example**  
Construct a time series of CPU utilization of a host and determine the sum squared of the measurements:  

```
WITH time_series_view AS (
    SELECT INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(time, ROUND(measure_value::double,2)), 
            SEQUENCE(ago(15m), ago(1m), 10s)) AS cpu_user
    FROM sample.DevOps
    WHERE hostname = 'host-Hovjv' and measure_name = 'cpu_utilization'
        AND time > ago(30m)
    GROUP BY hostname
)
SELECT REDUCE(cpu_user,
    DOUBLE '0.0',
    (s, x) -> x.value * x.value + s,
    s -> s)
from time_series_view
```

**Example**  
Construct a time series of CPU utilization of a host and determine the fraction of samples that are above the CPU threshold:  

```
WITH time_series_view AS (
    SELECT INTERPOLATE_LINEAR(
        CREATE_TIME_SERIES(time, ROUND(measure_value::double,2)), 
            SEQUENCE(ago(15m), ago(1m), 10s)) AS cpu_user
    FROM sample.DevOps
    WHERE hostname = 'host-Hovjv' and measure_name = 'cpu_utilization'
        AND time > ago(30m)
    GROUP BY hostname
)
SELECT ROUND(
    REDUCE(cpu_user, 
      -- initial state 
      CAST(ROW(0, 0) AS ROW(count_high BIGINT, count_total BIGINT)),
      -- function to count the total points and points above a certain threshold
      (s, x) -> CAST(ROW(s.count_high + IF(x.value > 70.0, 1, 0), s.count_total + 1) AS ROW(count_high BIGINT, count_total BIGINT)),
      -- output function converting the counts to fraction above threshold
      s -> IF(s.count_total = 0, NULL, CAST(s.count_high AS DOUBLE) / s.count_total)), 
    4) AS fraction_cpu_above_threshold
from time_series_view
```