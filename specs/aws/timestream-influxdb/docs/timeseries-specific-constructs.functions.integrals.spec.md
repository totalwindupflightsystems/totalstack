---
id: "@specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.integrals"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Integrals"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Integrals

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/timeseries-specific-constructs.functions.integrals
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Integral functions
<a name="timeseries-specific-constructs.functions.integrals"></a>

You can use integrals to find the area under the curve per unit of time for your time series events. As an example, suppose you're tracking the volume of requests received by your application per unit of time. In this scenario, you can use the integral function to determine the total volume of requests served per specified interval over a specific time period.

Amazon Timestream supports one variant of integral functions. This section provides usage information for the Timestream for LiveAnalytics integral function, as well as sample queries. 



## Usage information
<a name="w2aab7c59c13c13c15b9"></a>


| Function | Output data type | Description | 
| --- | --- | --- | 
| `integral_trapezoidal(timeseries(double))`<br />`integral_trapezoidal(timeseries(double), interval day to second)`<br />`integral_trapezoidal(timeseries(bigint))`<br />`integral_trapezoidal(timeseries(bigint), interval day to second)`<br />`integral_trapezoidal(timeseries(integer), interval day to second)`<br />`integral_trapezoidal(timeseries(integer))` | double | Approximates the [integral](https://wikipedia.org/wiki/Integral) per the specified `interval day to second` for the `timeseries` provided, using the [trapezoidal rule](https://wikipedia.org/wiki/Trapezoidal_rule). The interval day to second parameter is optional and the default is `1s`. For more information about intervals, see [Interval and duration](date-time-functions.md#date-time-functions-interval-duration). | 

## Query examples
<a name="w2aab7c59c13c13c15c11"></a>

**Example**  
Calculate the total volume of requests served per five minutes over the past hour by a specific host:  

```
SELECT INTEGRAL_TRAPEZOIDAL(CREATE_TIME_SERIES(time, measure_value::double), 5m) AS result FROM sample.DevOps 
WHERE measure_name = 'request' 
AND hostname = 'host-Hovjv' 
AND time > ago (1h) 
GROUP BY hostname, measure_name
```