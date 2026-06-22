---
id: "@specs/aws/opensearchserverless/docs/supported-ppl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Supported PPL commands"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Supported PPL commands

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/supported-ppl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Supported PPL commands
<a name="supported-ppl"></a>

The following tables show which PPL commands OpenSearch Dashboards supports for querying CloudWatch Logs, Amazon S3, or Security Lake, and which commands CloudWatch Logs Insights supports. CloudWatch Logs Insights uses the same PPL syntax as OpenSearch Dashboards when querying CloudWatch Logs, and the tables refer to both as CloudWatch Logs. 

**Note**  
When you analyze data outside of OpenSearch Service, commands might execute differently than they do on OpenSearch indexes.

**Topics**
+ [Commands](#supported-ppl-commands)
+ [Functions](#supported-ppl-functions)
+ [Additional information for CloudWatch Logs Insights users using OpenSearch PPL](#supported-ppl-for-cloudwatch-users)

## Commands
<a name="supported-ppl-commands"></a>


| PPL command | Description | CloudWatch Logs | Amazon S3 | Security Lake | Example command | 
| --- | --- | --- | --- | --- | --- | 
| [fields command](#supported-ppl-fields-command) | Displays a set of fields that needs projection. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> fields field1, field2</pre>  | 
| [where command](#supported-ppl-where-command) | Filters the data based on the conditions that you specify. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> where field1="success"<br />| where field2 != "i -023fe0a90929d8822"<br />| fields field3, col4, col5, col6<br />| head 1000</pre>  | 
| [stats command](#supported-ppl-stats-command) | Performs aggregations and calculations. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>stats count(),<br />      count(`field1`),<br />      min(`field1`),<br />      max(`field1`),<br />      avg(`field1`)<br />by field2<br />| head 1000</pre>  | 
| [parse command](#supported-ppl-parse-command) | Extracts a regular expression (regex) pattern from a string and displays the extracted pattern. The extracted pattern can be further used to create new fields or filter data. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>parse `field1` ".*/(?<field2>[^/]+$)"<br />| where field2 = "requestId"<br />| fields field2, `field2`<br />| head 1000</pre>  | 
| [patterns command](#supported-ppl-patterns-command) | Extracts log patterns from a text field and appends the results to the search result. Grouping logs by their patterns makes it easier to aggregate stats from large volumes of log data for analysis and troubleshooting. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>patterns new_field='no_numbers' pattern='[0-9]' message<br />| fields message, no_numbers</pre>  | 
| [sort command](#supported-ppl-sort-command) | Sort the displayed results by a field name. Use** sort -*FieldName*** to sort in descending order. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>stats count(),<br />      count(`field1`),<br />      min(`field1`) as field1Alias,<br />      max(`field1`),<br />      avg(`field1`)<br />by field2<br />| sort -field1Alias<br />| head 1000</pre>  | 
| [eval command](#supported-ppl-eval-command) | Modifies or processes the value of a field and stores it in a different field. This is useful to mathematically modify a column, apply string functions to a column, or apply date functions to a column. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval field2 = `field1` * 2<br />| fields field1, field2<br />| head 20</pre>  | 
| [rename command](#supported-ppl-rename-command) | Renames one or more fields in the search result. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>rename field2 as field1<br />| fields field1</pre>  | 
| [head command](#supported-ppl-head-command) | Limits the displayed query results to the frst N rows. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> fields `@message`<br />| head 20</pre>  | 
| [grok command](#supported-ppl-grok-command) | Parses a text field with a grok pattern based on regular expression, and appends the results to the search result. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> grok email '.+@%{HOSTNAME:host}'<br />| fields email</pre>  | 
| [top command](#supported-ppl-top-command) | Finds the most frequent values for a field. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> top 2 Field1 by Field2</pre>  | 
| [dedup command](#supported-ppl-dedup-command) | Removes duplicate entries based on the fields that you specify. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>dedup field1<br />| fields field1, field2, field3</pre>  | 
| [join command](#supported-ppl-join-commands) | Joins two datasets together. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>source=customer<br />| join ON c_custkey = o_custkey orders<br />| head 10</pre>  | 
| [lookup command](#supported-ppl-lookup-commands) | Enriches your search data by adding or replacing data from a lookup index (dimension table). You can extend fields of an index with values from a dimension table, append or replace values when lookup condition is matched | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>where orderType = 'Cancelled'<br />| lookup account_list, mkt_id AS mkt_code<br />  replace amount, account_name as name<br />| stats count(mkt_code), avg(amount)<br />  by name</pre>  | 
| [subquery command](#supported-ppl-subquery-commands) | Performs complex, nested queries within your Piped Processing Language (PPL) statements. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>where id in [<br />  subquery source=users<br />  | where user in [<br />    subquery source=actions<br />    | where action="login"<br />    | fields user<br />  ]<br />  | fields uid<br />]</pre>  | 
| [rare command](#supported-ppl-rare-command) | Finds the least frequent values of all fields in the field list. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> rare Field1 by Field2</pre>  | 
| [trendline command](#supported-ppl-trendline-commands) | Calculates the moving averages of fields. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> trendline sma(2, field1) as field1Alias</pre>  | 
| [eventstats command](#supported-ppl-eventstats-command) | Enriches your event data with calculated summary statistics. It analyzes specified fields within your events, computes various statistical measures, and then appends these results to each original event as new fields. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported (except `count()`) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> eventstats sum(field1) by field2</pre>  | 
| [flatten command](#supported-ppl-flatten-command) | Flattens a field, The field must be of this type: `struct<?,?> or array<struct<?,?>>` | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> source=table | flatten field1</pre>  | 
| [field summary](#supported-ppl-field-summary-command) | Calculates basic statistics for each field (count, distinct count, min, max, avg, stddev, and mean). | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported (one field per query) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>where field1 != 200<br />| fieldsummary includefields=field1 nulls=true</pre>  | 
| [fillnull command](#supported-ppl-fillnull-command) | Fills null fields with the value that you provide. It can be used in one or more fields. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>fields field1<br />| eval field2=field1<br />| fillnull value=0 field1</pre>  | 
| [expand command](#supported-ppl-expand-command) | Breaks down a field containing multiple values into separate rows, creating a new row for each value in the specified field. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>expand employee<br />| stats max(salary) as max<br />  by state, company</pre>  | 
| [describe command](#supported-ppl-describe-command) | Gets detailed information about the structure and metadata of tables, schemas, and catalogs | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> describe schema.table</pre>  | 

## Functions
<a name="supported-ppl-functions"></a>


| PPL function | Description | CloudWatch Logs | Amazon S3 | Security Lake | Example command | 
| --- | --- | --- | --- | --- | --- | 
| [PPL string functions](#supported-ppl-string-functions)<br />(`CONCAT`, `CONCAT_WS`, `LENGTH`, `LOWER`, `LTRIM`, `POSITION`, `REVERSE`, `RIGHT`, `RTRIM`, `SUBSTRING`, `TRIM`, `UPPER`) | Built-in functions in PPL that can manipulate and transform string and text data within PPL queries. For example, converting case, combining strings, extracting parts, and cleaning text. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval col1Len = LENGTH(col1)<br />| fields col1Len</pre>  | 
| [PPL date and time functions](#supported-ppl-date-time-functions)<br />(`DAY`, `DAYOFMONTH`, `DAY_OF_MONTH`,`DAYOFWEEK`, `DAY_OF_WEEK`, `DAYOFYEAR`, `DAY_OF_YEAR`, `DAYNAME`, `FROM_UNIXTIME`, `HOUR`, `HOUR_OF_DAY`, `LAST_DAY`, `LOCALTIMESTAMP`, `LOCALTIME`, `MAKE_DATE`, `MINUTE`, `MINUTE_OF_HOUR`, `MONTH`, `MONTHNAME`, `MONTH_OF_YEAR`, `NOW`, `QUARTER`, `SECOND`, `SECOND_OF_MINUTE`, `SUBDATE`, `SYSDATE`, `TIMESTAMP`, `UNIX_TIMESTAMP`, `WEEK`, `WEEKDAY`, `WEEK_OF_YEAR`, `DATE_ADD`, `DATE_SUB`, `TIMESTAMPADD`, `TIMESTAMPDIFF`, `UTC_TIMESTAMP`, `CURRENT_TIMEZONE`) | Built-in functions for handling and transforming date and timestamp data in PPL queries. For example, **date\_add**, **date\_format**, **datediff**, and **current\_date**. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval newDate = ADDDATE(DATE('2020-08-26'), 1)<br />| fields newDate</pre>  | 
| [PPL condition functions](#supported-ppl-condition-functions)<br />(`EXISTS`, `IF`, `IFNULL`, `ISNOTNULL`, `ISNULL`, `NULLIF`) | Built-in functions that perform calculations on multiple rows to produce a single summarized value. For example, **sum**, **count**, **avg**, **max**, and **min**. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval field2 = isnull(col1)<br />| fields field2, col1, field3  </pre>  | 
| [PPL mathematical functions](#supported-ppl-math-functions)<br />(`ABS`, `ACOS`, `ASIN`, `ATAN`, `ATAN2`, `CEIL`, `CEILING`, `CONV`, `COS`, `COT`, `CRC32`, `DEGREES`, `E`, `EXP`, `FLOOR`, `LN`, `LOG`, `LOG2`, `LOG10`, `MOD`, `PI`. `POW`, `POWER`, `RADIANS`, `RAND`, `ROUND`, `SIGN`, `SIN`, `SQRT`, `CBRT`) | Built-in functions for performing mathematical calculations and transformations in PPL queries. For example: **abs** (absolute value), **round** (rounds numbers), **sqrt** (square root), **pow** (power calculation), and **ceil** (rounds up to nearest integer). | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval field2 = ACOS(col1)<br />| fields col1</pre>  | 
| [PPL expressions](#supported-ppl-expressions)<br />(Arithmetic operators (`+`, `-`, `*`), Predicate operators (`>. <`, `IN)`) | Built-in functions for expressions, particularly value expressions, return a scalar value. Expressions have different types and forms. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>where age > (25 + 5)<br />| fields age  </pre>  | 
| [PPL IP address functions](#supported-ppl-ip-address-functions)<br />(`CIDRMATCH`) | Built-in functions for handling IP addresses such as CIDR. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>where cidrmatch(ip, '***********/24')<br />| fields ip </pre>  | 
| [PPL JSON functions](#supported-ppl-json-functions)<br />(`ARRAY_LENGTH`, `ARRAY_LENGTH`, `JSON`, `JSON_ARRAY`, `JSON_EXTRACT`, `JSON_KEYS`, `JSON_OBJECT`, `JSON_VALID`, `TO_JSON_STRING`) | Built-in functions for handling JSON including arrays, extracting, and validation. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval `json_extract('{"a":"b"}', '$.a')` = json_extract('{"a":"b"}', '$a')</pre>  | 
| [PPL Lambda functions](#supported-ppl-lambda-functions)<br />(`EXISTS`, `FILTER`, `REDUCE`, `TRANSFORM`) | Built-in functions for handling JSON including arrays, extracting, and validation. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval array = json_array(1, -1, 2),<br />     result = filter(array, x -> x > 0)<br />| fields result</pre>  | 
| [PPL cryptographic hash functions](#supported-ppl-cryptographic-functions)<br />(`MD5`, `SHA1`, `SHA2`) | Built-in functions that allow you to generate unique fingerprints of data, which can be used for verification, comparison, or as part of more complex security protocols. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>eval `MD5('hello')` = MD5('hello')<br />| fields `MD5('hello')`</pre>  | 

## Additional information for CloudWatch Logs Insights users using OpenSearch PPL
<a name="supported-ppl-for-cloudwatch-users"></a>

Although CloudWatch Logs Insights supports most OpenSearch PPL commands and functions, some commands and functions aren't currently supported. For example, it doesn't currently support Lookup commands in PPL. As of June 2, 2025, CloudWatch Logs Insights now supports JOIN, subqueries, Flatten, Fillnull, Expand, Cidrmatch, and JSON functions in PPL. For a complete list of supported query commands and functions, see the Amazon CloudWatch Logs columns in the above tables.

### Sample queries and quotas
<a name="sample-queries"></a>

The following applies to both CloudWatch Logs Insights users and OpenSearch users querying CloudWatch data.

For information about the limits that apply when querying CloudWatch Logs from OpenSearch Service, see [CloudWatch Logs quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) in the Amazon CloudWatch Logs User Guide. Limits involve the number of CloudWatch Log groups you can query, the maximum concurrent queries that you can execute, the maximum query execution time, and the maximum number of rows returned in results. The limits are the same regardless of which language you use to query CloudWatch Logs (namely, OpenSearch PPL, SQL, and Logs Insights QL). 

### PPL commands
<a name="supported-ppl-commands-details"></a>

**Topics**
+ [comment](#supported-ppl-comment)
+ [correlation command](#supported-ppl-correlation-commands)
+ [dedup command](#supported-ppl-dedup-command)
+ [describe command](#supported-ppl-describe-command)
+ [eval command](#supported-ppl-eval-command)
+ [eventstats command](#supported-ppl-eventstats-command)
+ [expand command](#supported-ppl-expand-commands)
+ [explain command](#supported-ppl-explain-command)
+ [fillnull command](#supported-ppl-fillnull-command)
+ [fields command](#supported-ppl-fields-command)
+ [flatten command](#supported-ppl-flatten-command)
+ [grok command](#supported-ppl-grok-command)
+ [head command](#supported-ppl-head-command)
+ [join command](#supported-ppl-join-commands)
+ [lookup command](#supported-ppl-lookup-commands)
+ [parse command](#supported-ppl-parse-command)
+ [patterns command](#supported-ppl-patterns-command)
+ [rare command](#supported-ppl-rare-command)
+ [rename command](#supported-ppl-rename-command)
+ [search command](#supported-ppl-search-command)
+ [sort command](#supported-ppl-sort-command)
+ [stats command](#supported-ppl-stats-command)
+ [subquery command](#supported-ppl-subquery-commands)
+ [top command](#supported-ppl-top-command)
+ [trendline command](#supported-ppl-trendline-commands)
+ [where command](#supported-ppl-where-command)
+ [field summary](#supported-ppl-field-summary-command)
+ [expand command](#supported-ppl-expand-command)
+ [PPL functions](#supported-ppl-functions-details)

#### comment
<a name="supported-ppl-comment"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

PPL supports both line comments and block comments. The system doesn't evaluate comment text.

**Line comments**  
Line comments begin with two slashes // and end with a new line. 

Example: 

```
os> source=accounts | top gender // finds most common gender of all the accounts
fetched rows / total rows = 2/2
+----------+
| gender   |
|----------|
| M        |
| F        |
+----------+
```

**Block Comments**  
Block comments begin with a slash followed by an asterisk \\\*, and end with an asterisk followed by a slash \*/. 

Example:

```
os> source=accounts | dedup 2 gender /* dedup the document with gender field keep 2 duplication */ | fields account_number, gender
fetched rows / total rows = 3/3
+------------------+----------+
| account_number   | gender   |
|------------------+----------|
| 1                | M        |
| 6                | M        |
| 13               | F        |
+------------------+----------+
```

#### correlation command
<a name="supported-ppl-correlation-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

You can correlate different data sources according to common dimensions and timeframes. 

This correlation is crucial when you're dealing with large amounts of data from various verticals that share the same time periods but aren't formally synchronized.

By correlating these different data sources based on timeframes and similar dimensions, you can enrich your data and uncover valuable insights.

**Example**  
The observability domain has three distinct data sources:
+ Logs
+ Metrics
+ Traces

These data sources might share common dimensions. To transition from one data source to another, you need to correlate them correctly. Using semantic naming conventions, you can identify shared elements across logs, traces, and metrics.

Example:

```
{
  "@timestamp": "2018-07-02T22:23:00.186Z",
  "aws": {
    "elb": {
      "backend": {
        "http": {
          "response": {
            "status_code": 500
          }
        },
        "ip": "********",
        "port": "80"
      },
      ...
     "target_port": [
        "10.0.0.1:80"
      ],
      "target_status_code": [
        "500"
      ],
      "traceId": "Root=1-58337262-36d228ad5d99923122bbe354",
      "type": "http"
    }
  },
  "cloud": {
    "provider": "aws"
  },
  "http": {
    "request": {
    ...
  },
  "communication": {
    "source": {
      "address": "**************",
      "ip": "**************",
      "port": 2817
    }
  },
  "traceId": "Root=1-58337262-36d228ad5d99923122bbe354"
}
```

This example shows an AWS ELB log arriving from a service residing on AWS. It shows a backend HTTP response with a status code of 500, indicating an error. This could trigger an alert or be part of your regular monitoring process. Your next step is to gather relevant data around this event for a thorough investigation.

While you might be tempted to query all data related to the timeframe, this approach can be overwhelming. You could end up with too much information, spending more time filtering out irrelevant data than identifying the root cause. 

Instead, you can use a more targeted approach by correlating data from different sources. You can use these dimensions for correlation:
+ **IP** - `"ip": "10.0.0.1" | "ip": "**************"`
+ **Port** - `"port": 2817 | "target_port": "10.0.0.1:80"`

Assuming you have access to additional traces and metrics indices, and you're familiar with your schema structure, you can create a more precise correlation query.

Here's an example of a trace index document containing HTTP information you might want to correlate:

```
{
  "traceId": "c1d985bd02e1dbb85b444011f19a1ecc",
  "spanId": "55a698828fe06a42",
  "traceState": [],
  "parentSpanId": "",
  "name": "mysql",
  "kind": "CLIENT",
  "@timestamp": "2021-11-13T20:20:39+00:00",
  "events": [
    {
      "@timestamp": "2021-03-25T17:21:03+00:00",
       ...
    }
  ],
  "links": [
    {
      "traceId": "c1d985bd02e1dbb85b444011f19a1ecc",
      "spanId": "55a698828fe06a42w2",
      },
      "droppedAttributesCount": 0
    }
  ],
  "resource": {
    "service@name": "database",
    "telemetry@sdk@name": "opentelemetry",
    "host@hostname": "ip-172-31-10-8.us-west-2.compute.internal"
  },
  "status": {
    ...
  },
  "attributes": {
    "http": {
      "user_agent": {
        "original": "Mozilla/5.0"
      },
      "network": {
         ...
        }
      },
      "request": {
         ...
        }
      },
      "response": {
        "status_code": "200",
        "body": {
          "size": 500
        }
      },
      "client": {
        "server": {
          "socket": {
            "address": "***********",
            "domain": "example.com",
            "port": 80
          },
          "address": "***********",
          "port": 80
        },
        "resend_count": 0,
        "url": {
          "full": "http://example.com"
        }
      },
      "server": {
        "route": "/index",
        "address": "***********",
        "port": 8080,
        "socket": {
         ...
        },
        "client": {
         ...
         }
        },
        "url": {
         ...
        }
      }
    }
  }
}
```

In this approach you can see the `traceId` and the http's client/server `ip` that can be correlated with the elb logs to better understand the system's behaviour and condition.

**New correlation query command**  
Here is the new command that would allow this type of investigation:

```
source alb_logs, traces | where alb_logs.ip="10.0.0.1" AND alb_logs.cloud.provider="aws"| 
correlate exact fields(traceId, ip) scope(@timestamp, 1D) mapping(alb_logs.ip = traces.attributes.http.server.address, alb_logs.traceId = traces.traceId )
```

Here's what each part of the command does:

1. `source alb_logs, traces` - This selects the data sources that you want to correlate.

1. `where ip="10.0.0.1" AND cloud.provider="aws"` - This narrows down the scope of your search.

1. `correlate exact fields(traceId, ip)` - This tells the system to correlate data based on exact matches of the following fields:
   + The `ip` field has an explicit filter condition, so it will be used in the correlation for all data sources.
   + The `traceId` field has no explicit filter, so it will match the same traceIds across all data sources.

The field names indicate the logical meaning of the function within the correlation command. The actual join condition relies on the mapping statement you provide.

The term `exact` means that the correlation statements will require all fields to match in order to fulfill the query statement.

The term `approximate` will attempt to match on a best case scenario and will not reject rows with partial matches.

**Addressing different field mapping**  
In cases where the same logical field (such as `ip`) has different names across your data sources, you need to provide the explicit mapping of path fields. To address this, you can extend your correlation conditions to match different field names with similar logical meanings. Here's how you might do this:

```
alb_logs.ip = traces.attributes.http.server.address, alb_logs.traceId = traces.traceId    
```

For each field participating in the correlation join, you should provide a relevant mapping statement that includes all tables to be joined by this correlation command.

**Example**  
In this example, there are 2 sources: `alb_logs, traces`

There are 2 fields: `traceId, ip`

There are 2 mapping statements: `alb_logs.ip = traces.attributes.http.server.address, alb_logs.traceId = traces.traceId`

**Scoping the correlation timeframes**  
To simplify the work done by the execution engine (driver), you can add the scope statement. This explicitly directs the join query on the time it should scope for this search.

`scope(@timestamp, 1D)` i

In this example, the search scope focuses on a daily basis, so correlations appearing on the same day are grouped together. This scoping mechanism simplifies and allows better control over results, enabling incremental search resolution based on your needs.

**Supporting drivers**  
The new correlation command is actually a 'hidden' join command. Therefore, only the following PPL drivers support this command. In these drivers, the correlation command will be directly translated into the appropriate Catalyst Join logical plan.

**Example**  
`source alb_logs, traces, metrics | where ip="10.0.0.1" AND cloud.provider="aws"| correlate exact on (ip, port) scope(@timestamp, 2018-07-02T22:23:00, 1 D)`

**Logical Plan:**

```
'Project [*]
+- 'Join Inner, ('ip && 'port)
   :- 'Filter (('ip === "10.0.0.1" & 'cloud.provider === "aws") & inTimeScope('@timestamp, "2018-07-02T22:23:00", "1 D"))
      +- 'UnresolvedRelation [alb_logs]
   +- 'Join Inner, ('ip & 'port)
      :- 'Filter (('ip === "10.0.0.1" & 'cloud.provider === "aws") & inTimeScope('@timestamp, "2018-07-02T22:23:00", "1 D"))
         +- 'UnresolvedRelation [traces]
      +- 'Filter (('ip === "10.0.0.1" & 'cloud.provider === "aws") & inTimeScope('@timestamp, "2018-07-02T22:23:00", "1 D"))
         +- 'UnresolvedRelation [metrics]
```

The catalyst engine optimizes this query according to the most efficient join ordering.

#### dedup command
<a name="supported-ppl-dedup-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `dedup` command to remove identical documents from your search results based on specified fields.

**Syntax**  
Use the following syntax:

```
dedup [int] <field-list> [keepempty=<bool>] [consecutive=<bool>] 
```

**`int`**
+ Optional. 
+ The `dedup` command retains multiple events for each combination when you specify <int>. The number for <int> must be greater than 0. If you don't specify a number, only the first occurring event is kept. All other duplicates are removed from the results. 
+ Default: 1

**`keepempty`**
+ Optional. 
+ If true, keeps documents where any field in the field-list has a NULL value or is MISSING.
+ Default: false

**`consecutive`**
+ Optional.
+ If true, removes only events with consecutive duplicate combinations of values.
+ Default: false

**`field-list`**
+ Mandatory. 
+ A comma-delimited list of fields. At least one field is required.

**Example 1: Dedup by one field**  
This example shows how to dedup documents using the gender field.

PPL query:

```
os> source=accounts | dedup gender | fields account_number, gender;
fetched rows / total rows = 2/2
+------------------+----------+
| account_number   | gender   |
|------------------+----------|
| 1                | M        |
| 13               | F        |
+------------------+----------+
```

**Example 2: Keep 2 duplicates documents**  
The example shows how to dedup documents with the gender field, keeping two duplicates.

PPL query:

```
os> source=accounts | dedup 2 gender | fields account_number, gender;
fetched rows / total rows = 3/3
+------------------+----------+
| account_number   | gender   |
|------------------+----------|
| 1                | M        |
| 6                | M        |
| 13               | F        |
+------------------+----------+
```

**Example 3: Keep or ignore the empty field by default**  
The example shows how to dedup the document by keeping the null value field.

PPL query:

```
os> source=accounts | dedup email keepempty=true | fields account_number, email;
fetched rows / total rows = 4/4
+------------------+-----------------------+
| account_number   | email                 |
+------------------+-----------------------+
| 1                | john_doe@example.com  |
| 6                | jane_doe@example.com  |
| 13               | null                  |
| 18               | juan_li@example.com   |
+------------------+-----------------------+
```

The example shows how to dedup the document by ignoring the empty value field.

PPL query:

```
os> source=accounts | dedup email | fields account_number, email;
fetched rows / total rows = 3/3
+------------------+-----------------------+
| account_number   | email                 |
+------------------+-----------------------+
| 1                | john_doe@example.com  |
| 6                | jane_doe@example.com  |
| 18               | juan_li@example.com   |
+------------------+-----------------------+
```

**Example 4: Dedup in consecutive documents**  
The example shows how to dedup in consecutive documents.

PPL query:

```
os> source=accounts | dedup gender consecutive=true | fields account_number, gender;
fetched rows / total rows = 3/3
+------------------+----------+
| account_number   | gender   |
+------------------+----------+
| 1                | M        |
| 13               | F        |
| 18               | M        |
+------------------+----------+
```

**Additional examples**
+ `source = table | dedup a | fields a,b,c`
+ `source = table | dedup a,b | fields a,b,c`
+ `source = table | dedup a keepempty=true | fields a,b,c`
+ `source = table | dedup a,b keepempty=true | fields a,b,c`
+ `source = table | dedup 1 a | fields a,b,c`
+ `source = table | dedup 1 a,b | fields a,b,c`
+ `source = table | dedup 1 a keepempty=true | fields a,b,c`
+ `source = table | dedup 1 a,b keepempty=true | fields a,b,c`
+ `source = table | dedup 2 a | fields a,b,c`
+ `source = table | dedup 2 a,b | fields a,b,c`
+ `source = table | dedup 2 a keepempty=true | fields a,b,c`
+ `source = table | dedup 2 a,b keepempty=true | fields a,b,c`
+ `source = table | dedup 1 a consecutive=true| fields a,b,c` (consecutive deduplication is unsupported)

**Limitation**
+ For `| dedup 2 a, b keepempty=false`

  ```
  DataFrameDropColumns('_row_number_)
  +- Filter ('_row_number_ <= 2) // allowed duplication = 2
     +- Window [row_number() windowspecdefinition('a, 'b, 'a ASC NULLS FIRST, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), currentrow$())) AS _row_number_], ['a, 'b], ['a ASC NULLS FIRST, 'b ASC NULLS FIRST]
         +- Filter (isnotnull('a) AND isnotnull('b)) // keepempty=false
            +- Project
               +- UnresolvedRelation
  ```
+ For `| dedup 2 a, b keepempty=true`

  ```
  Union
  :- DataFrameDropColumns('_row_number_)
  :  +- Filter ('_row_number_ <= 2)
  :     +- Window [row_number() windowspecdefinition('a, 'b, 'a ASC NULLS FIRST, 'b ASC NULLS FIRST, specifiedwindowframe(RowFrame, unboundedpreceding$(), currentrow$())) AS _row_number_], ['a, 'b], ['a ASC NULLS FIRST, 'b ASC NULLS FIRST]
  :        +- Filter (isnotnull('a) AND isnotnull('b))
  :           +- Project
  :              +- UnresolvedRelation
  +- Filter (isnull('a) OR isnull('b))
     +- Project
        +- UnresolvedRelation
  ```

#### describe command
<a name="supported-ppl-describe-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `describe` command to get detailed information about the structure and metadata of tables, schemas, and catalogs. Here are various examples and use cases of the `describe` command.

**Describe**
+ `describe table` This command is equal to the `DESCRIBE EXTENDED table` SQL command
+ `describe schema.table`
+ `describe schema.`table``
+ `describe catalog.schema.table`
+ `describe catalog.schema.`table``
+ `describe `catalog`.`schema`.`table``

#### eval command
<a name="supported-ppl-eval-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The `eval` command evaluates the expression and appends the result to the search result.

**Syntax**  
Use the following syntax:

```
eval <field>=<expression> ["," <field>=<expression> ]...    
```
+ `field`: Mandatory. If the field name doesn't exist, a new field is added. If the field name already exists, it will be overridden.
+  `expression`: Mandatory. Any expression supported by the system.

**Example 1: Create the new field**  
This example shows how to create a new `doubleAge` field for each document. The new `doubleAge` is the evaluation result of age multiplied by 2.

PPL query:

```
os> source=accounts | eval doubleAge = age * 2 | fields age, doubleAge ;
fetched rows / total rows = 4/4
+-------+-------------+
| age   | doubleAge   |
|-------+-------------|
| 32    | 64          |
| 36    | 72          |
| 28    | 56          |
| 33    | 66          |
+-------+-------------+
```

**Example 2: Override the existing field**  
This example shows how to override the existing age field with age plus 1.

PPL query:

```
os> source=accounts | eval age = age + 1 | fields age ;
fetched rows / total rows = 4/4
+-------+
| age   |
|-------|
| 33    |
| 37    |
| 29    |
| 34    |
+-------+
```

**Example 3: Create the new field with field defined in eval**  
This example shows how to create a new `ddAge` field with a field defined in the eval command. The new field `ddAge` is the evaluation result of `doubleAge` multiplied by 2, where `doubleAge` is defined in the eval command.

PPL query:

```
os> source=accounts | eval doubleAge = age * 2, ddAge = doubleAge * 2 | fields age, doubleAge, ddAge ;
fetched rows / total rows = 4/4
+-------+-------------+---------+
| age   | doubleAge   | ddAge   |
|-------+-------------+---------|
| 32    | 64          | 128     |
| 36    | 72          | 144     |
| 28    | 56          | 112     |
| 33    | 66          | 132     |
+-------+-------------+---------+
```

Assumptions: `a`, `b`, `c` are existing fields in `table`

**Additional examples**
+ `source = table | eval f = 1 | fields a,b,c,f`
+ `source = table | eval f = 1` (output a,b,c,f fields)
+ `source = table | eval n = now() | eval t = unix_timestamp(a) | fields n,t`
+ `source = table | eval f = a | where f > 1 | sort f | fields a,b,c | head 5`
+ `source = table | eval f = a * 2 | eval h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = b | stats avg(f) by h`
+ `source = table | eval f = ispresent(a)`
+ `source = table | eval r = coalesce(a, b, c) | fields r`
+ `source = table | eval e = isempty(a) | fields e`
+ `source = table | eval e = isblank(a) | fields e`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one', a = 2, 'two', a = 3, 'three', a = 4, 'four', a = 5, 'five', a = 6, 'six', a = 7, 'se7en', a = 8, 'eight', a = 9, 'nine')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else 'unknown')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else concat(a, ' is an incorrect binary digit'))`
+ `source = table | eval f = a in ('foo', 'bar') | fields f`
+ `source = table | eval f = a not in ('foo', 'bar') | fields f`

**Eval with case example:**  


```
source = table | eval e = eval status_category =
case(a >= 200 AND a < 300, 'Success',
a >= 300 AND a < 400, 'Redirection',
a >= 400 AND a < 500, 'Client Error',
a >= 500, 'Server Error'
else 'Unknown')
```

**Eval with another case example:**  


Assumptions: `a`, `b`, `c` are existing fields in `table`

**Additional examples**
+ `source = table | eval f = 1 | fields a,b,c,f`
+ `source = table | eval f = 1` (output a,b,c,f fields)
+ `source = table | eval n = now() | eval t = unix_timestamp(a) | fields n,t`
+ `source = table | eval f = a | where f > 1 | sort f | fields a,b,c | head 5`
+ `source = table | eval f = a * 2 | eval h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = b | stats avg(f) by h`
+ `source = table | eval f = ispresent(a)`
+ `source = table | eval r = coalesce(a, b, c) | fields r`
+ `source = table | eval e = isempty(a) | fields e`
+ `source = table | eval e = isblank(a) | fields e`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one', a = 2, 'two', a = 3, 'three', a = 4, 'four', a = 5, 'five', a = 6, 'six', a = 7, 'se7en', a = 8, 'eight', a = 9, 'nine')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else 'unknown')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else concat(a, ' is an incorrect binary digit'))`
+ `source = table | eval f = a in ('foo', 'bar') | fields f`
+ `source = table | eval f = a not in ('foo', 'bar') | fields f`

**Eval with case example:**  


```
source = table | eval e = eval status_category =
case(a >= 200 AND a < 300, 'Success',
a >= 300 AND a < 400, 'Redirection',
a >= 400 AND a < 500, 'Client Error',
a >= 500, 'Server Error'
else 'Unknown')
```

**Eval with another case example:**  


```
source = table |  where ispresent(a) |
eval status_category =
 case(a >= 200 AND a < 300, 'Success',
  a >= 300 AND a < 400, 'Redirection',
  a >= 400 AND a < 500, 'Client Error',
  a >= 500, 'Server Error'
  else 'Incorrect HTTP status code'
 )
 | stats count() by status_category
```

**Limitations**
+ Overriding existing fields is unsupported. Queries attempting to do so will throw exceptions with the message "Reference 'a' is ambiguous".

  ```
  - `source = table | eval a = 10 | fields a,b,c`
  - `source = table | eval a = a * 2 | stats avg(a)`
  - `source = table | eval a = abs(a) | where a > 0`
  - `source = table | eval a = signum(a) | where a < 0`
  ```

#### eventstats command
<a name="supported-ppl-eventstats-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `eventstats` command to enrich your event data with calculated summary statistics. It operates by analyzing specified fields within your events, computing various statistical measures, and then appending these results as new fields to each original event.

**Key aspects of eventstats**

1. It performs calculations across the entire result set or within defined groups.

1. The original events remain intact, with new fields added to contain the statistical results.

1. The command is particularly useful for comparative analysis, identifying outliers, or providing additional context to individual events.

**Difference between stats and eventstats**  
The `stats` and `eventstats` commands are both used for calculating statistics, but they have some key differences in how they operate and what they produce.

**Output format**
+ `stats`: Produces a summary table with only the calculated statistics.
+ `eventstats`: Adds the calculated statistics as new fields to the existing events, preserving the original data.

**Event retention**
+ `stats`: Reduces the result set to only the statistical summary, discarding individual events.
+ `eventstats`: Retains all original events and adds new fields with the calculated statistics.

**Use cases**
+ `stats`: Best for creating summary reports or dashboards. Often used as a final command to summarize results.
+ `eventstats`: Useful when you need to enrich events with statistical context for further analysis or filtering. Can be used mid-search to add statistics that can be used in subsequent commands.

**Syntax**  
Use the following syntax:

```
eventstats <aggregation>... [by-clause]    
```

**aggregation**
+ Mandatory. 
+ An aggregation function. 
+ The argument of aggregation must be a field.

**by-clause**
+ Optional.
+ Syntax: `by [span-expression,] [field,]...`
+ The by clause can include fields and expressions such as scalar functions and aggregation functions. You can also use the span clause to split a specific field into buckets of equal intervals. The eventstats command then performs aggregation based on these span buckets.
+ Default: If you don't specify a by clause, the eventstats command aggregates over the entire result set.

**span-expression**
+ Optional, at most one.
+ Syntax: `span(field_expr, interval_expr)`
+ The unit of the interval expression is the natural unit by default. However, for date and time type fields, you need to specify the unit in the interval expression when using date/time units.

  For example, to split the field `age` into buckets by 10 years, use `span(age, 10)`. For time-based fields, you can split a `timestamp` field into hourly intervals using `span(timestamp, 1h)`.


**Available time units**  

| Span interval units | 
| --- | 
| millisecond (ms) | 
| second (s) | 
| minute (m, case sensitive) | 
| hour (h) | 
| day (d) | 
| week (w) | 
| month (M, case sensitive) | 
| quarter (q) | 
| year (y) | 

**Aggregation functions**  


**`COUNT`**  
`COUNT` returns a count of the number of expr in the rows retrieved by a SELECT statement.

For CloudWatch Logs use queries, `COUNT` is not supported. 

Example:

```
os> source=accounts | eventstats count();
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+--------------------+------------+--------------------------+--------+-------+---------+
| account_number | balance  | firstname | lastname | age | gender | address            | employer   | email                    | city   | state | count() |
+----------------+----------+-----------+----------+-----+--------+--------------------+------------+--------------------------+--------+-------+---------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane       | AnyCorp    | janedoe@anycorp.com      | Brogan | IL    | 4       |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street | AnyCompany | marymajor@anycompany.com | Dante  | TN    | 4       |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street     | AnyOrg     |                          | Nogal  | VA    | 4       |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court  |            | juanli@exampleorg.com    | Orick  | MD    | 4       |
+----------------+----------+-----------+----------+-----+--------+--------------------+------------+--------------------------+--------+-------+---------+
```

**`SUM`**  
`SUM(expr)` returns the sum of expr.

Example:

```
os> source=accounts | eventstats sum(age) by gender;
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+------------+--------------------------+--------+-------+--------------------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer   | email                    | city   | state | sum(age) by gender |
+----------------+----------+-----------+----------+-----+--------+-----------------------+------------+--------------------------+--------+-------+--------------------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | 880 Any Lane          | AnyCorp    | janedoe@anycorp.com      | Brogan | IL    | 101                |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | AnyCompany | marymajor@anycompany.com | Dante  | TN    | 101                |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg     |                          | Nogal  | VA    | 28                 |
| 18             | 4180     | Juan      | Li       | 33  | M      | 467 Example Court     |            | juanli@exampleorg.com    | Orick  | MD    | 101                |
+----------------+----------+-----------+----------+-----+--------+-----------------------+------------+--------------------------+--------+-------+--------------------+
```

**`AVG`**  
`AVG(expr)` returns the average value of expr.

Example:

```
os> source=accounts | eventstats avg(age) by gender;
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+------------+---------------------------+--------+-------+--------------------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | avg(age) by gender |
+----------------+----------+-----------+----------+-----+--------+-----------------------+------------+---------------------------+--------+-------+--------------------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | 880 Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 33.67              |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 33.67              |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 28.00              |
| 18             | 4180     | Juan      | Li       | 33  | M      | 467 Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 33.67              |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+--------------------+
```

**MAX**  
`MAX(expr)` Returns the maximum value of expr.

Example

```
os> source=accounts | eventstats max(age);
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | max(age)  |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | 880 Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 36        |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 36        |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 36        |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 36        |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
```

**MIN**  
`MIN(expr)` Returns the minimum value of expr.

Example

```
os> source=accounts | eventstats min(age);
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | min(age)  |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | 880 Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 28        |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 28        |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | *** Any Street        | AnyOrg      |                          | Nogal  | VA    | 28        |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 28        |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+
```

**STDDEV\_SAMP**  
`STDDEV_SAMP(expr)` Return the sample standard deviation of expr.

Example

```
os> source=accounts | eventstats stddev_samp(age);
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | stddev_samp(age)       |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 3.304037933599835      |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 3.304037933599835      |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 3.304037933599835      |
| 18             | 4180     | Juan      | Li       | 33  | M      | 467 Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 3.304037933599835      |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
```

**STDDEV\_POP**  
`STDDEV_POP(expr)` Return the population standard deviation of expr.

Example

```
os> source=accounts | eventstats stddev_pop(age);
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | stddev_pop(age)        |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | 880 Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 2.****************     |
| 6              | 5686     | Mary      | Major    | 36  | M      | *** Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 2.****************     |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | *** Any Street        | AnyOrg      |                          | Nogal  | VA    | 2.****************     |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 2.****************     |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+------------------------+
```

**PERCENTILE or PERCENTILE\_APPROX**  
`PERCENTILE(expr, percent)` or `PERCENTILE_APPROX(expr, percent)` Return the approximate percentile value of expr at the specified percentage.

**percent**
+ The number must be a constant between 0 and 100.

Example

```
os> source=accounts | eventstats percentile(age, 90) by gender;
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+--------------------------------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | percentile(age, 90) by gender  |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+--------------------------------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 36                             |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 36                             |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 28                             |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 36                             |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+--------------------------------+
```

**Example 1: Calculate the average, sum and count of a field by group**  
The example show calculate the average age, sum age and count of events of all the accounts group by gender.

```
os> source=accounts | eventstats avg(age) as avg_age, sum(age) as sum_age, count() as count by gender;
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+-----------+-------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | avg_age   | sum_age   | count |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+-----------+-------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 33.666667 | 101       | 3     |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 33.666667 | 101       | 3     |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 28.000000 | 28        | 1     |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 33.666667 | 101       | 3     |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+-----------+-----------+-------+
```

**Example 2: Calculate the count by a span**  
The example gets the count of age by the interval of 10 years.

```
os> source=accounts | eventstats count(age) by span(age, 10) as age_span
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+----------+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                    | city   | state | age_span |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+----------+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane          | AnyCorp     | janedoe@anycorp.com      | Brogan | IL    | 3        |
| 6              | 5686     | Mary      | Major    | 36  | M      | 671 Example Street    | Any Company | marymajor@anycompany.com | Dante  | TN    | 3        |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | 789 Any Street        | AnyOrg      |                          | Nogal  | VA    | 1        |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com    | Orick  | MD    | 3        |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+--------------------------+--------+-------+----------+
```

**Example 3: Calculate the count by a gender and span**  
The example gets the count of age by the interval of 5 years and group by gender.

```
os> source=accounts | eventstats count() as cnt by span(age, 5) as age_span, gender
fetched rows / total rows = 4/4
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+---------------------------+--------+-------+-----+
| account_number | balance  | firstname | lastname | age | gender | address               | employer    | email                     | city   | state | cnt |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+---------------------------+--------+-------+-----+
| 1              | 39225    | Jane      | Doe      | 32  | M      | *** Any Lane          | AnyCorp     | janedoe@anycorp.com       | Brogan | IL    | 2   |
| 6              | 5686     | Mary      | Majo     | 36  | M      | 671 Example Street    | Any Company | hattiebond@anycompany.com | Dante  | TN    | 1   |
| 13             | 32838    | Nikki     | Wolf     | 28  | F      | *** Any Street        | AnyOrg      |                           | Nogal  | VA    | 1   |
| 18             | 4180     | Juan      | Li       | 33  | M      | *** Example Court     |             | juanli@exampleorg.com     | Orick  | MD    | 2   |
+----------------+----------+-----------+----------+-----+--------+-----------------------+-------------+---------------------------+--------+-------+-----+
```

**Usage**
+ `source = table | eventstats avg(a)`
+ `source = table | where a < 50 | eventstats avg(c)`
+ `source = table | eventstats max(c) by b`
+ `source = table | eventstats count(c) by b | head 5`
+ `source = table | eventstats distinct_count(c)`
+ `source = table | eventstats stddev_samp(c)`
+ `source = table | eventstats stddev_pop(c)`
+ `source = table | eventstats percentile(c, 90)`
+ `source = table | eventstats percentile_approx(c, 99)`

**Aggregations with span**  

+ `source = table | eventstats count(a) by span(a, 10) as a_span`
+ `source = table | eventstats sum(age) by span(age, 5) as age_span | head 2`
+ `source = table | eventstats avg(age) by span(age, 20) as age_span, country | sort - age_span | head 2`

**Aggregations with time window span (tumble windowing function)**  

+ `source = table | eventstats sum(productsAmount) by span(transactionDate, 1d) as age_date | sort age_date`
+ `source = table | eventstats sum(productsAmount) by span(transactionDate, 1w) as age_date, productId`

**Aggregations group by multiple levels**  

+ `source = table | eventstats avg(age) as avg_state_age by country, state | eventstats avg(avg_state_age) as avg_country_age by country`
+ `source = table | eventstats avg(age) as avg_city_age by country, state, city | eval new_avg_city_age = avg_city_age - 1 | eventstats avg(new_avg_city_age) as avg_state_age by country, state | where avg_state_age > 18 | eventstats avg(avg_state_age) as avg_adult_country_age by country`

#### expand command
<a name="supported-ppl-expand-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `expand` command to flatten a field of type:
+ `Array<Any>`
+ `Map<Any>`

**Syntax**  
Use the following syntax:

```
expand <field> [As alias]
```

**field**
+ The field to be expanded (exploded). Must be of a supported type.

**alias**
+ Optional. The name to be used instead of the original field name.

**Usage**  
The `expand` command produces a row for each element in the specified array or map field, where:
+ Array elements become individual rows.
+ Map key-value pairs are broken into separate rows, with each key-value represented as a row.
+ When an alias is provided, the exploded values are represented under the alias instead of the original field name.
+ This can be used in combination with other commands, such as `stats`, `eval`, and `parse` to manipulate or extract data post-expansion.

**Examples**
+ `source = table | expand employee | stats max(salary) as max by state, company`
+ `source = table | expand employee as worker | stats max(salary) as max by state, company`
+ `source = table | expand employee as worker | eval bonus = salary * 3 | fields worker, bonus`
+ `source = table | expand employee | parse description '(?<email>.+@.+)' | fields employee, email`
+ `source = table | eval array=json_array(1, 2, 3) | expand array as uid | fields name, occupation, uid`
+ `source = table | expand multi_valueA as multiA | expand multi_valueB as multiB`

#### explain command
<a name="supported-ppl-explain-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The `explain` command helps you understand query execution plans, enabling you to analyze and optimize your queries for better performance. This introduction provides a concise overview of the explain command's purpose and its importance in query optimization.

**Comment**
+ `source=accounts | top gender // finds most common gender of all the accounts` (line comment)
+ `source=accounts | dedup 2 gender /* dedup the document with gender field keep 2 duplication */ | fields account_number, gender` (block comment)

**Describe**
+ `describe table` This command is equal to the `DESCRIBE EXTENDED table` SQL command
+ `describe schema.table`
+ `describe schema.`table``
+ `describe catalog.schema.table`
+ `describe catalog.schema.`table``
+ `describe `catalog`.`schema`.`table``

**Explain**
+ `explain simple | source = table | where a = 1 | fields a,b,c`
+ `explain extended | source = table`
+ `explain codegen | source = table | dedup a | fields a,b,c`
+ `explain cost | source = table | sort a | fields a,b,c`
+ `explain formatted | source = table | fields - a`
+ `explain simple | describe table`

**Fields**
+ `source = table`
+ `source = table | fields a,b,c`
+ `source = table | fields + a,b,c`
+ `source = table | fields - b,c`
+ `source = table | eval b1 = b | fields - b1,c`

**Field summary**
+ `source = t | fieldsummary includefields=status_code nulls=false`
+ `source = t | fieldsummary includefields= id, status_code, request_path nulls=true`
+ `source = t | where status_code != 200 | fieldsummary includefields= status_code nulls=true`

**Nested field**
+ `source = catalog.schema.table1, catalog.schema.table2 | fields A.nested1, B.nested1`
+ `source = catalog.table | where struct_col2.field1.subfield > 'valueA' | sort int_col | fields int_col, struct_col.field1.subfield, struct_col2.field1.subfield`
+ `source = catalog.schema.table | where struct_col2.field1.subfield > 'valueA' | sort int_col | fields int_col, struct_col.field1.subfield, struct_col2.field1.subfield`

**Filters**
+ `source = table | where a = 1 | fields a,b,c`
+ `source = table | where a >= 1 | fields a,b,c`
+ `source = table | where a < 1 | fields a,b,c`
+ `source = table | where b != 'test' | fields a,b,c`
+ `source = table | where c = 'test' | fields a,b,c | head 3`
+ `source = table | where ispresent(b)`
+ `source = table | where isnull(coalesce(a, b)) | fields a,b,c | head 3`
+ `source = table | where isempty(a)`
+ `source = table | where isblank(a)`
+ `source = table | where case(length(a) > 6, 'True' else 'False') = 'True'`
+ `source = table | where a not in (1, 2, 3) | fields a,b,c`
+ `source = table | where a between 1 and 4` - Note: This returns a >= 1 and a <= 4, i.e. [1, 4]
+ `source = table | where b not between '2024-09-10' and '2025-09-10'` - Note: This returns b >= '\*\*\*\*\*\*\*\*\*\*' and b <= '2025-09-10'
+ `source = table | where cidrmatch(ip, '***********/24')`
+ `source = table | where cidrmatch(ipv6, '2003:db8::/32')`
+ `source = table | trendline sma(2, temperature) as temp_trend`

**IP related queries**
+ `source = table | where cidrmatch(ip, '**************')`
+ `source = table | where isV6 = false and isValid = true and cidrmatch(ipAddress, '**************')`
+ `source = table | where isV6 = true | eval inRange = case(cidrmatch(ipAddress, '2003:***::/32'), 'in' else 'out') | fields ip, inRange`

**Complex filters**  


```
source = table | eval status_category =
case(a >= 200 AND a < 300, 'Success',
    a >= 300 AND a < 400, 'Redirection',
    a >= 400 AND a < 500, 'Client Error',
    a >= 500, 'Server Error'
else 'Incorrect HTTP status code')
| where case(a >= 200 AND a < 300, 'Success',
    a >= 300 AND a < 400, 'Redirection',
    a >= 400 AND a < 500, 'Client Error',
    a >= 500, 'Server Error'
else 'Incorrect HTTP status code'
) = 'Incorrect HTTP status code'
```

```
source = table
| eval factor = case(a > 15, a - 14, isnull(b), a - 7, a < 3, a + 1 else 1)
| where case(factor = 2, 'even', factor = 4, 'even', factor = 6, 'even', factor = 8, 'even' else 'odd') = 'even'
| stats count() by factor
```

**Filters with logical conditions**
+ `source = table | where c = 'test' AND a = 1 | fields a,b,c`
+ `source = table | where c != 'test' OR a > 1 | fields a,b,c | head 1`
+ `source = table | where c = 'test' NOT a > 1 | fields a,b,c`

**Eval**  
Assumptions: `a`, `b`, `c` are existing fields in `table`
+ `source = table | eval f = 1 | fields a,b,c,f`
+ `source = table | eval f = 1` (output a,b,c,f fields)
+ `source = table | eval n = now() | eval t = unix_timestamp(a) | fields n,t`
+ `source = table | eval f = a | where f > 1 | sort f | fields a,b,c | head 5`
+ `source = table | eval f = a * 2 | eval h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = f * 2 | fields a,f,h`
+ `source = table | eval f = a * 2, h = b | stats avg(f) by h`
+ `source = table | eval f = ispresent(a)`
+ `source = table | eval r = coalesce(a, b, c) | fields r`
+ `source = table | eval e = isempty(a) | fields e`
+ `source = table | eval e = isblank(a) | fields e`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one', a = 2, 'two', a = 3, 'three', a = 4, 'four', a = 5, 'five', a = 6, 'six', a = 7, 'se7en', a = 8, 'eight', a = 9, 'nine')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else 'unknown')`
+ `source = table | eval f = case(a = 0, 'zero', a = 1, 'one' else concat(a, ' is an incorrect binary digit'))`
+ `source = table | eval digest = md5(fieldName) | fields digest`
+ `source = table | eval digest = sha1(fieldName) | fields digest`
+ `source = table | eval digest = sha2(fieldName,256) | fields digest`
+ `source = table | eval digest = sha2(fieldName,512) | fields digest`

#### fillnull command
<a name="supported-ppl-fillnull-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

**Description**  
Use the `fillnull` command to replace null values with a specified value in one or more fields of your search results. 

**Syntax**  
Use the following syntax:

```
fillnull [with <null-replacement> in <nullable-field>["," <nullable-field>]] | [using <source-field> = <null-replacement> [","<source-field> = <null-replacement>]]
```
+ null-replacement: Mandatory. The value used to replace null values.
+ nullable-field: Mandatory. Field reference. The null values in this field will be replaced with the value specified in null-replacement.

**Example 1: Fillnull one field**  
The example shows how to use fillnull on a single field:

```
os> source=logs | fields status_code | eval input=status_code | fillnull with 0 in status_code;
| input | status_code |
|-------|-------------|
| 403   | 403         |
| 403   | 403         |
| NULL  | 0           |
| NULL  | 0           |
| 200   | 200         |
| 404   | 404         |
| 500   | 500         |
| NULL  | 0           |
| 500   | 500         |
| 404   | 404         |
| 200   | 200         |
| 500   | 500         |
| NULL  | 0           |
| NULL  | 0           |
| 404   | 404         |
```

**Example 2: Fillnull applied to multiple fields**  
The example shows fillnull applied to multiple fields.

```
os> source=logs | fields request_path, timestamp | eval input_request_path=request_path, input_timestamp = timestamp | fillnull with '???' in request_path, timestamp;
| input_request_path | input_timestamp       | request_path | timestamp              |
|------------------------------------------------------------------------------------|
| /contact           | NULL                  | /contact     | ???                    |
| /home              | NULL                  | /home        | ???                    |
| /about             | 2023-10-01 10:30:00   | /about       | 2023-10-01 10:30:00    |
| /home              | 2023-10-01 10:15:00   | /home        | 2023-10-01 10:15:00    |
| NULL               | 2023-10-01 10:20:00   | ???          | 2023-10-01 10:20:00    |
| NULL               | 2023-10-01 11:05:00   | ???          | 2023-10-01 11:05:00    |
| /about             | NULL                  | /about       | ???                    |
| /home              | 2023-10-01 10:00:00   | /home        | 2023-10-01 10:00:00    |
| /contact           | NULL                  | /contact     | ???                    |
| NULL               | 2023-10-01 10:05:00   | ???          | 2023-10-01 10:05:00    |
| NULL               | 2023-10-01 10:50:00   | ???          | 2023-10-01 10:50:00    |
| /services          | NULL                  | /services    | ???                    |
| /home              | 2023-10-01 10:45:00   | /home        | 2023-10-01 10:45:00    |
| /services          | 2023-10-01 11:00:00   | /services    | 2023-10-01 11:00:00    |
| NULL               | 2023-10-01 10:35:00   | ???          | 2023-10-01 10:35:00    |
```

**Example 3: Fillnull applied to multiple fields with various null replacement values.**  
The example show fillnull with various values used to replace nulls.
+ `/error` in `request_path` field
+ `1970-01-01 00:00:00` in `timestamp` field

```
os> source=logs | fields request_path, timestamp | eval input_request_path=request_path, input_timestamp = timestamp | fillnull using request_path = '/error', timestamp='1970-01-01 00:00:00';

| input_request_path | input_timestamp       | request_path | timestamp              |
|------------------------------------------------------------------------------------|
| /contact           | NULL                  | /contact     | 1970-01-01 00:00:00    |
| /home              | NULL                  | /home        | 1970-01-01 00:00:00    |
| /about             | 2023-10-01 10:30:00   | /about       | 2023-10-01 10:30:00    |
| /home              | 2023-10-01 10:15:00   | /home        | 2023-10-01 10:15:00    |
| NULL               | 2023-10-01 10:20:00   | /error       | 2023-10-01 10:20:00    |
| NULL               | 2023-10-01 11:05:00   | /error       | 2023-10-01 11:05:00    |
| /about             | NULL                  | /about       | 1970-01-01 00:00:00    |
| /home              | 2023-10-01 10:00:00   | /home        | 2023-10-01 10:00:00    |
| /contact           | NULL                  | /contact     | 1970-01-01 00:00:00    |
| NULL               | 2023-10-01 10:05:00   | /error       | 2023-10-01 10:05:00    |
| NULL               | 2023-10-01 10:50:00   | /error       | 2023-10-01 10:50:00    |
| /services          | NULL                  | /services    | 1970-01-01 00:00:00    |
| /home              | 2023-10-01 10:45:00   | /home        | 2023-10-01 10:45:00    |
| /services          | 2023-10-01 11:00:00   | /services    | 2023-10-01 11:00:00    |
| NULL               | 2023-10-01 10:35:00   | /error       | 2023-10-01 10:35:00    |
```

#### fields command
<a name="supported-ppl-fields-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `fields` command to keep or remove fields from the search result.

**Syntax**  
Use the following syntax:

```
field [+|-] <field-list> 
```
+ `index`: Optional. 

  If the plus (\+) is used, only the fields specified in the field list will be kept. 

  If the minus (-) is used, all the fields specified in the field list will be removed. 

  *Default*: \+
+ `field list`: Mandatory. A comma-delimited list of fields to keep or remove.

**Example 1: Select specified fields from result**  
This example shows how to fetch `account_number`, `firstname`, and `lastname` fields from search results.

PPL query:

```
os> source=accounts | fields account_number, firstname, lastname;
fetched rows / total rows = 4/4
+------------------+-------------+------------+
| account_number   | firstname   | lastname   |
|------------------+-------------+------------|
| 1                | Jane        | Doe        |
| 6                | John        | Doe        |
| 13               | Jorge       | Souza      |
| 18               | Juan        | Li         |
+------------------+-------------+------------+
```

**Example 2: Remove specified fields from result**  
This example shows how to remove the `account_number` field from search results.

PPL query:

```
os> source=accounts | fields account_number, firstname, lastname | fields - account_number ;
fetched rows / total rows = 4/4
+-------------+------------+
| firstname   | lastname   |
|-------------+------------|
| Jane        | Doe        |
| John        | Doe        |
| Jorge       | Souza      |
| Juan        | Li         |
+-------------+------------+
```

**Additional examples**
+ `source = table`
+ `source = table | fields a,b,c`
+ `source = table | fields + a,b,c`
+ `source = table | fields - b,c`
+ `source = table | eval b1 = b | fields - b1,c`

Nested-fields example:

```
`source = catalog.schema.table1, catalog.schema.table2 | fields A.nested1, B.nested1`
`source = catalog.table | where struct_col2.field1.subfield > 'valueA' | sort int_col | fields  int_col, struct_col.field1.subfield, struct_col2.field1.subfield`
`source = catalog.schema.table | where struct_col2.field1.subfield > 'valueA' | sort int_col | fields  int_col, struct_col.field1.subfield, struct_col2.field1.subfield`
```

#### flatten command
<a name="supported-ppl-flatten-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the flatten command to expand fields of the following types:
+ `struct<?,?>`
+ `array<struct<?,?>>`

**Syntax**  
Use the following syntax:

```
flatten <field>
```
+ *field*: The field to be flattened. The field must be of supported type.

**Schema**


| col\_name | data\_type | 
| --- | --- | 
| \_time | string | 
| bridges | array<struct<length:bigint,name:string>> | 
| city | string | 
| coor | struct<alt:bigint,lat:double,long:double> | 
| country | string | 

**Data**  



| \_time | bridges | city | coor | country | 
| --- | --- | --- | --- | --- | 
| 2024-09-13T12:00:00 | [{801, Tower Bridge}, {928, London Bridge}] | London | {35, 51.5074, -0.1278} | England | 
| 2024-09-13T12:00:00 | [{232, Pont Neuf}, {160, Pont Alexandre III}] | Paris | {35, 48.8566, 2.3522} | France | 
| 2024-09-13T12:00:00 | [{48, Rialto Bridge}, {11, Bridge of Sighs}] | Venice | {2, 45.4408, 12.3155} | Italy | 
| 2024-09-13T12:00:00 | [{\*\*\*, Charles Bridge}, {343, Legion Bridge}] | Prague | {200, 50.0755, 14.4378} | Czech Republic | 
| 2024-09-13T12:00:00 | [{375, Chain Bridge}, {333, Liberty Bridge}] | Budapest | {96, 47.4979, 19.0402} | Hungary | 
| 1990-09-13T12:00:00 | NULL | Warsaw | NULL | Poland | 

**Example 1: flatten struct**  
This example shows how to flatten a struct field.

PPL query:

```
source=table | flatten coor
```


| \_time | bridges | city | country | alt | lat | long | 
| --- | --- | --- | --- | --- | --- | --- | 
| 2024-09-13T12:00:00 | [{801, Tower Bridge}, {928, London Bridge}] | London | England | 35 | 51.5074 | -0.1278 | 
| 2024-09-13T12:00:00 | [{232, Pont Neuf}, {160, Pont Alexandre III}] | Paris | France | 35 | 48.8566 | 2.3522 | 
| 2024-09-13T12:00:00 | [{48, Rialto Bridge}, {11, Bridge of Sighs}] | Venice | Italy | 2 | 45.4408 | 12.3155 | 
| 2024-09-13T12:00:00 | [{516, Charles Bridge}, {343, Legion Bridge}] | Prague | Czech Republic | 200 | 50.0755 | 14.4378 | 
| 2024-09-13T12:00:00 | [{375, Chain Bridge}, {333, Liberty Bridge}] | Budapest | Hungary | 96 | 47.4979 | 19.0402 | 
| 1990-09-13T12:00:00 | NULL | Warsaw | Poland | NULL | NULL | NULL | 

**Example 2: flatten array**  
The example shows how to flatten an array of struct fields.

PPL query:

```
source=table | flatten bridges
```


| \_time | city | coor | country | length | name | 
| --- | --- | --- | --- | --- | --- | 
| 2024-09-13T12:00:00 | London | {35, 51.5074, -0.1278} | England | 801 | Tower Bridge | 
| 2024-09-13T12:00:00 | London | {35, 51.5074, -0.1278} | England | 928 | London Bridge | 
| 2024-09-13T12:00:00 | Paris | {35, 48.8566, 2.3522} | France | 232 | Pont Neuf | 
| 2024-09-13T12:00:00 | Paris | {35, 48.8566, 2.3522} | France | 160 | Pont Alexandre III | 
| 2024-09-13T12:00:00 | Venice | {2, 45.4408, 12.3155} | Italy | 48 | Rialto Bridge | 
| 2024-09-13T12:00:00 | Venice | {2, 45.4408, 12.3155} | Italy | 11 | Bridge of Sighs | 
| 2024-09-13T12:00:00 | Prague | {200, 50.0755, 14.4378} | Czech Republic | 516 | Charles Bridge | 
| 2024-09-13T12:00:00 | Prague | {200, 50.0755, 14.4378} | Czech Republic | 343 | Legion Bridge | 
| 2024-09-13T12:00:00 | Budapest | {96, 47.4979, 19.0402} | Hungary | 375 | Chain Bridge | 
| 2024-09-13T12:00:00 | Budapest | {96, 47.4979, 19.0402} | Hungary | 333 | Liberty Bridge | 
| 1990-09-13T12:00:00 | Warsaw | NULL | Poland | NULL | NULL | 

**Example 3: flatten array and struct**  
This example shows how to flatten multiple fields.

PPL query:

```
source=table | flatten bridges | flatten coor
```


| \_time | city | country | length | name | alt | lat | long | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| 2024-09-13T12:00:00 | London | England | 801 | Tower Bridge | 35 | 51.5074 | -0.1278 | 
| 2024-09-13T12:00:00 | London | England | 928 | London Bridge | 35 | 51.5074 | -0.1278 | 
| 2024-09-13T12:00:00 | Paris | France | 232 | Pont Neuf | 35 | 48.8566 | 2.3522 | 
| 2024-09-13T12:00:00 | Paris | France | 160 | Pont Alexandre III | 35 | 48.8566 | 2.3522 | 
| 2024-09-13T12:00:00 | Venice | Italy | 48 | Rialto Bridge | 2 | 45.4408 | 12.3155 | 
| 2024-09-13T12:00:00 | Venice | Italy | 11 | Bridge of Sighs | 2 | 45.4408 | 12.3155 | 
| 2024-09-13T12:00:00 | Prague | Czech Republic | 516 | Charles Bridge | 200 | 50.0755 | 14.4378 | 
| 2024-09-13T12:00:00 | Prague | Czech Republic | 343 | Legion Bridge | 200 | 50.0755 | 14.4378 | 
| 2024-09-13T12:00:00 | Budapest | Hungary | 375 | Chain Bridge | 96 | 47.4979 | 19.0402 | 
| 2024-09-13T12:00:00 | Budapest | Hungary | 333 | Liberty Bridge | 96 | 47.4979 | 19.0402 | 
| 1990-09-13T12:00:00 | Warsaw | Poland | NULL | NULL | NULL | NULL | NULL | 

#### grok command
<a name="supported-ppl-grok-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The `grok` command parses a text field with a grok pattern and appends the results to the search result.

**Syntax**  
Use the following syntax:

```
grok <field> <pattern>
```

**field**
+ Mandatory. 
+ The field must be a text field.

**pattern**
+ Mandatory. 
+ The grok pattern used to extract new fields from the given text field. 
+ If a new field name already exists, it will replace the original field.

**Grok pattern**  
The grok pattern is used to match the text field of each document to extract new fields.

**Example 1: Create the new field**  
This example shows how to create a new field `host` for each document. `host` will be the host name after `@` in the `email` field. Parsing a null field will return an empty string.

```
os> source=accounts | grok email '.+@%{HOSTNAME:host}' | fields email, host ;
fetched rows / total rows = 4/4
+-------------------------+-------------+
| email                   | host        |
|-------------------------+-------------|
| jane_doe@example.com    | example.com |
| arnav_desai@example.net | example.net |
| null                    |             |
| juan_li@example.org     | example.org |
+-------------------------+-------------+
```

**Example 2: Override the existing field**  
This example shows how to override the existing `address` field with the street number removed.

```
os> source=accounts | grok address '%{NUMBER} %{GREEDYDATA:address}' | fields address ;
fetched rows / total rows = 4/4
+------------------+
| address          |
|------------------|
| Example Lane     |
| Any Street       |
| Main Street      |
| Example Court    |
+------------------+
```

**Example 3: Using grok to parse logs**  
This example shows how to use grok to parse raw logs.

```
os> source=apache | grok message '%{COMMONAPACHELOG}' | fields COMMONAPACHELOG, timestamp, response, bytes ;
fetched rows / total rows = 4/4
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------+------------+---------+
| COMMONAPACHELOG                                                                                                             | timestamp                  | response   | bytes   |
|-----------------------------------------------------------------------------------------------------------------------------+----------------------------+------------+---------|
| 177.95.8.74 - upton5450 [28/Sep/2022:10:15:57 -0700] "HEAD /e-business/mindshare HTTP/1.0" 404 19927                        | 28/Sep/2022:10:15:57 -0700 | 404        | 19927   |
| 127.45.152.6 - pouros8756 [28/Sep/2022:10:15:57 -0700] "GET /architectures/convergence/niches/mindshare HTTP/1.0" 100 28722 | 28/Sep/2022:10:15:57 -0700 | 100        | 28722   |
| *************** - - [28/Sep/2022:10:15:57 -0700] "PATCH /strategize/out-of-the-box HTTP/1.0" 401 27439                      | 28/Sep/2022:10:15:57 -0700 | 401        | 27439   |
| ************** - - [28/Sep/2022:10:15:57 -0700] "POST /users HTTP/1.1" 301 9481                                             | 28/Sep/2022:10:15:57 -0700 | 301        | 9481    |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------+------------+---------+
```

**Limitations**  
The grok command has the same limitations as the parse command.

#### head command
<a name="supported-ppl-head-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `head` command to return the first N number of specified results after an optional offset in search order.

**Syntax**  
Use the following syntax:

```
head [<size>] [from <offset>]
```

**<size>**
+ Optional integer. 
+ The number of results to return. 
+ Default: 10

**<offset>**
+ Integer after optional `from`. 
+ The number of results to skip. 
+ Default: 0

**Example 1: Get first 10 results**  
This example shows how to retrieve a maximum of 10 results from the accounts index.

PPL query:

```
os> source=accounts | fields firstname, age | head;
fetched rows / total rows = 4/4
+-------------+-------+
| firstname   | age   |
|-------------+-------|
| Jane        | 32    |
| John        | 36    |
| Jorge       | 28    |
| Juan        | 33    |
+-------------+-------+
```

**Example 2: Get first N results**  
The example shows the first N results from the accounts index.

PPL query:

```
os> source=accounts | fields firstname, age | head 3;
fetched rows / total rows = 3/3
+-------------+-------+
| firstname   | age   |
|-------------+-------|
| Jane        | 32    |
| John        | 36    |
| Jorge       | 28    |
+-------------+-------+
```

**Example 3: Get first N results after offset M**  
This example shows how to retrieve the first N results after skipping M results from the accounts index.

PPL query:

```
os> source=accounts | fields firstname, age | head 3 from 1;
fetched rows / total rows = 3/3
+-------------+-------+
| firstname   | age   |
|-------------+-------|
| John        | 36    |
| Jorge       | 28    |
| Juan        | 33    |
+-------------+-------+
```

#### join command
<a name="supported-ppl-join-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The join command allows you to combine data from multiple sources based on common fields, enabling you to perform complex analyses and gain deeper insights from your distributed datasets

**Schema**  
There are least two indices, `otel-v1-apm-span-*` (large) and `otel-v1-apm-service-map` (small).

Relevant fields from indices:

**`otel-v1-apm-span-*`**
+ traceId - A unique identifier for a trace. All spans from the same trace share the same traceId.
+ spanId - A unique identifier for a span within a trace, assigned when the span is created.
+ parentSpanId - The spanId of this span's parent span. If this is a root span, then this field must be empty.
+ durationInNanos - The difference in nanoseconds between startTime and endTime. (this is `latency` in UI)
+ serviceName - The resource from which the span originates.
+ traceGroup - The name of the trace's root span.

**`otel-v1-apm-service-map`**
+ serviceName - The name of the service that emitted the span.
+ destination.domain - The serviceName of the service being called by this client.
+ destination.resource - The span name (API, operation, and so on) being called by this client.
+ target.domain - The serviceName of the service being called by a client.
+ target.resource - The span name (API, operation, and so on) being called by a client.
+ traceGroupName - The top-level span name that started the request chain.

**Requirement**  
Support **join** to calculate the following:

For each service, join span index on service map index to calculate metrics under different type of filters.

This sample query calculates latency when filtered by trace group `client_cancel_order` for the `order` service. 

```
SELECT avg(durationInNanos)
FROM `otel-v1-apm-span-000001` t1
WHERE t1.serviceName = `order`
  AND ((t1.name in
          (SELECT target.resource
           FROM `otel-v1-apm-service-map`
           WHERE serviceName = `order`
             AND traceGroupName = `client_cancel_order`)
        AND t1.parentSpanId != NULL)
       OR (t1.parentSpanId = NULL
           AND t1.name = `client_cancel_order`))
  AND t1.traceId in
    (SELECT traceId
     FROM `otel-v1-apm-span-000001`
     WHERE serviceName = `order`)
```

**Migrate to PPL**  
Syntax of the join command

```
SEARCH source=<left-table>
| <other piped command>
| [joinType] JOIN
    [leftAlias]
    ON joinCriteria
    <right-table>
| <other piped command>
```

**Rewriting**  


```
SEARCH source=otel-v1-apm-span-000001
| WHERE serviceName = 'order'
| JOIN left=t1 right=t2
    ON t1.traceId = t2.traceId AND t2.serviceName = 'order'
    otel-v1-apm-span-000001 -- self inner join
| EVAL s_name = t1.name -- rename to avoid ambiguous
| EVAL s_parentSpanId = t1.parentSpanId -- RENAME command would be better when it is supported
| EVAL s_durationInNanos = t1.durationInNanos 
| FIELDS s_name, s_parentSpanId, s_durationInNanos -- reduce colunms in join
| LEFT JOIN left=s1 right=t3
    ON s_name = t3.target.resource AND t3.serviceName = 'order' AND t3.traceGroupName = 'client_cancel_order'
    otel-v1-apm-service-map
| WHERE (s_parentSpanId IS NOT NULL OR (s_parentSpanId IS NULL AND s_name = 'client_cancel_order'))
| STATS avg(s_durationInNanos) -- no need to add alias if there is no ambiguous
```

**joinType**
+ Syntax: `INNER | LEFT OUTER | CROSS`
+ Optional
+ The type of join to perform. The default is `INNER` if not specified.

**leftAlias**
+ Syntax: `left = <leftAlias>`
+ Optional
+ The subquery alias to use with the left join side, to avoid ambiguous naming.

**joinCriteria**
+ Syntax: `<expression>`
+ Required
+ The syntax starts with `ON`. It could be any comparison expression. Generally, the join criteria looks like `<leftAlias>.<leftField>=<rightAlias>.<rightField>`. 

  For example: `l.id = r.id`. If the join criteria contains multiple conditions, you can specify `AND` and `OR` operator between each comparison expression. For example, `l.id = r.id AND l.email = r.email AND (r.age > 65 OR r.age < 18)`.

**More examples**  
Migration from SQL query (TPC-H Q13):

```
SELECT c_count, COUNT(*) AS custdist
FROM
  ( SELECT c_custkey, COUNT(o_orderkey) c_count
    FROM customer LEFT OUTER JOIN orders ON c_custkey = o_custkey
        AND o_comment NOT LIKE '%unusual%packages%'
    GROUP BY c_custkey
  ) AS c_orders
GROUP BY c_count
ORDER BY custdist DESC, c_count DESC;
```

Rewritten by PPL join query:

```
SEARCH source=customer
| FIELDS c_custkey
| LEFT OUTER JOIN
    ON c_custkey = o_custkey AND o_comment NOT LIKE '%unusual%packages%'
    orders
| STATS count(o_orderkey) AS c_count BY c_custkey
| STATS count() AS custdist BY c_count
| SORT - custdist, - c_count
```

Limitation: sub searches are unsupported in join right side.

If sub searches are supported, you can rewrite the above PPL query as follows:

```
SEARCH source=customer
| FIELDS c_custkey
| LEFT OUTER JOIN
   ON c_custkey = o_custkey
   [
      SEARCH source=orders
      | WHERE o_comment NOT LIKE '%unusual%packages%'
      | FIELDS o_orderkey, o_custkey
   ]
| STATS count(o_orderkey) AS c_count BY c_custkey
| STATS count() AS custdist BY c_count
| SORT - custdist, - c_count
```

#### lookup command
<a name="supported-ppl-lookup-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `lookup` command to enrich your search data by adding or replacing data from a lookup index (dimension table). This command allows you to extend fields of an index with values from a dimension table. You can also use it to append or replace values when lookup conditions are met. The `lookup` command is more suitable than the `Join` command for enriching source data with a static dataset.

**Syntax**  
Use the following syntax:

```
SEARCH source=<sourceIndex>
| <other piped command>
| LOOKUP <lookupIndex> (<lookupMappingField> [AS <sourceMappingField>])...
    [(REPLACE | APPEND) (<inputField> [AS <outputField>])...]
| <other piped command>
```

**lookupIndex**
+ Required.
+ The name of the lookup index (dimension table).

**lookupMappingField**
+ Required.
+ A mapping key in the lookup index, analogous to a join key from the right table. You can specify multiple fields, separated by commas.

**sourceMappingField**
+ Optional.
+ Default: <lookupMappingField>.
+ A mapping key from the source query, analogous to a join key from the left side.

**inputField**
+ Optional.
+ Default: All fields of the lookup index where matched values are found.
+ A field in the lookup index where matched values are applied to the result output. You can specify multiple fields, separated by commas.

**outputField**
+ Optional.
+ Default: `<inputField>`.
+ A field in the output. You can specify multiple output fields. If you specify an existing field name from the source query, its values will be replaced or appended by matched values from inputField. If you specify a new field name, it will be added to the results.

**REPLACE \| APPEND**
+ Optional.
+ Default: REPLACE
+ Specifies how to handle matched values. If you specify REPLACE, matched values in <lookupIndex> field overwrite the values in result. If you specify `APPEND`, matched values in <lookupIndex> field only append to the missing values in result.

**Usage**
+ LOOKUP <lookupIndex> id AS cid REPLACE mail AS email
+ LOOKUP <lookupIndex> name REPLACE mail AS email
+ LOOKUP <lookupIndex> id AS cid, name APPEND address, mail AS email
+ LOOKUP <lookupIndex> id

**Example**  
See the following examples.

```
SEARCH source=<sourceIndex>
| WHERE orderType = 'Cancelled'
| LOOKUP account_list, mkt_id AS mkt_code REPLACE amount, account_name AS name
| STATS count(mkt_code), avg(amount) BY name
```

```
SEARCH source=<sourceIndex>
| DEDUP market_id
| EVAL category=replace(category, "-", ".")
| EVAL category=ltrim(category, "dvp.")
| LOOKUP bounce_category category AS category APPEND classification
```

```
SEARCH source=<sourceIndex>
| LOOKUP bounce_category category
```

#### parse command
<a name="supported-ppl-parse-command"></a>

The `parse` command parses a text field with a regular expression and appends the result to the search result.

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

**Syntax**  
Use the following syntax:

```
parse <field> <pattern>    
```

**`field`**
+ Mandatory. 
+ The field must be a text field.

**`pattern`**
+ Mandatory string. 
+ This is the regular expression pattern used to extract new fields from the given text field. 
+ If a new field name already exists, it will replace the original field.

**Regular expression**  
The regular expression pattern is used to match the whole text field of each document with Java regex engine. Each named capture group in the expression will become a new `STRING` field.

**Example 1: Create a new field**  
The example shows how to create a new field `host` for each document. `host` will be the host name after `@` in the `email` field. Parsing a null field will return an empty string.

PPL query:

```
os> source=accounts | parse email '.+@(?<host>.+)' | fields email, host ;
fetched rows / total rows = 4/4
+-----------------------+-------------+
| email                 | host        |
|-----------------------+-------------|
| jane_doe@example.com  | example.com |
| john_doe@example.net  | example.net |
| null                  |             |
| juan_li@example.org   | example.org |
+-----------------------+-------------+
```

**Example 2: Override an existing field**  
The example shows how to override the existing `address` field with the street number removed.

PPL query:

```
os> source=accounts | parse address '\d+ (?<address>.+)' | fields address ;
fetched rows / total rows = 4/4
+------------------+
| address          |
|------------------|
| Example Lane     |
| Example Street   |
| Example Avenue   |
| Example Court    |
+------------------+
```

**Example 3: Filter and sort by casted parsed field**  
The example shows how to sort street numbers that are higher than 500 in the `address` field.

PPL query:

```
os> source=accounts | parse address '(?<streetNumber>\d+) (?<street>.+)' | where cast(streetNumber as int) > 500 | sort num(streetNumber) | fields streetNumber, street ;
fetched rows / total rows = 3/3
+----------------+----------------+
| streetNumber   | street         |
|----------------+----------------|
| ***            | Example Street |
| ***            | Example Avenue |
| 880            | Example Lane   |
+----------------+----------------+
```

**Limitations**  
There are a few limitations with the parse command:
+ Fields defined by parse cannot be parsed again.

  The following command will not work:

  ```
  source=accounts | parse address '\d+ (?<street>.+)' | parse street '\w+ (?<road>\w+)'
  ```
+ Fields defined by parse cannot be overridden with other commands.

  `where` will not match any documents since `street` cannot be overridden:

  ```
  source=accounts | parse address '\d+ (?<street>.+)' | eval street='1' | where street='1' ;        
  ```
+ The text field used by parse cannot be overridden.

  `street` will not be successfully parsed since `address` is overridden:

  ```
  source=accounts | parse address '\d+ (?<street>.+)' | eval address='1' ;        
  ```
+ Fields defined by parse cannot be filtered or sorted after using them in the `stats` command.

  `where` in the following command will not work:

  ```
  source=accounts | parse email '.+@(?<host>.+)' | stats avg(age) by host | where host=pyrami.com ;        
  ```

#### patterns command
<a name="supported-ppl-patterns-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The `patterns` command extracts log patterns from a text field and appends the results to the search result. Grouping logs by their patterns makes it easier to aggregate stats from large volumes of log data for analysis and troubleshooting.

**Syntax**  
Use the following syntax:

```
patterns [new_field=<new-field-name>] [pattern=<pattern>] <field>    
```

**new-field-name**
+ Optional string. 
+ This is the name of the new field for extracted patterns.
+ The default is `patterns_field`. 
+ If the name already exists, it will replace the original field.

**pattern**
+ Optional string. 
+ This it the regex pattern of characters that should be filtered out from the text field. 
+ If absent, the default pattern is alphanumeric characters (`[a-zA-Z\d]`).

**field**
+ Mandatory. 
+ The field must be a text field.

**Example 1: Create the new field**  
The example shows how to use extract punctuations in `email` for each document. Parsing a null field will return an empty string.

PPL query:

```
os> source=accounts | patterns email | fields email, patterns_field ;
fetched rows / total rows = 4/4
+-----------------------+------------------+
| email                 | patterns_field   |
|-----------------------+------------------|
| jane_doe@example.com  | @.               |
| john_doe@example.net  | @.               |
| null                  |                  |
| juan_li@example.org   | @.               |
+-----------------------+------------------+
```

**Example 2: Extract log patterns**  
The example shows how to extract punctuations from a raw log field using the default patterns.

PPL query:

```
os> source=apache | patterns message | fields message, patterns_field ;
fetched rows / total rows = 4/4
+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------+
| message                                                                                                                     | patterns_field                  |
|-----------------------------------------------------------------------------------------------------------------------------+---------------------------------|
| 177.95.8.74 - upton5450 [28/Sep/2022:10:15:57 -0700] "HEAD /e-business/mindshare HTTP/1.0" 404 19927                        | ... -  [//::: -] " /-/ /."      |
| ************ - pouros8756 [28/Sep/2022:10:15:57 -0700] "GET /architectures/convergence/niches/mindshare HTTP/1.0" 100 28722 | ... -  [//::: -] " //// /."     |
| *************** - - [28/Sep/2022:10:15:57 -0700] "PATCH /strategize/out-of-the-box HTTP/1.0" 401 27439                      | ... - - [//::: -] " //--- /."   |
| ************** - - [28/Sep/2022:10:15:57 -0700] "POST /users HTTP/1.1" 301 9481                                             | ... - - [//::: -] " / /."       |
+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------+
```

**Example 3: Extract log patterns with custom regex pattern**  
The example shows how to extract punctuations from a raw log field using user defined patterns.

PPL query:

```
os> source=apache | patterns new_field='no_numbers' pattern='[0-9]' message | fields message, no_numbers ;
fetched rows / total rows = 4/4
+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| message                                                                                                                     | no_numbers                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------|
| 177.95.8.74 - upton5450 [28/Sep/2022:10:15:57 -0700] "HEAD /e-business/mindshare HTTP/1.0" 404 19927                        | ... - upton [/Sep/::: -] "HEAD /e-business/mindshare HTTP/."                         |
| 127.45.152.6 - pouros8756 [28/Sep/2022:10:15:57 -0700] "GET /architectures/convergence/niches/mindshare HTTP/1.0" 100 28722 | ... - pouros [/Sep/::: -] "GET /architectures/convergence/niches/mindshare HTTP/."   |
| *************** - - [28/Sep/2022:10:15:57 -0700] "PATCH /strategize/out-of-the-box HTTP/1.0" 401 27439                      | ... - - [/Sep/::: -] "PATCH /strategize/out-of-the-box HTTP/."                       |
| ************** - - [28/Sep/2022:10:15:57 -0700] "POST /users HTTP/1.1" 301 9481                                             | ... - - [/Sep/::: -] "POST /users HTTP/."                                            |
+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
```

**Limitation**  
The patterns command has the same limitations as the parse command.

#### rare command
<a name="supported-ppl-rare-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `rare` command to find the least common tuple of values of all fields in the field list.

**Note**  
A maximum of 10 results is returned for each distinct tuple of values of the group-by fields.

**Syntax**  
Use the following syntax:

```
rare [N] <field-list> [by-clause] rare_approx [N] <field-list> [by-clause]
```

**field-list**
+ Mandatory. 
+ A comma-delimited list of field names.

**by-clause**
+ Optional. 
+ One or more fields to group the results by.

**N**
+ The number of results to return. 
+ Default: 10

**rare\_approx**
+ The approximate count of the rare (n) fields by using estimated [cardinality by HyperLogLog\+\+ algorithm](https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html).

**Example 1: Find the least common values in a field**  
The example finds the least common gender of all the accounts.

PPL query:

```
os> source=accounts | rare gender;
os> source=accounts | rare_approx 10 gender;
os> source=accounts | rare_approx gender;
fetched rows / total rows = 2/2
+----------+
| gender   |
|----------|
| F        |
| M        |
+----------+
```

**Example 2: Find the least common values organized by gender**  
The example finds the least common age of all the accounts group by gender.

PPL query:

```
os> source=accounts | rare 5 age by gender;
os> source=accounts | rare_approx 5 age by gender;
fetched rows / total rows = 4/4
+----------+-------+
| gender   | age   |
|----------+-------|
| F        | 28    |
| M        | 32    |
| M        | 33    |
| M        | 36    |
+----------+-------+
```

#### rename command
<a name="supported-ppl-rename-command"></a>

Use the `rename` command to change the names of one or more fields in the search result.

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

**Syntax**  
Use the following syntax:

```
rename <source-field> AS <target-field>["," <source-field> AS <target-field>]...    
```

**source-field**
+ Mandatory. 
+ This is the name of the field you want to rename.

**target-field**
+ Mandatory. 
+ This is the name you want to rename to.

**Example 1: Rename one field**  
This example shows how to rename a single field.

PPL query:

```
os> source=accounts | rename account_number as an | fields an;
fetched rows / total rows = 4/4
+------+
| an   |
|------|
| 1    |
| 6    |
| 13   |
| 18   |
+------+
```

**Example 2: Rename multiple fields**  
This example shows how to rename multiple fields.

PPL query:

```
os> source=accounts | rename account_number as an, employer as emp | fields an, emp;
fetched rows / total rows = 4/4
+------+---------+
| an   | emp     |
|------+---------|
| 1    | Pyrami  |
| 6    | Netagy  |
| 13   | Quility |
| 18   | null    |
+------+---------+
```

**Limitations**
+ Overriding existing field is unsupported:

  ```
  source=accounts | grok address '%{NUMBER} %{GREEDYDATA:address}' | fields address        
  ```

#### search command
<a name="supported-ppl-search-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `search` command to retrieve documents from an index. The `search` command can only be used as the first command in a PPL query.

**Syntax**  
Use the following syntax:

```
search source=[<remote-cluster>:]<index> [boolean-expression]    
```

**search**
+ Optional.
+ Search keywords, which can be omitted.

**index**
+ Mandatory.
+ The search command must specify which index to query from. 
+ The index name can be prefixed by `<cluster name>:` for cross-cluster searches.

**bool-expression**
+ Optional. 
+ Any expression that evaluates to a boolean value.

**Example 1: Fetch all the data**  
The example show fetch all the document from accounts index.

PPL query:

```
os> source=accounts;
+------------------+-------------+----------------------+-----------+----------+--------+----------------+---------+-------+-----------------------+------------+
| account_number   | firstname   | address              | balance   | gender   | city   | employer       | state   | age   | email                 | lastname   |
|------------------+-------------+----------------------+-----------+----------+--------+----------------+---------+-------+-----------------------+------------|
| 1                | Jorge       | *** Any Lane         | 39225     | M        | Brogan | ExampleCorp    | IL      | 32    | jane_doe@example.com  | Souza      |
| 6                | John        | *** Example Street   | 5686      | M        | Dante  | AnyCorp        | TN      | 36    | john_doe@example.com  | Doe        |
| 13               | Jane        | *** Any Street       | *****     | F        | Nogal  | ExampleCompany | VA      | 28    | null                  | Doe        |
| 18               | Juan        | *** Example Court    | 4180      | M        | Orick  | null           | MD      | 33    | juan_li@example.org   | Li         |
+------------------+-------------+----------------------+-----------+----------+--------+----------------+---------+-------+-----------------------+------------+
```

**Example 2: Fetch data with condition**  
The example show fetch all the document from accounts index with .

PPL query:

```
os> SEARCH source=accounts account_number=1 or gender="F";
+------------------+-------------+--------------------+-----------+----------+--------+----------------+---------+-------+-------------------------+------------+
| account_number   | firstname   | address            | balance   | gender   | city   | employer       | state   | age   | email                -  | lastname   |
|------------------+-------------+--------------------+-----------+----------+--------+----------------+---------+-------+-------------------------+------------|
| 1                | Jorge       | *** Any Lane       | *****     | M        | Brogan | ExampleCorp    | IL      | 32    | jorge_souza@example.com | Souza      |
| 13               | Jane        | *** Any Street     | *****     | F        | Nogal  | ExampleCompany | VA      | 28    | null                    | Doe        |
+------------------+-------------+--------------------+-----------+----------+--------+-----------------+---------+-------+------------------------+------------+
```

#### sort command
<a name="supported-ppl-sort-command"></a>

Use the `sort` command to sort search result by specified fields.

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

**Syntax**  
Use the following syntax:

```
sort <[+|-] sort-field>...
```

**[\+\|-]**
+ Optional. 
+ The plus [\+] stands for ascending order with NULL/MISSING values first.
+ The minus [-] stands for descending order with NULL/MISSING values last.
+ Default: Ascending order with NULL/MISSING values first.

**sort-field**
+ Mandatory. 
+ The field used for sorting.

**Example 1: Sort by one field**  
The example shows how to sort the document with the age field in ascending order.

PPL query:

```
os> source=accounts | sort age | fields account_number, age;
fetched rows / total rows = 4/4
+------------------+-------+
| account_number   | age   |
|------------------+-------|
| 13               | 28    |
| 1                | 32    |
| 18               | 33    |
| 6                | 36    |
+------------------+-------+
```

**Example 2: Sort by one field and return all the results**  
The example shows how to sort the document with the age field in ascending order.

PPL query:

```
os> source=accounts | sort age | fields account_number, age;
fetched rows / total rows = 4/4
+------------------+-------+
| account_number   | age   |
|------------------+-------|
| 13               | 28    |
| 1                | 32    |
| 18               | 33    |
| 6                | 36    |
+------------------+-------+
```

**Example 3: Sort by one field in descending order**  
The example shows how to sort the document with the age field in descending order.

PPL query:

```
os> source=accounts | sort - age | fields account_number, age;
fetched rows / total rows = 4/4
+------------------+-------+
| account_number   | age   |
|------------------+-------|
| 6                | 36    |
| 18               | 33    |
| 1                | 32    |
| 13               | 28    |
+------------------+-------+
```

**Example 4: Sort by multiple fields**  
The example shows how to sort the document with the gender field in ascending order and the age field in descending order.

PPL query:

```
os> source=accounts | sort + gender, - age | fields account_number, gender, age;
fetched rows / total rows = 4/4
+------------------+----------+-------+
| account_number   | gender   | age   |
|------------------+----------+-------|
| 13               | F        | 28    |
| 6                | M        | 36    |
| 18               | M        | 33    |
| 1                | M        | 32    |
+------------------+----------+-------+
```

**Example 5: Sort by field include null value**  
The example shows how to sort the employer field by the default option (ascending order and null first). The result shows that the null value is in the first row.

PPL query:

```
os> source=accounts | sort employer | fields employer;
fetched rows / total rows = 4/4
+------------+
| employer   |
|------------|
| null       |
| AnyCompany |
| AnyCorp    |
| AnyOrgty   |
+------------+
```

#### stats command
<a name="supported-ppl-stats-command"></a>

Use the `stats` command to calculate the aggregation from search result.

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

**NULL/MISSING values handling**  



**NULL/MISSING values handling**  

| Function | NULL | MISSING | 
| --- | --- | --- | 
| COUNT | Not counted | Not counted | 
| SUM | Ignore | Ignore | 
| AVG | Ignore | Ignore | 
| MAX | Ignore | Ignore | 
| MIN | Ignore | Ignore | 

**Syntax**  
Use the following syntax:

```
stats <aggregation>... [by-clause]    
```

**aggregation**
+ Mandatory. 
+ An aggregation function applied to a field.

**by-clause**
+ Optional.
+ Syntax: `by [span-expression,] [field,]...`
+ Specifies fields and expressions for grouping the aggregation results. The by-clause allows you to group your aggregation results using fields and expressions. You can use scalar functions, aggregation functions, and even span expressions to split specific fields into buckets of equal intervals. 
+ Default: If no `<by-clause>` is specified, the stats command returns a single row representing the aggregation over the entire result set.

**span-expression**  

+ Optional, at most one.
+ Syntax: `span(field_expr, interval_expr)`
+ The unit of the interval expression is the natural unit by default. If the field is a date and time type field, and the interval is in date/time units, you specify the unit in the interval expression.
+ For example, splitting the `age` field into buckets by 10 years, it looks like `span(age, 10)`. To split a timestamp field into hourly intervals, use `span(timestamp, 1h)`.


**Available time units**  

| Span interval units | 
| --- | 
| millisecond (ms) | 
| second (s) | 
| minute (m, case sensitive) | 
| hour (h) | 
| day (d) | 
| week (w) | 
| month (M, case sensitive) | 
| quarter (q) | 
| year (y) | 

**Aggregation functions**  


**`COUNT`**  
Returns a count of the number of expr in the rows retrieved by a SELECT statement.

Example:

```
os> source=accounts | stats count();
fetched rows / total rows = 1/1
+-----------+
| count()   |
|-----------|
| 4         |
+-----------+
```

**`SUM`**  
Use `SUM(expr)` to return the sum of expr.

Example

```
os> source=accounts | stats sum(age) by gender;
fetched rows / total rows = 2/2
+------------+----------+
| sum(age)   | gender   |
|------------+----------|
| 28         | F        |
| 101        | M        |
+------------+----------+
```

**`AVG`**  
Use `AVG(expr)` to return the average value of expr.

Example

```
os> source=accounts | stats avg(age) by gender;
fetched rows / total rows = 2/2
+--------------------+----------+
| avg(age)           | gender   |
|--------------------+----------|
| 28.0               | F        |
| 33.666666666666664 | M        |
+--------------------+----------+
```

**`MAX`**  
Use `MAX(expr)` to return the maximum value of expr.

Example

```
os> source=accounts | stats max(age);
fetched rows / total rows = 1/1
+------------+
| max(age)   |
|------------|
| 36         |
+------------+
```

**`MIN`**  
Use `MIN(expr)` to return the minimum value of expr.

Example

```
os> source=accounts | stats min(age);
fetched rows / total rows = 1/1
+------------+
| min(age)   |
|------------|
| 28         |
+------------+
```

**`STDDEV_SAMP`**  
Use `STDDEV_SAMP(expr)` to return the sample standard deviation of expr.

Example:

```
os> source=accounts | stats stddev_samp(age);
fetched rows / total rows = 1/1
+--------------------+
| stddev_samp(age)   |
|--------------------|
| 3.304037933599835  |
+--------------------+
```

**STDDEV\_POP**  
Use `STDDEV_POP(expr)` to return the population standard deviation of expr.

Example:

```
os> source=accounts | stats stddev_pop(age);
fetched rows / total rows = 1/1
+--------------------+
| stddev_pop(age)    |
|--------------------|
| 2.**************** |
+--------------------+
```

**TAKE**  
Use `TAKE(field [, size])` to return the original values of a field. It does not guarantee on the order of values.

**field**
+ Mandatory. 
+ The field must be a text field.

**size**
+ Optional integer. 
+ The number of values should be returned. 
+ Default is 10.

**Example**  


```
os> source=accounts | stats take(firstname);
fetched rows / total rows = 1/1
+-----------------------------+
| take(firstname)             |
|-----------------------------|
| [Jane, Mary, Nikki, Juan    |
+-----------------------------+
```

**PERCENTILE or PERCENTILE\_APPROX**  
Use `PERCENTILE(expr, percent)` or `PERCENTILE_APPROX(expr, percent)` to return the approximate percentile value of expr at the specified percentage.

**percent**
+ The number must be a constant between 0 and 100.

**Example**  


```
os> source=accounts | stats percentile(age, 90) by gender;
fetched rows / total rows = 2/2
+-----------------------+----------+
| percentile(age, 90)   | gender   |
|-----------------------+----------|
| 28                    | F        |
| 36                    | M        |
+-----------------------+----------+
```

**Example 1: Calculate the count of events**  
The example shows how to calculate the count of events in the accounts.

```
os> source=accounts | stats count();
fetched rows / total rows = 1/1
+-----------+
| count()   |
|-----------|
| 4         |
+-----------+
```

**Example 2: Calculate the average of a field**  
The example shows how to calculate the average age for all accounts.

```
os> source=accounts | stats avg(age);
fetched rows / total rows = 1/1
+------------+
| avg(age)   |
|------------|
| 32.25      |
+------------+
```

**Example 3: Calculate the average of a field by group**  
The example shows how to calculate the average age for all accounts, grouped by gender.

```
os> source=accounts | stats avg(age) by gender;
fetched rows / total rows = 2/2
+--------------------+----------+
| avg(age)           | gender   |
|--------------------+----------|
| 28.0               | F        |
| 33.666666666666664 | M        |
+--------------------+----------+
```

**Example 4: Calculate the average, sum, and count of a field by group**  
The example shows how to calculate the average age, sum age, and count of events for all the accounts, grouped by gender.

```
os> source=accounts | stats avg(age), sum(age), count() by gender;
fetched rows / total rows = 2/2
+--------------------+------------+-----------+----------+
| avg(age)           | sum(age)   | count()   | gender   |
|--------------------+------------+-----------+----------|
| 28.0               | 28         | 1         | F        |
| 33.666666666666664 | 101        | 3         | M        |
+--------------------+------------+-----------+----------+
```

**Example 5: Calculate the maximum of a field**  
The example calculates the maximum age for all accounts.

```
os> source=accounts | stats max(age);
fetched rows / total rows = 1/1
+------------+
| max(age)   |
|------------|
| 36         |
+------------+
```

**Example 6: Calculate the maximum and minimum of a field by group**  
The example calculates the maximum and minimum age values for all accounts, grouped by gender.

```
os> source=accounts | stats max(age), min(age) by gender;
fetched rows / total rows = 2/2
+------------+------------+----------+
| max(age)   | min(age)   | gender   |
|------------+------------+----------|
| 28         | 28         | F        |
| 36         | 32         | M        |
+------------+------------+----------+
```

**Example 7: Calculate the distinct count of a field**  
To get the count of distinct values of a field, you can use the `DISTINCT_COUNT` (or `DC`) function instead of `COUNT`. The example calculates both the count and the distinct count of gender field of all the accounts.

```
os> source=accounts | stats count(gender), distinct_count(gender);
fetched rows / total rows = 1/1
+-----------------+--------------------------+
| count(gender)   | distinct_count(gender)   |
|-----------------+--------------------------|
| 4               | 2                        |
+-----------------+--------------------------+
```

**Example 8: Calculate the count by a span**  
The example gets the count of age by the interval of 10 years.

```
os> source=accounts | stats count(age) by span(age, 10) as age_span
fetched rows / total rows = 2/2
+--------------+------------+
| count(age)   | age_span   |
|--------------+------------|
| 1            | 20         |
| 3            | 30         |
+--------------+------------+
```

**Example 9: Calculate the count by a gender and span**  
This example counts records grouped by gender and age spans of 5 years.

```
os> source=accounts | stats count() as cnt by span(age, 5) as age_span, gender
fetched rows / total rows = 3/3
+-------+------------+----------+
| cnt   | age_span   | gender   |
|-------+------------+----------|
| 1     | 25         | F        |
| 2     | 30         | M        |
| 1     | 35         | M        |
+-------+------------+----------+
```

The span expression always appears as the first grouping key, regardless of the order specified in the command.

```
os> source=accounts | stats count() as cnt by gender, span(age, 5) as age_span
fetched rows / total rows = 3/3
+-------+------------+----------+
| cnt   | age_span   | gender   |
|-------+------------+----------|
| 1     | 25         | F        |
| 2     | 30         | M        |
| 1     | 35         | M        |
+-------+------------+----------+
```

**Example 10: Calculate the count and get email list by a gender and span**  
The example gets the count of age by the interval of 10 years and group by gender, additionally for each row get a list of at most 5 emails.

```
os> source=accounts | stats count() as cnt, take(email, 5) by span(age, 5) as age_span, gender
fetched rows / total rows = 3/3
+-------+----------------------------------------------------+------------+----------+
| cnt   | take(email, 5)                                     | age_span   | gender   |
|-------+----------------------------------------------------+------------+----------|
| 1     | []                                                 | 25         | F        |
| 2     | [janedoe@anycompany.com,juanli@examplecompany.org] | 30         | M        |
| 1     | [marymajor@examplecorp.com]                        | 35         | M        |
+-------+----------------------------------------------------+------------+----------+
```

**Example 11: Calculate the percentile of a field**  
The example shows how to calculate the percentile 90th age of all the accounts.

```
os> source=accounts | stats percentile(age, 90);
fetched rows / total rows = 1/1
+-----------------------+
| percentile(age, 90)   |
|-----------------------|
| 36                    |
+-----------------------+
```

**Example 12: Calculate the percentile of a field by group**  
The example shows how to calculate the percentile 90th age of all the accounts group by gender.

```
os> source=accounts | stats percentile(age, 90) by gender;
fetched rows / total rows = 2/2
+-----------------------+----------+
| percentile(age, 90)   | gender   |
|-----------------------+----------|
| 28                    | F        |
| 36                    | M        |
+-----------------------+----------+
```

**Example 13: Calculate the percentile by a gender and span**  
The example gets the percentile 90th age by the interval of 10 years and group by gender.

```
os> source=accounts | stats percentile(age, 90) as p90 by span(age, 10) as age_span, gender
fetched rows / total rows = 2/2
+-------+------------+----------+
| p90   | age_span   | gender   |
|-------+------------+----------|
| 28    | 20         | F        |
| 36    | 30         | M        |
+-------+------------+----------+
```

```
- `source = table | stats avg(a) `
- `source = table | where a < 50 | stats avg(c) `
- `source = table | stats max(c) by b`
- `source = table | stats count(c) by b | head 5`
- `source = table | stats distinct_count(c)`
- `source = table | stats stddev_samp(c)`
- `source = table | stats stddev_pop(c)`
- `source = table | stats percentile(c, 90)`
- `source = table | stats percentile_approx(c, 99)`
```

**Aggregations with span**  


```
- `source = table  | stats count(a) by span(a, 10) as a_span`
- `source = table  | stats sum(age) by span(age, 5) as age_span | head 2`
- `source = table  | stats avg(age) by span(age, 20) as age_span, country  | sort - age_span |  head 2`
```

**Aggregations with timewindow span (tumble windowing function)**  


```
- `source = table | stats sum(productsAmount) by span(transactionDate, 1d) as age_date | sort age_date`
- `source = table | stats sum(productsAmount) by span(transactionDate, 1w) as age_date, productId`
```

**Aggregations group by multiple levels**  


```
- `source = table | stats avg(age) as avg_state_age by country, state | stats avg(avg_state_age) as avg_country_age by country`
- `source = table | stats avg(age) as avg_city_age by country, state, city | eval new_avg_city_age = avg_city_age - 1 | stats avg(new_avg_city_age) as avg_state_age by country, state | where avg_state_age > 18 | stats avg(avg_state_age) as avg_adult_country_age by country`
```

#### subquery command
<a name="supported-ppl-subquery-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `subquery` command to perform complex, nested queries within your Piped Processing Language (PPL) statements.

```
source=logs | where field in [ subquery source=events | where condition | fields field ]
```

In this example, the primary search (`source=logs`) is filtered by results from the subquery (`source=events`).

The subquery command supports multiple levels of nesting for complex data analysis.

**Nested Subquery Example**  


```
source=logs | where id in [ subquery source=users | where user in [ subquery source=actions | where action="login" | fields user] | fields uid ]  
```

**InSubquery Usage**
+ `source = outer | where a in [ source = inner | fields b ]`
+ `source = outer | where (a) in [ source = inner | fields b ]`
+ `source = outer | where (a,b,c) in [ source = inner | fields d,e,f ]`
+ `source = outer | where a not in [ source = inner | fields b ]`
+ `source = outer | where (a) not in [ source = inner | fields b ]`
+ `source = outer | where (a,b,c) not in [ source = inner | fields d,e,f ]`
+ `source = outer a in [ source = inner | fields b ]` (search filtering with subquery)
+ `source = outer a not in [ source = inner | fields b ]` (search filtering with subquery)
+ `source = outer | where a in [ source = inner1 | where b not in [ source = inner2 | fields c ] | fields b ]` (nested)
+ `source = table1 | inner join left = l right = r on l.a = r.a AND r.a in [ source = inner | fields d ] | fields l.a, r.a, b, c` (as join filter)

**SQL Migration Examples with IN-Subquery PPL**  
TPC-H Q4 (in-subquery with aggregation)

```
select
  o_orderpriority,
  count(*) as order_count
from
  orders
where
  o_orderdate >= date '1993-07-01'
  and o_orderdate < date '1993-07-01' + interval '3' month
  and o_orderkey in (
    select
      l_orderkey
    from
      lineitem
    where l_commitdate < l_receiptdate
  )
group by
  o_orderpriority
order by
  o_orderpriority
```

Rewritten by PPL InSubquery query:

```
source = orders
| where o_orderdate >= "1993-07-01" and o_orderdate < "1993-10-01" and o_orderkey IN
  [ source = lineitem
    | where l_commitdate < l_receiptdate
    | fields l_orderkey
  ]
| stats count(1) as order_count by o_orderpriority
| sort o_orderpriority
| fields o_orderpriority, order_count
```

TPC-H Q20 (nested in-subquery)

```
select
  s_name,
  s_address
from
  supplier,
  nation
where
  s_suppkey in (
    select
      ps_suppkey
    from
      partsupp
    where
      ps_partkey in (
        select
          p_partkey
        from
          part
        where
          p_name like 'forest%'
      )
  )
  and s_nationkey = n_nationkey
  and n_name = 'CANADA'
order by
  s_name
```

Rewritten by PPL InSubquery query:

```
source = supplier
| where s_suppkey IN [
    source = partsupp
    | where ps_partkey IN [
        source = part
        | where like(p_name, "forest%")
        | fields p_partkey
      ]
    | fields ps_suppkey
  ]
| inner join left=l right=r on s_nationkey = n_nationkey and n_name = 'CANADA'
  nation
| sort s_name
```

**ExistsSubquery usage**  
Assumptions: `a`, `b` are fields of table outer, `c`, `d` are fields of table inner, `e`, `f` are fields of table inner2.
+ `source = outer | where exists [ source = inner | where a = c ]`
+ `source = outer | where not exists [ source = inner | where a = c ]`
+ `source = outer | where exists [ source = inner | where a = c and b = d ]`
+ `source = outer | where not exists [ source = inner | where a = c and b = d ]`
+ `source = outer exists [ source = inner | where a = c ]` (search filtering with subquery)
+ `source = outer not exists [ source = inner | where a = c ]` (search filtering with subquery)
+ `source = table as t1 exists [ source = table as t2 | where t1.a = t2.a ]` (table alias is useful in exists subquery)
+ `source = outer | where exists [ source = inner1 | where a = c and exists [ source = inner2 | where c = e ] ]` (nested)
+ `source = outer | where exists [ source = inner1 | where a = c | where exists [ source = inner2 | where c = e ] ]` (nested)
+ `source = outer | where exists [ source = inner | where c > 10 ]` (uncorrelated exists)
+ `source = outer | where not exists [ source = inner | where c > 10 ]` (uncorrelated exists)
+ `source = outer | where exists [ source = inner ] | eval l = "nonEmpty" | fields l` (special uncorrelated exists)

**ScalarSubquery usage**  
Assumptions: `a`, `b` are fields of table outer, `c`, `d` are fields of table inner, `e`, `f` are fields of table nested

**Uncorrelated scalar subquery**  
In Select:
+ `source = outer | eval m = [ source = inner | stats max(c) ] | fields m, a`
+ `source = outer | eval m = [ source = inner | stats max(c) ] + b | fields m, a`

In Where:
+ `source = outer | where a > [ source = inner | stats min(c) ] | fields a`

In Search filter:
+ `source = outer a > [ source = inner | stats min(c) ] | fields a`

**Correlated scalar subquery**  
In Select:
+ `source = outer | eval m = [ source = inner | where outer.b = inner.d | stats max(c) ] | fields m, a`
+ `source = outer | eval m = [ source = inner | where b = d | stats max(c) ] | fields m, a`
+ `source = outer | eval m = [ source = inner | where outer.b > inner.d | stats max(c) ] | fields m, a`

In Where:
+ `source = outer | where a = [ source = inner | where outer.b = inner.d | stats max(c) ]`
+ `source = outer | where a = [ source = inner | where b = d | stats max(c) ]`
+ `source = outer | where [ source = inner | where outer.b = inner.d OR inner.d = 1 | stats count() ] > 0 | fields a`

In Search filter:
+ `source = outer a = [ source = inner | where b = d | stats max(c) ]`
+ `source = outer [ source = inner | where outer.b = inner.d OR inner.d = 1 | stats count() ] > 0 | fields a`

**Nested scalar subquery**  

+ `source = outer | where a = [ source = inner | stats max(c) | sort c ] OR b = [ source = inner | where c = 1 | stats min(d) | sort d ]`
+ `source = outer | where a = [ source = inner | where c = [ source = nested | stats max(e) by f | sort f ] | stats max(d) by c | sort c | head 1 ]`

**(Relation) Subquery**  
`InSubquery`, `ExistsSubquery` and `ScalarSubquery` are all subquery expressions. But `RelationSubquery` is not a subquery expression, it is a subquery plan which is common used in Join or From clause.
+ `source = table1 | join left = l right = r [ source = table2 | where d > 10 | head 5 ]` (subquery in join right side)
+ `source = [ source = table1 | join left = l right = r [ source = table2 | where d > 10 | head 5 ] | stats count(a) by b ] as outer | head 1`

**Additional Context**  
`InSubquery`, `ExistsSubquery`, and `ScalarSubquery` are subquery expressions commonly used in `where` clauses and search filters.

Where command:

```
| where <boolean expression> | ...    
```

Search filter:

```
search source=* <boolean expression> | ...    
```

A subquery expression could be used in a boolean expression:

```
| where orders.order_id in [ source=returns | where return_reason="damaged" | field order_id ]    
```

The `orders.order_id in [ source=... ]` is a `<boolean expression>`.

In general, we name this kind of subquery clause the `InSubquery` expression. It is a `<boolean expression>`.

**Subquery with different join types**  
Example using a `ScalarSubquery`:

```
source=employees
| join source=sales on employees.employee_id = sales.employee_id
| where sales.sale_amount > [ source=targets | where target_met="true" | fields target_value ]
```

Unlike InSubquery, ExistsSubquery, and ScalarSubquery, a RelationSubquery is not a subquery expression. Instead, it's a subquery plan.

```
SEARCH source=customer
| FIELDS c_custkey
| LEFT OUTER JOIN left = c, right = o ON c.c_custkey = o.o_custkey
   [
      SEARCH source=orders
      | WHERE o_comment NOT LIKE '%unusual%packages%'
      | FIELDS o_orderkey, o_custkey
   ]
| STATS ...
```

#### top command
<a name="supported-ppl-top-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `top` command to find the most common tuple of values of all fields in the field list.

**Syntax**  
Use the following syntax:

```
top [N] <field-list> [by-clause] top_approx [N] <field-list> [by-clause]
```

**N**
+ The number of results to return. 
+ Default: 10

**field-list**
+ Mandatory. 
+ A comma-delimited list of field names.

**by-clause**
+ Optional. 
+ One or more fields to group the results by.

**top\_approx**
+ An approximate count of the (n) top fields by using the estimated [cardinality by HyperLogLog\+\+ algorithm](https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html).

**Example 1: Find the most common values in a field**  
The example finds the most common gender for all accounts.

PPL query:

```
os> source=accounts | top gender;
os> source=accounts | top_approx gender;
fetched rows / total rows = 2/2
+----------+
| gender   |
|----------|
| M        |
| F        |
+----------+
```

**Example 2: Find the most common values in a field (limited to 1)**  
The example finds the single most common gender for all accounts.

PPL query:

```
os> source=accounts | top_approx 1 gender;
fetched rows / total rows = 1/1
+----------+
| gender   |
|----------|
| M        |
+----------+
```

**Example 3: Find the most common values, grouped by gender**  
The example finds the most common age for all accounts, grouped by gender.

PPL query:

```
os> source=accounts | top 1 age by gender;
os> source=accounts | top_approx 1 age by gender;
fetched rows / total rows = 2/2
+----------+-------+
| gender   | age   |
|----------+-------|
| F        | 28    |
| M        | 32    |
+----------+-------+
```

#### trendline command
<a name="supported-ppl-trendline-commands"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `trendline` command to calculate moving averages of fields.

**Syntax**  
Use the following syntax

```
TRENDLINE [sort <[+|-] sort-field>] SMA(number-of-datapoints, field) [AS alias] [SMA(number-of-datapoints, field) [AS alias]]... 
```

**[\+\|-]**
+ Optional. 
+ The plus [\+] stands for ascending order with NULL/MISSING values first.
+ The minus [-] stands for descending order with NULL/MISSING values last. 
+ Default: Ascending order with NULL/MISSING values first.

**sort-field**
+ Mandatory when sorting is used. 
+ The field used for sorting.

**number-of-datapoints**
+ Mandatory. 
+ The number of datapoints that calculate the moving average.
+ Must be greater than zero.

**field**
+ Mandatory. 
+ The name of the field the moving average should be calculated for.

**alias**
+ Optional. 
+ The name of the resulting column containing the moving average.

Only the Simple Moving Average (SMA) type is supported. It is calculated like this:

```
f[i]: The value of field 'f' in the i-th data-point
n: The number of data-points in the moving window (period)
t: The current time index

SMA(t) = (1/n) * Σ(f[i]), where i = t-n+1 to t
```

**Example 1: Calculate simple moving average for a timeseries of temperatures**  
The example calculates the simple moving average over temperatures using two datapoints.

PPL query:

```
os> source=t | trendline sma(2, temperature) as temp_trend;
fetched rows / total rows = 5/5
+-----------+---------+--------------------+----------+
|temperature|device-id|           timestamp|temp_trend|
+-----------+---------+--------------------+----------+
|         12|     1492|2023-04-06 17:07:...|      NULL|
|         12|     1492|2023-04-06 17:07:...|      12.0|
|         13|      256|2023-04-06 17:07:...|      12.5|
|         14|      257|2023-04-06 17:07:...|      13.5|
|         15|      258|2023-04-06 17:07:...|      14.5|
+-----------+---------+--------------------+----------+
```

**Example 2: Calculate simple moving averages for a timeseries of temperatures with sorting**  
The example calculates two simple moving average over temperatures using two and three datapoints sorted descending by device-id.

PPL query:

```
os> source=t | trendline sort - device-id sma(2, temperature) as temp_trend_2 sma(3, temperature) as temp_trend_3;
fetched rows / total rows = 5/5
+-----------+---------+--------------------+------------+------------------+
|temperature|device-id|           timestamp|temp_trend_2|      temp_trend_3|
+-----------+---------+--------------------+------------+------------------+
|         15|      258|2023-04-06 17:07:...|        NULL|              NULL|
|         14|      257|2023-04-06 17:07:...|        14.5|              NULL|
|         13|      256|2023-04-06 17:07:...|        13.5|              14.0|
|         12|     1492|2023-04-06 17:07:...|        12.5|              13.0|
|         12|     1492|2023-04-06 17:07:...|        12.0|12.333333333333334|
+-----------+---------+--------------------+------------+------------------+
```

#### where command
<a name="supported-ppl-where-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

The `where` command uses a bool-expression to filter the search result. It only returns the result when bool-expression evaluates to true.

**Syntax**  
Use the following syntax:

```
where <boolean-expression>    
```

**bool-expression**
+ Optional. 
+ Any expression which could be evaluated to a boolean value.

**Example 1: Filter result set with condition**  
The example shows how to fetch documents from the accounts index that meet specific conditions.

PPL query:

```
os> source=accounts | where account_number=1 or gender="F" | fields account_number, gender;
fetched rows / total rows = 2/2
+------------------+----------+
| account_number   | gender   |
|------------------+----------|
| 1                | M        |
| 13               | F        |
+------------------+----------+
```

**Additional examples**  


**Filters with logical conditions**
+ `source = table | where c = 'test' AND a = 1 | fields a,b,c`
+ `source = table | where c != 'test' OR a > 1 | fields a,b,c | head 1`
+ `source = table | where c = 'test' NOT a > 1 | fields a,b,c`
+ `source = table | where a = 1 | fields a,b,c`
+ `source = table | where a >= 1 | fields a,b,c`
+ `source = table | where a < 1 | fields a,b,c`
+ `source = table | where b != 'test' | fields a,b,c`
+ `source = table | where c = 'test' | fields a,b,c | head 3`
+ `source = table | where ispresent(b)`
+ `source = table | where isnull(coalesce(a, b)) | fields a,b,c | head 3`
+ `source = table | where isempty(a)`
+ `source = table | where isblank(a)`
+ `source = table | where case(length(a) > 6, 'True' else 'False') = 'True'`
+ `source = table | where a between 1 and 4` - Note: This returns a >= 1 and a <= 4, i.e. [1, 4]
+ `source = table | where b not between '2024-09-10' and '2025-09-10'` - Note: This returns b >= '\*\*\*\*\*\*\*\*\*\*' and b <= '2025-09-10'
+ `source = table | where cidrmatch(ip, '***********/24')`
+ `source = table | where cidrmatch(ipv6, '2003:db8::/32')`

```
source = table | eval status_category =
    case(a >= 200 AND a < 300, 'Success',
    a >= 300 AND a < 400, 'Redirection',
    a >= 400 AND a < 500, 'Client Error',
    a >= 500, 'Server Error'
    else 'Incorrect HTTP status code')
    | where case(a >= 200 AND a < 300, 'Success',
    a >= 300 AND a < 400, 'Redirection',
    a >= 400 AND a < 500, 'Client Error',
    a >= 500, 'Server Error'
    else 'Incorrect HTTP status code'
    ) = 'Incorrect HTTP status code'
```

```
source = table
    | eval factor = case(a > 15, a - 14, isnull(b), a - 7, a < 3, a + 1 else 1)
    | where case(factor = 2, 'even', factor = 4, 'even', factor = 6, 'even', factor = 8, 'even' else 'odd') = 'even'
    |  stats count() by factor
```

#### field summary
<a name="supported-ppl-field-summary-command"></a>

**Note**  
To see which AWS data source integrations support this PPL command, see [Commands](#supported-ppl-commands).

Use the `fieldsummary` command to calculate basic statistics for each field (count, distinct count, min, max, avg, stddev, mean) and determine the data type of each field. This command can be used with any preceding pipe and will take them into account.

**Syntax**  
Use the following syntax. For CloudWatch Logs use cases, only one field in a query is supported.

```
... | fieldsummary <field-list> (nulls=true/false)
```

**includefields**
+ List of all the columns to be collected with statistics into a unified result set.

**Nulls**
+ Optional. 
+  If set to true, include null values in the aggregation calculations (replace null with zero for numeric values).

**Example 1**  
PPL query:

```
os> source = t | where status_code != 200 | fieldsummary includefields= status_code nulls=true
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
| Fields           | COUNT       | COUNT_DISTINCT    |  MIN  |  MAX   |  AVG   |  MEAN   |        STDDEV       | NUlls | TYPEOF |
|------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
| "status_code"    |      2      |         2         | 301   |   403  |  352.0 |  352.0  |  72.12489168102785  |  0    | "int"  |
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
```

**Example 2**  
PPL query:

```
os> source = t | fieldsummary includefields= id, status_code, request_path nulls=true
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
| Fields           | COUNT       | COUNT_DISTINCT    |  MIN  |  MAX   |  AVG   |  MEAN   |        STDDEV       | NUlls | TYPEOF |
|------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
|       "id"       |      6      |         6         | 1     |   6    |  3.5   |   3.5  |  1.8708286933869707  |  0    | "int"  |
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
| "status_code"    |      4      |         3         | 200   |   403  |  184.0 |  184.0  |  161.16699413961905 |  2    | "int"  |
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
| "request_path"   |      2      |         2         | /about| /home  |  0.0    |  0.0     |      0            |  2    |"string"|
+------------------+-------------+------------+------------+------------+------------+------------+------------+----------------|
```

#### expand command
<a name="supported-ppl-expand-command"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

Use the `expand` command to flatten a field of type Array<Any> or Map<Any>, producing individual rows for each element or key-value pair.

**Syntax**  
Use the following syntax:

```
expand <field> [As alias]
```

**field**
+ The field to be expanded (exploded). 
+ The field must be of a supported type.

**alias**
+ Optional.
+ The name to be used instead of the original field name.

**Usage guidelines**  
The expand command produces a row for each element in the specified array or map field, where:
+ Array elements become individual rows. 
+ Map key-value pairs are broken into separate rows, with each key-value represented as a row. 
+ When an alias is provided, the exploded values are represented under the alias instead of the original field name. 

You can use this command in combination with other commands, such as stats, eval, and parse, to manipulate or extract data post-expansion.

**Examples**
+ `source = table | expand employee | stats max(salary) as max by state, company `
+ `source = table | expand employee as worker | stats max(salary) as max by state, company `
+ `source = table | expand employee as worker | eval bonus = salary * 3 | fields worker, bonus` 
+ `source = table | expand employee | parse description '(?<email>.+@.+)' | fields employee, email` 
+ `source = table | eval array=json_array(1, 2, 3) | expand array as uid | fields name, occupation, uid `
+ `source = table | expand multi_valueA as multiA | expand multi_valueB as multiB` 

You can use the expand command in combination with other commands such as eval, stats, and more. Using multiple expand commands will create a Cartesian product of all the internal elements within each composite array or map.

**Effective SQL push-down query**  
The expand command is translated into an equivalent SQL operation using LATERAL VIEW explode, allowing for efficient exploding of arrays or maps at the SQL query level.

```
SELECT customer exploded_productId
FROM table
LATERAL VIEW explode(productId) AS exploded_productId
```

The explode command offers the following functionality: 
+ It is a column operation that returns a new column. 
+ It creates a new row for every element in the exploded column. 
+ Internal nulls are ignored as part of the exploded field (no row is created/exploded for null).

#### PPL functions
<a name="supported-ppl-functions-details"></a>

**Topics**
+ [PPL condition functions](#supported-ppl-condition-functions)
+ [PPL cryptographic hash functions](#supported-ppl-cryptographic-functions)
+ [PPL date and time functions](#supported-ppl-date-time-functions)
+ [PPL expressions](#supported-ppl-expressions)
+ [PPL IP address functions](#supported-ppl-ip-address-functions)
+ [PPL JSON functions](#supported-ppl-json-functions)
+ [PPL Lambda functions](#supported-ppl-lambda-functions)
+ [PPL mathematical functions](#supported-ppl-math-functions)
+ [PPL string functions](#supported-ppl-string-functions)
+ [PPL type conversion functions](#supported-ppl-type-conversion-functions)

##### PPL condition functions
<a name="supported-ppl-condition-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### ISNULL
<a name="supported-ppl-condition-functions-isnull"></a>

**Description**: `isnull(field)` returns true if the field is null.

**Argument type:**
+ All supported data types.

**Return type:**
+ BOOLEAN

**Example**:

```
os> source=accounts | eval result = isnull(employer) | fields result, employer, firstname
fetched rows / total rows = 4/4
+----------+-------------+-------------+
| result   | employer    | firstname   |
|----------+-------------+-------------|
| False    | AnyCompany  | Mary        |
| False    | ExampleCorp | Jane        |
| False    | ExampleOrg  | Nikki       |
| True     | null        | Juan        |
+----------+-------------+-------------+
```

##### ISNOTNULL
<a name="supported-ppl-condition-functions-isnotnull"></a>

**Description**: `isnotnull(field)` returns true if the field is not null.

**Argument type:**
+ All supported data types.

**Return type:**
+ BOOLEAN

**Example**:

```
os> source=accounts | where not isnotnull(employer) | fields account_number, employer
fetched rows / total rows = 1/1
+------------------+------------+
| account_number   | employer   |
|------------------+------------|
| 18               | null       |
+------------------+------------+
```

##### EXISTS
<a name="supported-ppl-condition-functions-exists"></a>

**Example**:

```
os> source=accounts | where exists(email) | fields account_number, email
fetched rows / total rows = 1/1
```

##### IFNULL
<a name="supported-ppl-condition-functions-ifnull"></a>

**Description**: `ifnull(field1, field2)` returns `field2` if `field1` is null.

**Argument type:**
+ All supported data types. 
+ If the two parameters have different types, the function will fail the semantic check.

**Return type:**
+ Any

**Example**:

```
os> source=accounts | eval result = ifnull(employer, 'default') | fields result, employer, firstname
fetched rows / total rows = 4/4
+------------+------------+-------------+
| result     | employer   | firstname   |
|------------+------------+-------------|
| AnyCompany | AnyCompany | Mary        |
| ExampleCorp| ExampleCorp| Jane        |
| ExampleOrg | ExampleOrg | Nikki       |
| default    | null       | Juan        |
+------------+------------+-------------+
```

##### NULLIF
<a name="supported-ppl-condition-functions-nullif"></a>

**Description**: `nullif(field1, field2)` return null if two parameters are same, otherwise return field1.

**Argument type:**
+ All supported data types. 
+ If the two parameters have different types, the function will fail the semantic check.

**Return type:**
+ Any

**Example**:

```
os> source=accounts | eval result = nullif(employer, 'AnyCompany') | fields result, employer, firstname
fetched rows / total rows = 4/4
+----------------+----------------+-------------+
| result         | employer       | firstname   |
|----------------+----------------+-------------|
| null           | AnyCompany     | Mary        |
| ExampleCorp    | ExampleCorp    | Jane        |
| ExampleOrg     | ExampleOrg     | Nikki       |
| null           | null           | Juan        |
+----------------+----------------+-------------+
```

##### IF
<a name="supported-ppl-condition-functions-if"></a>

**Description**: `if(condition, expr1, expr2)` returns `expr1` if the condition is true, otherwise it returns `expr2`.

**Argument type:**
+ All supported data types. 
+ If the two parameters have different types, the function will fail the semantic check.

**Return type:**
+ Any

**Example**:

```
os> source=accounts | eval result = if(true, firstname, lastname) | fields result, firstname, lastname
fetched rows / total rows = 4/4
+----------+-------------+----------+
| result   | firstname | lastname   |
|----------+-------------+----------|
| Jane     | Jane      | Doe        |
| Mary     | Mary      | Major      |
| Pat      | Pat       | Candella   |
| Dale     | Jorge     | Souza      |
+----------+-----------+------------+

os> source=accounts | eval result = if(false, firstname, lastname) | fields result, firstname, lastname
fetched rows / total rows = 4/4
+----------+-------------+------------+
| result   | firstname   | lastname   |
|----------+-------------+------------|
| Doe      | Jane        | Doe        |
| Major    | Mary        | Major      |
| Candella | Pat         | Candella   |
| Souza    | Jorge       | Souza      |
+----------+-------------+------------+

os> source=accounts | eval is_vip = if(age > 30 AND isnotnull(employer), true, false) | fields is_vip, firstname, lastname
fetched rows / total rows = 4/4
+----------+-------------+------------+
| is_vip   | firstname   | lastname   |
|----------+-------------+------------|
| True     | Jane        | Doe        |
| True     | Mary        | Major      |
| False    | Pat         | Candella   |
| False    | Jorge       | Souza      |
+----------+-------------+------------+
```

##### PPL cryptographic hash functions
<a name="supported-ppl-cryptographic-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### MD5
<a name="supported-ppl-cryptographic-functions-md5"></a>

MD5 calculates the MD5 digest and returns the value as a 32 character hex string.

**Usage**: `md5('hello')`

**Argument type:**
+ STRING

**Return type:**
+ STRING

**Example:**

```
os> source=people | eval `MD5('hello')` = MD5('hello') | fields `MD5('hello')`
fetched rows / total rows = 1/1
+----------------------------------+
| MD5('hello')                     |
|----------------------------------|
| <32 character hex string>        |
+----------------------------------+
```

##### SHA1
<a name="supported-ppl-cryptographic-functions-sha1"></a>

SHA1 returns the hex string result of SHA-1.

**Usage**: `sha1('hello')`

**Argument type:**
+ STRING

**Return type:**
+ STRING

**Example:**

```
os> source=people | eval `SHA1('hello')` = SHA1('hello') | fields `SHA1('hello')`
fetched rows / total rows = 1/1
+------------------------------------------+
| SHA1('hello')                            |
|------------------------------------------|
| <40-character SHA-1 hash result>         |
+------------------------------------------+
```

##### SHA2
<a name="supported-ppl-cryptographic-functions-sha2"></a>

SHA2 returns the hex string result of SHA-2 family of hash functions (SHA-224, SHA-256, SHA-384, and SHA-512). The numBits indicates the desired bit length of the result, which must have a value of 224, 256, 384, 512

**Usage:**
+ `sha2('hello',256)`
+ `sha2('hello',512)`

**Argument type:**
+ STRING, INTEGER

**Return type:**
+ STRING

**Example:**

```
os> source=people | eval `SHA2('hello',256)` = SHA2('hello',256) | fields `SHA2('hello',256)`
fetched rows / total rows = 1/1
+------------------------------------------------------------------+
| SHA2('hello',256)                                                |
|------------------------------------------------------------------|
| <64-character SHA-256 hash result>                               |
+------------------------------------------------------------------+

os> source=people | eval `SHA2('hello',512)` = SHA2('hello',512) | fields `SHA2('hello',512)`
fetched rows / total rows = 1/1
+------------------------------------------------------------------+
| SHA2('hello',512)                                                |                                                                |
|------------------------------------------------------------------|
| <128-character SHA-512 hash result>                              |
+------------------------------------------------------------------+
```

##### PPL date and time functions
<a name="supported-ppl-date-time-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `DAY`
<a name="supported-ppl-date-time-functions-day"></a>

**Usage**: `DAY(date)` extracts the day of the month for a date, in the range 1 to 31.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAYOFMONTH`, `DAY_OF_MONTH`

**Example**:

```
os> source=people | eval `DAY(DATE('2020-08-26'))` = DAY(DATE('2020-08-26')) | fields `DAY(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+---------------------------+
| DAY(DATE('2020-08-26'))   |
|---------------------------|
| 26                        |
+---------------------------+
```

##### `DAYOFMONTH`
<a name="supported-ppl-date-time-functions-dayofmonth"></a>

**Usage**: `DAYOFMONTH(date)` extracts the day of the month for a date, in the range 1 to 31.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAY`, `DAY_OF_MONTH`

**Example**:

```
os> source=people | eval `DAYOFMONTH(DATE('2020-08-26'))` = DAYOFMONTH(DATE('2020-08-26')) | fields `DAYOFMONTH(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+----------------------------------+
| DAYOFMONTH(DATE('2020-08-26'))   |
|----------------------------------|
| 26                               |
+----------------------------------+
```

##### `DAY_OF_MONTH`
<a name="supported-ppl-date-time-functions-day-of-month"></a>

**Usage**: `DAY_OF_MONTH(DATE)` extracts the day of the month for a date, in the range 1 to 31.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAY`, `DAYOFMONTH`

**Example**:

```
os> source=people | eval `DAY_OF_MONTH(DATE('2020-08-26'))` = DAY_OF_MONTH(DATE('2020-08-26')) | fields `DAY_OF_MONTH(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+------------------------------------+
| DAY_OF_MONTH(DATE('2020-08-26'))   |
|------------------------------------|
| 26                                 |
+------------------------------------+
```

##### `DAYOFWEEK`
<a name="supported-ppl-date-time-functions-dayofweek"></a>

**Usage**: `DAYOFWEEK(DATE)` returns the weekday index for a date (1 = Sunday, 2 = Monday, ..., 7 = Saturday).

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAY_OF_WEEK`

**Example**:

```
os> source=people | eval `DAYOFWEEK(DATE('2020-08-26'))` = DAYOFWEEK(DATE('2020-08-26')) | fields `DAYOFWEEK(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+---------------------------------+
| DAYOFWEEK(DATE('2020-08-26'))   |
|---------------------------------|
| 4                               |
+---------------------------------+
```

##### `DAY_OF_WEEK`
<a name="supported-ppl-date-time-functions-day-of-week"></a>

**Usage**: `DAY_OF_WEEK(DATE)` returns the weekday index for a date (1 = Sunday, 2 = Monday, ..., 7 = Saturday).

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAYOFWEEK`

**Example**:

```
os> source=people | eval `DAY_OF_WEEK(DATE('2020-08-26'))` = DAY_OF_WEEK(DATE('2020-08-26')) | fields `DAY_OF_WEEK(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-----------------------------------+
| DAY_OF_WEEK(DATE('2020-08-26'))   |
|-----------------------------------|
| 4                                 |
+-----------------------------------+
```

##### `DAYOFYEAR`
<a name="supported-ppl-date-time-functions-dayofyear"></a>

**Usage**: `DAYOFYEAR(DATE)` returns the day of the year for a date, in the range 1 to 366.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAY_OF_YEAR`

**Example**:

```
os> source=people | eval `DAYOFYEAR(DATE('2020-08-26'))` = DAYOFYEAR(DATE('2020-08-26')) | fields `DAYOFYEAR(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+---------------------------------+
| DAYOFYEAR(DATE('2020-08-26'))   |
|---------------------------------|
| 239                             |
+---------------------------------+
```

##### `DAY_OF_YEAR`
<a name="supported-ppl-date-time-functions-day-of-year"></a>

**Usage**: `DAY_OF_YEAR(DATE)` returns the day of the year for a date, in the range 1 to 366.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `DAYOFYEAR`

**Example**:

```
os> source=people | eval `DAY_OF_YEAR(DATE('2020-08-26'))` = DAY_OF_YEAR(DATE('2020-08-26')) | fields `DAY_OF_YEAR(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-----------------------------------+
| DAY_OF_YEAR(DATE('2020-08-26'))   |
|-----------------------------------|
| 239                               |
+-----------------------------------+
```

##### `DAYNAME`
<a name="supported-ppl-date-time-functions-dayname"></a>

**Usage**: `DAYNAME(DATE)` returns the name of the weekday for a date, including Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: STRING

**Example**:

```
os> source=people | eval `DAYNAME(DATE('2020-08-26'))` = DAYNAME(DATE('2020-08-26')) | fields `DAYNAME(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-------------------------------+
| DAYNAME(DATE('2020-08-26'))   |
|-------------------------------|
| Wednesday                     |
+-------------------------------+
```

##### `FROM_UNIXTIME`
<a name="supported-ppl-date-time-functions-from-unixtime"></a>

**Usage**: `FROM_UNIXTIME` returns a representation of the argument given as a timestamp or character string value. This function performs a reverse conversion of the `UNIX_TIMESTAMP` function. 

If you provide a second argument, `FROM_UNIXTIME` uses it to format the result similar to the `DATE_FORMAT` function. 

If the timestamp is outside of the range 1970-01-01 00:00:00 to 3001-01-18 23:59:59.999999 (0 to 32536771199.999999 epoch time), the function returns `NULL`.

**Argument type**: DOUBLE, STRING

**Return type map**:

DOUBLE -> TIMESTAMP

DOUBLE, STRING -> STRING

**Examples**:

```
os> source=people | eval `FROM_UNIXTIME(1220249547)` = FROM_UNIXTIME(1220249547) | fields `FROM_UNIXTIME(1220249547)`
fetched rows / total rows = 1/1
+-----------------------------+
| FROM_UNIXTIME(1220249547)   |
|-----------------------------|
| 2008-09-01 06:12:27         |
+-----------------------------+

os> source=people | eval `FROM_UNIXTIME(1220249547, 'HH:mm:ss')` = FROM_UNIXTIME(1220249547, 'HH:mm:ss') | fields `FROM_UNIXTIME(1220249547, 'HH:mm:ss')`
fetched rows / total rows = 1/1
+-----------------------------------------+
| FROM_UNIXTIME(1220249547, 'HH:mm:ss')   |
|-----------------------------------------|
| 06:12:27                                |
+-----------------------------------------+
```

##### `HOUR`
<a name="supported-ppl-date-time-functions-hour"></a>

**Usage**: `HOUR(TIME)` extracts the hour value for time. 

Unlike a standard time of day, the time value in this function can have a range larger than 23. As a result, the return value of `HOUR(TIME)` can be greater than 23.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `HOUR_OF_DAY`

**Example**:

```
os> source=people | eval `HOUR(TIME('01:02:03'))` = HOUR(TIME('01:02:03')) | fields `HOUR(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+--------------------------+
| HOUR(TIME('01:02:03'))   |
|--------------------------|
| 1                        |
+--------------------------+
```

##### `HOUR_OF_DAY`
<a name="supported-ppl-date-time-functions-hour-of-day"></a>

**Usage**: `HOUR_OF_DAY(TIME)` extracts the hour value from the given time. 

Unlike a standard time of day, the time value in this function can have a range larger than 23. As a result, the return value of `HOUR_OF_DAY(TIME)` can be greater than 23.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `HOUR`

**Example**:

```
os> source=people | eval `HOUR_OF_DAY(TIME('01:02:03'))` = HOUR_OF_DAY(TIME('01:02:03')) | fields `HOUR_OF_DAY(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+---------------------------------+
| HOUR_OF_DAY(TIME('01:02:03'))   |
|---------------------------------|
| 1                               |
+---------------------------------+
```

##### `LAST_DAY`
<a name="supported-ppl-date-time-functions-last-day"></a>

**Usage**: `LAST_DAY` returns the last day of the month as a DATE value for the given date argument.

**Argument type**: DATE/STRING/TIMESTAMP/TIME

**Return type**: DATE

**Example**:

```
os> source=people | eval `last_day('2023-02-06')` = last_day('2023-02-06') | fields `last_day('2023-02-06')`
fetched rows / total rows = 1/1
+--------------------------+
| last_day('2023-02-06')   |
|--------------------------|
| 2023-02-28               |
+--------------------------+
```

##### `LOCALTIMESTAMP`
<a name="supported-ppl-date-time-functions-localtimestamp"></a>

**Usage**: `LOCALTIMESTAMP()` is a synonyms for `NOW()`.

**Example**:

```
> source=people | eval `LOCALTIMESTAMP()` = LOCALTIMESTAMP() | fields `LOCALTIMESTAMP()`
fetched rows / total rows = 1/1
+---------------------+
| LOCALTIMESTAMP()    |
|---------------------|
| 2022-08-02 15:54:19 |
+---------------------+
```

##### `LOCALTIME`
<a name="supported-ppl-date-time-functions-localtime"></a>

**Usage**: `LOCALTIME()` is a synonym for `NOW()`.

**Example**:

```
> source=people | eval `LOCALTIME()` = LOCALTIME() | fields `LOCALTIME()`
fetched rows / total rows = 1/1
+---------------------+
| LOCALTIME()         |
|---------------------|
| 2022-08-02 15:54:19 |
+---------------------+
```

##### `MAKE_DATE`
<a name="supported-ppl-date-time-functions-make-date"></a>

**Usage**: `MAKE_DATE` returns a date value based on the given year, month, and day values. All arguments are rounded to integers.

**Specifications**: 1. MAKE\_DATE(INTEGER, INTEGER, INTEGER) -> DATE

**Argument type**: INTEGER, INTEGER, INTEGER

**Return type**: DATE

**Example**:

```
os> source=people | eval `MAKE_DATE(1945, 5, 9)` = MAKEDATE(1945, 5, 9) | fields `MAKEDATE(1945, 5, 9)`
fetched rows / total rows = 1/1
+------------------------+
| MAKEDATE(1945, 5, 9)   |
|------------------------|
| 1945-05-09             |
+------------------------+
```

##### `MINUTE`
<a name="supported-ppl-date-time-functions-minute"></a>

**Usage**: `MINUTE(TIME)` returns the minute component of the given time, as an integer in the range 0 to 59.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `MINUTE_OF_HOUR`

**Example**:

```
os> source=people | eval `MINUTE(TIME('01:02:03'))` =  MINUTE(TIME('01:02:03')) | fields `MINUTE(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+----------------------------+
| MINUTE(TIME('01:02:03'))   |
|----------------------------|
| 2                          |
+----------------------------+
```

##### `MINUTE_OF_HOUR`
<a name="supported-ppl-date-time-functions-minute-of-hour"></a>

**Usage**: `MINUTE_OF_HOUR(TIME)` returns the minute component of the given time, as an integer in the range 0 to 59.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `MINUTE`

**Example**:

```
os> source=people | eval `MINUTE_OF_HOUR(TIME('01:02:03'))` =  MINUTE_OF_HOUR(TIME('01:02:03')) | fields `MINUTE_OF_HOUR(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+------------------------------------+
| MINUTE_OF_HOUR(TIME('01:02:03'))   |
|------------------------------------|
| 2                                  |
+------------------------------------+
```

##### `MONTH`
<a name="supported-ppl-date-time-functions-month"></a>

**Usage**: `MONTH(DATE)` returns the month of the given date as an integer, in the range 1 to 12 (where 1 represents January and 12 represents December).

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `MONTH_OF_YEAR`

**Example**:

```
os> source=people | eval `MONTH(DATE('2020-08-26'))` =  MONTH(DATE('2020-08-26')) | fields `MONTH(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-----------------------------+
| MONTH(DATE('2020-08-26'))   |
|-----------------------------|
| 8                           |
+-----------------------------+
```

##### `MONTHNAME`
<a name="supported-ppl-date-time-functions-monthname"></a>

**Usage**: `MONTHNAME(DATE)` returns the month of the given date as an integer, in the range 1 to 12 (where 1 represents January and 12 represents December).

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `MONTH_OF_YEAR`

**Example**:

```
os> source=people | eval `MONTHNAME(DATE('2020-08-26'))` = MONTHNAME(DATE('2020-08-26')) | fields `MONTHNAME(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+---------------------------------+
| MONTHNAME(DATE('2020-08-26'))   |
|---------------------------------|
| August                          |
+---------------------------------+
```

##### `MONTH_OF_YEAR`
<a name="supported-ppl-date-time-functions-month-of-year"></a>

**Usage**: `MONTH_OF_YEAR(DATE)`returns the month of the given date as an integer, in the range 1 to 12 (where 1 represents January and 12 represents December).

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `MONTH`

**Example**:

```
os> source=people | eval `MONTH_OF_YEAR(DATE('2020-08-26'))` =  MONTH_OF_YEAR(DATE('2020-08-26')) | fields `MONTH_OF_YEAR(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-------------------------------------+
| MONTH_OF_YEAR(DATE('2020-08-26'))   |
|-------------------------------------|
| 8                                   |
+-------------------------------------+
```

##### `NOW`
<a name="supported-ppl-date-time-functions-now"></a>

**Usage**: `NOW` returns the current date and time as a `TIMESTAMP` value in the 'YYYY-MM-DD hh:mm:ss' format. The value is expressed in the cluster time zone. 

**Note**  
`NOW()` returns a constant time that indicates when the statement began to execute. This differs from `SYSDATE()`, which returns the exact time of execution.

**Return type**: TIMESTAMP

**Specification**: NOW() -> TIMESTAMP

**Example**:

```
os> source=people | eval `value_1` = NOW(), `value_2` = NOW() | fields `value_1`, `value_2`
fetched rows / total rows = 1/1
+---------------------+---------------------+
| value_1             | value_2             |
|---------------------+---------------------|
| 2022-08-02 15:39:05 | 2022-08-02 15:39:05 |
+---------------------+---------------------+
```

##### `QUARTER`
<a name="supported-ppl-date-time-functions-quarter"></a>

**Usage**: `QUARTER(DATE)` returns the quarter of the year for the given date as an integer, in the range 1 to 4.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Example**:

```
os> source=people | eval `QUARTER(DATE('2020-08-26'))` = QUARTER(DATE('2020-08-26')) | fields `QUARTER(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+-------------------------------+
| QUARTER(DATE('2020-08-26'))   |
|-------------------------------|
| 3                             |
+-------------------------------+
```

##### `SECOND`
<a name="supported-ppl-date-time-functions-second"></a>

**Usage**: `SECOND(TIME)` returns the second component of the given time as an integer, in the range 0 to 59.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `SECOND_OF_MINUTE`

**Example**:

```
os> source=people | eval `SECOND(TIME('01:02:03'))` = SECOND(TIME('01:02:03')) | fields `SECOND(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+----------------------------+
| SECOND(TIME('01:02:03'))   |
|----------------------------|
| 3                          |
+----------------------------+
```

##### `SECOND_OF_MINUTE`
<a name="supported-ppl-date-time-functions-second-of-minute"></a>

**Usage**: `SECOND_OF_MINUTE(TIME)` returns the second component of the given time as an integer, in the range 0 to 59.

**Argument type**: STRING/TIME/TIMESTAMP

**Return type**: INTEGER

**Synonyms**: `SECOND`

**Example**:

```
os> source=people | eval `SECOND_OF_MINUTE(TIME('01:02:03'))` = SECOND_OF_MINUTE(TIME('01:02:03')) | fields `SECOND_OF_MINUTE(TIME('01:02:03'))`
fetched rows / total rows = 1/1
+--------------------------------------+
| SECOND_OF_MINUTE(TIME('01:02:03'))   |
|--------------------------------------|
| 3                                    |
+--------------------------------------+
```

##### `SUBDATE`
<a name="supported-ppl-date-time-functions-subdate"></a>

**Usage**: `SUBDATE(DATE, DAYS)` subtracts the second argument (such as `DATE` or `DAYS`) from the given date.

**Argument type**: DATE/TIMESTAMP, LONG

**Return type map**: (DATE, LONG) -> DATE

**Antonyms**: `ADDDATE`

**Example**:

```
os> source=people | eval `'2008-01-02' - 31d` = SUBDATE(DATE('2008-01-02'), 31), `'2020-08-26' - 1` = SUBDATE(DATE('2020-08-26'), 1), `ts '2020-08-26 01:01:01' - 1` = SUBDATE(TIMESTAMP('2020-08-26 01:01:01'), 1) | fields `'2008-01-02' - 31d`, `'2020-08-26' - 1`, `ts '2020-08-26 01:01:01' - 1`
fetched rows / total rows = 1/1
+----------------------+--------------------+--------------------------------+
| '2008-01-02' - 31d   | '2020-08-26' - 1   | ts '2020-08-26 01:01:01' - 1   |
|----------------------+--------------------+--------------------------------|
| 2007-12-02 00:00:00  | 2020-08-25         | 2020-08-25 01:01:01            |
+----------------------+--------------------+--------------------------------+
```

##### `SYSDATE`
<a name="supported-ppl-date-time-functions-sysdate"></a>

**Usage**: `SYSDATE()` returns the current date and time as a `TIMESTAMP` value in the 'YYYY-MM-DD hh:mm:ss.nnnnnn' format. 

`SYSDATE()`returns the exact time at which it executes. This differs from NOW(), which returns a constant time indicating when the statement began to execute. 

**Optional argument type**: INTEGER (0 to 6) - Specifies the number of digits for fractional seconds in the return value.

**Return type**: TIMESTAMP

**Example**:

```
os> source=people | eval `SYSDATE()` = SYSDATE() | fields `SYSDATE()`
fetched rows / total rows = 1/1
+----------------------------+
| SYSDATE()                  |
|----------------------------|
| 2022-08-02 15:39:05.123456 |
+----------------------------+
```

##### `TIMESTAMP`
<a name="supported-ppl-date-time-functions-timestamp"></a>

**Usage**: `TIMESTAMP(EXPR)` constructs a timestamp type with the input string `expr` as an timestamp. 

With a single argument, `TIMESTAMP(expr)` constructs a timestamp from the input. If `expr` is a string, it's interpreted as a timestamp. For non-string arguments, the function casts `expr` to a timestamp using the UTC timezone. When `expr` is a `TIME` value, the function applies today's date before casting.

When used with two arguments, `TIMESTAMP(expr1, expr2)` adds the time expression (`expr2`) to the date or timestamp expression (`expr1`) and returns the result as a timestamp value.

**Argument type**: STRING/DATE/TIME/TIMESTAMP

**Return type map**:

(STRING/DATE/TIME/TIMESTAMP) -> TIMESTAMP

(STRING/DATE/TIME/TIMESTAMP, STRING/DATE/TIME/TIMESTAMP) -> TIMESTAMP

**Example**:

```
os> source=people | eval `TIMESTAMP('2020-08-26 13:49:00')` = TIMESTAMP('2020-08-26 13:49:00'), `TIMESTAMP('2020-08-26 13:49:00', TIME('12:15:42'))` = TIMESTAMP('2020-08-26 13:49:00', TIME('12:15:42')) | fields `TIMESTAMP('2020-08-26 13:49:00')`, `TIMESTAMP('2020-08-26 13:49:00', TIME('12:15:42'))`
fetched rows / total rows = 1/1
+------------------------------------+------------------------------------------------------+
| TIMESTAMP('2020-08-26 13:49:00')   | TIMESTAMP('2020-08-26 13:49:00', TIME('12:15:42'))   |
|------------------------------------+------------------------------------------------------|
| 2020-08-26 13:49:00                | 2020-08-27 02:04:42                                  |
+------------------------------------+------------------------------------------------------+
```

##### `UNIX_TIMESTAMP`
<a name="supported-ppl-date-time-functions-unix-timestamp"></a>

**Usage**: `UNIX_TIMESTAMP` converts a given date argument to Unix time (seconds since the Epoch, which began at the start of 1970). If no argument is provided, it returns the current Unix time. 

The date argument can be a `DATE`, a `TIMESTAMP` string, or a number in one of these formats: `YYMMDD`, `YYMMDDhhmmss`, `YYYYMMDD`, or `YYYYMMDDhhmmss`. If the argument includes a time component, it may optionally include fractional seconds.

If the argument is in an invalid format or falls outside the range of 1970-01-01 00:00:00 to 3001-01-18 23:59:59.999999 (0 to 32536771199.999999 in epoch time), the function returns `NULL`.

The function accepts `DATE`, `TIMESTAMP`, or `DOUBLE` as argument types, or no argument. It always returns a `DOUBLE` value representing the Unix timestamp.

For the reverse conversion, you can use the FROM\_UNIXTIME function.

**Argument type**: <NONE>/DOUBLE/DATE/TIMESTAMP

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `UNIX_TIMESTAMP(double)` = UNIX_TIMESTAMP(20771122143845), `UNIX_TIMESTAMP(timestamp)` = UNIX_TIMESTAMP(TIMESTAMP('1996-11-15 17:05:42')) | fields `UNIX_TIMESTAMP(double)`, `UNIX_TIMESTAMP(timestamp)`
fetched rows / total rows = 1/1
+--------------------------+-----------------------------+
| UNIX_TIMESTAMP(double)   | UNIX_TIMESTAMP(timestamp)   |
|--------------------------+-----------------------------|
| 3404817525.0             | 848077542.0                 |
+--------------------------+-----------------------------+
```

##### `WEEK`
<a name="supported-ppl-date-time-functions-week"></a>

**Usage**: `WEEK(DATE)` returns the week number for a given date.

**Argument type**: DATE/TIMESTAMP/STRING

**Return type**: INTEGER

**Synonyms**: `WEEK_OF_YEAR`

**Example**:

```
os> source=people | eval `WEEK(DATE('2008-02-20'))` = WEEK(DATE('2008-02-20')) | fields `WEEK(DATE('2008-02-20'))`
fetched rows / total rows = 1/1
+----------------------------+
| WEEK(DATE('2008-02-20'))   |
|----------------------------|
| 8                          |
+----------------------------+
```

##### `WEEKDAY`
<a name="supported-ppl-date-time-functions-weekday"></a>

**Usage**: `WEEKDAY(DATE)` returns the weekday index for date (0 = Monday, 1 = Tuesday, ..., 6 = Sunday).

It is similar to the `dayofweek` function, but returns different indexes for each day.

**Argument type**: STRING/DATE/TIME/TIMESTAMP

**Return type**: INTEGER

**Example**:

```
os> source=people | eval `weekday(DATE('2020-08-26'))` = weekday(DATE('2020-08-26')) | eval `weekday(DATE('2020-08-27'))` = weekday(DATE('2020-08-27')) | fields `weekday(DATE('2020-08-26'))`, `weekday(DATE('2020-08-27'))`
fetched rows / total rows = 1/1
+-------------------------------+-------------------------------+
| weekday(DATE('2020-08-26'))   | weekday(DATE('2020-08-27'))   |
|-------------------------------+-------------------------------|
| 2                             | 3                             |
+-------------------------------+-------------------------------+
```

##### `WEEK_OF_YEAR`
<a name="supported-ppl-date-time-functions-week-of-year"></a>

**Usage**: `WEEK_OF_YEAR(DATE)` returns the week number for the given date.

**Argument type**: DATE/TIMESTAMP/STRING

**Return type**: INTEGER

**Synonyms**: `WEEK`

**Example**:

```
os> source=people | eval `WEEK_OF_YEAR(DATE('2008-02-20'))` = WEEK(DATE('2008-02-20'))| fields `WEEK_OF_YEAR(DATE('2008-02-20'))`
fetched rows / total rows = 1/1
+------------------------------------+
| WEEK_OF_YEAR(DATE('2008-02-20'))   |
|------------------------------------|
| 8                                  |
+------------------------------------+
```

##### `YEAR`
<a name="supported-ppl-date-time-functions-year"></a>

**Usage**: `YEAR(DATE)` returns the year for date, in the range 1000 to 9999, or 0 for the "zero" date.

**Argument type**: STRING/DATE/TIMESTAMP

**Return type**: INTEGER

**Example**:

```
os> source=people | eval `YEAR(DATE('2020-08-26'))` = YEAR(DATE('2020-08-26')) | fields `YEAR(DATE('2020-08-26'))`
fetched rows / total rows = 1/1
+----------------------------+
| YEAR(DATE('2020-08-26'))   |
|----------------------------|
| 2020                       |
+----------------------------+
```

##### `DATE_ADD`
<a name="supported-ppl-date-time-functions-date-add"></a>

**Usage**: `DATE_ADD(date, INTERVAL expr unit)` adds the specified interval to the given date.

**Argument type**: DATE, INTERVAL

**Return type**: DATE

**Antonyms**: `DATE_SUB`

**Example**:

```
os> source=people | eval `'2020-08-26' + 1d` = DATE_ADD(DATE('2020-08-26'), INTERVAL 1 DAY) | fields `'2020-08-26' + 1d`
fetched rows / total rows = 1/1
+---------------------+
| '2020-08-26' + 1d   |
|---------------------|
| 2020-08-27          |
+---------------------+
```

##### `DATE_SUB`
<a name="supported-ppl-date-time-functions-date-sub"></a>

**Usage**: `DATE_SUB(date, INTERVAL expr unit)` subtracts the interval expr from date.

**Argument type**: DATE, INTERVAL

**Return type**: DATE

**Antonyms**: `DATE_ADD`

**Example**:

```
os> source=people | eval `'2008-01-02' - 31d` = DATE_SUB(DATE('2008-01-02'), INTERVAL 31 DAY) | fields `'2008-01-02' - 31d`
fetched rows / total rows = 1/1
+---------------------+
| '2008-01-02' - 31d  |
|---------------------|
| 2007-12-02          |
+---------------------+
```

##### `TIMESTAMPADD`
<a name="supported-ppl-date-time-functions-timestampadd"></a>

**Usage**: Returns a `TIMESTAMP` value after adding a specified time interval to a given date.

**Arguments**: 
+ interval: INTERVAL (SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR) 
+ integer: INTEGER 
+ date: DATE, TIMESTAMP, or STRING

If you provide a `STRING` as the date argument, format it as a valid `TIMESTAMP`. The function automatically converts a `DATE` argument to a `TIMESTAMP`.

**Examples**:

```
os> source=people | eval `TIMESTAMPADD(DAY, 17, '2000-01-01 00:00:00')` = TIMESTAMPADD(DAY, 17, '2000-01-01 00:00:00') | eval `TIMESTAMPADD(QUARTER, -1, '2000-01-01 00:00:00')` = TIMESTAMPADD(QUARTER, -1, '2000-01-01 00:00:00') | fields `TIMESTAMPADD(DAY, 17, '2000-01-01 00:00:00')`, `TIMESTAMPADD(QUARTER, -1, '2000-01-01 00:00:00')`
fetched rows / total rows = 1/1
+----------------------------------------------+--------------------------------------------------+
| TIMESTAMPADD(DAY, 17, '2000-01-01 00:00:00') | TIMESTAMPADD(QUARTER, -1, '2000-01-01 00:00:00') |
|----------------------------------------------+--------------------------------------------------|
| 2000-01-18 00:00:00                          | 1999-10-01 00:00:00                              |
+----------------------------------------------+--------------------------------------------------+
```

##### `TIMESTAMPDIFF`
<a name="supported-ppl-date-time-functions-timestampdiff"></a>

**Usage**: `TIMESTAMPDIFF(interval, start, end)` returns the difference between the start and end date/times in specified interval units.

**Arguments**: 
+ interval: INTERVAL (SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR) 
+ start: DATE, TIMESTAMP, or STRING 
+ end: DATE, TIMESTAMP, or STRING

The function automatically converts arguments to `TIMESTAMP` when appropriate. Format `STRING` arguments as valid `TIMESTAMP`s.

**Examples**:

```
os> source=people | eval `TIMESTAMPDIFF(YEAR, '1997-01-01 00:00:00', '2001-03-06 00:00:00')` = TIMESTAMPDIFF(YEAR, '1997-01-01 00:00:00', '2001-03-06 00:00:00') | eval `TIMESTAMPDIFF(SECOND, timestamp('1997-01-01 00:00:23'), timestamp('1997-01-01 00:00:00'))` = TIMESTAMPDIFF(SECOND, timestamp('1997-01-01 00:00:23'), timestamp('1997-01-01 00:00:00')) | fields `TIMESTAMPDIFF(YEAR, '1997-01-01 00:00:00', '2001-03-06 00:00:00')`, `TIMESTAMPDIFF(SECOND, timestamp('1997-01-01 00:00:23'), timestamp('1997-01-01 00:00:00'))`
fetched rows / total rows = 1/1
+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| TIMESTAMPDIFF(YEAR, '1997-01-01 00:00:00', '2001-03-06 00:00:00') | TIMESTAMPDIFF(SECOND, timestamp('1997-01-01 00:00:23'), timestamp('1997-01-01 00:00:00')) |
|-------------------------------------------------------------------+-------------------------------------------------------------------------------------------|
| 4                                                                 | -23                                                                                       |
+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
```

##### `UTC_TIMESTAMP`
<a name="supported-ppl-date-time-functions-utc-timestamp"></a>

**Usage**: `UTC_TIMESTAMP` returns the current UTC timestamp as a value in 'YYYY-MM-DD hh:mm:ss'.

**Return type**: TIMESTAMP

**Specification**: UTC\_TIMESTAMP() -> TIMESTAMP

**Example**:

```
> source=people | eval `UTC_TIMESTAMP()` = UTC_TIMESTAMP() | fields `UTC_TIMESTAMP()`
fetched rows / total rows = 1/1
+---------------------+
| UTC_TIMESTAMP()     |
|---------------------|
| 2022-10-03 17:54:28 |
+---------------------+
```

##### `CURRENT_TIMEZONE`
<a name="supported-ppl-date-time-functions-current-timezone"></a>

**Usage**: `CURRENT_TIMEZONE` returns the current local timezone.

**Return type**: STRING

**Example**:

```
> source=people | eval `CURRENT_TIMEZONE()` = CURRENT_TIMEZONE() | fields `CURRENT_TIMEZONE()`
fetched rows / total rows = 1/1
+------------------------+
| CURRENT_TIMEZONE()     |
|------------------------|
| America/Chicago        |
+------------------------+
```

##### PPL expressions
<a name="supported-ppl-expressions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

Expressions, particularly value expressions, return a scalar value. Expressions have different types and forms. For example, there are literal values as atom expressions and arithmetic, predicate and function expressions built on top of them. You can use expressions in different clauses, such as using arithmetic expressions in `Filter` and `Stats` commands.

**Operators**

An arithmetic expression is an expression formed by numeric literals and binary arithmetic operators as follows:

1. `+`: Add.

1. `-`: Subtract.

1. `*`: Multiply.

1. `/`: Divide (For integers, the result is an integer with the fractional part discarded)

1. `%`: Modulo (Use with integers only; the result is the remainder of the division)

**Precedence**

Use parentheses to control the precedence of arithmetic operators. Otherwise, operators of higher precedence are performed first.

**Type conversion**

Implicit type conversion is performed when looking up operator signatures. For example, an integer `+` a real number matches signature `+(double,double)` which results in a real number. This rule also applies to function calls.

Example for different type of arithmetic expressions:

```
os> source=accounts | where age > (25 + 5) | fields age ;
fetched rows / total rows = 3/3
+-------+
| age   |
|-------|
| 32    |
| 36    |
| 33    |
+-------+
```

**Predicate operators**  
A predicate operator is an expression that evaluates to be true. The `MISSING` and `NULL` value comparison follow these rules: 
+ A `MISSING` value only equals a `MISSING` value and is less than other values. 
+ A `NULL` value equals a `NULL` value, is larger than a `MISSING` value, but is less than all other values.

**Operators**


**Predicate operators**  

| Name | Description | 
| --- | --- | 
| > | Greater than operator | 
| >= | Greater than or equal operator | 
| < | Less than operator | 
| \!= | Not equal operator | 
| <= | Less than or equal operator | 
| = | Equal operator | 
| LIKE | Simple pattern matching | 
| IN | NULL value test | 
| AND | AND operator | 
| OR | OR operator | 
| XOR | XOR operator | 
| NOT | NOT NULL value test | 

You can compare datetimes. When comparing different datetime types (for example `DATE` and `TIME`), both convert to `DATETIME`. The following rules apply to conversion:
+  `TIME` applies to today's date.
+ `DATE` is interpreted at midnight.

**Basic predicate operator**  
Example for comparison operators:

```
os> source=accounts | where age > 33 | fields age ;
fetched rows / total rows = 1/1
+-------+
| age   |
|-------|
| 36    |
+-------+
```

**`IN`**  
Example of the `IN` operator test field in value lists:

```
os> source=accounts | where age in (32, 33) | fields age ;
fetched rows / total rows = 2/2
+-------+
| age   |
|-------|
| 32    |
| 33    |
+-------+
```

**`OR`**  
Example of the `OR` operator:

```
os> source=accounts | where age = 32 OR age = 33 | fields age ;
fetched rows / total rows = 2/2
+-------+
| age   |
|-------|
| 32    |
| 33    |
+-------+
```

**`NOT`**  
Example of the `NOT` operator:

```
os> source=accounts | where age not in (32, 33) | fields age ;
fetched rows / total rows = 2/2
+-------+
| age   |
|-------|
| 36    |
| 28    |
+-------+
```

##### PPL IP address functions
<a name="supported-ppl-ip-address-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `CIDRMATCH`
<a name="supported-ppl-address-functions-cidrmatch"></a>

**Usage**: `CIDRMATCH(ip, cidr)` checks if the specified IP address is within the given cidr range.

**Argument type:**
+ STRING, STRING
+ Return type: BOOLEAN

**Example**:

```
os> source=ips | where cidrmatch(ip, '***********/24') | fields ip
fetched rows / total rows = 1/1
+--------------+
| ip           |
|--------------|
| ***********  |
+--------------+

os> source=ipsv6 | where cidrmatch(ip, '2003:db8::/32') | fields ip
fetched rows / total rows = 1/1
+-----------------------------------------+
| ip                                      |
|-----------------------------------------|
| 2003:0db8:****:****:****:****:****:0000 |
+-----------------------------------------+
```

**Note**  
`ip` can be an IPv4 or an IPv6 address.
`cidr` can be an IPv4 or an IPv6 block.
`ip` and `cidr` must be either both IPv4 or both IPv6.
`ip` and `cidr` must both be valid and non-empty/non-null.

##### PPL JSON functions
<a name="supported-ppl-json-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `JSON`
<a name="supported-ppl-json-functions-json"></a>

**Usage**: `json(value)` evaluates whether a string can be parsed as JSON format. The function returns the original string if it's valid JSON, or null if it's invalid.

**Argument type**: STRING

**Return type**: STRING/NULL. A STRING expression of a valid JSON object format.

**Examples**:

```
os> source=people | eval `valid_json()` = json('[1,2,3,{"f1":1,"f2":[5,6]},4]') | fields valid_json
fetched rows / total rows = 1/1
+---------------------------------+
| valid_json                      |
+---------------------------------+
| [1,2,3,{"f1":1,"f2":[5,6]},4]   |
+---------------------------------+

os> source=people | eval `invalid_json()` = json('{"invalid": "json"') | fields invalid_json
fetched rows / total rows = 1/1
+----------------+
| invalid_json   |
+----------------+
| null           |
+----------------+
```

##### `JSON_OBJECT`
<a name="supported-ppl-json-functions-json-object"></a>

**Usage**: `json_object(<key>, <value>[, <key>, <value>]...)` returns a JSON object from members of key-value pairs.

**Argument type:**
+ A <key> must be STRING.
+ A <value> can be any data types.

**Return type**: JSON\_OBJECT. A StructType expression of a valid JSON object.

**Examples**:

```
os> source=people | eval result = json_object('key', 123.45) | fields result
fetched rows / total rows = 1/1
+------------------+
| result           |
+------------------+
| {"key":123.45}   |
+------------------+

os> source=people | eval result = json_object('outer', json_object('inner', 123.45)) | fields result
fetched rows / total rows = 1/1
+------------------------------+
| result                       |
+------------------------------+
| {"outer":{"inner":123.45}}   |
+------------------------------+
```

##### `JSON_ARRAY`
<a name="supported-ppl-json-functions-json-array"></a>

**Usage**: `json_array(<value>...)` creates a JSON ARRAY using a list of values.

**Argument type**: A `<value>` can be any kind of value such as string, number, or boolean.

**Return type**: ARRAY. An array of any supported data type for a valid JSON array.

**Examples**:

```
os> source=people | eval `json_array` = json_array(1, 2, 0, -1, 1.1, -0.11)
fetched rows / total rows = 1/1
+------------------------------+
| json_array                   |
+------------------------------+
| [1.0,2.0,0.0,-1.0,1.1,-0.11] |
+------------------------------+

os> source=people | eval `json_array_object` = json_object("array", json_array(1, 2, 0, -1, 1.1, -0.11))
fetched rows / total rows = 1/1
+----------------------------------------+
| json_array_object                      |
+----------------------------------------+
| {"array":[1.0,2.0,0.0,-1.0,1.1,-0.11]} |
+----------------------------------------+
```

##### `TO_JSON_STRING`
<a name="supported-ppl-json-functions-to-json-string"></a>

**Usage**: `to_json_string(jsonObject)` returns a JSON string with a given json object value.

**Argument type**: JSON\_OBJECT 

**Return type**: STRING

**Examples**:

```
os> source=people | eval `json_string` = to_json_string(json_array(1, 2, 0, -1, 1.1, -0.11)) | fields json_string
fetched rows / total rows = 1/1
+--------------------------------+
| json_string                    |
+--------------------------------+
| [1.0,2.0,0.0,-1.0,1.1,-0.11]   |
+--------------------------------+

os> source=people | eval `json_string` = to_json_string(json_object('key', 123.45)) | fields json_string
fetched rows / total rows = 1/1
+-----------------+
| json_string     |
+-----------------+
| {'key', 123.45} |
+-----------------+
```

##### `ARRAY_LENGTH`
<a name="supported-ppl-json-functions-array-length"></a>

**Usage**: `array_length(jsonArray)` returns the number of elements in the outermost array.

**Argument type**: ARRAY. An ARRAY or JSON\_ARRAY object.

**Return type**: INTEGER

**Example**:

```
os> source=people | eval `json_array` = json_array_length(json_array(1,2,3,4)), `empty_array` = json_array_length(json_array())
fetched rows / total rows = 1/1
+--------------+---------------+
| json_array   | empty_array   |
+--------------+---------------+
| 4            | 0             |
+--------------+---------------+
```

##### `JSON_EXTRACT`
<a name="supported-ppl-json-functions-json-extract"></a>

**Usage**: `json_extract(jsonStr, path)` extracts a JSON object from a JSON string based on the specified JSON path. The function returns null if the input JSON string is invalid.

**Argument type**: STRING, STRING

**Return type**: STRING
+ A STRING expression of a valid JSON object format.
+ `NULL` is returned in case of an invalid JSON.

**Examples**:

```
os> source=people | eval `json_extract('{"a":"b"}', '$.a')` = json_extract('{"a":"b"}', '$a')
fetched rows / total rows = 1/1
+----------------------------------+
| json_extract('{"a":"b"}', 'a')   |
+----------------------------------+
| b                                |
+----------------------------------+

os> source=people | eval `json_extract('{"a":[{"b":1},{"b":2}]}', '$.a[1].b')` = json_extract('{"a":[{"b":1},{"b":2}]}', '$.a[1].b')
fetched rows / total rows = 1/1
+-----------------------------------------------------------+
| json_extract('{"a":[{"b":1.0},{"b":2.0}]}', '$.a[1].b')   |
+-----------------------------------------------------------+
| 2.0                                                       |
+-----------------------------------------------------------+

os> source=people | eval `json_extract('{"a":[{"b":1},{"b":2}]}', '$.a[*].b')` = json_extract('{"a":[{"b":1},{"b":2}]}', '$.a[*].b')
fetched rows / total rows = 1/1
+-----------------------------------------------------------+
| json_extract('{"a":[{"b":1.0},{"b":2.0}]}', '$.a[*].b')   |
+-----------------------------------------------------------+
| [1.0,2.0]                                                 |
+-----------------------------------------------------------+

os> source=people | eval `invalid_json` = json_extract('{"invalid": "json"')
fetched rows / total rows = 1/1
+----------------+
| invalid_json   |
+----------------+
| null           |
+----------------+
```

##### `JSON_KEYS`
<a name="supported-ppl-json-functions-json-keys"></a>

**Usage**: `json_keys(jsonStr)` returns all the keys of the outermost JSON object as an array.

**Argument type**: STRING. A STRING expression of a valid JSON object format.

**Return type**: ARRAY[STRING]. The function returns `NULL` for any other valid JSON string, an empty string, or an invalid JSON.

**Examples**:

```
os> source=people | eval `keys` = json_keys('{"f1":"abc","f2":{"f3":"a","f4":"b"}}')
fetched rows / total rows = 1/1
+------------+
| keus       |
+------------+
| [f1, f2]   |
+------------+

os> source=people | eval `keys` = json_keys('[1,2,3,{"f1":1,"f2":[5,6]},4]')
fetched rows / total rows = 1/1
+--------+
| keys   |
+--------+
| null   |
+--------+
```

##### `JSON_VALID`
<a name="supported-ppl-json-functions-json-valid"></a>

**Usage**: `json_valid(jsonStr)` evaluates whether a JSON string uses valid JSON syntax and returns TRUE or FALSE.

**Argument type**: STRING

**Return type**: BOOLEAN

**Examples**:

```
os> source=people | eval `valid_json` = json_valid('[1,2,3,4]'), `invalid_json` = json_valid('{"invalid": "json"') | feilds `valid_json`, `invalid_json`
fetched rows / total rows = 1/1
+--------------+----------------+
| valid_json   | invalid_json   |
+--------------+----------------+
| True         | False          |
+--------------+----------------+

os> source=accounts | where json_valid('[1,2,3,4]') and isnull(email) | fields account_number, email
fetched rows / total rows = 1/1
+------------------+---------+
| account_number   | email   |
|------------------+---------|
| 13               | null    |
+------------------+---------+
```

##### PPL Lambda functions
<a name="supported-ppl-lambda-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `EXISTS`
<a name="supported-ppl-lambda-functions-exists"></a>

**Usage**: `exists(array, lambda)` evaluates whether a Lambda predicate holds for one or more elements in the array.

**Argument type**: ARRAY, LAMBDA

**Return type**: BOOLEAN. Returns `TRUE` if at least one element in the array satisfies the Lambda predicate, otherwise `FALSE`.

**Examples**:

```
 os> source=people | eval array = json_array(1, -1, 2), result = exists(array, x -> x > 0) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| true      |
+-----------+

os> source=people | eval array = json_array(-1, -3, -2), result = exists(array, x -> x > 0) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| false     |
+-----------+
```

##### `FILTER`
<a name="supported-ppl-lambda-functions-filter"></a>

**Usage**: `filter(array, lambda)` filters the input array using the given Lambda function.

**Argument type**: ARRAY, LAMBDA

**Return type**: ARRAY. An ARRAY that contains all elements in the input array that satisfy the lambda predicate.

**Examples**:

```
 os> source=people | eval array = json_array(1, -1, 2), result = filter(array, x -> x > 0) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| [1, 2]    |
+-----------+

os> source=people | eval array = json_array(-1, -3, -2), result = filter(array, x -> x > 0) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| []        |
+-----------+
```

##### `TRANSFORM`
<a name="supported-ppl-lambda-functions-transform"></a>

**Usage**: `transform(array, lambda)` transforms elements in an array using the Lambda transform function. The second argument implies the index of the element if using binary Lambda function. This is similar to a `map` in functional programming.

**Argument type**: ARRAY, LAMBDA

**Return type**: ARRAY. An ARRAY that contains the result of applying the lambda transform function to each element in the input array.

**Examples**:

```
os> source=people | eval array = json_array(1, 2, 3), result = transform(array, x -> x + 1) | fields result
fetched rows / total rows = 1/1
+--------------+
| result       |
+--------------+
| [2, 3, 4]    |
+--------------+

os> source=people | eval array = json_array(1, 2, 3), result = transform(array, (x, i) -> x + i) | fields result
fetched rows / total rows = 1/1
+--------------+
| result       |
+--------------+
| [1, 3, 5]    |
+--------------+
```

##### `REDUCE`
<a name="supported-ppl-lambda-functions-reduce"></a>

**Usage**: `reduce(array, start, merge_lambda, finish_lambda)` reduces an array to a single value by applying lambda functions. The function applies the merge\_lambda to the start value and all array elements, then applies the `finish_lambda` to the result.

**Argument type**: ARRAY, ANY, LAMBDA, LAMBDA

**Return type**: ANY. The final result of applying the Lambda functions to the start value and the input array.

**Examples**:

```
 os> source=people | eval array = json_array(1, 2, 3), result = reduce(array, 0, (acc, x) -> acc + x) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| 6         |
+-----------+

os> source=people | eval array = json_array(1, 2, 3), result = reduce(array, 10, (acc, x) -> acc + x) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| 16        |
+-----------+

os> source=people | eval array = json_array(1, 2, 3), result = reduce(array, 0, (acc, x) -> acc + x, acc -> acc * 10) | fields result
fetched rows / total rows = 1/1
+-----------+
| result    |
+-----------+
| 60        |
+-----------+
```

##### PPL mathematical functions
<a name="supported-ppl-math-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `ABS`
<a name="supported-ppl-math-functions-abs"></a>

**Usage**: `ABS(x) `calculates the absolute value of x.

**Argument type: **INTEGER/LONG/FLOAT/DOUBLE

**Return type:** INTEGER/LONG/FLOAT/DOUBLE

**Example**:

```
os> source=people | eval `ABS(-1)` = ABS(-1) | fields `ABS(-1)`
fetched rows / total rows = 1/1
+-----------+
| ABS(-1)   |
|-----------|
| 1         |
+-----------+
```

##### `ACOS`
<a name="supported-ppl-math-functions-acos"></a>

**Usage**: `ACOS(x)` calculates the arc cosine of x. It returns `NULL` if x is not in the range -1 to 1.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `ACOS(0)` = ACOS(0) | fields `ACOS(0)`
fetched rows / total rows = 1/1
+--------------------+
| ACOS(0)            |
|--------------------|
| 1.5707963267948966 |
+--------------------+
```

##### `ASIN`
<a name="supported-ppl-math-functions-asin"></a>

**Usage**: `asin(x)` calculates the arc sine of x. It returns `NULL` if x is not in the range -1 to 1.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `ASIN(0)` = ASIN(0) | fields `ASIN(0)`
fetched rows / total rows = 1/1
+-----------+
| ASIN(0)   |
|-----------|
| 0.0       |
+-----------+
```

##### `ATAN`
<a name="supported-ppl-math-functions-atan"></a>

**Usage**: `ATAN(x)` calculates the arc tangent of x. `atan(y, x)` calculates the arc tangent of y / x, except that the signs of both arguments determine the quadrant of the result.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `ATAN(2)` = ATAN(2), `ATAN(2, 3)` = ATAN(2, 3) | fields `ATAN(2)`, `ATAN(2, 3)`
fetched rows / total rows = 1/1
+--------------------+--------------------+
| ATAN(2)            | ATAN(2, 3)         |
|--------------------+--------------------|
| 1.1071487177940904 | 0.5880026035475675 |
+--------------------+--------------------+
```

##### `ATAN2`
<a name="supported-ppl-math-functions-atan2"></a>

**Usage**: `ATAN2(y, x)` calculates the arc tangent of y / x, except that the signs of both arguments determine the quadrant of the result.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `ATAN2(2, 3)` = ATAN2(2, 3) | fields `ATAN2(2, 3)`
fetched rows / total rows = 1/1
+--------------------+
| ATAN2(2, 3)        |
|--------------------|
| 0.5880026035475675 |
+--------------------+
```

##### `CBRT`
<a name="supported-ppl-math-functions-cbrt"></a>

**Usage**: `CBRT` calculates the cube root of a number.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE:

INTEGER/LONG/FLOAT/DOUBLE -> DOUBLE

**Example**:

```
opensearchsql> source=location | eval `CBRT(8)` = CBRT(8), `CBRT(9.261)` = CBRT(9.261), `CBRT(-27)` = CBRT(-27) | fields `CBRT(8)`, `CBRT(9.261)`, `CBRT(-27)`;
fetched rows / total rows = 2/2
+-----------+---------------+-------------+
| CBRT(8)   | CBRT(9.261)   | CBRT(-27)   |
|-----------+---------------+-------------|
| 2.0       | 2.1           | -3.0        |
| 2.0       | 2.1           | -3.0        |
+-----------+---------------+-------------+
```

##### `CEIL`
<a name="supported-ppl-math-functions-ceil"></a>

**Usage**: An alias for the `CEILING` function. `CEILING(T)` takes the ceiling of value T.

**Limitation**: `CEILING` only works as expected when IEEE 754 double type displays a decimal when stored.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: LONG

**Example**:

```
os> source=people | eval `CEILING(0)` = CEILING(0), `CEILING(50.00005)` = CEILING(50.00005), `CEILING(-50.00005)` = CEILING(-50.00005) | fields `CEILING(0)`, `CEILING(50.00005)`, `CEILING(-50.00005)`
fetched rows / total rows = 1/1
+--------------+---------------------+----------------------+
| CEILING(0)   | CEILING(50.00005)   | CEILING(-50.00005)   |
|--------------+---------------------+----------------------|
| 0            | 51                  | -50                  |
+--------------+---------------------+----------------------+

os> source=people | eval `CEILING(3147483647.12345)` = CEILING(3147483647.12345), `CEILING(113147483647.12345)` = CEILING(113147483647.12345), `CEILING(3147483647.00001)` = CEILING(3147483647.00001) | fields `CEILING(3147483647.12345)`, `CEILING(113147483647.12345)`, `CEILING(3147483647.00001)`
fetched rows / total rows = 1/1
+-----------------------------+-------------------------------+-----------------------------+
| CEILING(3147483647.12345)   | CEILING(113147483647.12345)   | CEILING(3147483647.00001)   |
|-----------------------------+-------------------------------+-----------------------------|
| 3147483648                  | 113147483648                  | 3147483648                  |
+-----------------------------+-------------------------------+-----------------------------+
```

##### `CONV`
<a name="supported-ppl-math-functions-conv"></a>

**Usage**: `CONV(x, a, b)` converts the number x from a base to b base.

**Argument type**: x: STRING, a: INTEGER, b: INTEGER

**Return type**: STRING

**Example**:

```
os> source=people | eval `CONV('12', 10, 16)` = CONV('12', 10, 16), `CONV('2C', 16, 10)` = CONV('2C', 16, 10), `CONV(12, 10, 2)` = CONV(12, 10, 2), `CONV(1111, 2, 10)` = CONV(1111, 2, 10) | fields `CONV('12', 10, 16)`, `CONV('2C', 16, 10)`, `CONV(12, 10, 2)`, `CONV(1111, 2, 10)`
fetched rows / total rows = 1/1
+----------------------+----------------------+-------------------+---------------------+
| CONV('12', 10, 16)   | CONV('2C', 16, 10)   | CONV(12, 10, 2)   | CONV(1111, 2, 10)   |
|----------------------+----------------------+-------------------+---------------------|
| c                    | 44                   | 1100              | 15                  |
+----------------------+----------------------+-------------------+---------------------+
```

##### `COS`
<a name="supported-ppl-math-functions-cos"></a>

**Usage**: `COS(x)` calculates the cosine of x, where x is given in radians.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type:** DOUBLE

**Example**:

```
os> source=people | eval `COS(0)` = COS(0) | fields `COS(0)`
fetched rows / total rows = 1/1
+----------+
| COS(0)   |
|----------|
| 1.0      |
+----------+
```

##### `COT`
<a name="supported-ppl-math-functions-cot"></a>

**Usage**: `COT(x)` calculates the cotangent of x. It returns out-of-range error if x is equal to 0.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `COT(1)` = COT(1) | fields `COT(1)`
fetched rows / total rows = 1/1
+--------------------+
| COT(1)             |
|--------------------|
| 0.6420926159343306 |
+--------------------+
```

##### `CRC32`
<a name="supported-ppl-math-functions-crc32"></a>

**Usage**: `CRC32` calculates a cyclic redundancy check value and returns a 32-bit unsigned value.

**Argument type**: STRING

**Return type**: LONG

**Example**:

```
os> source=people | eval `CRC32('MySQL')` = CRC32('MySQL') | fields `CRC32('MySQL')`
fetched rows / total rows = 1/1
+------------------+
| CRC32('MySQL')   |
|------------------|
| 3259397556       |
+------------------+
```

##### `DEGREES`
<a name="supported-ppl-math-functions-degrees"></a>

**Usage**: `DEGREES(x)` converts x from radians to degrees.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `DEGREES(1.57)` = DEGREES(1.57) | fields `DEGREES(1.57)`
fetched rows / total rows  = 1/1
+-------------------+
| DEGREES(1.57)     |
|-------------------|
| 89.95437383553924 |
+-------------------+
```

##### `E`
<a name="supported-ppl-math-functions-e"></a>

**Usage**: `E()` returns the Euler's number.

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `E()` = E() | fields `E()`
fetched rows / total rows = 1/1
+-------------------+
| E()               |
|-------------------|
| 2.718281828459045 |
+-------------------+
```

##### `EXP`
<a name="supported-ppl-math-functions-exp"></a>

**Usage**: `EXP(x)` returns e raised to the power of x.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `EXP(2)` = EXP(2) | fields `EXP(2)`
fetched rows / total rows = 1/1
+------------------+
| EXP(2)           |
|------------------|
| 7.38905609893065 |
+------------------+
```

##### `FLOOR`
<a name="supported-ppl-math-functions-floor"></a>

**Usage**: `FLOOR(T)` takes the floor of value T.

**Limitation**: `FLOOR` only works as expected when IEEE 754 double type displays a decimal when stored.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: LONG

**Example**:

```
os> source=people | eval `FLOOR(0)` = FLOOR(0), `FLOOR(50.00005)` = FLOOR(50.00005), `FLOOR(-50.00005)` = FLOOR(-50.00005) | fields `FLOOR(0)`, `FLOOR(50.00005)`, `FLOOR(-50.00005)`
fetched rows / total rows = 1/1
+------------+-------------------+--------------------+
| FLOOR(0)   | FLOOR(50.00005)   | FLOOR(-50.00005)   |
|------------+-------------------+--------------------|
| 0          | 50                | -51                |
+------------+-------------------+--------------------+

os> source=people | eval `FLOOR(3147483647.12345)` = FLOOR(3147483647.12345), `FLOOR(113147483647.12345)` = FLOOR(113147483647.12345), `FLOOR(3147483647.00001)` = FLOOR(3147483647.00001) | fields `FLOOR(3147483647.12345)`, `FLOOR(113147483647.12345)`, `FLOOR(3147483647.00001)`
fetched rows / total rows = 1/1
+---------------------------+-----------------------------+---------------------------+
| FLOOR(3147483647.12345)   | FLOOR(113147483647.12345)   | FLOOR(3147483647.00001)   |
|---------------------------+-----------------------------+---------------------------|
| 3147483647                | 113147483647                | 3147483647                |
+---------------------------+-----------------------------+---------------------------+

os> source=people | eval `FLOOR(282474973688888.022)` = FLOOR(282474973688888.022), `FLOOR(9223372036854775807.022)` = FLOOR(9223372036854775807.022), `FLOOR(9223372036854775807.0000001)` = FLOOR(9223372036854775807.0000001) | fields `FLOOR(282474973688888.022)`, `FLOOR(9223372036854775807.022)`, `FLOOR(9223372036854775807.0000001)`
fetched rows / total rows = 1/1
+------------------------------+----------------------------------+--------------------------------------+
| FLOOR(282474973688888.022)   | FLOOR(9223372036854775807.022)   | FLOOR(9223372036854775807.0000001)   |
|------------------------------+----------------------------------+--------------------------------------|
| 282474973688888              | 9223372036854775807              | 9223372036854775807                  |
+------------------------------+----------------------------------+--------------------------------------+
```

##### `LN`
<a name="supported-ppl-math-functions-ln"></a>

**Usage**: `LN(x)` returns the natural logarithm of x.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `LN(2)` = LN(2) | fields `LN(2)`
fetched rows / total rows = 1/1
+--------------------+
| LN(2)              |
|--------------------|
| 0.6931471805599453 |
+--------------------+
```

##### `LOG`
<a name="supported-ppl-math-functions-log"></a>

**Usage**: `LOG(x)` returns the natural logarithm of x that is the base e logarithm of the x. log(B, x) is equivalent to log(x)/log(B).

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `LOG(2)` = LOG(2), `LOG(2, 8)` = LOG(2, 8) | fields `LOG(2)`, `LOG(2, 8)`
fetched rows / total rows = 1/1
+--------------------+-------------+
| LOG(2)             | LOG(2, 8)   |
|--------------------+-------------|
| 0.6931471805599453 | 3.0         |
+--------------------+-------------+
```

##### `LOG2`
<a name="supported-ppl-math-functions-log2"></a>

**Usage**: `LOG2(x)` is equivalent to `log(x)`/`log(2)`.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `LOG2(8)` = LOG2(8) | fields `LOG2(8)`
fetched rows / total rows = 1/1
+-----------+
| LOG2(8)   |
|-----------|
| 3.0       |
+-----------+
```

##### `LOG10`
<a name="supported-ppl-math-functions-log10"></a>

**Usage**: `LOG10(x)` is equivalent to `log(x)`/`log(10)`.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `LOG10(100)` = LOG10(100) | fields `LOG10(100)`
fetched rows / total rows = 1/1
+--------------+
| LOG10(100)   |
|--------------|
| 2.0          |
+--------------+
```

##### `MOD`
<a name="supported-ppl-math-functions-mod"></a>

**Usage**: `MOD(n, m)` calculates the remainder of the number n divided by m.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: Wider type between types of n and m if m is nonzero value. If m equals to 0, then returns NULL.

**Example**:

```
os> source=people | eval `MOD(3, 2)` = MOD(3, 2), `MOD(3.1, 2)` = MOD(3.1, 2) | fields `MOD(3, 2)`, `MOD(3.1, 2)`
fetched rows / total rows = 1/1
+-------------+---------------+
| MOD(3, 2)   | MOD(3.1, 2)   |
|-------------+---------------|
| 1           | 1.1           |
+-------------+---------------+
```

##### `PI`
<a name="supported-ppl-math-functions-pi"></a>

**Usage**: `PI() `returns the constant pi.

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `PI()` = PI() | fields `PI()`
fetched rows / total rows = 1/1
+-------------------+
| PI()              |
|-------------------|
| 3.141592653589793 |
+-------------------+
```

##### `POW`
<a name="supported-ppl-math-functions-pow"></a>

**Usage**: `POW(x, y)` calculates the value of x raised to the power of y. Bad inputs return a `NULL` result.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Synonyms**: `POWER(_, _)`

**Example**:

```
os> source=people | eval `POW(3, 2)` = POW(3, 2), `POW(-3, 2)` = POW(-3, 2), `POW(3, -2)` = POW(3, -2) | fields `POW(3, 2)`, `POW(-3, 2)`, `POW(3, -2)`
fetched rows / total rows = 1/1
+-------------+--------------+--------------------+
| POW(3, 2)   | POW(-3, 2)   | POW(3, -2)         |
|-------------+--------------+--------------------|
| 9.0         | 9.0          | 0.1111111111111111 |
+-------------+--------------+--------------------+
```

##### POWER
<a name="supported-ppl-math-functions-power"></a>

**Usage**: `POWER(x, y)` calculates the value of x raised to the power of y. Bad inputs return a `NULL` result.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Synonyms**: `POW(_, _)`

**Example**:

```
os> source=people | eval `POWER(3, 2)` = POWER(3, 2), `POWER(-3, 2)` = POWER(-3, 2), `POWER(3, -2)` = POWER(3, -2) | fields `POWER(3, 2)`, `POWER(-3, 2)`, `POWER(3, -2)`
fetched rows / total rows = 1/1
+---------------+----------------+--------------------+
| POWER(3, 2)   | POWER(-3, 2)   | POWER(3, -2)       |
|---------------+----------------+--------------------|
| 9.0           | 9.0            | 0.1111111111111111 |
+---------------+----------------+--------------------+
```

##### `RADIANS`
<a name="supported-ppl-math-functions-radians"></a>

**Usage**: `RADIANS(x)` converts x from degrees to radians.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type**: DOUBLE

**Example**:

```
os> source=people | eval `RADIANS(90)` = RADIANS(90) | fields `RADIANS(90)`
fetched rows / total rows  = 1/1
+--------------------+
| RADIANS(90)        |
|--------------------|
| 1.5707963267948966 |
+--------------------+
```

##### `RAND`
<a name="supported-ppl-math-functions-rand"></a>

**Usage**: `RAND()`/`RAND(N)` returns a random floating-point value in the range 0 <= value < 1.0. If you specify integer N, the function initializes the seed before execution. One implication of this behavior is that with an identical argument N, `rand(N)` returns the same value each time, producing a repeatable sequence of column values.

**Argument type**: INTEGER

**Return type**: FLOAT

**Example**:

```
os> source=people | eval `RAND(3)` = RAND(3) | fields `RAND(3)`
fetched rows / total rows = 1/1
+------------+
| RAND(3)    |
|------------|
| 0.73105735 |
+------------+
```

##### `ROUND`
<a name="supported-ppl-math-functions-round"></a>

**Usage**: `ROUND(x, d)` rounds the argument x to d decimal places. If you don't specify d, it defaults to 0.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type map**:
+ (INTEGER/LONG [,INTEGER]) -> LONG
+ (FLOAT/DOUBLE [,INTEGER]) -> LONG

**Example**:

```
os> source=people | eval `ROUND(12.34)` = ROUND(12.34), `ROUND(12.34, 1)` = ROUND(12.34, 1), `ROUND(12.34, -1)` = ROUND(12.34, -1), `ROUND(12, 1)` = ROUND(12, 1) | fields `ROUND(12.34)`, `ROUND(12.34, 1)`, `ROUND(12.34, -1)`, `ROUND(12, 1)`
fetched rows / total rows = 1/1
+----------------+-------------------+--------------------+----------------+
| ROUND(12.34)   | ROUND(12.34, 1)   | ROUND(12.34, -1)   | ROUND(12, 1)   |
|----------------+-------------------+--------------------+----------------|
| 12.0           | 12.3              | 10.0               | 12             |
+----------------+-------------------+--------------------+----------------+
```

##### `SIGN`
<a name="supported-ppl-math-functions-sign"></a>

**Usage**: `SIGN` returns the sign of the argument as -1, 0, or 1, depending on whether the number is negative, zero, or positive.

**Argument type**: INTEGER/LONG/FLOAT/DOUBLE

**Return type:** INTEGER

**Example**:

```
os> source=people | eval `SIGN(1)` = SIGN(1), `SIGN(0)` = SIGN(0), `SIGN(-1.1)` = SIGN(-1.1) | fields `SIGN(1)`, `SIGN(0)`, `SIGN(-1.1)`
fetched rows / total rows = 1/1
+-----------+-----------+--------------+
| SIGN(1)   | SIGN(0)   | SIGN(-1.1)   |
|-----------+-----------+--------------|
| 1         | 0         | -1           |
+-----------+-----------+--------------+
```

##### `SIN`
<a name="supported-ppl-math-functions-sin"></a>

**Usage**: `sin(x)` calculates the sine of x, where x is given in radians.

**Argument type: **INTEGER/LONG/FLOAT/DOUBLE

**Return type: **DOUBLE

**Example**:

```
os> source=people | eval `SIN(0)` = SIN(0) | fields `SIN(0)`
fetched rows / total rows = 1/1
+----------+
| SIN(0)   |
|----------|
| 0.0      |
+----------+
```

##### `SQRT`
<a name="supported-ppl-math-functions-sqrt"></a>

**Usage**: `SQRT` calculates the square root of a non-negative number.

**Argument type: **INTEGER/LONG/FLOAT/DOUBLE

**Return type map:**
+ (Non-negative) INTEGER/LONG/FLOAT/DOUBLE -> DOUBLE
+ (Negative) INTEGER/LONG/FLOAT/DOUBLE -> NULL

**Example**:

```
os> source=people | eval `SQRT(4)` = SQRT(4), `SQRT(4.41)` = SQRT(4.41) | fields `SQRT(4)`, `SQRT(4.41)`
fetched rows / total rows = 1/1
+-----------+--------------+
| SQRT(4)   | SQRT(4.41)   |
|-----------+--------------|
| 2.0       | 2.1          |
+-----------+--------------+
```

##### PPL string functions
<a name="supported-ppl-string-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `CONCAT`
<a name="supported-ppl-string-functions-concat"></a>

**Usage**: `CONCAT(str1, str2, ...., str_9)` adds up to 9 strings together.

**Argument type:**
+ STRING, STRING, ...., STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `CONCAT('hello', 'world')` = CONCAT('hello', 'world'), `CONCAT('hello ', 'whole ', 'world', '!')` = CONCAT('hello ', 'whole ', 'world', '!') | fields `CONCAT('hello', 'world')`, `CONCAT('hello ', 'whole ', 'world', '!')`
fetched rows / total rows = 1/1
+----------------------------+--------------------------------------------+
| CONCAT('hello', 'world')   | CONCAT('hello ', 'whole ', 'world', '!')   |
|----------------------------+--------------------------------------------|
| helloworld                 | hello whole world!                         |
+----------------------------+--------------------------------------------+
```

##### `CONCAT_WS`
<a name="supported-ppl-string-functions-concat-ws"></a>

**Usage**: `CONCAT_WS(sep, str1, str2)` concatenates two or more strings using a specified separator between them.

**Argument type:**
+ STRING, STRING, ...., STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `CONCAT_WS(',', 'hello', 'world')` = CONCAT_WS(',', 'hello', 'world') | fields `CONCAT_WS(',', 'hello', 'world')`
fetched rows / total rows = 1/1
+------------------------------------+
| CONCAT_WS(',', 'hello', 'world')   |
|------------------------------------|
| hello,world                        |
+------------------------------------+
```

##### `LENGTH`
<a name="supported-ppl-string-functions-length"></a>

**Usage**: `length(str)` returns the length of the input string measured in bytes.

**Argument type:**
+ STRING
+ Return type: INTEGER

**Example**:

```
os> source=people | eval `LENGTH('helloworld')` = LENGTH('helloworld') | fields `LENGTH('helloworld')`
fetched rows / total rows = 1/1
+------------------------+
| LENGTH('helloworld')   |
|------------------------|
| 10                     |
+------------------------+
```

##### `LOWER`
<a name="supported-ppl-string-functions-lower"></a>

**Usage**: `lower(string)` converts the input string to lowercase.

**Argument type:**
+ STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `LOWER('helloworld')` = LOWER('helloworld'), `LOWER('HELLOWORLD')` = LOWER('HELLOWORLD') | fields `LOWER('helloworld')`, `LOWER('HELLOWORLD')`
fetched rows / total rows = 1/1
+-----------------------+-----------------------+
| LOWER('helloworld')   | LOWER('HELLOWORLD')   |
|-----------------------+-----------------------|
| helloworld            | helloworld            |
+-----------------------+-----------------------+
```

##### `LTRIM`
<a name="supported-ppl-string-functions-ltrim"></a>

**Usage**: `ltrim(str)` removes leading space characters from the input string.

**Argument type:**
+ STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `LTRIM('   hello')` = LTRIM('   hello'), `LTRIM('hello   ')` = LTRIM('hello   ') | fields `LTRIM('   hello')`, `LTRIM('hello   ')`
fetched rows / total rows = 1/1
+---------------------+---------------------+
| LTRIM('   hello')   | LTRIM('hello   ')   |
|---------------------+---------------------|
| hello               | hello               |
+---------------------+---------------------+
```

##### `POSITION`
<a name="supported-ppl-string-functions-position"></a>

**Usage**: `POSITION(substr IN str)` returns the position of the first occurrence of substring in string. It returns 0 if the substring is not in the string. It returns NULL if any argument is NULL.

**Argument type:**
+ STRING, STRING
+ Return type INTEGER

**Example**:

```
os> source=people | eval `POSITION('world' IN 'helloworld')` = POSITION('world' IN 'helloworld'), `POSITION('invalid' IN 'helloworld')`= POSITION('invalid' IN 'helloworld')  | fields `POSITION('world' IN 'helloworld')`, `POSITION('invalid' IN 'helloworld')`
fetched rows / total rows = 1/1
+-------------------------------------+---------------------------------------+
| POSITION('world' IN 'helloworld')   | POSITION('invalid' IN 'helloworld')   |
|-------------------------------------+---------------------------------------|
| 6                                   | 0                                     |
+-------------------------------------+---------------------------------------+
```

##### `REVERSE`
<a name="supported-ppl-string-functions-reverse"></a>

**Usage**: `REVERSE(str)` returns the reversed string of the input string.

**Argument type:**
+ STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `REVERSE('abcde')` = REVERSE('abcde') | fields `REVERSE('abcde')`
fetched rows / total rows = 1/1
+--------------------+
| REVERSE('abcde')   |
|--------------------|
| edcba              |
+--------------------+
```

##### `RIGHT`
<a name="supported-ppl-string-functions-right"></a>

**Usage**: `right(str, len)` returns the rightmost characters from the input string. It returns 0 if the substring is not in the string. It returns NULL if any argument is NULL.

**Argument type:**
+ STRING, INTEGER
+ Return type: STRING

**Example**:

```
os> source=people | eval `RIGHT('helloworld', 5)` = RIGHT('helloworld', 5), `RIGHT('HELLOWORLD', 0)` = RIGHT('HELLOWORLD', 0) | fields `RIGHT('helloworld', 5)`, `RIGHT('HELLOWORLD', 0)`
fetched rows / total rows = 1/1
+--------------------------+--------------------------+
| RIGHT('helloworld', 5)   | RIGHT('HELLOWORLD', 0)   |
|--------------------------+--------------------------|
| world                    |                          |
+--------------------------+--------------------------+
```

##### `RTRIM`
<a name="supported-ppl-string-functions-rtrim"></a>

**Usage**: `rtrim(str)` trims trailing space characters from the input string.

**Argument type:**
+ STRING
+ Return type: **STRING**

**Example**:

```
os> source=people | eval `RTRIM('   hello')` = RTRIM('   hello'), `RTRIM('hello   ')` = RTRIM('hello   ') | fields `RTRIM('   hello')`, `RTRIM('hello   ')`
fetched rows / total rows = 1/1
+---------------------+---------------------+
| RTRIM('   hello')   | RTRIM('hello   ')   |
|---------------------+---------------------|
|    hello            | hello               |
+---------------------+---------------------+
```

##### `SUBSTRING`
<a name="supported-ppl-string-functions-substring"></a>

**Usage**: `substring(str, start)` or `substring(str, start, length)` returns a substring of the input string. With no length specified, it returns the entire string from the start position.

**Argument type:**
+ STRING, INTEGER, INTEGER
+ Return type: STRING

**Example**:

```
os> source=people | eval `SUBSTRING('helloworld', 5)` = SUBSTRING('helloworld', 5), `SUBSTRING('helloworld', 5, 3)` = SUBSTRING('helloworld', 5, 3) | fields `SUBSTRING('helloworld', 5)`, `SUBSTRING('helloworld', 5, 3)`
fetched rows / total rows = 1/1
+------------------------------+---------------------------------+
| SUBSTRING('helloworld', 5)   | SUBSTRING('helloworld', 5, 3)   |
|------------------------------+---------------------------------|
| oworld                       | owo                             |
+------------------------------+---------------------------------+
```

##### `TRIM`
<a name="supported-ppl-string-functions-trim"></a>

**Usage**: `trim(string)` removes leading and trailing whitespace from the input string.

**Argument type:**
+ STRING
+ Return type: **STRING**

**Example**:

```
os> source=people | eval `TRIM('   hello')` = TRIM('   hello'), `TRIM('hello   ')` = TRIM('hello   ') | fields `TRIM('   hello')`, `TRIM('hello   ')`
fetched rows / total rows = 1/1
+--------------------+--------------------+
| TRIM('   hello')   | TRIM('hello   ')   |
|--------------------+--------------------|
| hello              | hello              |
+--------------------+--------------------+
```

##### `UPPER`
<a name="supported-ppl-string-functions-upper"></a>

**Usage**: `upper(string)` converts the input string to uppercase.

**Argument type:**
+ STRING
+ Return type: STRING

**Example**:

```
os> source=people | eval `UPPER('helloworld')` = UPPER('helloworld'), `UPPER('HELLOWORLD')` = UPPER('HELLOWORLD') | fields `UPPER('helloworld')`, `UPPER('HELLOWORLD')`
fetched rows / total rows = 1/1
+-----------------------+-----------------------+
| UPPER('helloworld')   | UPPER('HELLOWORLD')   |
|-----------------------+-----------------------|
| HELLOWORLD            | HELLOWORLD            |
+-----------------------+-----------------------+
```

##### PPL type conversion functions
<a name="supported-ppl-type-conversion-functions"></a>

**Note**  
To see which AWS data source integrations support this PPL function, see [Functions](#supported-ppl-functions).

##### `TRIM`
<a name="supported-ppl-conversion-functions-cast"></a>

**Usage**: `cast(expr as dateType)` casts the `expr` to the `dataType` and returns the value of the `dataType`. 

The following conversion rules apply:


**Type conversion rules**  

| Src/Target | STRING | NUMBER | BOOLEAN | TIMESTAMP | DATE | TIME | 
| --- | --- | --- | --- | --- | --- | --- | 
| STRING |  | Note1 | Note1 | TIMESTAMP() | DATE() | TIME() | 
| NUMBER | Note1 |  | v\!=0 | N/A | N/A | N/A | 
| BOOLEAN | Note1 | v?1:0 |  | N/A | N/A | N/A | 
| TIMESTAMP | Note1 | N/A | N/A |  | DATE() | TIME() | 
| DATE | Note1 | N/A | N/A | N/A |  | N/A | 
| TIME | Note1 | N/A | N/A | N/A | N/A |  | 

**Cast to string example:**

```
os> source=people | eval `cbool` = CAST(true as string), `cint` = CAST(1 as string), `cdate` = CAST(CAST('2012-08-07' as date) as string) | fields `cbool`, `cint`, `cdate`
fetched rows / total rows = 1/1
+---------+--------+------------+
| cbool   | cint   | cdate      |
|---------+--------+------------|
| true    | 1      | 2012-08-07 |
+---------+--------+------------+
```

**Cast to number example:**

```
os> source=people | eval `cbool` = CAST(true as int), `cstring` = CAST('1' as int) | fields `cbool`, `cstring`
fetched rows / total rows = 1/1
+---------+-----------+
| cbool   | cstring   |
|---------+-----------|
| 1       | 1         |
+---------+-----------+
```

**Cast to date example:**

```
os> source=people | eval `cdate` = CAST('2012-08-07' as date), `ctime` = CAST('01:01:01' as time), `ctimestamp` = CAST('2012-08-07 01:01:01' as timestamp) | fields `cdate`, `ctime`, `ctimestamp`
fetched rows / total rows = 1/1
+------------+----------+---------------------+
| cdate      | ctime    | ctimestamp          |
|------------+----------+---------------------|
| 2012-08-07 | 01:01:01 | 2012-08-07 01:01:01 |
+------------+----------+---------------------+
```

**Chained cast example:**

```
os> source=people | eval `cbool` = CAST(CAST(true as string) as boolean) | fields `cbool`
fetched rows / total rows = 1/1
+---------+
| cbool   |
|---------|
| True    |
+---------+
```