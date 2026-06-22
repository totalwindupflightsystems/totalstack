---
id: "@specs/aws/timestream-influxdb/docs/supported-data-types"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Supported data types"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Supported data types

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-data-types
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Supported data types
<a name="supported-data-types"></a>

Timestream for LiveAnalytics's query language supports the following data types.

**Note**  
Data types supported for writes are described in [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types).


| Data type | Description | 
| --- | --- | 
| `int` | Represents a 32-bit integer. | 
| `bigint` | Represents a 64-bit signed integer. | 
| `boolean` | One of the two truth values of logic, `True` and `False`. | 
| `double` | Represents a 64-bit variable-precision data type. Implements [IEEE Standard 754 for Binary Floating-Point Arithmetic](https://standards.ieee.org/standard/754-2019.html). The query language is for reading data. There are functions for `Infinity` and `NaN` double values which can be used in queries. But you cannot write those values to Timestream.  | 
| `varchar` | Variable length character data with a maximum size of 2KB. | 
| `array[{{T}},...]` | Contains one or more elements of a specified data type {{T}}, where {{T}} can be any of the data types supported in Timestream. | 
|  `row({{T}},...)`  | Contains one or more named fields of data type {{T}}. The fields may be of any data type supported by Timestream, and are accessed with the dot field reference operator:<pre>.</pre> | 
| `date` | Represents a date in the form `{{YYYY}}-{{MM}}-{{DD}}`. where {{YYYY}} is the year, {{MM}} is the month, and {{DD}} is the day, respectively. The supported range is from `1970-01-01` to `2262-04-11`. <br /> *Example:* <pre>1971-02-03</pre> | 
| `time` | Represents the time of day in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). The `time` datatype is represented in the form `{{HH}}.{{MM}}.{{SS}}.{{sssssssss}}.` Supports nanosecond precision. <br /> *Example:* <pre>17:02:07.496000000</pre> | 
| `timestamp` | Represents an instance in time using nanosecond precision time in UTC.<br />`{{YYYY}}-{{MM}}-{{DD}} {{hh}}:{{mm}}:{{ss}}.{{sssssssss}}`<br />Query supports timestamps in the range `1677-09-21 00:12:44.000000000` to `2262-04-11 23:47:16.854775807`. | 
| `interval` | Represents an interval of time as a string literal `{{Xt}}`, composed of two parts, {{X}} and {{t}}.<br /> {{X}} is an numeric value greater than or equal to `0`, and {{t}} is a unit of time like second or hour. The unit is not pluralized. The unit of time {{t}} is must be one of the following string literals: [See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html)<br /> *Examples:* <pre>17s</pre><pre>12second</pre><pre>21hour</pre><pre>2d</pre> | 
| `timeseries[row(timestamp, {{T}},...)]` | Represents the values of a measure recorded over a time interval as an `array` composed of `row` objects. Each `row` contains a `timestamp` and one or more measure values of data type {{T}}, where {{T}} can be any one of `bigint`, `boolean`, `double`, or `varchar`. Rows are assorted in ascending order by `timestamp`. The *timeseries* datatype represents the values of a measure over time. | 
| `unknown` | Represents null data. | 