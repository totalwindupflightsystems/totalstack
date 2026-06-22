---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-schedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Schedule expressions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Schedule expressions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-schedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Schedule expressions for scheduled queries
<a name="scheduledqueries-schedule"></a>

You can create scheduled queries on an automated schedule by using Amazon Timestream for LiveAnalytics scheduled queries that use cron or rate expressions. All scheduled queries use the UTC time zone, and the minimum possible precision for schedules is 1 minute. 

Two ways to specify the schedule expressions are *cron* and *rate*. Cron expressions offer more fine grained schedule control, while rate expressions are simpler to express but lack the fine-grained control. 

For example, with a cron expression, you can define a scheduled query that gets triggered at a specified time on a certain day of each week or month, or a specified minute every hour only on Monday - Friday, and so on. In contrast, rate expressions initiate a scheduled query at a regular rate, such as once every minute, hour, or day, starting from the exact time when the scheduled query is created.

**Cron expression**
+ *Syntax*

  ```
  cron(fields)
  ```

  Cron expressions have six required fields, which are separated by white space.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-schedule.html)

**Wildcard characters**
  + The \*,\* (comma) wildcard includes additional values. In the Month field, JAN,FEB,MAR would include January, February, and March.
  + The \*-\* (dash) wildcard specifies ranges. In the Day field, 1-15 would include days 1 through 15 of the specified month. 
  + The \*\*\* (asterisk) wildcard includes all values in the field. In the Hours field, \*\*\* would include every hour. You cannot use \*\*\* in both the Day-of-month and Day-of-week fields. If you use it in one, you must use \*?\* in the other.
  + The \*/\* (forward slash) wildcard specifies increments. In the Minutes field, you could enter 1/10 to specify every 10th minute, starting from the first minute of the hour (for example, the 11th, 21st, and 31st minute, and so on). 
  + The \*?\* (question mark) wildcard specifies one or another. In the Day-of-month field you could enter \*7\* and if you didn't care what day of the week the 7th was, you could enter \*?\* in the Day-of-week field.
  + The \*L\* wildcard in the Day-of-month or Day-of-week fields specifies the last day of the month or week. 
  + The W wildcard in the Day-of-month field specifies a weekday. In the Day-of-month field, 3W specifies the weekday closest to the third day of the month. 
  + The \*\#\* wildcard in the Day-of-week field specifies a certain instance of the specified day of the week within a month. For example, 3\#2 would be the second Tuesday of the month: the 3 refers to Tuesday because it is the third day of each week, and the 2 refers to the second day of that type within the month. 
**Note**  
If you use a '\#' character, you can define only one expression in the day-of-week field. For example, "3\#1,6\#3" is not valid because it is interpreted as two expressions. 

**Limitations**
  + You can't specify the Day-of-month and Day-of-week fields in the same cron expression. If you specify a value (or a \*) in one of the fields, you must use a \*?\* (question mark) in the other.
  + Cron expressions that lead to rates faster than 1 minute are not supported.

  **Examples**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-schedule.html)

**Rate expressions**
+ A rate expression starts when you create the scheduled event rule, and then runs on its defined schedule. Rate expressions have two required fields. Fields are separated by white space. 

  *Syntax*

  ```
  rate(value unit)
  ```
  + `value`: A positive number.
  + `unit`: The unit of time. Different units are required for values of 1 (for example, minute) and values over 1 (for example, minutes). Valid values: minute \| minutes \| hour \| hours \| day \| days