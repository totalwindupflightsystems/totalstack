---
id: "@specs/aws/timestream-influxdb/docs/Telegraf.how-it-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Mapping Telegraf/InfluxDB metrics to Timestream for LiveAnalytics"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Mapping Telegraf/InfluxDB metrics to Timestream for LiveAnalytics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Telegraf.how-it-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Mapping Telegraf/InfluxDB metrics to the Timestream for LiveAnalytics model
<a name="Telegraf.how-it-works"></a>

 When writing data from Telegraf to Timestream for LiveAnalytics, the data is mapped as follows.
+ The timestamp is written as the time field.
+ Tags are written as dimensions.
+ Fields are written as measures.
+ Measurements are mostly written as table names (more on this below).

The Timestream for LiveAnalytics output plugin for Telegraf offers multiple options for organizing and storing data in Timestream for LiveAnalytics. This can be described with an example which begins with the data in line protocol format.

`weather,location=us-midwest,season=summer temperature=82,humidity=71 1465839830100400200 airquality,location=us-west no2=5,pm25=16 1465839830100400200`

The following describes the data.
+ The measurement names are `weather` and `airquality`.
+ The tags are `location` and `season`.
+ The fields are `temperature`, `humidity`, `no2`, and `pm25`.

**Topics**
+ [Storing the data in multiple tables](#Telegraf.how-it-works.multi-table-single-measure.title)
+ [Storing the data in a single table](#Telegraf.how-it-works.single-table-single-measure.title)

## Storing the data in multiple tables
<a name="Telegraf.how-it-works.multi-table-single-measure.title"></a>

You can choose to create a separate table per measurement and store each field in a separate row per table.

The configuration is `mapping_mode = "multi-table"`.
+ The Timestream for LiveAnalytics adapter will create two tables, namely, `weather` and `airquality`.
+ Each table row will contain a single field only.

The resulting Timestream for LiveAnalytics tables, `weather` and `airquality`, will look like this.


**`weather`**  

| time | location | season | measure\_name | measure\_value::bigint | 
| --- | --- | --- | --- | --- | 
| 2016-06-13 17:43:50 | us-midwest | summer | temperature | 82 | 
| 2016-06-13 17:43:50 | us-midwest | summer | humidity | 71 | 


**`airquality`**  

| time | location | measure\_name | measure\_value::bigint | 
| --- | --- | --- | --- | 
| 2016-06-13 17:43:50 | us-midwest | no2  | 5 | 
| 2016-06-13 17:43:50 | us-midwest | pm25  | 16 | 

## Storing the data in a single table
<a name="Telegraf.how-it-works.single-table-single-measure.title"></a>

You can choose to store all the measurements in a single table and store each field in a separate table row.

The configuration is `mapping_mode = "single-table"`. There are two addition configurations when using `single-table`, `single_table_name` and `single_table_dimension_name_for_telegraf_measurement_name`.
+ The Timestream for LiveAnalytics output plugin will create a single table with name {{<single\_table\_name>}} which includes a {{<single\_table\_dimension\_name\_for\_telegraf\_measurement\_name>}} column.
+ The table may contain multiple fields in a single table row.

The resulting Timestream for LiveAnalytics table will look like this.


**`weather`**  

| time | location | season | {{<single\_table\_dimension\_name\_ for\_telegraf\_measurement\_name>}} | measure\_name | measure\_value::bigint | 
| --- | --- | --- | --- | --- | --- | 
| 2016-06-13 17:43:50 | us-midwest | summer | weather | temperature | 82 | 
| 2016-06-13 17:43:50 | us-midwest | summer | weather | humidity | 71 | 
| 2016-06-13 17:43:50 | us-midwest | summer | airquality | no2 | 5 | 
| 2016-06-13 17:43:50 | us-midwest | summer | weather | pm25 | 16 | 