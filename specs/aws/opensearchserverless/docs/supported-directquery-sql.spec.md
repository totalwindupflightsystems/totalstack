---
id: "@specs/aws/opensearchserverless/docs/supported-directquery-sql"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Supported SQL commands"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Supported SQL commands

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/supported-directquery-sql
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Supported OpenSearch SQL commands and functions
<a name="supported-directquery-sql"></a>

The following reference tables show which SQL commands are supported in OpenSearch Discover for querying data in Amazon S3, Security Lake, or CloudWatch Logs, and which SQL commands are supported in CloudWatch Logs Insights. The SQL syntax supported in CloudWatch Logs Insights and that supported in OpenSearch Discover for querying CloudWatch Logs are the same, and referenced as CloudWatch Logs in the following tables.

**Note**  
OpenSearch also has SQL support for querying data that is ingested in OpenSearch and stored in indexes. This SQL dialect is different than the SQL used in direct query and is referred to as [OpenSearch SQL on indexes](https://opensearch.org/docs/latest/search-plugins/sql/sql/index/).

**Topics**
+ [Commands](#supported-sql-data-retrieval)
+ [Functions](#supported-sql-functions)
+ [General SQL restrictions](#general-sql-restrictions)
+ [Additional information for CloudWatch Logs Insights users using OpenSearch SQL](#supported-sql-for-multi-log-queries)

## Commands
<a name="supported-sql-data-retrieval"></a>

**Note**  
In the example commands column, replace `{{<tableName/logGroup>}}` as needed depending on which data source you're querying.   
Example command: `SELECT Body , Operation FROM <tableName/logGroup>` 
If you're querying Amazon S3 or Security Lake, use: `SELECT Body , Operation FROM table_name` 
If you're querying CloudWatch Logs, use: `SELECT Body , Operation FROM `LogGroupA`` 


| Command | Description | CloudWatch Logs | Amazon S3 | Security Lake | Example command | 
| --- | --- | --- | --- | --- | --- | 
| [SELECT clause](#supported-sql-select) | Displays projected values. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    method,<br />    status <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [WHERE clause](#supported-sql-where) | Filters log events based on the provided field criteria. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    {{<tableName/logGroup>}}<br />WHERE <br />    status = 100</pre>  | 
| [GROUP BY clause](#supported-sql-group-by) | Groups log events based on category and finds the average based on stats. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    method,<br />    status,<br />    COUNT(*) AS request_count,<br />    SUM(bytes) AS total_bytes <br />FROM <br />    {{<tableName/logGroup>}} <br />GROUP BY <br />    method, <br />    status</pre>  | 
| [HAVING clause](#supported-sql-having) | Filters the results based on grouping conditions. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    method,<br />    status,<br />    COUNT(*) AS request_count,<br />    SUM(bytes) AS total_bytes <br />FROM <br />    {{<tableName/logGroup>}} <br />GROUP BY <br />    method,<br />    status<br />HAVING <br />    COUNT(*) > 5</pre>  | 
| [ORDER BY clause](#supported-sql-order-by) | Orders the results based on fields in the order clause. You can sort in either descending or ascending order. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    {{<tableName/logGroup>}} <br />ORDER BY <br />    status DESC</pre>  | 
| [JOIN clause](#supported-sql-join) <br />( `INNER` \| `CROSS` \| `LEFT` `OUTER` ) | Joins the results for two tables based on common fields. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported (must use `Inner` and `Left Outer` keywords for join; Only only one JOIN operation is supported in a SELECT statement) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported (must use Inner, Left Outer, and Cross keywords for join) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported (must use Inner, Left Outer, and Cross keywords for join) |  <pre>SELECT <br />    A.Body,<br />    B.Timestamp<br />FROM <br />    {{<tableNameA/logGroupA>}} AS A <br />INNER JOIN <br />    {{<tableNameB/logGroupB>}} AS B <br />    ON A.`requestId` = B.`requestId`</pre>  | 
| [LIMIT clause](#supported-sql-limit) | Restricts the results to first N rows. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    {{<tableName/logGroup>}} <br />LIMIT <br />    10</pre>  | 
| [CASE clause](#supported-sql-case) | Evaluates conditions and returns a value when the first condition is met. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT<br />    method,<br />    status,<br />    CASE<br />        WHEN status BETWEEN 100 AND 199 THEN 'Informational'<br />        WHEN status BETWEEN 200 AND 299 THEN 'Success'<br />        WHEN status BETWEEN 300 AND 399 THEN 'Redirection'<br />        WHEN status BETWEEN 400 AND 499 THEN 'Client Error'<br />        WHEN status BETWEEN 500 AND 599 THEN 'Server Error'<br />        ELSE 'Unknown Status'<br />    END AS status_category,<br />    CASE method<br />        WHEN 'GET' THEN 'Read Operation'<br />        WHEN 'POST' THEN 'Create Operation'<br />        WHEN 'PUT' THEN 'Update Operation'<br />        WHEN 'PATCH' THEN 'Partial Update Operation'<br />        WHEN 'DELETE' THEN 'Delete Operation'<br />        ELSE 'Other Operation'<br />    END AS operation_type,<br />    bytes,<br />    datetime<br />FROM {{<tableName/logGroup>}}                         </pre>  | 
| [Common table expression](#supported-sql-cte) | Creates a named temporary result set within a SELECT, INSERT, UPDATE, DELETE, or MERGE statement. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>WITH RequestStats AS (<br />    SELECT <br />        method,<br />        status,<br />        bytes,<br />        COUNT(*) AS request_count<br />    FROM <br />        tableName<br />    GROUP BY <br />        method,<br />        status,<br />        bytes<br />)<br />SELECT <br />    method,<br />    status,<br />    bytes,<br />    request_count <br />FROM <br />    RequestStats <br />WHERE <br />    bytes > 1000</pre>  | 
| [EXPLAIN](#supported-sql-explain) | Displays the execution plan of a SQL statement without actually executing it. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>EXPLAIN<br />SELECT <br />    k,<br />    SUM(v)<br />FROM <br />    VALUES <br />        (1, 2),<br />        (1, 3) AS t(k, v)<br />GROUP BY <br />    k</pre>  | 
| [LATERAL SUBQUERY clause](#supported-sql-lateral-subquery) | Allows a subquery in the FROM clause to reference columns from preceding items in the same FROM clause. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> SELECT <br />    * <br />FROM <br />    tableName<br />LATERAL (<br />    SELECT <br />        * <br />    FROM <br />        t2 <br />    WHERE <br />        t1.c1 = t2.c1<br />)</pre>  | 
| [LATERAL VIEW clause](#supported-sql-lateral-view) | Generates a virtual table by applying a table-generating function to each row of a base table. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    tableName<br />LATERAL VIEW <br />    EXPLODE(ARRAY(30, 60)) tableName AS c_age<br />LATERAL VIEW <br />    EXPLODE(ARRAY(40, 80)) AS d_age</pre>  | 
| [LIKE predicate](#supported-sql-like-predicate) | Matches a string against a pattern using wildcard characters. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> SELECT <br />    method,<br />    status,<br />    request,<br />    host <br />FROM <br />    {{<tableName/logGroup>}} <br />WHERE <br />    method LIKE 'D%'</pre>  | 
| [OFFSET](#supported-sql-offset) | Specifies the number of rows to skip before starting to return rows from the query. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported when used in conjunction with a LIMIT clause in a query. For example:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-directquery-sql.html) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> SELECT <br />    method,<br />    status,<br />    bytes,<br />    datetime <br />FROM <br />    {{<tableName/logGroup>}} <br />ORDER BY <br />    datetime<br />OFFSET <br />    10 </pre>  | 
| [PIVOT clause](#supported-sql-pivot) | Transforms rows into columns, rotating data from a row-based format to a column-based format. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    (<br />        SELECT <br />            method,<br />            status,<br />            bytes<br />        FROM <br />            {{<tableName/logGroup>}}<br />    ) AS SourceTable <br />PIVOT <br />(<br />    SUM(bytes) <br />    FOR method IN ('GET', 'POST', 'PATCH', 'PUT', 'DELETE')<br />) AS PivotTable</pre>  | 
| [Set operators](#supported-sql-set) | Combines the results of two or more SELECT statements (e.g., UNION, INTERSECT, EXCEPT). | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    method,<br />    status,<br />    bytes<br />FROM <br />    {{<tableName/logGroup>}}<br />WHERE <br />    status = '416'<br /><br />UNION<br /><br />SELECT <br />    method,<br />    status,<br />    bytes<br />FROM <br />    {{<tableName/logGroup>}}<br />WHERE <br />    bytes > 20000</pre>  | 
| [SORT BY clause](#supported-sql-sort-by) | Specifies the order in which to return the query results. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    method,<br />    status,<br />    bytes<br />FROM <br />    {{<tableName/logGroup>}}<br />SORT BY <br />    bytes DESC</pre>  | 
| [UNPIVOT](#supported-sql-unpivot) | Transforms columns into rows, rotating data from a column-based format to a row-based format. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> SELECT <br />    status,<br />    REPLACE(method, '_bytes', '') AS request_method,<br />    bytes,<br />    datetime <br />FROM <br />    PivotedData <br />UNPIVOT <br />(<br />    bytes <br />    FOR method IN <br />    (<br />        GET_bytes,<br />        POST_bytes,<br />        PATCH_bytes,<br />        PUT_bytes,<br />        DELETE_bytes<br />    )<br />) AS UnpivotedData</pre>  | 

## Functions
<a name="supported-sql-functions"></a>

**Note**  
In the example commands column, replace `{{<tableName/logGroup>}}` as needed depending on which data source you're querying.   
Example command: `SELECT Body , Operation FROM <tableName/logGroup>` 
If you're querying Amazon S3 or Security Lake, use: `SELECT Body , Operation FROM table_name` 
If you're querying CloudWatch Logs, use: `SELECT Body , Operation FROM `LogGroupA`` 


| Available SQL Grammar | Description | CloudWatch Logs | Amazon S3 | Security Lake | Example command | 
| --- | --- | --- | --- | --- | --- | 
| [String functions](#supported-sql-string) | Built-in functions that can manipulate and transform string and text data within SQL queries. For example, converting case, combining strings, extracting parts, and cleaning text. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    UPPER(method) AS upper_method,<br />    LOWER(host) AS lower_host <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Date and time functions](#supported-sql-date-time) | Built-in functions for handling and transforming date and timestamp data in queries. For example, **date\_add**, **date\_format**, **datediff**, and **current\_date**. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    TO_TIMESTAMP(datetime) AS timestamp,<br />    TIMESTAMP_SECONDS(UNIX_TIMESTAMP(datetime)) AS from_seconds,<br />    UNIX_TIMESTAMP(datetime) AS to_unix,<br />    FROM_UTC_TIMESTAMP(datetime, 'PST') AS to_pst,<br />    TO_UTC_TIMESTAMP(datetime, 'EST') AS from_est <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Aggregate functions](#supported-sql-aggregate) | Built-in functions that perform calculations on multiple rows to produce a single summarized value. For example, **sum**, **count**, **avg**, **max**, and **min**. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png)Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    COUNT(*) AS total_records,<br />    COUNT(DISTINCT method) AS unique_methods,<br />    SUM(bytes) AS total_bytes,<br />    AVG(bytes) AS avg_bytes,<br />    MIN(bytes) AS min_bytes,<br />    MAX(bytes) AS max_bytes <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Conditional functions](#supported-sql-conditional) | Built-in functions that perform actions based on specified conditions, or that evaluate expressions conditionally. For example, **CASE** and **IF**. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    CASE <br />        WHEN method = 'GET' AND bytes < 1000 THEN 'Small Read'<br />        WHEN method = 'POST' AND bytes > 10000 THEN 'Large Write'<br />        WHEN status >= 400 OR bytes = 0 THEN 'Problem'<br />        ELSE 'Normal'<br />    END AS request_type <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [JSON functions](#supported-sql-json) | Built-in functions for parsing, extracting, modifying, and querying JSON-formatted data within SQL queries (e.g., from\_json, to\_json, get\_json\_object, json\_tuple) allowing manipulation of JSON structures in datasets. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    FROM_JSON(<br />        @message, <br />        'STRUCT<<br />            host: STRING,<br />            user-identifier: STRING,<br />            datetime: STRING,<br />            method: STRING,<br />            status: INT,<br />            bytes: INT<br />        >'<br />    ) AS parsed_json <br />FROM <br />    {{<tableName/logGroup>}} </pre>  | 
| [Array functions](#supported-sql-array) | Built-in functions for working with array-type columns in SQL queries, allowing operations like accessing, modifying, and analyzing array data (e.g., size, explode, array\_contains). | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    scores,<br />    size(scores) AS length,<br />    array_contains(scores, 90) AS has_90 <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Window functions](#supported-sql-window) | Built-in functions that perform calculations across a specified set of rows related to the current row (window), enabling operations like ranking, running totals, and moving averages (e.g., ROW\_NUMBER, RANK, LAG, LEAD) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre> SELECT <br />    field1,<br />    field2,<br />    RANK() OVER (ORDER BY field2 DESC) AS field2Rank <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Conversion functions](#supported-sql-conversion) | Built-in functions for converting data from one type to another within SQL queries, enabling data type transformations and format conversions (e.g., CAST, TO\_DATE, TO\_TIMESTAMP, BINARY) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    CAST('123' AS INT) AS converted_number,<br />    CAST(123 AS STRING) AS converted_string <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Predicate functions](#supported-sql-predicate) | Built-in functions that evaluate conditions and return boolean values (true/false) based on specified criteria or patterns (e.g., IN, LIKE, BETWEEN, IS NULL, EXISTS) | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    * <br />FROM <br />    {{<tableName/logGroup>}} <br />WHERE <br />    id BETWEEN 50000 AND 75000</pre>  | 
| [Map functions](#supported-sql-map) | Applies a specified function to each element in a collection, transforming the data into a new set of values. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    MAP_FILTER(<br />        MAP(<br />            'method', method,<br />            'status', CAST(status AS STRING),<br />            'bytes', CAST(bytes AS STRING)<br />        ),<br />        (k, v) -> k IN ('method', 'status') AND v != 'null'<br />    ) AS filtered_map <br />FROM <br />    {{<tableName/logGroup>}} <br />WHERE <br />    status = 100</pre>  | 
| [Mathematical functions](#supported-sql-math) | Performs mathematical operations on numeric data, such as calculating averages, sums, or trigonometric values. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    bytes,<br />    bytes + 1000 AS added,<br />    bytes - 1000 AS subtracted,<br />    bytes * 2 AS doubled,<br />    bytes / 1024 AS kilobytes,<br />    bytes % 1000 AS remainder <br />FROM <br />    {{<tableName/logGroup>}}</pre>  | 
| [Multi-log group functions](#multi-log-queries) | Enables users to specify multiple log groups in a SQL SELECT statement | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | Not applicable | Not applicable |  <pre>SELECT <br />    lg1.Column1,<br />    lg1.Column2 <br />FROM <br />    `logGroups(logGroupIdentifier: ['LogGroup1', 'LogGroup2'])` AS lg1 <br />WHERE <br />    lg1.Column3 = "Success"<br /></pre>  | 
| [Generator functions](#supported-sql-generator) | Creates an iterator object that yields a sequence of values, allowing for efficient memory usage in large data sets. | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/negative_icon.png) Not supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported | ![](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/success_icon.png) Supported |  <pre>SELECT <br />    explode(array(10, 20)) </pre>  | 

## General SQL restrictions
<a name="general-sql-restrictions"></a>

The following restrictions apply when using OpenSearch SQL with CloudWatch Logs, Amazon S3, and Security Lake.

1. You can only use one JOIN operation in a SELECT statement.

1. Only one level of nested subqueries is supported.

1. Multiple statement queries separated by semi-colons aren't supported.

1. Queries containing field names that are identical but differ only in case (such as field1 and FIELD1) are not supported.

   For example, the following queries are not supported:

   ```
   Select AWSAccountId, awsaccountid from LogGroup
   ```

   However, the following query is because the field name (@logStream) is identical in both log groups:

   ```
   Select a.`@logStream`, b.`@logStream` from Table A INNER Join Table B on a.id = b.id 
   ```

1. Functions and expressions must operate on field names and be part of a SELECT statement with a log group specified in the FROM clause.

   For example, this query is not supported:

   ```
   SELECT cos(10) FROM LogGroup
   ```

   This query is supported:

   ```
   SELECT cos(field1) FROM LogGroup
   ```

## Additional information for CloudWatch Logs Insights users using OpenSearch SQL
<a name="supported-sql-for-multi-log-queries"></a>

 CloudWatch Logs supports OpenSearch SQL queries in the Logs Insights console, API, and CLI. It supports most commands, including SELECT, FROM, WHERE, GROUP BY, HAVING, JOINS, and nested queries, along with JSON, math, string, and conditional functions. However, CloudWatch Logs supports only read operations, so it doesn't allow DDL or DML statements. See the tables in the previous sections for a full list of supported commands and functions. 

### Multi-log group functions
<a name="multi-log-queries"></a>

CloudWatch Logs Insights supports the ability to query multiple log groups. To address this use case in SQL, you can use the `logGroups` command. This command is specific to querying data in CloudWatch Logs Insights involving one or more log groups. Use this syntax to query multiple log groups by specifying them in the command, instead of writing a query for each of the log groups and combining them with a `UNION` command. 

Syntax:

```
`logGroups(
    logGroupIdentifier: ['LogGroup1','LogGroup2', ...'LogGroupn']
)
```

In this syntax, you can specify up to 50 log groups in the `logGroupIndentifier` parameter. To reference log groups in a monitoring account, use ARNs instead of `LogGroup` names.

Example query:

```
SELECT LG1.Column1, LG1.Column2 from `logGroups(
    logGroupIdentifier: ['LogGroup1', 'LogGroup2']
)` as LG1 
WHERE LG1.Column1 = 'ABC'
```

The following syntax involving multiple log groups after the `FROM` statement is not supported when querying CloudWatch Logs:

```
SELECT Column1, Column2 FROM 'LogGroup1', 'LogGroup2', ...'LogGroupn' 
WHERE Column1 = 'ABC'
```

### Restrictions
<a name="restrictions"></a>

When you use SQL or PPL commands, enclose certain fields in backticks to query them. Backticks are required for fields with special characters (non-alphabetic and non-numeric). For example, enclose `@message`, `Operation.Export,` and `Test::Field` in backticks. You don't need to enclose columns with purely alphabetic names in backticks.

Example query with simple fields:

```
SELECT SessionToken, Operation, StartTime  FROM `LogGroup-A`
LIMIT 1000;
```

Same query with backticks appended:

```
SELECT `SessionToken`, `Operation`, `StartTime`  FROM `LogGroup-A`
LIMIT 1000;
```

For additional general restrictions that aren't specific to CloudWatch Logs, see [General SQL restrictions](#general-sql-restrictions).

### Sample queries and quotas
<a name="samples"></a>

**Note**  
The following applies to both CloudWatch Logs Insights users and OpenSearch users querying CloudWatch data.

For sample SQL queries that you can use in CloudWatch Logs, see **Saved and sample queries** in the Amazon CloudWatch Logs Insights console for examples.

For information about the limits that apply when querying CloudWatch Logs from OpenSearch Service, see [CloudWatch Logs quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) in the Amazon CloudWatch Logs User Guide. Limits involve the number of CloudWatch Log groups you can query, the maximum concurrent queries that you can execute, the maximum query execution time, and the maximum number of rows returned in results. The limits are the same regardless of which language you use for querying CloudWatch Logs (namely, OpenSearch PPL, SQL, and Logs Insights). 

### SQL commands
<a name="supported-sql-commands-details"></a>

**Topics**
+ [String functions](#supported-sql-string)
+ [Date and time functions](#supported-sql-date-time)
+ [Aggregate functions](#supported-sql-aggregate)
+ [Conditional functions](#supported-sql-conditional)
+ [JSON functions](#supported-sql-json)
+ [Array functions](#supported-sql-array)
+ [Window functions](#supported-sql-window)
+ [Conversion functions](#supported-sql-conversion)
+ [Predicate functions](#supported-sql-predicate)
+ [Map functions](#supported-sql-map)
+ [Mathematical functions](#supported-sql-math)
+ [Generator functions](#supported-sql-generator)
+ [SELECT clause](#supported-sql-select)
+ [WHERE clause](#supported-sql-where)
+ [GROUP BY clause](#supported-sql-group-by)
+ [HAVING clause](#supported-sql-having)
+ [ORDER BY clause](#supported-sql-order-by)
+ [JOIN clause](#supported-sql-join)
+ [LIMIT clause](#supported-sql-limit)
+ [CASE clause](#supported-sql-case)
+ [Common table expression](#supported-sql-cte)
+ [EXPLAIN](#supported-sql-explain)
+ [LATERAL SUBQUERY clause](#supported-sql-lateral-subquery)
+ [LATERAL VIEW clause](#supported-sql-lateral-view)
+ [LIKE predicate](#supported-sql-like-predicate)
+ [OFFSET](#supported-sql-offset)
+ [PIVOT clause](#supported-sql-pivot)
+ [Set operators](#supported-sql-set)
+ [SORT BY clause](#supported-sql-sort-by)
+ [UNPIVOT](#supported-sql-unpivot)

#### String functions
<a name="supported-sql-string"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| ascii(str) | Returns the numeric value of the first character of str. | 
| base64(bin) | Converts the argument from a binary bin to a base 64 string. | 
| bit\_length(expr) | Returns the bit length of string data or number of bits of binary data. | 
| btrim(str) | Removes the leading and trailing space characters from str. | 
| btrim(str, trimStr) | Remove the leading and trailing trimStr characters from str. | 
| char(expr) | Returns the ASCII character having the binary equivalent to expr. If n is larger than 256 the result is equivalent to chr(n % 256) | 
| char\_length(expr) | Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros. | 
| character\_length(expr) | Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros. | 
| chr(expr) | Returns the ASCII character having the binary equivalent to expr. If n is larger than 256 the result is equivalent to chr(n % 256) | 
| concat\_ws(sep[, str \| array(str)]\+) | Returns the concatenation of the strings separated by sep, skipping null values. | 
| contains(left, right) | Returns a boolean. The value is True if right is found inside left. Returns NULL if either input expression is NULL. Otherwise, returns False. Both left or right must be of STRING or BINARY type. | 
| decode(bin, charset) | Decodes the first argument using the second argument character set. | 
| decode(expr, search, result [, search, result ] ... [, default]) | Compares expr to each search value in order. If expr is equal to a search value, decode returns the corresponding result. If no match is found, then it returns default. If default is omitted, it returns null. | 
| elt(n, input1, input2, ...) | Returns the n-th input, e.g., returns input2 when n is 2.  | 
| encode(str, charset) | Encodes the first argument using the second argument character set. | 
| endswith(left, right) | Returns a boolean. The value is True if left ends with right. Returns NULL if either input expression is NULL. Otherwise, returns False. Both left or right must be of STRING or BINARY type. | 
| find\_in\_set(str, str\_array) | Returns the index (1-based) of the given string (str) in the comma-delimited list (str\_array). Returns 0, if the string was not found or if the given string (str) contains a comma. | 
| format\_number(expr1, expr2) | Formats the number expr1 like '\#,\#\#\#,\#\#\#.\#\#', rounded to expr2 decimal places. If expr2 is 0, the result has no decimal point or fractional part. expr2 also accept a user specified format. This is supposed to function like MySQL's FORMAT. | 
| format\_string(strfmt, obj, ...) | Returns a formatted string from printf-style format strings. | 
| initcap(str) | Returns str with the first letter of each word in uppercase. All other letters are in lowercase. Words are delimited by white space. | 
| instr(str, substr) | Returns the (1-based) index of the first occurrence of substr in str. | 
| lcase(str) | Returns str with all characters changed to lowercase. | 
| left(str, len) | Returns the leftmost len(len can be string type) characters from the string str,if len is less or equal than 0 the result is an empty string. | 
| len(expr) | Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros. | 
| length(expr) | Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros. | 
| levenshtein(str1, str2[, threshold]) | Returns the Levenshtein distance between the two given strings. If threshold is set and distance more than it, return -1. | 
| locate(substr, str[, pos]) | Returns the position of the first occurrence of substr in str after position pos. The given pos and return value are 1-based. | 
| lower(str) | Returns str with all characters changed to lowercase. | 
| lpad(str, len[, pad]) | Returns str, left-padded with pad to a length of len. If str is longer than len, the return value is shortened to len characters or bytes. If pad is not specified, str will be padded to the left with space characters if it is a character string, and with zeros if it is a byte sequence. | 
| ltrim(str) | Removes the leading space characters from str. | 
| luhn\_check(str ) | Checks that a string of digits is valid according to the Luhn algorithm. This checksum function is widely applied on credit card numbers and government identification numbers to distinguish valid numbers from mistyped, incorrect numbers. | 
| mask(input[, upperChar, lowerChar, digitChar, otherChar]) | masks the given string value. The function replaces characters with 'X' or 'x', and numbers with 'n'. This can be useful for creating copies of tables with sensitive information removed. | 
| octet\_length(expr) | Returns the byte length of string data or number of bytes of binary data. | 
| overlay(input, replace, pos[, len]) | Replace input with replace that starts at pos and is of length len. | 
| position(substr, str[, pos]) | Returns the position of the first occurrence of substr in str after position pos. The given pos and return value are 1-based. | 
| printf(strfmt, obj, ...) | Returns a formatted string from printf-style format strings. | 
| regexp\_count(str, regexp) | Returns a count of the number of times that the regular expression pattern regexp is matched in the string str. | 
| regexp\_extract(str, regexp[, idx]) | Extract the first string in the str that match the regexp expression and corresponding to the regex group index. | 
| regexp\_extract\_all(str, regexp[, idx]) | Extract all strings in the str that match the regexp expression and corresponding to the regex group index. | 
| regexp\_instr(str, regexp) | Searches a string for a regular expression and returns an integer that indicates the beginning position of the matched substring. Positions are 1-based, not 0-based. If no match is found, returns 0. | 
| regexp\_replace(str, regexp, rep[, position]) | Replaces all substrings of str that match regexp with rep. | 
| regexp\_substr(str, regexp) | Returns the substring that matches the regular expression regexp within the string str. If the regular expression is not found, the result is null. | 
| repeat(str, n) | Returns the string which repeats the given string value n times. | 
| replace(str, search[, replace]) | Replaces all occurrences of search with replace. | 
| right(str, len) | Returns the rightmost len(len can be string type) characters from the string str,if len is less or equal than 0 the result is an empty string. | 
| rpad(str, len[, pad]) | Returns str, right-padded with pad to a length of len. If str is longer than len, the return value is shortened to len characters. If pad is not specified, str will be padded to the right with space characters if it is a character string, and with zeros if it is a binary string. | 
| rtrim(str) | Removes the trailing space characters from str. | 
| sentences(str[, lang, country]) | Splits str into an array of array of words. | 
| soundex(str) | Returns Soundex code of the string. | 
| space(n) | Returns a string consisting of n spaces. | 
| split(str, regex, limit) | Splits str around occurrences that match regex and returns an array with a length of at most limit | 
| split\_part(str, delimiter, partNum) | Splits str by delimiter and return requested part of the split (1-based). If any input is null, returns null. if partNum is out of range of split parts, returns empty string. If partNum is 0, throws an error. If partNum is negative, the parts are counted backward from the end of the string. If the delimiter is an empty string, the str is not split. | 
| startswith(left, right) | Returns a boolean. The value is True if left starts with right. Returns NULL if either input expression is NULL. Otherwise, returns False. Both left or right must be of STRING or BINARY type. | 
| substr(str, pos[, len]) | Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len. | 
| substr(str FROM pos[ FOR len]]) | Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len. | 
| substring(str, pos[, len]) | Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len. | 
| substring(str FROM pos[ FOR len]]) | Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len. | 
| substring\_index(str, delim, count) | Returns the substring from str before count occurrences of the delimiter delim. If count is positive, everything to the left of the final delimiter (counting from the left) is returned. If count is negative, everything to the right of the final delimiter (counting from the right) is returned. The function substring\_index performs a case-sensitive match when searching for delim. | 
| to\_binary(str[, fmt]) | Converts the input str to a binary value based on the supplied fmt. fmt can be a case-insensitive string literal of "hex", "utf-8", "utf8", or "base64". By default, the binary format for conversion is "hex" if fmt is omitted. The function returns NULL if at least one of the input parameters is NULL. | 
| to\_char(numberExpr, formatExpr) | Convert numberExpr to a string based on the formatExpr. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: '0' or '9': Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input value, generating a result string of the same length as the corresponding sequence in the format string. The result string is left-padded with zeros if the 0/9 sequence comprises more digits than the matching part of the decimal value, starts with 0, and is before the decimal point. Otherwise, it is padded with spaces. '.' or 'D': Specifies the position of the decimal point (optional, only allowed once). ',' or 'G': Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. ' | 
| to\_number(expr, fmt) | Convert string 'expr' to a number based on the string format 'fmt'. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: '0' or '9': Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input string. If the 0/9 sequence starts with 0 and is before the decimal point, it can only match a digit sequence of the same size. Otherwise, if the sequence starts with 9 or is after the decimal point, it can match a digit sequence that has the same or smaller size. '.' or 'D': Specifies the position of the decimal point (optional, only allowed once). ',' or 'G': Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. 'expr' must match the grouping separator relevant for the size of the number. ' | 
| to\_varchar(numberExpr, formatExpr) | Convert numberExpr to a string based on the formatExpr. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: '0' or '9': Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input value, generating a result string of the same length as the corresponding sequence in the format string. The result string is left-padded with zeros if the 0/9 sequence comprises more digits than the matching part of the decimal value, starts with 0, and is before the decimal point. Otherwise, it is padded with spaces. '.' or 'D': Specifies the position of the decimal point (optional, only allowed once). ',' or 'G': Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. ' | 
| translate(input, from, to) | Translates the input string by replacing the characters present in the from string with the corresponding characters in the to string. | 
| trim(str) | Removes the leading and trailing space characters from str. | 
| trim(BOTH FROM str) | Removes the leading and trailing space characters from str. | 
| trim(LEADING FROM str) | Removes the leading space characters from str. | 
| trim(TRAILING FROM str) | Removes the trailing space characters from str. | 
| trim(trimStr FROM str) | Remove the leading and trailing trimStr characters from str. | 
| trim(BOTH trimStr FROM str) | Remove the leading and trailing trimStr characters from str. | 
| trim(LEADING trimStr FROM str) | Remove the leading trimStr characters from str. | 
| trim(TRAILING trimStr FROM str) | Remove the trailing trimStr characters from str. | 
| try\_to\_binary(str[, fmt]) | This is a special version of to\_binary that performs the same operation, but returns a NULL value instead of raising an error if the conversion cannot be performed. | 
| try\_to\_number(expr, fmt) | Convert string 'expr' to a number based on the string format fmt. Returns NULL if the string 'expr' does not match the expected format. The format follows the same semantics as the to\_number function. | 
| ucase(str) | Returns str with all characters changed to uppercase. | 
| unbase64(str) | Converts the argument from a base 64 string str to a binary. | 
| upper(str) | Returns str with all characters changed to uppercase. | 



**Examples**

```
-- ascii
SELECT ascii('222');
+----------+
|ascii(222)|
+----------+
|        50|
+----------+
SELECT ascii(2);
+--------+
|ascii(2)|
+--------+
|      50|
+--------+
-- base64
SELECT base64('Feathers');
+-----------------+
|base64(Feathers)|
+-----------------+
|     RmVhdGhlcnM=|
+-----------------+
SELECT base64(x'537061726b2053514c');
+-----------------------------+
|base64(X'537061726B2053514C')|
+-----------------------------+
|                 U3BhcmsgU1FM|
+-----------------------------+
-- bit_length
SELECT bit_length('Feathers');
+---------------------+
|bit_length(Feathers)|
+---------------------+
|                   64|
+---------------------+
SELECT bit_length(x'537061726b2053514c');
+---------------------------------+
|bit_length(X'537061726B2053514C')|
+---------------------------------+
|                               72|
+---------------------------------+
-- btrim
SELECT btrim('    Feathers   ');
+----------------------+
|btrim(    Feathers   )|
+----------------------+
|              Feathers|
+----------------------+
SELECT btrim(encode('    Feathers   ', 'utf-8'));
+-------------------------------------+
|btrim(encode(    Feathers   , utf-8))|
+-------------------------------------+
|                             Feathers|
+-------------------------------------+
SELECT btrim('Feathers', 'Fe');
+---------------------+
|btrim(Alphabet, Al)|
+---------------------+
|               athers|
+---------------------+
SELECT btrim(encode('Feathers', 'utf-8'), encode('Al', 'utf-8'));
+---------------------------------------------------+
|btrim(encode(Feathers, utf-8), encode(Al, utf-8))|
+---------------------------------------------------+
|                                             athers|
+---------------------------------------------------+
-- char
SELECT char(65);
+--------+
|char(65)|
+--------+
|       A|
+--------+
-- char_length
SELECT char_length('Feathers ');
+-----------------------+
|char_length(Feathers )|
+-----------------------+
|                     9 |
+-----------------------+
SELECT char_length(x'537061726b2053514c');
+----------------------------------+
|char_length(X'537061726B2053514C')|
+----------------------------------+
|                                 9|
+----------------------------------+
SELECT CHAR_LENGTH('Feathers ');
+-----------------------+
|char_length(Feathers )|
+-----------------------+
|                     9|
+-----------------------+
SELECT CHARACTER_LENGTH('Feathers ');
+----------------------------+
|character_length(Feathers )|
+----------------------------+
|                          9|
+----------------------------+
-- character_length
SELECT character_length('Feathers ');
+----------------------------+
|character_length(Feathers )|
+----------------------------+
|                          9|
+----------------------------+
SELECT character_length(x'537061726b2053514c');
+---------------------------------------+
|character_length(X'537061726B2053514C')|
+---------------------------------------+
|                                      9|
+---------------------------------------+
SELECT CHAR_LENGTH('Feathers ');
+-----------------------+
|char_length(Feathers )|
+-----------------------+
|                     9|
+-----------------------+
SELECT CHARACTER_LENGTH('Feathers ');
+----------------------------+
|character_length(Feathers )|
+----------------------------+
|                          9|
+----------------------------+
-- chr
SELECT chr(65);
+-------+
|chr(65)|
+-------+
|      A|
+-------+
-- concat_ws
SELECT concat_ws(' ', 'Fea', 'thers');
+------------------------+
|concat_ws( , Fea, thers)|
+------------------------+
|               Feathers|
+------------------------+
SELECT concat_ws('s');
+------------+
|concat_ws(s)|
+------------+
|            |
+------------+
SELECT concat_ws('/', 'foo', null, 'bar');
+----------------------------+
|concat_ws(/, foo, NULL, bar)|
+----------------------------+
|                     foo/bar|
+----------------------------+
SELECT concat_ws(null, 'Fea', 'thers');
+---------------------------+
|concat_ws(NULL, Fea, thers)|
+---------------------------+
|                       NULL|
+---------------------------+
-- contains
SELECT contains('Feathers', 'Fea');
+--------------------------+
|contains(Feathers, Fea)|
+--------------------------+
|                      true|
+--------------------------+
SELECT contains('Feathers', 'SQL');
+--------------------------+
|contains(Feathers, SQL)|
+--------------------------+
|                     false|
+--------------------------+
SELECT contains('Feathers', null);
+-------------------------+
|contains(Feathers, NULL)|
+-------------------------+
|                     NULL|
+-------------------------+
SELECT contains(x'537061726b2053514c', x'537061726b');
+----------------------------------------------+
|contains(X'537061726B2053514C', X'537061726B')|
+----------------------------------------------+
|                                          true|
+----------------------------------------------+
-- decode
SELECT decode(encode('abc', 'utf-8'), 'utf-8');
+---------------------------------+
|decode(encode(abc, utf-8), utf-8)|
+---------------------------------+
|                              abc|
+---------------------------------+
SELECT decode(2, 1, 'Southlake', 2, 'San Francisco', 3, 'New Jersey', 4, 'Seattle', 'Non domestic');
+----------------------------------------------------------------------------------+
|decode(2, 1, Southlake, 2, San Francisco, 3, New Jersey, 4, Seattle, Non domestic)|
+----------------------------------------------------------------------------------+
|                                                                     San Francisco|
+----------------------------------------------------------------------------------+
SELECT decode(6, 1, 'Southlake', 2, 'San Francisco', 3, 'New Jersey', 4, 'Seattle', 'Non domestic');
+----------------------------------------------------------------------------------+
|decode(6, 1, Southlake, 2, San Francisco, 3, New Jersey, 4, Seattle, Non domestic)|
+----------------------------------------------------------------------------------+
|                                                                      Non domestic|
+----------------------------------------------------------------------------------+
SELECT decode(6, 1, 'Southlake', 2, 'San Francisco', 3, 'New Jersey', 4, 'Seattle');
+--------------------------------------------------------------------+
|decode(6, 1, Southlake, 2, San Francisco, 3, New Jersey, 4, Seattle)|
+--------------------------------------------------------------------+
|                                                                NULL|
+--------------------------------------------------------------------+
SELECT decode(null, 6, 'Fea', NULL, 'thers', 4, 'rock');
+-------------------------------------------+
|decode(NULL, 6, Fea, NULL, thers, 4, rock)|
+-------------------------------------------+
|                                      thers|
+-------------------------------------------+
-- elt
SELECT elt(1, 'scala', 'java');
+-------------------+
|elt(1, scala, java)|
+-------------------+
|              scala|
+-------------------+
SELECT elt(2, 'a', 1);
+------------+
|elt(2, a, 1)|
+------------+
|           1|
+------------+
-- encode
SELECT encode('abc', 'utf-8');
+------------------+
|encode(abc, utf-8)|
+------------------+
|        [61 62 63]|
+------------------+
-- endswith
SELECT endswith('Feathers', 'ers');
+------------------------+
|endswith(Feathers, ers)|
+------------------------+
|                    true|
+------------------------+
SELECT endswith('Feathers', 'SQL');
+--------------------------+
|endswith(Feathers, SQL)|
+--------------------------+
|                     false|
+--------------------------+
SELECT endswith('Feathers', null);
+-------------------------+
|endswith(Feathers, NULL)|
+-------------------------+
|                     NULL|
+-------------------------+
SELECT endswith(x'537061726b2053514c', x'537061726b');
+----------------------------------------------+
|endswith(X'537061726B2053514C', X'537061726B')|
+----------------------------------------------+
|                                         false|
+----------------------------------------------+
SELECT endswith(x'537061726b2053514c', x'53514c');
+------------------------------------------+
|endswith(X'537061726B2053514C', X'53514C')|
+------------------------------------------+
|                                      true|
+------------------------------------------+
-- find_in_set
SELECT find_in_set('ab','abc,b,ab,c,def');
+-------------------------------+
|find_in_set(ab, abc,b,ab,c,def)|
+-------------------------------+
|                              3|
+-------------------------------+
-- format_number
SELECT format_number(12332.123456, 4);
+------------------------------+
|format_number(12332.123456, 4)|
+------------------------------+
|                   12,332.1235|
+------------------------------+
SELECT format_number(12332.123456, '##################.###');
+---------------------------------------------------+
|format_number(12332.123456, ##################.###)|
+---------------------------------------------------+
|                                          12332.123|
+---------------------------------------------------+
-- format_string
SELECT format_string("Hello World %d %s", 100, "days");
+-------------------------------------------+
|format_string(Hello World %d %s, 100, days)|
+-------------------------------------------+
|                       Hello World 100 days|
+-------------------------------------------+
-- initcap
SELECT initcap('Feathers');
+------------------+
|initcap(Feathers)|
+------------------+
|         Feathers|
+------------------+
-- instr
SELECT instr('Feathers', 'ers');
+--------------------+
|instr(Feathers, ers)|
+--------------------+
|                   6|
+--------------------+
-- lcase
SELECT lcase('Feathers');
+---------------+
|lcase(Feathers)|
+---------------+
|       feathers|
+---------------+
-- left
SELECT left('Feathers', 3);
+------------------+
|left(Feathers, 3)|
+------------------+
|               Fea|
+------------------+
SELECT left(encode('Feathers', 'utf-8'), 3);
+---------------------------------+
|left(encode(Feathers, utf-8), 3)|
+---------------------------------+
|                       [RmVh]|
+---------------------------------+
-- len
SELECT len('Feathers ');
+---------------+
|len(Feathers )|
+---------------+
|             9|
+---------------+
SELECT len(x'537061726b2053514c');
+--------------------------+
|len(X'537061726B2053514C')|
+--------------------------+
|                         9|
+--------------------------+
SELECT CHAR_LENGTH('Feathers ');
+-----------------------+
|char_length(Feathers )|
+-----------------------+
|                     9|
+-----------------------+
SELECT CHARACTER_LENGTH('Feathers ');
+----------------------------+
|character_length(Feathers )|
+----------------------------+
|                          9|
+----------------------------+
-- length
SELECT length('Feathers ');
+------------------+
|length(Feathers )|
+------------------+
|                9|
+------------------+
SELECT length(x'537061726b2053514c');
+-----------------------------+
|length(X'537061726B2053514C')|
+-----------------------------+
|                            9|
+-----------------------------+
SELECT CHAR_LENGTH('Feathers ');
+-----------------------+
|char_length(Feathers )|
+-----------------------+
|                     9|
+-----------------------+
SELECT CHARACTER_LENGTH('Feathers ');
+----------------------------+
|character_length(Feathers )|
+----------------------------+
|                          9|
+----------------------------+
-- levenshtein
SELECT levenshtein('kitten', 'sitting');
+----------------------------+
|levenshtein(kitten, sitting)|
+----------------------------+
|                           3|
+----------------------------+
SELECT levenshtein('kitten', 'sitting', 2);
+-------------------------------+
|levenshtein(kitten, sitting, 2)|
+-------------------------------+
|                             -1|
+-------------------------------+
-- locate
SELECT locate('bar', 'foobarbar');
+-------------------------+
|locate(bar, foobarbar, 1)|
+-------------------------+
|                        4|
+-------------------------+
SELECT locate('bar', 'foobarbar', 5);
+-------------------------+
|locate(bar, foobarbar, 5)|
+-------------------------+
|                        7|
+-------------------------+
SELECT POSITION('bar' IN 'foobarbar');
+-------------------------+
|locate(bar, foobarbar, 1)|
+-------------------------+
|                        4|
+-------------------------+
-- lower
SELECT lower('Feathers');
+---------------+
|lower(Feathers)|
+---------------+
|       feathers|
+---------------+
-- lpad
SELECT lpad('hi', 5, '??');
+---------------+
|lpad(hi, 5, ??)|
+---------------+
|          ???hi|
+---------------+
SELECT lpad('hi', 1, '??');
+---------------+
|lpad(hi, 1, ??)|
+---------------+
|              h|
+---------------+
SELECT lpad('hi', 5);
+--------------+
|lpad(hi, 5,  )|
+--------------+
|            hi|
+--------------+
SELECT hex(lpad(unhex('aabb'), 5));
+--------------------------------+
|hex(lpad(unhex(aabb), 5, X'00'))|
+--------------------------------+
|                      000000AABB|
+--------------------------------+
SELECT hex(lpad(unhex('aabb'), 5, unhex('1122')));
+--------------------------------------+
|hex(lpad(unhex(aabb), 5, unhex(1122)))|
+--------------------------------------+
|                            112211AABB|
+--------------------------------------+
-- ltrim
SELECT ltrim('    Feathers   ');
+----------------------+
|ltrim(    Feathers   )|
+----------------------+
|           Feathers   |
+----------------------+
-- luhn_check
SELECT luhn_check('8112189876');
+----------------------+
|luhn_check(8112189876)|
+----------------------+
|                  true|
+----------------------+
SELECT luhn_check('79927398713');
+-----------------------+
|luhn_check(79927398713)|
+-----------------------+
|                   true|
+-----------------------+
SELECT luhn_check('79927398714');
+-----------------------+
|luhn_check(79927398714)|
+-----------------------+
|                  false|
+-----------------------+
-- mask
SELECT mask('abcd-EFGH-8765-4321');
+----------------------------------------+
|mask(abcd-EFGH-8765-4321, X, x, n, NULL)|
+----------------------------------------+
|                     xxxx-XXXX-nnnn-nnnn|
+----------------------------------------+
SELECT mask('abcd-EFGH-8765-4321', 'Q');
+----------------------------------------+
|mask(abcd-EFGH-8765-4321, Q, x, n, NULL)|
+----------------------------------------+
|                     xxxx-QQQQ-nnnn-nnnn|
+----------------------------------------+
SELECT mask('AbCD123-@$#', 'Q', 'q');
+--------------------------------+
|mask(AbCD123-@$#, Q, q, n, NULL)|
+--------------------------------+
|                     QqQQnnn-@$#|
+--------------------------------+
SELECT mask('AbCD123-@$#');
+--------------------------------+
|mask(AbCD123-@$#, X, x, n, NULL)|
+--------------------------------+
|                     XxXXnnn-@$#|
+--------------------------------+
SELECT mask('AbCD123-@$#', 'Q');
+--------------------------------+
|mask(AbCD123-@$#, Q, x, n, NULL)|
+--------------------------------+
|                     QxQQnnn-@$#|
+--------------------------------+
SELECT mask('AbCD123-@$#', 'Q', 'q');
+--------------------------------+
|mask(AbCD123-@$#, Q, q, n, NULL)|
+--------------------------------+
|                     QqQQnnn-@$#|
+--------------------------------+
SELECT mask('AbCD123-@$#', 'Q', 'q', 'd');
+--------------------------------+
|mask(AbCD123-@$#, Q, q, d, NULL)|
+--------------------------------+
|                     QqQQddd-@$#|
+--------------------------------+
SELECT mask('AbCD123-@$#', 'Q', 'q', 'd', 'o');
+-----------------------------+
|mask(AbCD123-@$#, Q, q, d, o)|
+-----------------------------+
|                  QqQQdddoooo|
+-----------------------------+
SELECT mask('AbCD123-@$#', NULL, 'q', 'd', 'o');
+--------------------------------+
|mask(AbCD123-@$#, NULL, q, d, o)|
+--------------------------------+
|                     AqCDdddoooo|
+--------------------------------+
SELECT mask('AbCD123-@$#', NULL, NULL, 'd', 'o');
+-----------------------------------+
|mask(AbCD123-@$#, NULL, NULL, d, o)|
+-----------------------------------+
|                        AbCDdddoooo|
+-----------------------------------+
SELECT mask('AbCD123-@$#', NULL, NULL, NULL, 'o');
+--------------------------------------+
|mask(AbCD123-@$#, NULL, NULL, NULL, o)|
+--------------------------------------+
|                           AbCD123oooo|
+--------------------------------------+
SELECT mask(NULL, NULL, NULL, NULL, 'o');
+-------------------------------+
|mask(NULL, NULL, NULL, NULL, o)|
+-------------------------------+
|                           NULL|
+-------------------------------+
SELECT mask(NULL);
+-------------------------+
|mask(NULL, X, x, n, NULL)|
+-------------------------+
|                     NULL|
+-------------------------+
SELECT mask('AbCD123-@$#', NULL, NULL, NULL, NULL);
+-----------------------------------------+
|mask(AbCD123-@$#, NULL, NULL, NULL, NULL)|
+-----------------------------------------+
|                              AbCD123-@$#|
+-----------------------------------------+
-- octet_length
SELECT octet_length('Feathers');
+-----------------------+
|octet_length(Feathers)|
+-----------------------+
|                      8|
+-----------------------+
SELECT octet_length(x'537061726b2053514c');
+-----------------------------------+
|octet_length(X'537061726B2053514C')|
+-----------------------------------+
|                                  9|
+-----------------------------------+
-- overlay
SELECT overlay('Feathers' PLACING '_' FROM 6);
+----------------------------+
|overlay(Feathers, _, 6, -1)|
+----------------------------+
|                   Feathe_ers|
+----------------------------+
SELECT overlay('Feathers' PLACING 'ures' FROM 5);
+-------------------------------+
|overlay(Feathers, ures, 5, -1)|
+-------------------------------+
|                     Features  |
+-------------------------------+
-- position
SELECT position('bar', 'foobarbar');
+---------------------------+
|position(bar, foobarbar, 1)|
+---------------------------+
|                          4|
+---------------------------+
SELECT position('bar', 'foobarbar', 5);
+---------------------------+
|position(bar, foobarbar, 5)|
+---------------------------+
|                          7|
+---------------------------+
SELECT POSITION('bar' IN 'foobarbar');
+-------------------------+
|locate(bar, foobarbar, 1)|
+-------------------------+
|                        4|
+-------------------------+
-- printf
SELECT printf("Hello World %d %s", 100, "days");
+------------------------------------+
|printf(Hello World %d %s, 100, days)|
+------------------------------------+
|                Hello World 100 days|
+------------------------------------+
-- regexp_count
SELECT regexp_count('Steven Jones and Stephen Smith are the best players', 'Ste(v|ph)en');
+------------------------------------------------------------------------------+
|regexp_count(Steven Jones and Stephen Smith are the best players, Ste(v|ph)en)|
+------------------------------------------------------------------------------+
|                                                                             2|
+------------------------------------------------------------------------------+
SELECT regexp_count('abcdefghijklmnopqrstuvwxyz', '[a-z]{3}');
+--------------------------------------------------+
|regexp_count(abcdefghijklmnopqrstuvwxyz, [a-z]{3})|
+--------------------------------------------------+
|                                                 8|
+--------------------------------------------------+
-- regexp_extract
SELECT regexp_extract('100-200', '(\\d+)-(\\d+)', 1);
+---------------------------------------+
|regexp_extract(100-200, (\d+)-(\d+), 1)|
+---------------------------------------+
|                                    100|
+---------------------------------------+
-- regexp_extract_all
SELECT regexp_extract_all('100-200, 300-400', '(\\d+)-(\\d+)', 1);
+----------------------------------------------------+
|regexp_extract_all(100-200, 300-400, (\d+)-(\d+), 1)|
+----------------------------------------------------+
|                                          [100, 300]|
+----------------------------------------------------+
-- regexp_instr
SELECT regexp_instr('user@opensearch.org', '@[^.]*');
+----------------------------------------------+
|regexp_instr(user@opensearch.org, @[^.]*, 0)|
+----------------------------------------------+
|                                             5|
+----------------------------------------------+
-- regexp_replace
SELECT regexp_replace('100-200', '(\\d+)', 'num');
+--------------------------------------+
|regexp_replace(100-200, (\d+), num, 1)|
+--------------------------------------+
|                               num-num|
+--------------------------------------+
-- regexp_substr
SELECT regexp_substr('Steven Jones and Stephen Smith are the best players', 'Ste(v|ph)en');
+-------------------------------------------------------------------------------+
|regexp_substr(Steven Jones and Stephen Smith are the best players, Ste(v|ph)en)|
+-------------------------------------------------------------------------------+
|                                                                         Steven|
+-------------------------------------------------------------------------------+
SELECT regexp_substr('Steven Jones and Stephen Smith are the best players', 'Jeck');
+------------------------------------------------------------------------+
|regexp_substr(Steven Jones and Stephen Smith are the best players, Jeck)|
+------------------------------------------------------------------------+
|                                                                    NULL|
+------------------------------------------------------------------------+
-- repeat
SELECT repeat('123', 2);
+--------------+
|repeat(123, 2)|
+--------------+
|        123123|
+--------------+
-- replace
SELECT replace('ABCabc', 'abc', 'DEF');
+-------------------------+
|replace(ABCabc, abc, DEF)|
+-------------------------+
|                   ABCDEF|
+-------------------------+
-- right
SELECT right('Feathers', 3);
+-------------------+
|right(Feathers, 3)|
+-------------------+
|                ers|
+-------------------+
-- rpad
SELECT rpad('hi', 5, '??');
+---------------+
|rpad(hi, 5, ??)|
+---------------+
|          hi???|
+---------------+
SELECT rpad('hi', 1, '??');
+---------------+
|rpad(hi, 1, ??)|
+---------------+
|              h|
+---------------+
SELECT rpad('hi', 5);
+--------------+
|rpad(hi, 5,  )|
+--------------+
|         hi   |
+--------------+
SELECT hex(rpad(unhex('aabb'), 5));
+--------------------------------+
|hex(rpad(unhex(aabb), 5, X'00'))|
+--------------------------------+
|                      AABB000000|
+--------------------------------+
SELECT hex(rpad(unhex('aabb'), 5, unhex('1122')));
+--------------------------------------+
|hex(rpad(unhex(aabb), 5, unhex(1122)))|
+--------------------------------------+
|                            AABB112211|
+--------------------------------------+
-- rtrim
SELECT rtrim('    Feathers   ');
+----------------------+
|rtrim(    Feathers   )|
+----------------------+
|              Feathers|
+----------------------+
-- sentences
SELECT sentences('Hi there! Good morning.');
+--------------------------------------+
|sentences(Hi there! Good morning., , )|
+--------------------------------------+
|                  [[Hi, there], [Go...|
+--------------------------------------+
-- soundex
SELECT soundex('Miller');
+---------------+
|soundex(Miller)|
+---------------+
|           M460|
+---------------+
-- space
SELECT concat(space(2), '1');
+-------------------+
|concat(space(2), 1)|
+-------------------+
|                  1|
+-------------------+
-- split
SELECT split('oneAtwoBthreeC', '[ABC]');
+--------------------------------+
|split(oneAtwoBthreeC, [ABC], -1)|
+--------------------------------+
|             [one, two, three, ]|
+--------------------------------+
SELECT split('oneAtwoBthreeC', '[ABC]', -1);
+--------------------------------+
|split(oneAtwoBthreeC, [ABC], -1)|
+--------------------------------+
|             [one, two, three, ]|
+--------------------------------+
SELECT split('oneAtwoBthreeC', '[ABC]', 2);
+-------------------------------+
|split(oneAtwoBthreeC, [ABC], 2)|
+-------------------------------+
|              [one, twoBthreeC]|
+-------------------------------+
-- split_part
SELECT split_part('11.12.13', '.', 3);
+--------------------------+
|split_part(11.12.13, ., 3)|
+--------------------------+
|                        13|
+--------------------------+
-- startswith
SELECT startswith('Feathers', 'Fea');
+----------------------------+
|startswith(Feathers, Fea)|
+----------------------------+
|                        true|
+----------------------------+
SELECT startswith('Feathers', 'SQL');
+--------------------------+
|startswith(Feathers, SQL)|
+--------------------------+
|                     false|
+--------------------------+
SELECT startswith('Feathers', null);
+---------------------------+
|startswith(Feathers, NULL)|
+---------------------------+
|                       NULL|
+---------------------------+
SELECT startswith(x'537061726b2053514c', x'537061726b');
+------------------------------------------------+
|startswith(X'537061726B2053514C', X'537061726B')|
+------------------------------------------------+
|                                            true|
+------------------------------------------------+
SELECT startswith(x'537061726b2053514c', x'53514c');
+--------------------------------------------+
|startswith(X'537061726B2053514C', X'53514C')|
+--------------------------------------------+
|                                       false|
+--------------------------------------------+
-- substr
SELECT substr('Feathers', 5);
+--------------------------------+
|substr(Feathers, 5, 2147483647)|
+--------------------------------+
|                           hers |
+--------------------------------+
SELECT substr('Feathers', -3);
+---------------------------------+
|substr(Feathers, -3, 2147483647)|
+---------------------------------+
|                              ers|
+---------------------------------+
SELECT substr('Feathers', 5, 1);
+-----------------------+
|substr(Feathers, 5, 1)|
+-----------------------+
|                      h|
+-----------------------+
SELECT substr('Feathers' FROM 5);
+-----------------------------------+
|substring(Feathers, 5, 2147483647)|
+-----------------------------------+
|                              hers |
+-----------------------------------+
SELECT substr('Feathers' FROM -3);
+------------------------------------+
|substring(Feathers, -3, 2147483647)|
+------------------------------------+
|                                 ers|
+------------------------------------+
SELECT substr('Feathers' FROM 5 FOR 1);
+--------------------------+
|substring(Feathers, 5, 1)|
+--------------------------+
|                         h|
+--------------------------+
-- substring
SELECT substring('Feathers', 5);
+-----------------------------------+
|substring(Feathers, 5, 2147483647)|
+-----------------------------------+
|                              hers |
+-----------------------------------+
SELECT substring('Feathers', -3);
+------------------------------------+
|substring(Feathers, -3, 2147483647)|
+------------------------------------+
|                                 ers|
+------------------------------------+
SELECT substring('Feathers', 5, 1);
+--------------------------+
|substring(Feathers, 5, 1)|
+--------------------------+
|                         h|
+--------------------------+
SELECT substring('Feathers' FROM 5);
+-----------------------------------+
|substring(Feathers, 5, 2147483647)|
+-----------------------------------+
|                              hers |
+-----------------------------------+
SELECT substring('Feathers' FROM -3);
+------------------------------------+
|substring(Feathers, -3, 2147483647)|
+------------------------------------+
|                                 ers|
+------------------------------------+
SELECT substring('Feathers' FROM 5 FOR 1);
+--------------------------+
|substring(Feathers, 5, 1)|
+--------------------------+
|                         h|
+--------------------------+
-- substring_index
SELECT substring_index('www.apache.org', '.', 2);
+-------------------------------------+
|substring_index(www.apache.org, ., 2)|
+-------------------------------------+
|                           www.apache|
+-------------------------------------+
-- to_binary
SELECT to_binary('abc', 'utf-8');
+---------------------+
|to_binary(abc, utf-8)|
+---------------------+
|           [61 62 63]|
+---------------------+
-- to_char
SELECT to_char(454, '999');
+-----------------+
|to_char(454, 999)|
+-----------------+
|              454|
+-----------------+
SELECT to_char(454.00, '000D00');
+-----------------------+
|to_char(454.00, 000D00)|
+-----------------------+
|                 454.00|
+-----------------------+
SELECT to_char(12454, '99G999');
+----------------------+
|to_char(12454, 99G999)|
+----------------------+
|                12,454|
+----------------------+
SELECT to_char(78.12, '$99.99');
+----------------------+
|to_char(78.12, $99.99)|
+----------------------+
|                $78.12|
+----------------------+
SELECT to_char(-12454.8, '99G999D9S');
+----------------------------+
|to_char(-12454.8, 99G999D9S)|
+----------------------------+
|                   12,454.8-|
+----------------------------+
-- to_number
SELECT to_number('454', '999');
+-------------------+
|to_number(454, 999)|
+-------------------+
|                454|
+-------------------+
SELECT to_number('454.00', '000.00');
+-------------------------+
|to_number(454.00, 000.00)|
+-------------------------+
|                   454.00|
+-------------------------+
SELECT to_number('12,454', '99,999');
+-------------------------+
|to_number(12,454, 99,999)|
+-------------------------+
|                    12454|
+-------------------------+
SELECT to_number('$78.12', '$99.99');
+-------------------------+
|to_number($78.12, $99.99)|
+-------------------------+
|                    78.12|
+-------------------------+
SELECT to_number('12,454.8-', '99,999.9S');
+-------------------------------+
|to_number(12,454.8-, 99,999.9S)|
+-------------------------------+
|                       -12454.8|
+-------------------------------+
-- to_varchar
SELECT to_varchar(454, '999');
+-----------------+
|to_char(454, 999)|
+-----------------+
|              454|
+-----------------+
SELECT to_varchar(454.00, '000D00');
+-----------------------+
|to_char(454.00, 000D00)|
+-----------------------+
|                 454.00|
+-----------------------+
SELECT to_varchar(12454, '99G999');
+----------------------+
|to_char(12454, 99G999)|
+----------------------+
|                12,454|
+----------------------+
SELECT to_varchar(78.12, '$99.99');
+----------------------+
|to_char(78.12, $99.99)|
+----------------------+
|                $78.12|
+----------------------+
SELECT to_varchar(-12454.8, '99G999D9S');
+----------------------------+
|to_char(-12454.8, 99G999D9S)|
+----------------------------+
|                   12,454.8-|
+----------------------------+
-- translate
SELECT translate('AaBbCc', 'abc', '123');
+---------------------------+
|translate(AaBbCc, abc, 123)|
+---------------------------+
|                     A1B2C3|
+---------------------------+
-- try_to_binary
SELECT try_to_binary('abc', 'utf-8');
+-------------------------+
|try_to_binary(abc, utf-8)|
+-------------------------+
|               [61 62 63]|
+-------------------------+
select try_to_binary('a!', 'base64');
+-------------------------+
|try_to_binary(a!, base64)|
+-------------------------+
|                     NULL|
+-------------------------+
select try_to_binary('abc', 'invalidFormat');
+---------------------------------+
|try_to_binary(abc, invalidFormat)|
+---------------------------------+
|                             NULL|
+---------------------------------+
-- try_to_number
SELECT try_to_number('454', '999');
+-----------------------+
|try_to_number(454, 999)|
+-----------------------+
|                    454|
+-----------------------+
SELECT try_to_number('454.00', '000.00');
+-----------------------------+
|try_to_number(454.00, 000.00)|
+-----------------------------+
|                       454.00|
+-----------------------------+
SELECT try_to_number('12,454', '99,999');
+-----------------------------+
|try_to_number(12,454, 99,999)|
+-----------------------------+
|                        12454|
+-----------------------------+
SELECT try_to_number('$78.12', '$99.99');
+-----------------------------+
|try_to_number($78.12, $99.99)|
+-----------------------------+
|                        78.12|
+-----------------------------+
SELECT try_to_number('12,454.8-', '99,999.9S');
+-----------------------------------+
|try_to_number(12,454.8-, 99,999.9S)|
+-----------------------------------+
|                           -12454.8|
+-----------------------------------+
-- ucase
SELECT ucase('Feathers');
+---------------+
|ucase(Feathers)|
+---------------+
|       FEATHERS|
+---------------+
-- unbase64
SELECT unbase64('U3BhcmsgU1FM');
+----------------------+
|unbase64(U3BhcmsgU1FM)|
+----------------------+
|  [53 70 61 72 6B 2...|
+----------------------+
-- upper
SELECT upper('Feathers');
+---------------+
|upper(Feathers)|
+---------------+
|       FEATHERS|
+---------------+
```

#### Date and time functions
<a name="supported-sql-date-time"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| add\_months(start\_date, num\_months) | Returns the date that is num\_months after start\_date. | 
| convert\_timezone([sourceTz, ]targetTz, sourceTs) | Converts the timestamp without time zone sourceTs from the sourceTz time zone to targetTz. | 
| curdate() | Returns the current date at the start of query evaluation. All calls of curdate within the same query return the same value. | 
| current\_date() | Returns the current date at the start of query evaluation. All calls of current\_date within the same query return the same value. | 
| current\_date | Returns the current date at the start of query evaluation. | 
| current\_timestamp() | Returns the current timestamp at the start of query evaluation. All calls of current\_timestamp within the same query return the same value. | 
| current\_timestamp | Returns the current timestamp at the start of query evaluation. | 
| current\_timezone() | Returns the current session local timezone. | 
| date\_add(start\_date, num\_days) | Returns the date that is num\_days after start\_date. | 
| date\_diff(endDate, startDate) | Returns the number of days from startDate to endDate. | 
| date\_format(timestamp, fmt) | Converts timestamp to a value of string in the format specified by the date format fmt. | 
| date\_from\_unix\_date(days) | Create date from the number of days since 1970-01-01. | 
| date\_part(field, source) | Extracts a part of the date/timestamp or interval source. | 
| date\_sub(start\_date, num\_days) | Returns the date that is num\_days before start\_date. | 
| date\_trunc(fmt, ts) | Returns timestamp ts truncated to the unit specified by the format model fmt. | 
| dateadd(start\_date, num\_days) | Returns the date that is num\_days after start\_date. | 
| datediff(endDate, startDate) | Returns the number of days from startDate to endDate. | 
| datepart(field, source) | Extracts a part of the date/timestamp or interval source. | 
| day(date) | Returns the day of month of the date/timestamp. | 
| dayofmonth(date) | Returns the day of month of the date/timestamp. | 
| dayofweek(date) | Returns the day of the week for date/timestamp (1 = Sunday, 2 = Monday, ..., 7 = Saturday). | 
| dayofyear(date) | Returns the day of year of the date/timestamp. | 
| extract(field FROM source) | Extracts a part of the date/timestamp or interval source. | 
| from\_unixtime(unix\_time[, fmt]) | Returns unix\_time in the specified fmt. | 
| from\_utc\_timestamp(timestamp, timezone) | Given a timestamp like '2017-07-14 02:40:00.0', interprets it as a time in UTC, and renders that time as a timestamp in the given time zone. For example, 'GMT\+1' would yield '2017-07-14 03:40:00.0'. | 
| hour(timestamp) | Returns the hour component of the string/timestamp. | 
| last\_day(date) | Returns the last day of the month which the date belongs to. | 
| localtimestamp() | Returns the current timestamp without time zone at the start of query evaluation. All calls of localtimestamp within the same query return the same value. | 
| localtimestamp | Returns the current local date-time at the session time zone at the start of query evaluation. | 
| make\_date(year, month, day) | Create date from year, month and day fields.  | 
| make\_dt\_interval([days[, hours[, mins[, secs]]]]) | Make DayTimeIntervalType duration from days, hours, mins and secs. | 
| make\_interval([years[, months[, weeks[, days[, hours[, mins[, secs]]]]]]]) | Make interval from years, months, weeks, days, hours, mins and secs. | 
| make\_timestamp(year, month, day, hour, min, sec[, timezone]) | Create timestamp from year, month, day, hour, min, sec and timezone fields.  | 
| make\_timestamp\_ltz(year, month, day, hour, min, sec[, timezone]) | Create the current timestamp with local time zone from year, month, day, hour, min, sec and timezone fields. | 
| make\_timestamp\_ntz(year, month, day, hour, min, sec) | Create local date-time from year, month, day, hour, min, sec fields.  | 
| make\_ym\_interval([years[, months]]) | Make year-month interval from years, months. | 
| minute(timestamp) | Returns the minute component of the string/timestamp. | 
| month(date) | Returns the month component of the date/timestamp. | 
| months\_between(timestamp1, timestamp2[, roundOff]) | If timestamp1 is later than timestamp2, then the result is positive. If timestamp1 and timestamp2 are on the same day of month, or both are the last day of month, time of day will be ignored. Otherwise, the difference is calculated based on 31 days per month, and rounded to 8 digits unless roundOff=false. | 
| next\_day(start\_date, day\_of\_week) | Returns the first date which is later than start\_date and named as indicated. The function returns NULL if at least one of the input parameters is NULL.  | 
| now() | Returns the current timestamp at the start of query evaluation. | 
| quarter(date) | Returns the quarter of the year for date, in the range 1 to 4. | 
| second(timestamp) | Returns the second component of the string/timestamp. | 
| session\_window(time\_column, gap\_duration) | Generates session window given a timestamp specifying column and gap duration. See 'Types of time windows' in Structured Streaming guide doc for detailed explanation and examples. | 
| timestamp\_micros(microseconds) | Creates timestamp from the number of microseconds since UTC epoch. | 
| timestamp\_millis(milliseconds) | Creates timestamp from the number of milliseconds since UTC epoch. | 
| timestamp\_seconds(seconds) | Creates timestamp from the number of seconds (can be fractional) since UTC epoch. | 
| to\_date(date\_str[, fmt]) | Parses the date\_str expression with the fmt expression to a date. Returns null with invalid input. By default, it follows casting rules to a date if the fmt is omitted. | 
| to\_timestamp(timestamp\_str[, fmt]) | Parses the timestamp\_str expression with the fmt expression to a timestamp. Returns null with invalid input. By default, it follows casting rules to a timestamp if the fmt is omitted.  | 
| to\_timestamp\_ltz(timestamp\_str[, fmt]) | Parses the timestamp\_str expression with the fmt expression to a timestamp with local time zone. Returns null with invalid input. By default, it follows casting rules to a timestamp if the fmt is omitted. | 
| to\_timestamp\_ntz(timestamp\_str[, fmt]) | Parses the timestamp\_str expression with the fmt expression to a timestamp without time zone. Returns null with invalid input. By default, it follows casting rules to a timestamp if the fmt is omitted. | 
| to\_unix\_timestamp(timeExp[, fmt]) | Returns the UNIX timestamp of the given time. | 
| to\_utc\_timestamp(timestamp, timezone) | Given a timestamp like '2017-07-14 02:40:00.0', interprets it as a time in the given time zone, and renders that time as a timestamp in UTC. For example, 'GMT\+1' would yield '2017-07-14 01:40:00.0'. | 
| trunc(date, fmt) | Returns date with the time portion of the day truncated to the unit specified by the format model fmt. | 
| try\_to\_timestamp(timestamp\_str[, fmt]) | Parses the timestamp\_str expression with the fmt expression to a timestamp.  | 
| unix\_date(date) | Returns the number of days since 1970-01-01. | 
| unix\_micros(timestamp) | Returns the number of microseconds since 1970-01-01 00:00:00 UTC. | 
| unix\_millis(timestamp) | Returns the number of milliseconds since 1970-01-01 00:00:00 UTC. Truncates higher levels of precision. | 
| unix\_seconds(timestamp) | Returns the number of seconds since 1970-01-01 00:00:00 UTC. Truncates higher levels of precision. | 
| unix\_timestamp([timeExp[, fmt]]) | Returns the UNIX timestamp of current or specified time. | 
| weekday(date) | Returns the day of the week for date/timestamp (0 = Monday, 1 = Tuesday, ..., 6 = Sunday). | 
| weekofyear(date) | Returns the week of the year of the given date. A week is considered to start on a Monday and week 1 is the first week with >3 days. | 
| window(time\_column, window\_duration[, slide\_duration[, start\_time]]) | Bucketize rows into one or more time windows given a timestamp specifying column. Window starts are inclusive but the window ends are exclusive, e.g. 12:05 will be in the window [12:05,12:10) but not in [12:00,12:05). Windows can support microsecond precision. Windows in the order of months are not supported. See 'Window Operations on Event Time' in Structured Streaming guide doc for detailed explanation and examples. | 
| window\_time(window\_column) | Extract the time value from time/session window column which can be used for event time value of window. The extracted time is (window.end - 1) which reflects the fact that the the aggregating windows have exclusive upper bound - [start, end) See 'Window Operations on Event Time' in Structured Streaming guide doc for detailed explanation and examples. | 
| year(date) | Returns the year component of the date/timestamp. | 

**Examples**

```
-- add_months
SELECT add_months('2016-08-31', 1);
+-------------------------+
|add_months(2016-08-31, 1)|
+-------------------------+
|               2016-09-30|
+-------------------------+
-- convert_timezone
SELECT convert_timezone('Europe/Brussels', 'America/Los_Angeles', timestamp_ntz'2021-12-06 00:00:00');
+-------------------------------------------------------------------------------------------+
|convert_timezone(Europe/Brussels, America/Los_Angeles, TIMESTAMP_NTZ '2021-12-06 00:00:00')|
+-------------------------------------------------------------------------------------------+
|                                                                        2021-12-05 15:00:00|
+-------------------------------------------------------------------------------------------+
SELECT convert_timezone('Europe/Brussels', timestamp_ntz'2021-12-05 15:00:00');
+------------------------------------------------------------------------------------------+
|convert_timezone(current_timezone(), Europe/Brussels, TIMESTAMP_NTZ '2021-12-05 15:00:00')|
+------------------------------------------------------------------------------------------+
|                                                                       2021-12-05 07:00:00|
+------------------------------------------------------------------------------------------+
-- curdate
SELECT curdate();
+--------------+
|current_date()|
+--------------+
|    2024-02-24|
+--------------+
-- current_date
SELECT current_date();
+--------------+
|current_date()|
+--------------+
|    2024-02-24|
+--------------+
SELECT current_date;
+--------------+
|current_date()|
+--------------+
|    2024-02-24|
+--------------+
-- current_timestamp
SELECT current_timestamp();
+--------------------+
| current_timestamp()|
+--------------------+
|2024-02-24 16:36:...|
+--------------------+
SELECT current_timestamp;
+--------------------+
| current_timestamp()|
+--------------------+
|2024-02-24 16:36:...|
+--------------------+
-- current_timezone
SELECT current_timezone();
+------------------+
|current_timezone()|
+------------------+
|        Asia/Seoul|
+------------------+
-- date_add
SELECT date_add('2016-07-30', 1);
+-----------------------+
|date_add(2016-07-30, 1)|
+-----------------------+
|             2016-07-31|
+-----------------------+
-- date_diff
SELECT date_diff('2009-07-31', '2009-07-30');
+---------------------------------+
|date_diff(2009-07-31, 2009-07-30)|
+---------------------------------+
|                                1|
+---------------------------------+
SELECT date_diff('2009-07-30', '2009-07-31');
+---------------------------------+
|date_diff(2009-07-30, 2009-07-31)|
+---------------------------------+
|                               -1|
+---------------------------------+
-- date_format
SELECT date_format('2016-04-08', 'y');
+--------------------------+
|date_format(2016-04-08, y)|
+--------------------------+
|                      2016|
+--------------------------+
-- date_from_unix_date
SELECT date_from_unix_date(1);
+----------------------+
|date_from_unix_date(1)|
+----------------------+
|            1970-01-02|
+----------------------+
-- date_part
SELECT date_part('YEAR', TIMESTAMP '2019-08-12 01:00:00.123456');
+-------------------------------------------------------+
|date_part(YEAR, TIMESTAMP '2019-08-12 01:00:00.123456')|
+-------------------------------------------------------+
|                                                   2019|
+-------------------------------------------------------+
SELECT date_part('week', timestamp'2019-08-12 01:00:00.123456');
+-------------------------------------------------------+
|date_part(week, TIMESTAMP '2019-08-12 01:00:00.123456')|
+-------------------------------------------------------+
|                                                     33|
+-------------------------------------------------------+
SELECT date_part('doy', DATE'2019-08-12');
+---------------------------------+
|date_part(doy, DATE '2019-08-12')|
+---------------------------------+
|                              224|
+---------------------------------+
SELECT date_part('SECONDS', timestamp'2019-10-01 00:00:01.000001');
+----------------------------------------------------------+
|date_part(SECONDS, TIMESTAMP '2019-10-01 00:00:01.000001')|
+----------------------------------------------------------+
|                                                  1.000001|
+----------------------------------------------------------+
SELECT date_part('days', interval 5 days 3 hours 7 minutes);
+-------------------------------------------------+
|date_part(days, INTERVAL '5 03:07' DAY TO MINUTE)|
+-------------------------------------------------+
|                                                5|
+-------------------------------------------------+
SELECT date_part('seconds', interval 5 hours 30 seconds 1 milliseconds 1 microseconds);
+-------------------------------------------------------------+
|date_part(seconds, INTERVAL '05:00:30.001001' HOUR TO SECOND)|
+-------------------------------------------------------------+
|                                                    30.001001|
+-------------------------------------------------------------+
SELECT date_part('MONTH', INTERVAL '2021-11' YEAR TO MONTH);
+--------------------------------------------------+
|date_part(MONTH, INTERVAL '2021-11' YEAR TO MONTH)|
+--------------------------------------------------+
|                                                11|
+--------------------------------------------------+
SELECT date_part('MINUTE', INTERVAL '123 23:55:59.002001' DAY TO SECOND);
+---------------------------------------------------------------+
|date_part(MINUTE, INTERVAL '123 23:55:59.002001' DAY TO SECOND)|
+---------------------------------------------------------------+
|                                                             55|
+---------------------------------------------------------------+
-- date_sub
SELECT date_sub('2016-07-30', 1);
+-----------------------+
|date_sub(2016-07-30, 1)|
+-----------------------+
|             2016-07-29|
+-----------------------+
-- date_trunc
SELECT date_trunc('YEAR', '2015-03-05T09:32:05.359');
+-----------------------------------------+
|date_trunc(YEAR, 2015-03-05T09:32:05.359)|
+-----------------------------------------+
|                      2015-01-01 00:00:00|
+-----------------------------------------+
SELECT date_trunc('MM', '2015-03-05T09:32:05.359');
+---------------------------------------+
|date_trunc(MM, 2015-03-05T09:32:05.359)|
+---------------------------------------+
|                    2015-03-01 00:00:00|
+---------------------------------------+
SELECT date_trunc('DD', '2015-03-05T09:32:05.359');
+---------------------------------------+
|date_trunc(DD, 2015-03-05T09:32:05.359)|
+---------------------------------------+
|                    2015-03-05 00:00:00|
+---------------------------------------+
SELECT date_trunc('HOUR', '2015-03-05T09:32:05.359');
+-----------------------------------------+
|date_trunc(HOUR, 2015-03-05T09:32:05.359)|
+-----------------------------------------+
|                      2015-03-05 09:00:00|
+-----------------------------------------+
SELECT date_trunc('MILLISECOND', '2015-03-05T09:32:05.123456');
+---------------------------------------------------+
|date_trunc(MILLISECOND, 2015-03-05T09:32:05.123456)|
+---------------------------------------------------+
|                               2015-03-05 09:32:...|
+---------------------------------------------------+
-- dateadd
SELECT dateadd('2016-07-30', 1);
+-----------------------+
|date_add(2016-07-30, 1)|
+-----------------------+
|             2016-07-31|
+-----------------------+
-- datediff
SELECT datediff('2009-07-31', '2009-07-30');
+--------------------------------+
|datediff(2009-07-31, 2009-07-30)|
+--------------------------------+
|                               1|
+--------------------------------+
SELECT datediff('2009-07-30', '2009-07-31');
+--------------------------------+
|datediff(2009-07-30, 2009-07-31)|
+--------------------------------+
|                              -1|
+--------------------------------+
-- datepart
SELECT datepart('YEAR', TIMESTAMP '2019-08-12 01:00:00.123456');
+----------------------------------------------------------+
|datepart(YEAR FROM TIMESTAMP '2019-08-12 01:00:00.123456')|
+----------------------------------------------------------+
|                                                      2019|
+----------------------------------------------------------+
SELECT datepart('week', timestamp'2019-08-12 01:00:00.123456');
+----------------------------------------------------------+
|datepart(week FROM TIMESTAMP '2019-08-12 01:00:00.123456')|
+----------------------------------------------------------+
|                                                        33|
+----------------------------------------------------------+
SELECT datepart('doy', DATE'2019-08-12');
+------------------------------------+
|datepart(doy FROM DATE '2019-08-12')|
+------------------------------------+
|                                 224|
+------------------------------------+
SELECT datepart('SECONDS', timestamp'2019-10-01 00:00:01.000001');
+-------------------------------------------------------------+
|datepart(SECONDS FROM TIMESTAMP '2019-10-01 00:00:01.000001')|
+-------------------------------------------------------------+
|                                                     1.000001|
+-------------------------------------------------------------+
SELECT datepart('days', interval 5 days 3 hours 7 minutes);
+----------------------------------------------------+
|datepart(days FROM INTERVAL '5 03:07' DAY TO MINUTE)|
+----------------------------------------------------+
|                                                   5|
+----------------------------------------------------+
SELECT datepart('seconds', interval 5 hours 30 seconds 1 milliseconds 1 microseconds);
+----------------------------------------------------------------+
|datepart(seconds FROM INTERVAL '05:00:30.001001' HOUR TO SECOND)|
+----------------------------------------------------------------+
|                                                       30.001001|
+----------------------------------------------------------------+
SELECT datepart('MONTH', INTERVAL '2021-11' YEAR TO MONTH);
+-----------------------------------------------------+
|datepart(MONTH FROM INTERVAL '2021-11' YEAR TO MONTH)|
+-----------------------------------------------------+
|                                                   11|
+-----------------------------------------------------+
SELECT datepart('MINUTE', INTERVAL '123 23:55:59.002001' DAY TO SECOND);
+------------------------------------------------------------------+
|datepart(MINUTE FROM INTERVAL '123 23:55:59.002001' DAY TO SECOND)|
+------------------------------------------------------------------+
|                                                                55|
+------------------------------------------------------------------+
-- day
SELECT day('2009-07-30');
+---------------+
|day(2009-07-30)|
+---------------+
|             30|
+---------------+
-- dayofmonth
SELECT dayofmonth('2009-07-30');
+----------------------+
|dayofmonth(2009-07-30)|
+----------------------+
|                    30|
+----------------------+
-- dayofweek
SELECT dayofweek('2009-07-30');
+---------------------+
|dayofweek(2009-07-30)|
+---------------------+
|                    5|
+---------------------+
-- dayofyear
SELECT dayofyear('2016-04-09');
+---------------------+
|dayofyear(2016-04-09)|
+---------------------+
|                  100|
+---------------------+
-- extract
SELECT extract(YEAR FROM TIMESTAMP '2019-08-12 01:00:00.123456');
+---------------------------------------------------------+
|extract(YEAR FROM TIMESTAMP '2019-08-12 01:00:00.123456')|
+---------------------------------------------------------+
|                                                     2019|
+---------------------------------------------------------+
SELECT extract(week FROM timestamp'2019-08-12 01:00:00.123456');
+---------------------------------------------------------+
|extract(week FROM TIMESTAMP '2019-08-12 01:00:00.123456')|
+---------------------------------------------------------+
|                                                       33|
+---------------------------------------------------------+
SELECT extract(doy FROM DATE'2019-08-12');
+-----------------------------------+
|extract(doy FROM DATE '2019-08-12')|
+-----------------------------------+
|                                224|
+-----------------------------------+
SELECT extract(SECONDS FROM timestamp'2019-10-01 00:00:01.000001');
+------------------------------------------------------------+
|extract(SECONDS FROM TIMESTAMP '2019-10-01 00:00:01.000001')|
+------------------------------------------------------------+
|                                                    1.000001|
+------------------------------------------------------------+
SELECT extract(days FROM interval 5 days 3 hours 7 minutes);
+---------------------------------------------------+
|extract(days FROM INTERVAL '5 03:07' DAY TO MINUTE)|
+---------------------------------------------------+
|                                                  5|
+---------------------------------------------------+
SELECT extract(seconds FROM interval 5 hours 30 seconds 1 milliseconds 1 microseconds);
+---------------------------------------------------------------+
|extract(seconds FROM INTERVAL '05:00:30.001001' HOUR TO SECOND)|
+---------------------------------------------------------------+
|                                                      30.001001|
+---------------------------------------------------------------+
SELECT extract(MONTH FROM INTERVAL '2021-11' YEAR TO MONTH);
+----------------------------------------------------+
|extract(MONTH FROM INTERVAL '2021-11' YEAR TO MONTH)|
+----------------------------------------------------+
|                                                  11|
+----------------------------------------------------+
SELECT extract(MINUTE FROM INTERVAL '123 23:55:59.002001' DAY TO SECOND);
+-----------------------------------------------------------------+
|extract(MINUTE FROM INTERVAL '123 23:55:59.002001' DAY TO SECOND)|
+-----------------------------------------------------------------+
|                                                               55|
+-----------------------------------------------------------------+
-- from_unixtime
SELECT from_unixtime(0, 'yyyy-MM-dd HH:mm:ss');
+-------------------------------------+
|from_unixtime(0, yyyy-MM-dd HH:mm:ss)|
+-------------------------------------+
|                  1970-01-01 09:00:00|
+-------------------------------------+
SELECT from_unixtime(0);
+-------------------------------------+
|from_unixtime(0, yyyy-MM-dd HH:mm:ss)|
+-------------------------------------+
|                  1970-01-01 09:00:00|
+-------------------------------------+
-- from_utc_timestamp
SELECT from_utc_timestamp('2016-08-31', 'Asia/Seoul');
+------------------------------------------+
|from_utc_timestamp(2016-08-31, Asia/Seoul)|
+------------------------------------------+
|                       2016-08-31 09:00:00|
+------------------------------------------+
-- hour
SELECT hour('2009-07-30 12:58:59');
+-------------------------+
|hour(2009-07-30 12:58:59)|
+-------------------------+
|                       12|
+-------------------------+
-- last_day
SELECT last_day('2009-01-12');
+--------------------+
|last_day(2009-01-12)|
+--------------------+
|          2009-01-31|
+--------------------+
-- localtimestamp
SELECT localtimestamp();
+--------------------+
|    localtimestamp()|
+--------------------+
|2024-02-24 16:36:...|
+--------------------+
-- make_date
SELECT make_date(2013, 7, 15);
+----------------------+
|make_date(2013, 7, 15)|
+----------------------+
|            2013-07-15|
+----------------------+
SELECT make_date(2019, 7, NULL);
+------------------------+
|make_date(2019, 7, NULL)|
+------------------------+
|                    NULL|
+------------------------+
-- make_dt_interval
SELECT make_dt_interval(1, 12, 30, 01.001001);
+-------------------------------------+
|make_dt_interval(1, 12, 30, 1.001001)|
+-------------------------------------+
|                 INTERVAL '1 12:30...|
+-------------------------------------+
SELECT make_dt_interval(2);
+-----------------------------------+
|make_dt_interval(2, 0, 0, 0.000000)|
+-----------------------------------+
|               INTERVAL '2 00:00...|
+-----------------------------------+
SELECT make_dt_interval(100, null, 3);
+----------------------------------------+
|make_dt_interval(100, NULL, 3, 0.000000)|
+----------------------------------------+
|                                    NULL|
+----------------------------------------+
-- make_interval
SELECT make_interval(100, 11, 1, 1, 12, 30, 01.001001);
+----------------------------------------------+
|make_interval(100, 11, 1, 1, 12, 30, 1.001001)|
+----------------------------------------------+
|                          100 years 11 mont...|
+----------------------------------------------+
SELECT make_interval(100, null, 3);
+----------------------------------------------+
|make_interval(100, NULL, 3, 0, 0, 0, 0.000000)|
+----------------------------------------------+
|                                          NULL|
+----------------------------------------------+
SELECT make_interval(0, 1, 0, 1, 0, 0, 100.000001);
+-------------------------------------------+
|make_interval(0, 1, 0, 1, 0, 0, 100.000001)|
+-------------------------------------------+
|                       1 months 1 days 1...|
+-------------------------------------------+
-- make_timestamp
SELECT make_timestamp(2014, 12, 28, 6, 30, 45.887);
+-------------------------------------------+
|make_timestamp(2014, 12, 28, 6, 30, 45.887)|
+-------------------------------------------+
|                       2014-12-28 06:30:...|
+-------------------------------------------+
SELECT make_timestamp(2014, 12, 28, 6, 30, 45.887, 'CET');
+------------------------------------------------+
|make_timestamp(2014, 12, 28, 6, 30, 45.887, CET)|
+------------------------------------------------+
|                            2014-12-28 14:30:...|
+------------------------------------------------+
SELECT make_timestamp(2019, 6, 30, 23, 59, 60);
+---------------------------------------+
|make_timestamp(2019, 6, 30, 23, 59, 60)|
+---------------------------------------+
|                    2019-07-01 00:00:00|
+---------------------------------------+
SELECT make_timestamp(2019, 6, 30, 23, 59, 1);
+--------------------------------------+
|make_timestamp(2019, 6, 30, 23, 59, 1)|
+--------------------------------------+
|                   2019-06-30 23:59:01|
+--------------------------------------+
SELECT make_timestamp(null, 7, 22, 15, 30, 0);
+--------------------------------------+
|make_timestamp(NULL, 7, 22, 15, 30, 0)|
+--------------------------------------+
|                                  NULL|
+--------------------------------------+
-- make_timestamp_ltz
SELECT make_timestamp_ltz(2014, 12, 28, 6, 30, 45.887);
+-----------------------------------------------+
|make_timestamp_ltz(2014, 12, 28, 6, 30, 45.887)|
+-----------------------------------------------+
|                           2014-12-28 06:30:...|
+-----------------------------------------------+
SELECT make_timestamp_ltz(2014, 12, 28, 6, 30, 45.887, 'CET');
+----------------------------------------------------+
|make_timestamp_ltz(2014, 12, 28, 6, 30, 45.887, CET)|
+----------------------------------------------------+
|                                2014-12-28 14:30:...|
+----------------------------------------------------+
SELECT make_timestamp_ltz(2019, 6, 30, 23, 59, 60);
+-------------------------------------------+
|make_timestamp_ltz(2019, 6, 30, 23, 59, 60)|
+-------------------------------------------+
|                        2019-07-01 00:00:00|
+-------------------------------------------+
SELECT make_timestamp_ltz(null, 7, 22, 15, 30, 0);
+------------------------------------------+
|make_timestamp_ltz(NULL, 7, 22, 15, 30, 0)|
+------------------------------------------+
|                                      NULL|
+------------------------------------------+
-- make_timestamp_ntz
SELECT make_timestamp_ntz(2014, 12, 28, 6, 30, 45.887);
+-----------------------------------------------+
|make_timestamp_ntz(2014, 12, 28, 6, 30, 45.887)|
+-----------------------------------------------+
|                           2014-12-28 06:30:...|
+-----------------------------------------------+
SELECT make_timestamp_ntz(2019, 6, 30, 23, 59, 60);
+-------------------------------------------+
|make_timestamp_ntz(2019, 6, 30, 23, 59, 60)|
+-------------------------------------------+
|                        2019-07-01 00:00:00|
+-------------------------------------------+
SELECT make_timestamp_ntz(null, 7, 22, 15, 30, 0);
+------------------------------------------+
|make_timestamp_ntz(NULL, 7, 22, 15, 30, 0)|
+------------------------------------------+
|                                      NULL|
+------------------------------------------+
-- make_ym_interval
SELECT make_ym_interval(1, 2);
+----------------------+
|make_ym_interval(1, 2)|
+----------------------+
|  INTERVAL '1-2' YE...|
+----------------------+
SELECT make_ym_interval(1, 0);
+----------------------+
|make_ym_interval(1, 0)|
+----------------------+
|  INTERVAL '1-0' YE...|
+----------------------+
SELECT make_ym_interval(-1, 1);
+-----------------------+
|make_ym_interval(-1, 1)|
+-----------------------+
|   INTERVAL '-0-11' ...|
+-----------------------+
SELECT make_ym_interval(2);
+----------------------+
|make_ym_interval(2, 0)|
+----------------------+
|  INTERVAL '2-0' YE...|
+----------------------+
-- minute
SELECT minute('2009-07-30 12:58:59');
+---------------------------+
|minute(2009-07-30 12:58:59)|
+---------------------------+
|                         58|
+---------------------------+
-- month
SELECT month('2016-07-30');
+-----------------+
|month(2016-07-30)|
+-----------------+
|                7|
+-----------------+
-- months_between
SELECT months_between('1997-02-28 10:30:00', '1996-10-30');
+-----------------------------------------------------+
|months_between(1997-02-28 10:30:00, 1996-10-30, true)|
+-----------------------------------------------------+
|                                           3.94959677|
+-----------------------------------------------------+
SELECT months_between('1997-02-28 10:30:00', '1996-10-30', false);
+------------------------------------------------------+
|months_between(1997-02-28 10:30:00, 1996-10-30, false)|
+------------------------------------------------------+
|                                    3.9495967741935485|
+------------------------------------------------------+
-- next_day
SELECT next_day('2015-01-14', 'TU');
+------------------------+
|next_day(2015-01-14, TU)|
+------------------------+
|              2015-01-20|
+------------------------+
-- now
SELECT now();
+--------------------+
|               now()|
+--------------------+
|2024-02-24 16:36:...|
+--------------------+
-- quarter
SELECT quarter('2016-08-31');
+-------------------+
|quarter(2016-08-31)|
+-------------------+
|                  3|
+-------------------+
-- second
SELECT second('2009-07-30 12:58:59');
+---------------------------+
|second(2009-07-30 12:58:59)|
+---------------------------+
|                         59|
+---------------------------+
-- session_window
SELECT a, session_window.start, session_window.end, count(*) as cnt FROM VALUES ('A1', '2021-01-01 00:00:00'), ('A1', '2021-01-01 00:04:30'), ('A1', '2021-01-01 00:10:00'), ('A2', '2021-01-01 00:01:00') AS tab(a, b) GROUP by a, session_window(b, '5 minutes') ORDER BY a, start;
+---+-------------------+-------------------+---+
|  a|              start|                end|cnt|
+---+-------------------+-------------------+---+
| A1|2021-01-01 00:00:00|2021-01-01 00:09:30|  2|
| A1|2021-01-01 00:10:00|2021-01-01 00:15:00|  1|
| A2|2021-01-01 00:01:00|2021-01-01 00:06:00|  1|
+---+-------------------+-------------------+---+
SELECT a, session_window.start, session_window.end, count(*) as cnt FROM VALUES ('A1', '2021-01-01 00:00:00'), ('A1', '2021-01-01 00:04:30'), ('A1', '2021-01-01 00:10:00'), ('A2', '2021-01-01 00:01:00'), ('A2', '2021-01-01 00:04:30') AS tab(a, b) GROUP by a, session_window(b, CASE WHEN a = 'A1' THEN '5 minutes' WHEN a = 'A2' THEN '1 minute' ELSE '10 minutes' END) ORDER BY a, start;
+---+-------------------+-------------------+---+
|  a|              start|                end|cnt|
+---+-------------------+-------------------+---+
| A1|2021-01-01 00:00:00|2021-01-01 00:09:30|  2|
| A1|2021-01-01 00:10:00|2021-01-01 00:15:00|  1|
| A2|2021-01-01 00:01:00|2021-01-01 00:02:00|  1|
| A2|2021-01-01 00:04:30|2021-01-01 00:05:30|  1|
+---+-------------------+-------------------+---+
-- timestamp_micros
SELECT timestamp_micros(1230219000123123);
+----------------------------------+
|timestamp_micros(1230219000123123)|
+----------------------------------+
|              2008-12-26 00:30:...|
+----------------------------------+
-- timestamp_millis
SELECT timestamp_millis(1230219000123);
+-------------------------------+
|timestamp_millis(1230219000123)|
+-------------------------------+
|           2008-12-26 00:30:...|
+-------------------------------+
-- timestamp_seconds
SELECT timestamp_seconds(1230219000);
+-----------------------------+
|timestamp_seconds(1230219000)|
+-----------------------------+
|          2008-12-26 00:30:00|
+-----------------------------+
SELECT timestamp_seconds(1230219000.123);
+---------------------------------+
|timestamp_seconds(1230219000.123)|
+---------------------------------+
|             2008-12-26 00:30:...|
+---------------------------------+
-- to_date
SELECT to_date('2009-07-30 04:17:52');
+----------------------------+
|to_date(2009-07-30 04:17:52)|
+----------------------------+
|                  2009-07-30|
+----------------------------+
SELECT to_date('2016-12-31', 'yyyy-MM-dd');
+-------------------------------+
|to_date(2016-12-31, yyyy-MM-dd)|
+-------------------------------+
|                     2016-12-31|
+-------------------------------+
-- to_timestamp
SELECT to_timestamp('2016-12-31 00:12:00');
+---------------------------------+
|to_timestamp(2016-12-31 00:12:00)|
+---------------------------------+
|              2016-12-31 00:12:00|
+---------------------------------+
SELECT to_timestamp('2016-12-31', 'yyyy-MM-dd');
+------------------------------------+
|to_timestamp(2016-12-31, yyyy-MM-dd)|
+------------------------------------+
|                 2016-12-31 00:00:00|
+------------------------------------+
-- to_timestamp_ltz
SELECT to_timestamp_ltz('2016-12-31 00:12:00');
+-------------------------------------+
|to_timestamp_ltz(2016-12-31 00:12:00)|
+-------------------------------------+
|                  2016-12-31 00:12:00|
+-------------------------------------+
SELECT to_timestamp_ltz('2016-12-31', 'yyyy-MM-dd');
+----------------------------------------+
|to_timestamp_ltz(2016-12-31, yyyy-MM-dd)|
+----------------------------------------+
|                     2016-12-31 00:00:00|
+----------------------------------------+
-- to_timestamp_ntz
SELECT to_timestamp_ntz('2016-12-31 00:12:00');
+-------------------------------------+
|to_timestamp_ntz(2016-12-31 00:12:00)|
+-------------------------------------+
|                  2016-12-31 00:12:00|
+-------------------------------------+
SELECT to_timestamp_ntz('2016-12-31', 'yyyy-MM-dd');
+----------------------------------------+
|to_timestamp_ntz(2016-12-31, yyyy-MM-dd)|
+----------------------------------------+
|                     2016-12-31 00:00:00|
+----------------------------------------+
-- to_unix_timestamp
SELECT to_unix_timestamp('2016-04-08', 'yyyy-MM-dd');
+-----------------------------------------+
|to_unix_timestamp(2016-04-08, yyyy-MM-dd)|
+-----------------------------------------+
|                               1460041200|
+-----------------------------------------+
-- to_utc_timestamp
SELECT to_utc_timestamp('2016-08-31', 'Asia/Seoul');
+----------------------------------------+
|to_utc_timestamp(2016-08-31, Asia/Seoul)|
+----------------------------------------+
|                     2016-08-30 15:00:00|
+----------------------------------------+
-- trunc
SELECT trunc('2019-08-04', 'week');
+-----------------------+
|trunc(2019-08-04, week)|
+-----------------------+
|             2019-07-29|
+-----------------------+
SELECT trunc('2019-08-04', 'quarter');
+--------------------------+
|trunc(2019-08-04, quarter)|
+--------------------------+
|                2019-07-01|
+--------------------------+
SELECT trunc('2009-02-12', 'MM');
+---------------------+
|trunc(2009-02-12, MM)|
+---------------------+
|           2009-02-01|
+---------------------+
SELECT trunc('2015-10-27', 'YEAR');
+-----------------------+
|trunc(2015-10-27, YEAR)|
+-----------------------+
|             2015-01-01|
+-----------------------+
-- try_to_timestamp
SELECT try_to_timestamp('2016-12-31 00:12:00');
+-------------------------------------+
|try_to_timestamp(2016-12-31 00:12:00)|
+-------------------------------------+
|                  2016-12-31 00:12:00|
+-------------------------------------+
SELECT try_to_timestamp('2016-12-31', 'yyyy-MM-dd');
+----------------------------------------+
|try_to_timestamp(2016-12-31, yyyy-MM-dd)|
+----------------------------------------+
|                     2016-12-31 00:00:00|
+----------------------------------------+
SELECT try_to_timestamp('foo', 'yyyy-MM-dd');
+---------------------------------+
|try_to_timestamp(foo, yyyy-MM-dd)|
+---------------------------------+
|                             NULL|
+---------------------------------+
-- unix_date
SELECT unix_date(DATE("1970-01-02"));
+---------------------+
|unix_date(1970-01-02)|
+---------------------+
|                    1|
+---------------------+
-- unix_micros
SELECT unix_micros(TIMESTAMP('1970-01-01 00:00:01Z'));
+---------------------------------+
|unix_micros(1970-01-01 00:00:01Z)|
+---------------------------------+
|                          1000000|
+---------------------------------+
-- unix_millis
SELECT unix_millis(TIMESTAMP('1970-01-01 00:00:01Z'));
+---------------------------------+
|unix_millis(1970-01-01 00:00:01Z)|
+---------------------------------+
|                             1000|
+---------------------------------+
-- unix_seconds
SELECT unix_seconds(TIMESTAMP('1970-01-01 00:00:01Z'));
+----------------------------------+
|unix_seconds(1970-01-01 00:00:01Z)|
+----------------------------------+
|                                 1|
+----------------------------------+
-- unix_timestamp
SELECT unix_timestamp();
+--------------------------------------------------------+
|unix_timestamp(current_timestamp(), yyyy-MM-dd HH:mm:ss)|
+--------------------------------------------------------+
|                                              1708760216|
+--------------------------------------------------------+
SELECT unix_timestamp('2016-04-08', 'yyyy-MM-dd');
+--------------------------------------+
|unix_timestamp(2016-04-08, yyyy-MM-dd)|
+--------------------------------------+
|                            1460041200|
+--------------------------------------+
-- weekday
SELECT weekday('2009-07-30');
+-------------------+
|weekday(2009-07-30)|
+-------------------+
|                  3|
+-------------------+
-- weekofyear
SELECT weekofyear('2008-02-20');
+----------------------+
|weekofyear(2008-02-20)|
+----------------------+
|                     8|
+----------------------+
-- window
SELECT a, window.start, window.end, count(*) as cnt FROM VALUES ('A1', '2021-01-01 00:00:00'), ('A1', '2021-01-01 00:04:30'), ('A1', '2021-01-01 00:06:00'), ('A2', '2021-01-01 00:01:00') AS tab(a, b) GROUP by a, window(b, '5 minutes') ORDER BY a, start;
+---+-------------------+-------------------+---+
|  a|              start|                end|cnt|
+---+-------------------+-------------------+---+
| A1|2021-01-01 00:00:00|2021-01-01 00:05:00|  2|
| A1|2021-01-01 00:05:00|2021-01-01 00:10:00|  1|
| A2|2021-01-01 00:00:00|2021-01-01 00:05:00|  1|
+---+-------------------+-------------------+---+
SELECT a, window.start, window.end, count(*) as cnt FROM VALUES ('A1', '2021-01-01 00:00:00'), ('A1', '2021-01-01 00:04:30'), ('A1', '2021-01-01 00:06:00'), ('A2', '2021-01-01 00:01:00') AS tab(a, b) GROUP by a, window(b, '10 minutes', '5 minutes') ORDER BY a, start;
+---+-------------------+-------------------+---+
|  a|              start|                end|cnt|
+---+-------------------+-------------------+---+
| A1|2020-12-31 23:55:00|2021-01-01 00:05:00|  2|
| A1|2021-01-01 00:00:00|2021-01-01 00:10:00|  3|
| A1|2021-01-01 00:05:00|2021-01-01 00:15:00|  1|
| A2|2020-12-31 23:55:00|2021-01-01 00:05:00|  1|
| A2|2021-01-01 00:00:00|2021-01-01 00:10:00|  1|
+---+-------------------+-------------------+---+
-- window_time
SELECT a, window.start as start, window.end as end, window_time(window), cnt FROM (SELECT a, window, count(*) as cnt FROM VALUES ('A1', '2021-01-01 00:00:00'), ('A1', '2021-01-01 00:04:30'), ('A1', '2021-01-01 00:06:00'), ('A2', '2021-01-01 00:01:00') AS tab(a, b) GROUP by a, window(b, '5 minutes') ORDER BY a, window.start);
+---+-------------------+-------------------+--------------------+---+
|  a|              start|                end| window_time(window)|cnt|
+---+-------------------+-------------------+--------------------+---+
| A1|2021-01-01 00:00:00|2021-01-01 00:05:00|2021-01-01 00:04:...|  2|
| A1|2021-01-01 00:05:00|2021-01-01 00:10:00|2021-01-01 00:09:...|  1|
| A2|2021-01-01 00:00:00|2021-01-01 00:05:00|2021-01-01 00:04:...|  1|
+---+-------------------+-------------------+--------------------+---+
-- year
SELECT year('2016-07-30');
+----------------+
|year(2016-07-30)|
+----------------+
|            2016|
+----------------+
```

#### Aggregate functions
<a name="supported-sql-aggregate"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

Aggregate functions operate on values across rows to perform mathematical calculations such as sum, average, counting, minimum/maximum values, standard deviation, and estimation, as well as some non-mathematical operations. 

**Syntax **

```
aggregate_function(input1 [, input2, ...]) FILTER (WHERE boolean_expression) 
```

**Parameters **
+ `boolean_expression` - Specifies any expression that evaluates to a result type boolean. Two or more expressions may be combined together using the logical operators ( AND, OR ). 

**Ordered-set aggregate functions **

These aggregate functions use different syntax than the other aggregate functions so that to specify an expression (typically a column name) by which to order the values. 

**Syntax **

```
{ PERCENTILE_CONT | PERCENTILE_DISC }(percentile) WITHIN GROUP (ORDER BY { order_by_expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ] }) FILTER (WHERE boolean_expression) 
```

**Parameters **
+ `percentile` - The percentile of the value that you want to find. The percentile must be a constant between 0.0 and 1.0. 
+ `order_by_expression` - The expression (typically a column name) by which to order the values before aggregating them. 
+ `boolean_expression` - Specifies any expression that evaluates to a result type boolean. Two or more expressions may be combined together using the logical operators ( AND, OR ). 

**Examples**

```
CREATE OR REPLACE TEMPORARY VIEW basic_pays AS SELECT * FROM VALUES
('Jane Doe','Accounting',8435),
('Akua Mansa','Accounting',9998),
('John Doe','Accounting',8992),
('Juan Li','Accounting',8870),
('Carlos Salazar','Accounting',11472),
('Arnav Desai','Accounting',6627),
('Saanvi Sarkar','IT',8113),
('Shirley Rodriguez','IT',5186),
('Nikki Wolf','Sales',9181),
('Alejandro Rosalez','Sales',9441),
('Nikhil Jayashankar','Sales',6660),
('Richard Roe','Sales',10563),
('Pat Candella','SCM',10449),
('Gerard Hernandez','SCM',6949),
('Pamela Castillo','SCM',11303),
('Paulo Santos','SCM',11798),
('Jorge Souza','SCM',10586)
AS basic_pays(employee_name, department, salary);
SELECT * FROM basic_pays;
+-------------------+----------+------+
|    employee_name  |department|salary|
+-------------------+----------+------+
| Arnav Desai       |Accounting|  6627|
| Jorge Souza       |       SCM| 10586|
| Jane Doe          |Accounting|  8435|
| Nikhil Jayashankar|     Sales|  6660|
| Diego Vanauf      |     Sales| 10563|
| Carlos Salazar    |Accounting| 11472|
| Gerard Hernandez  |       SCM|  6949|
| John Doe          |Accounting|  8992|
| Nikki Wolf        |     Sales|  9181|
| Paulo Santos      |       SCM| 11798|
| Saanvi Sarkar     |        IT|  8113|
| Shirley Rodriguez |        IT|  5186|
| Pat Candella      |       SCM| 10449|
| Akua Mansa        |Accounting|  9998|
| Pamela Castillo   |       SCM| 11303|
| Alejandro Rosalez |     Sales|  9441|
| Juan Li           |Accounting|  8870|
+-------------------+----------+------+
SELECT
department,
percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS pc1,
percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) FILTER (WHERE employee_name LIKE '%Bo%') AS pc2,
percentile_cont(0.25) WITHIN GROUP (ORDER BY salary DESC) AS pc3,
percentile_cont(0.25) WITHIN GROUP (ORDER BY salary DESC) FILTER (WHERE employee_name LIKE '%Bo%') AS pc4,
percentile_disc(0.25) WITHIN GROUP (ORDER BY salary) AS pd1,
percentile_disc(0.25) WITHIN GROUP (ORDER BY salary) FILTER (WHERE employee_name LIKE '%Bo%') AS pd2,
percentile_disc(0.25) WITHIN GROUP (ORDER BY salary DESC) AS pd3,
percentile_disc(0.25) WITHIN GROUP (ORDER BY salary DESC) FILTER (WHERE employee_name LIKE '%Bo%') AS pd4
FROM basic_pays
GROUP BY department
ORDER BY department;
+----------+-------+--------+-------+--------+-----+-----+-----+-----+
|department|    pc1|     pc2|    pc3|     pc4|  pd1|  pd2|  pd3|  pd4|
+----------+-------+--------+-------+--------+-----+-----+-----+-----+
|Accounting|8543.75| 7838.25| 9746.5|10260.75| 8435| 6627| 9998|11472|
|        IT|5917.75|    NULL|7381.25|    NULL| 5186| NULL| 8113| NULL|
|     Sales|8550.75|    NULL| 9721.5|    NULL| 6660| NULL|10563| NULL|
|       SCM|10449.0|10786.25|11303.0|11460.75|10449|10449|11303|11798|
+----------+-------+--------+-------+--------+-----+-----+-----+-----+
```

#### Conditional functions
<a name="supported-sql-conditional"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| coalesce(expr1, expr2, ...) | Returns the first non-null argument if exists. Otherwise, null. | 
| if(expr1, expr2, expr3) | If expr1 evaluates to true, then returns expr2; otherwise returns expr3. | 
| ifnull(expr1, expr2) | Returns expr2 if expr1 is null, or expr1 otherwise. | 
| nanvl(expr1, expr2) | Returns expr1 if it's not NaN, or expr2 otherwise. | 
| nullif(expr1, expr2) | Returns null if expr1 equals to expr2, or expr1 otherwise. | 
| nvl(expr1, expr2) | Returns expr2 if expr1 is null, or expr1 otherwise. | 
| nvl2(expr1, expr2, expr3) | Returns expr2 if expr1 is not null, or expr3 otherwise. | 
| CASE WHEN expr1 THEN expr2 [WHEN expr3 THEN expr4]\* [ELSE expr5] END | When expr1 = true, returns expr2; else when expr3 = true, returns expr4; else returns expr5. | 

**Examples**

```
-- coalesce
SELECT coalesce(NULL, 1, NULL);
+-----------------------+
|coalesce(NULL, 1, NULL)|
+-----------------------+
|                      1|
+-----------------------+
-- if
SELECT if(1 < 2, 'a', 'b');
+-------------------+
|(IF((1 < 2), a, b))|
+-------------------+
|                  a|
+-------------------+
-- ifnull
SELECT ifnull(NULL, array('2'));
+----------------------+
|ifnull(NULL, array(2))|
+----------------------+
|                   [2]|
+----------------------+
-- nanvl
SELECT nanvl(cast('NaN' as double), 123);
+-------------------------------+
|nanvl(CAST(NaN AS DOUBLE), 123)|
+-------------------------------+
|                          123.0|
+-------------------------------+
-- nullif
SELECT nullif(2, 2);
+------------+
|nullif(2, 2)|
+------------+
|        NULL|
+------------+
-- nvl
SELECT nvl(NULL, array('2'));
+-------------------+
|nvl(NULL, array(2))|
+-------------------+
|                [2]|
+-------------------+
-- nvl2
SELECT nvl2(NULL, 2, 1);
+----------------+
|nvl2(NULL, 2, 1)|
+----------------+
|               1|
+----------------+
-- when
SELECT CASE WHEN 1 > 0 THEN 1 WHEN 2 > 0 THEN 2.0 ELSE 1.2 END;
+-----------------------------------------------------------+
|CASE WHEN (1 > 0) THEN 1 WHEN (2 > 0) THEN 2.0 ELSE 1.2 END|
+-----------------------------------------------------------+
|                                                        1.0|
+-----------------------------------------------------------+
SELECT CASE WHEN 1 < 0 THEN 1 WHEN 2 > 0 THEN 2.0 ELSE 1.2 END;
+-----------------------------------------------------------+
|CASE WHEN (1 < 0) THEN 1 WHEN (2 > 0) THEN 2.0 ELSE 1.2 END|
+-----------------------------------------------------------+
|                                                        2.0|
+-----------------------------------------------------------+
SELECT CASE WHEN 1 < 0 THEN 1 WHEN 2 < 0 THEN 2.0 END;
+--------------------------------------------------+
|CASE WHEN (1 < 0) THEN 1 WHEN (2 < 0) THEN 2.0 END|
+--------------------------------------------------+
|                                              NULL|
+--------------------------------------------------+
```

#### JSON functions
<a name="supported-sql-json"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).




****  

| Function | Description | 
| --- | --- | 
| from\_json(jsonStr, schema[, options]) | Returns a struct value with the given `jsonStr` and `schema`. | 
| get\_json\_object(json\_txt, path) | Extracts a json object from `path`. | 
| json\_array\_length(jsonArray) | Returns the number of elements in the outermost JSON array. | 
| json\_object\_keys(json\_object) | Returns all the keys of the outermost JSON object as an array. | 
| json\_tuple(jsonStr, p1, p2, ..., pn) | Returns a tuple like the function get\_json\_object, but it takes multiple names. All the input parameters and output column types are string. | 
| schema\_of\_json(json[, options]) | Returns schema in the DDL format of JSON string. | 
| to\_json(expr[, options]) | Returns a JSON string with a given struct value | 

**Examples**

```
-- from_json
SELECT from_json('{"a":1, "b":0.8}', 'a INT, b DOUBLE');
+---------------------------+
| from_json({"a":1, "b":0.8}) |
+---------------------------+
| {1, 0.8}                  |
+---------------------------+

SELECT from_json('{"time":"26/08/2015"}', 'time Timestamp', map('timestampFormat', 'dd/MM/yyyy'));
+--------------------------------+
| from_json({"time":"26/08/2015"}) |
+--------------------------------+
| {2015-08-26 00:00...           |
+--------------------------------+

SELECT from_json('{"teacher": "Alice", "student": [{"name": "Bob", "rank": 1}, {"name": "Charlie", "rank": 2}]}', 'STRUCT<teacher: STRING, student: ARRAY<STRUCT<name: STRING, rank: INT>>>');
+--------------------------------------------------------------------------------------------------------+
| from_json({"teacher": "Alice", "student": [{"name": "Bob", "rank": 1}, {"name": "Charlie", "rank": 2}]}) |
+--------------------------------------------------------------------------------------------------------+
| {Alice, [{Bob, 1}...                                                                                   |
+--------------------------------------------------------------------------------------------------------+

-- get_json_object
SELECT get_json_object('{"a":"b"}', '$.a');
+-------------------------------+
| get_json_object({"a":"b"}, $.a) |
+-------------------------------+
| b                             |
+-------------------------------+

-- json_array_length
SELECT json_array_length('[1,2,3,4]');
+----------------------------+
| json_array_length([1,2,3,4]) |
+----------------------------+
| 4                          |
+----------------------------+

SELECT json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]');
+------------------------------------------------+
| json_array_length([1,2,3,{"f1":1,"f2":[5,6]},4]) |
+------------------------------------------------+
| 5                                              |
+------------------------------------------------+

SELECT json_array_length('[1,2');
+-----------------------+
| json_array_length([1,2) |
+-----------------------+
| NULL                  |
+-----------------------+

-- json_object_keys
SELECT json_object_keys('{}');
+--------------------+
| json_object_keys({}) |
+--------------------+
| []                 |
+--------------------+

SELECT json_object_keys('{"key": "value"}');
+----------------------------------+
| json_object_keys({"key": "value"}) |
+----------------------------------+
| [key]                            |
+----------------------------------+

SELECT json_object_keys('{"f1":"abc","f2":{"f3":"a", "f4":"b"}}');
+--------------------------------------------------------+
| json_object_keys({"f1":"abc","f2":{"f3":"a", "f4":"b"}}) |
+--------------------------------------------------------+
| [f1, f2]                                               |
+--------------------------------------------------------+

-- json_tuple
SELECT json_tuple('{"a":1, "b":2}', 'a', 'b');
+---+---+
| c0| c1|
+---+---+
|  1|  2|
+---+---+

-- schema_of_json
SELECT schema_of_json('[{"col":0}]');
+---------------------------+
| schema_of_json([{"col":0}]) |
+---------------------------+
| ARRAY<STRUCT<col:...      |
+---------------------------+

SELECT schema_of_json('[{"col":01}]', map('allowNumericLeadingZeros', 'true'));
+----------------------------+
| schema_of_json([{"col":01}]) |
+----------------------------+
| ARRAY<STRUCT<col:...       |
+----------------------------+

-- to_json
SELECT to_json(named_struct('a', 1, 'b', 2));
+---------------------------------+
| to_json(named_struct(a, 1, b, 2)) |
+---------------------------------+
| {"a":1,"b":2}                   |
+---------------------------------+

SELECT to_json(named_struct('time', to_timestamp('2015-08-26', 'yyyy-MM-dd')), map('timestampFormat', 'dd/MM/yyyy'));
+-----------------------------------------------------------------+
| to_json(named_struct(time, to_timestamp(2015-08-26, yyyy-MM-dd))) |
+-----------------------------------------------------------------+
| {"time":"26/08/20...                                            |
+-----------------------------------------------------------------+

SELECT to_json(array(named_struct('a', 1, 'b', 2)));
+----------------------------------------+
| to_json(array(named_struct(a, 1, b, 2))) |
+----------------------------------------+
| [{"a":1,"b":2}]                        |
+----------------------------------------+

SELECT to_json(map('a', named_struct('b', 1)));
+-----------------------------------+
| to_json(map(a, named_struct(b, 1))) |
+-----------------------------------+
| {"a":{"b":1}}                     |
+-----------------------------------+

SELECT to_json(map(named_struct('a', 1),named_struct('b', 2)));
+----------------------------------------------------+
| to_json(map(named_struct(a, 1), named_struct(b, 2))) |
+----------------------------------------------------+
| {"[1]":{"b":2}}                                    |
+----------------------------------------------------+

SELECT to_json(map('a', 1));
+------------------+
| to_json(map(a, 1)) |
+------------------+
| {"a":1}          |
+------------------+

SELECT to_json(array(map('a', 1)));
+-------------------------+
| to_json(array(map(a, 1))) |
+-------------------------+
| [{"a":1}]               |
+-------------------------+
```

#### Array functions
<a name="supported-sql-array"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| array(expr, ...) | Returns an array with the given elements. | 
| array\_append(array, element) | Add the element at the end of the array passed as first argument. Type of element should be similar to type of the elements of the array. Null element is also appended into the array. But if the array passed, is NULL output is NULL | 
| array\_compact(array) | Removes null values from the array. | 
| array\_contains(array, value) | Returns true if the array contains the value. | 
| array\_distinct(array) | Removes duplicate values from the array. | 
| array\_except(array1, array2) | Returns an array of the elements in array1 but not in array2, without duplicates. | 
| array\_insert(x, pos, val) | Places val into index pos of array x. Array indices start at 1. The maximum negative index is -1 for which the function inserts new element after the current last element. Index above array size appends the array, or prepends the array if index is negative, with 'null' elements. | 
| array\_intersect(array1, array2) | Returns an array of the elements in the intersection of array1 and array2, without duplicates. | 
| array\_join(array, delimiter[, nullReplacement]) | Concatenates the elements of the given array using the delimiter and an optional string to replace nulls. If no value is set for nullReplacement, any null value is filtered. | 
| array\_max(array) | Returns the maximum value in the array. NaN is greater than any non-NaN elements for double/float type. NULL elements are skipped. | 
| array\_min(array) | Returns the minimum value in the array. NaN is greater than any non-NaN elements for double/float type. NULL elements are skipped. | 
| array\_position(array, element) | Returns the (1-based) index of the first matching element of the array as long, or 0 if no match is found. | 
| array\_prepend(array, element) | Add the element at the beginning of the array passed as first argument. Type of element should be the same as the type of the elements of the array. Null element is also prepended to the array. But if the array passed is NULL output is NULL | 
| array\_remove(array, element) | Remove all elements that equal to element from array. | 
| array\_repeat(element, count) | Returns the array containing element count times. | 
| array\_union(array1, array2) | Returns an array of the elements in the union of array1 and array2, without duplicates. | 
| arrays\_overlap(a1, a2) | Returns true if a1 contains at least a non-null element present also in a2. If the arrays have no common element and they are both non-empty and either of them contains a null element null is returned, false otherwise. | 
| arrays\_zip(a1, a2, ...) | Returns a merged array of structs in which the N-th struct contains all N-th values of input arrays. | 
| flatten(arrayOfArrays) | Transforms an array of arrays into a single array. | 
| get(array, index) | Returns element of array at given (0-based) index. If the index points outside of the array boundaries, then this function returns NULL. | 
| sequence(start, stop, step) | Generates an array of elements from start to stop (inclusive), incrementing by step. The type of the returned elements is the same as the type of argument expressions. Supported types are: byte, short, integer, long, date, timestamp. The start and stop expressions must resolve to the same type. If start and stop expressions resolve to the 'date' or 'timestamp' type then the step expression must resolve to the 'interval' or 'year-month interval' or 'day-time interval' type, otherwise to the same type as the start and stop expressions. | 
| shuffle(array) | Returns a random permutation of the given array. | 
| slice(x, start, length) | Subsets array x starting from index start (array indices start at 1, or starting from the end if start is negative) with the specified length. | 
| sort\_array(array[, ascendingOrder]) | Sorts the input array in ascending or descending order according to the natural ordering of the array elements. NaN is greater than any non-NaN elements for double/float type. Null elements will be placed at the beginning of the returned array in ascending order or at the end of the returned array in descending order. | 

**Examples**

```
-- array
SELECT array(1, 2, 3);
+--------------+
|array(1, 2, 3)|
+--------------+
|     [1, 2, 3]|
+--------------+
-- array_append
SELECT array_append(array('b', 'd', 'c', 'a'), 'd');
+----------------------------------+
|array_append(array(b, d, c, a), d)|
+----------------------------------+
|                   [b, d, c, a, d]|
+----------------------------------+
SELECT array_append(array(1, 2, 3, null), null);
+----------------------------------------+
|array_append(array(1, 2, 3, NULL), NULL)|
+----------------------------------------+
|                    [1, 2, 3, NULL, N...|
+----------------------------------------+
SELECT array_append(CAST(null as Array<Int>), 2);
+---------------------+
|array_append(NULL, 2)|
+---------------------+
|                 NULL|
+---------------------+
-- array_compact
SELECT array_compact(array(1, 2, 3, null));
+-----------------------------------+
|array_compact(array(1, 2, 3, NULL))|
+-----------------------------------+
|                          [1, 2, 3]|
+-----------------------------------+
SELECT array_compact(array("a", "b", "c"));
+-----------------------------+
|array_compact(array(a, b, c))|
+-----------------------------+
|                    [a, b, c]|
+-----------------------------+
-- array_contains
SELECT array_contains(array(1, 2, 3), 2);
+---------------------------------+
|array_contains(array(1, 2, 3), 2)|
+---------------------------------+
|                             true|
+---------------------------------+
-- array_distinct
SELECT array_distinct(array(1, 2, 3, null, 3));
+---------------------------------------+
|array_distinct(array(1, 2, 3, NULL, 3))|
+---------------------------------------+
|                        [1, 2, 3, NULL]|
+---------------------------------------+
-- array_except
SELECT array_except(array(1, 2, 3), array(1, 3, 5));
+--------------------------------------------+
|array_except(array(1, 2, 3), array(1, 3, 5))|
+--------------------------------------------+
|                                         [2]|
+--------------------------------------------+
-- array_insert
SELECT array_insert(array(1, 2, 3, 4), 5, 5);
+-------------------------------------+
|array_insert(array(1, 2, 3, 4), 5, 5)|
+-------------------------------------+
|                      [1, 2, 3, 4, 5]|
+-------------------------------------+
SELECT array_insert(array(5, 4, 3, 2), -1, 1);
+--------------------------------------+
|array_insert(array(5, 4, 3, 2), -1, 1)|
+--------------------------------------+
|                       [5, 4, 3, 2, 1]|
+--------------------------------------+
SELECT array_insert(array(5, 3, 2, 1), -4, 4);
+--------------------------------------+
|array_insert(array(5, 3, 2, 1), -4, 4)|
+--------------------------------------+
|                       [5, 4, 3, 2, 1]|
+--------------------------------------+
-- array_intersect
SELECT array_intersect(array(1, 2, 3), array(1, 3, 5));
+-----------------------------------------------+
|array_intersect(array(1, 2, 3), array(1, 3, 5))|
+-----------------------------------------------+
|                                         [1, 3]|
+-----------------------------------------------+
-- array_join
SELECT array_join(array('hello', 'world'), ' ');
+----------------------------------+
|array_join(array(hello, world),  )|
+----------------------------------+
|                       hello world|
+----------------------------------+
SELECT array_join(array('hello', null ,'world'), ' ');
+----------------------------------------+
|array_join(array(hello, NULL, world),  )|
+----------------------------------------+
|                             hello world|
+----------------------------------------+
SELECT array_join(array('hello', null ,'world'), ' ', ',');
+-------------------------------------------+
|array_join(array(hello, NULL, world),  , ,)|
+-------------------------------------------+
|                              hello , world|
+-------------------------------------------+
-- array_max
SELECT array_max(array(1, 20, null, 3));
+--------------------------------+
|array_max(array(1, 20, NULL, 3))|
+--------------------------------+
|                              20|
+--------------------------------+
-- array_min
SELECT array_min(array(1, 20, null, 3));
+--------------------------------+
|array_min(array(1, 20, NULL, 3))|
+--------------------------------+
|                               1|
+--------------------------------+
-- array_position
SELECT array_position(array(312, 773, 708, 708), 708);
+----------------------------------------------+
|array_position(array(312, 773, 708, 708), 708)|
+----------------------------------------------+
|                                             3|
+----------------------------------------------+
SELECT array_position(array(312, 773, 708, 708), 414);
+----------------------------------------------+
|array_position(array(312, 773, 708, 708), 414)|
+----------------------------------------------+
|                                             0|
+----------------------------------------------+
-- array_prepend
SELECT array_prepend(array('b', 'd', 'c', 'a'), 'd');
+-----------------------------------+
|array_prepend(array(b, d, c, a), d)|
+-----------------------------------+
|                    [d, b, d, c, a]|
+-----------------------------------+
SELECT array_prepend(array(1, 2, 3, null), null);
+-----------------------------------------+
|array_prepend(array(1, 2, 3, NULL), NULL)|
+-----------------------------------------+
|                     [NULL, 1, 2, 3, N...|
+-----------------------------------------+
SELECT array_prepend(CAST(null as Array<Int>), 2);
+----------------------+
|array_prepend(NULL, 2)|
+----------------------+
|                  NULL|
+----------------------+
-- array_remove
SELECT array_remove(array(1, 2, 3, null, 3), 3);
+----------------------------------------+
|array_remove(array(1, 2, 3, NULL, 3), 3)|
+----------------------------------------+
|                            [1, 2, NULL]|
+----------------------------------------+
-- array_repeat
SELECT array_repeat('123', 2);
+--------------------+
|array_repeat(123, 2)|
+--------------------+
|          [123, 123]|
+--------------------+
-- array_union
SELECT array_union(array(1, 2, 3), array(1, 3, 5));
+-------------------------------------------+
|array_union(array(1, 2, 3), array(1, 3, 5))|
+-------------------------------------------+
|                               [1, 2, 3, 5]|
+-------------------------------------------+
-- arrays_overlap
SELECT arrays_overlap(array(1, 2, 3), array(3, 4, 5));
+----------------------------------------------+
|arrays_overlap(array(1, 2, 3), array(3, 4, 5))|
+----------------------------------------------+
|                                          true|
+----------------------------------------------+
-- arrays_zip
SELECT arrays_zip(array(1, 2, 3), array(2, 3, 4));
+------------------------------------------+
|arrays_zip(array(1, 2, 3), array(2, 3, 4))|
+------------------------------------------+
|                      [{1, 2}, {2, 3}, ...|
+------------------------------------------+
SELECT arrays_zip(array(1, 2), array(2, 3), array(3, 4));
+-------------------------------------------------+
|arrays_zip(array(1, 2), array(2, 3), array(3, 4))|
+-------------------------------------------------+
|                             [{1, 2, 3}, {2, 3...|
+-------------------------------------------------+
-- flatten
SELECT flatten(array(array(1, 2), array(3, 4)));
+----------------------------------------+
|flatten(array(array(1, 2), array(3, 4)))|
+----------------------------------------+
|                            [1, 2, 3, 4]|
+----------------------------------------+
-- get
SELECT get(array(1, 2, 3), 0);
+----------------------+
|get(array(1, 2, 3), 0)|
+----------------------+
|                     1|
+----------------------+
SELECT get(array(1, 2, 3), 3);
+----------------------+
|get(array(1, 2, 3), 3)|
+----------------------+
|                  NULL|
+----------------------+
SELECT get(array(1, 2, 3), -1);
+-----------------------+
|get(array(1, 2, 3), -1)|
+-----------------------+
|                   NULL|
+-----------------------+
-- sequence
SELECT sequence(1, 5);
+---------------+
| sequence(1, 5)|
+---------------+
|[1, 2, 3, 4, 5]|
+---------------+
SELECT sequence(5, 1);
+---------------+
| sequence(5, 1)|
+---------------+
|[5, 4, 3, 2, 1]|
+---------------+
SELECT sequence(to_date('2018-01-01'), to_date('2018-03-01'), interval 1 month);
+----------------------------------------------------------------------+
|sequence(to_date(2018-01-01), to_date(2018-03-01), INTERVAL '1' MONTH)|
+----------------------------------------------------------------------+
|                                                  [2018-01-01, 2018...|
+----------------------------------------------------------------------+
SELECT sequence(to_date('2018-01-01'), to_date('2018-03-01'), interval '0-1' year to month);
+--------------------------------------------------------------------------------+
|sequence(to_date(2018-01-01), to_date(2018-03-01), INTERVAL '0-1' YEAR TO MONTH)|
+--------------------------------------------------------------------------------+
|                                                            [2018-01-01, 2018...|
+--------------------------------------------------------------------------------+
-- shuffle
SELECT shuffle(array(1, 20, 3, 5));
+---------------------------+
|shuffle(array(1, 20, 3, 5))|
+---------------------------+
|              [5, 1, 20, 3]|
+---------------------------+
SELECT shuffle(array(1, 20, null, 3));
+------------------------------+
|shuffle(array(1, 20, NULL, 3))|
+------------------------------+
|              [1, NULL, 20, 3]|
+------------------------------+
-- slice
SELECT slice(array(1, 2, 3, 4), 2, 2);
+------------------------------+
|slice(array(1, 2, 3, 4), 2, 2)|
+------------------------------+
|                        [2, 3]|
+------------------------------+
SELECT slice(array(1, 2, 3, 4), -2, 2);
+-------------------------------+
|slice(array(1, 2, 3, 4), -2, 2)|
+-------------------------------+
|                         [3, 4]|
+-------------------------------+
-- sort_array
SELECT sort_array(array('b', 'd', null, 'c', 'a'), true);
+-----------------------------------------+
|sort_array(array(b, d, NULL, c, a), true)|
+-----------------------------------------+
|                       [NULL, a, b, c, d]|
+-----------------------------------------+
```

#### Window functions
<a name="supported-sql-window"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

Window functions operate on a group of rows, referred to as a window, and calculate a return value for each row based on the group of rows. Window functions are useful for processing tasks such as calculating a moving average, computing a cumulative statistic, or accessing the value of rows given the relative position of the current row. 

**Syntax** 

```
window_function [ nulls_option ] OVER ( [ { PARTITION | DISTRIBUTE } BY partition_col_name = partition_col_val ( [ , ... ] ) ] { ORDER | SORT } BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ] [ window_frame ] ) 
```

**Parameters** 
+ 

  window\_function 

  Ranking functions 

  Syntax: `RANK | DENSE_RANK | PERCENT_RANK | NTILE | ROW_NUMBER `

  Analytic functions 

  Syntax: `CUME_DIST | LAG | LEAD | NTH_VALUE | FIRST_VALUE | LAST_VALUE `

  Aggregate functions 

  Syntax: `MAX | MIN | COUNT | SUM | AVG | ... `
+ `nulls_option` - Specifies whether or not to skip null values when evaluating the window function. RESPECT NULLS means not skipping null values, while IGNORE NULLS means skipping. If not specified, the default is RESPECT NULLS. 

  Syntax: `{ IGNORE | RESPECT } NULLS `

  Note: `Only LAG` \| `LEAD` \| `NTH_VALUE` \| `FIRST_VALUE` \| `LAST_VALUE` can be used with `IGNORE NULLS`. 
+ `window_frame` - Specifies which row to start the window on and where to end it. 

  Syntax: `{ RANGE | ROWS } { frame_start | BETWEEN frame_start AND frame_end }` 

  frame\_start and frame\_end have the following syntax: 

  Syntax: `UNBOUNDED PRECEDING | offset PRECEDING | CURRENT ROW | offset FOLLOWING | UNBOUNDED FOLLOWING `

  offset: specifies the offset from the position of the current row. 

  **Note** If frame\_end is omitted, it defaults to CURRENT ROW. 

**Examples**

```
CREATE TABLE employees (name STRING, dept STRING, salary INT, age INT);
INSERT INTO employees VALUES ("Lisa", "Sales", 10000, 35);
INSERT INTO employees VALUES ("Evan", "Sales", 32000, 38);
INSERT INTO employees VALUES ("Fred", "Engineering", 21000, 28);
INSERT INTO employees VALUES ("Alex", "Sales", 30000, 33);
INSERT INTO employees VALUES ("Tom", "Engineering", 23000, 33);
INSERT INTO employees VALUES ("Jane", "Marketing", 29000, 28);
INSERT INTO employees VALUES ("Jeff", "Marketing", 35000, 38);
INSERT INTO employees VALUES ("Paul", "Engineering", 29000, 23);
INSERT INTO employees VALUES ("Chloe", "Engineering", 23000, 25);
SELECT * FROM employees;
+-----+-----------+------+-----+
| name|       dept|salary|  age|
+-----+-----------+------+-----+
|Chloe|Engineering| 23000|   25|
| Fred|Engineering| 21000|   28|
| Paul|Engineering| 29000|   23|
|Helen|  Marketing| 29000|   40|
|  Tom|Engineering| 23000|   33|
| Jane|  Marketing| 29000|   28|
| Jeff|  Marketing| 35000|   38|
| Evan|      Sales| 32000|   38|
| Lisa|      Sales| 10000|   35|
| Alex|      Sales| 30000|   33|
+-----+-----------+------+-----+
SELECT name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary) AS rank FROM employees;
+-----+-----------+------+----+
| name|       dept|salary|rank|
+-----+-----------+------+----+
| Lisa|      Sales| 10000|   1|
| Alex|      Sales| 30000|   2|
| Evan|      Sales| 32000|   3|
| Fred|Engineering| 21000|   1|
|  Tom|Engineering| 23000|   2|
|Chloe|Engineering| 23000|   2|
| Paul|Engineering| 29000|   4|
|Helen|  Marketing| 29000|   1|
| Jane|  Marketing| 29000|   1|
| Jeff|  Marketing| 35000|   3|
+-----+-----------+------+----+
SELECT name, dept, salary, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary ROWS BETWEEN
UNBOUNDED PRECEDING AND CURRENT ROW) AS dense_rank FROM employees;
+-----+-----------+------+----------+
| name|       dept|salary|dense_rank|
+-----+-----------+------+----------+
| Lisa|      Sales| 10000|         1|
| Alex|      Sales| 30000|         2|
| Evan|      Sales| 32000|         3|
| Fred|Engineering| 21000|         1|
|  Tom|Engineering| 23000|         2|
|Chloe|Engineering| 23000|         2|
| Paul|Engineering| 29000|         3|
|Helen|  Marketing| 29000|         1|
| Jane|  Marketing| 29000|         1|
| Jeff|  Marketing| 35000|         2|
+-----+-----------+------+----------+
SELECT name, dept, age, CUME_DIST() OVER (PARTITION BY dept ORDER BY age
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cume_dist FROM employees;
+-----+-----------+------+------------------+
| name|       dept|age   |         cume_dist|
+-----+-----------+------+------------------+
| Alex|      Sales|    33|0.3333333333333333|
| Lisa|      Sales|    35|0.6666666666666666|
| Evan|      Sales|    38|               1.0|
| Paul|Engineering|    23|              0.25|
|Chloe|Engineering|    25|              0.75|
| Fred|Engineering|    28|              0.25|
|  Tom|Engineering|    33|               1.0|
| Jane|  Marketing|    28|0.3333333333333333|
| Jeff|  Marketing|    38|0.6666666666666666|
|Helen|  Marketing|    40|               1.0|
+-----+-----------+------+------------------+
SELECT name, dept, salary, MIN(salary) OVER (PARTITION BY dept ORDER BY salary) AS min
FROM employees;
+-----+-----------+------+-----+
| name|       dept|salary|  min|
+-----+-----------+------+-----+
| Lisa|      Sales| 10000|10000|
| Alex|      Sales| 30000|10000|
| Evan|      Sales| 32000|10000|
|Helen|  Marketing| 29000|29000|
| Jane|  Marketing| 29000|29000|
| Jeff|  Marketing| 35000|29000|
| Fred|Engineering| 21000|21000|
|  Tom|Engineering| 23000|21000|
|Chloe|Engineering| 23000|21000|
| Paul|Engineering| 29000|21000|
+-----+-----------+------+-----+
SELECT name, salary,
LAG(salary) OVER (PARTITION BY dept ORDER BY salary) AS lag,
LEAD(salary, 1, 0) OVER (PARTITION BY dept ORDER BY salary) AS lead
FROM employees;
+-----+-----------+------+-----+-----+
| name|       dept|salary|  lag| lead|
+-----+-----------+------+-----+-----+
| Lisa|      Sales| 10000|NULL |30000|
| Alex|      Sales| 30000|10000|32000|
| Evan|      Sales| 32000|30000|    0|
| Fred|Engineering| 21000| NULL|23000|
|Chloe|Engineering| 23000|21000|23000|
|  Tom|Engineering| 23000|23000|29000|
| Paul|Engineering| 29000|23000|    0|
|Helen|  Marketing| 29000| NULL|29000|
| Jane|  Marketing| 29000|29000|35000|
| Jeff|  Marketing| 35000|29000|    0|
+-----+-----------+------+-----+-----+
SELECT id, v,
LEAD(v, 0) IGNORE NULLS OVER w lead,
LAG(v, 0) IGNORE NULLS OVER w lag,
NTH_VALUE(v, 2) IGNORE NULLS OVER w nth_value,
FIRST_VALUE(v) IGNORE NULLS OVER w first_value,
LAST_VALUE(v) IGNORE NULLS OVER w last_value
FROM test_ignore_null
WINDOW w AS (ORDER BY id)
ORDER BY id;
+--+----+----+----+---------+-----------+----------+
|id|   v|lead| lag|nth_value|first_value|last_value|
+--+----+----+----+---------+-----------+----------+
| 0|NULL|NULL|NULL|     NULL|       NULL|      NULL|
| 1|   x|   x|   x|     NULL|          x|         x|
| 2|NULL|NULL|NULL|     NULL|          x|         x|
| 3|NULL|NULL|NULL|     NULL|          x|         x|
| 4|   y|   y|   y|        y|          x|         y|
| 5|NULL|NULL|NULL|        y|          x|         y|
| 6|   z|   z|   z|        y|          x|         z|
| 7|   v|   v|   v|        y|          x|         v|
| 8|NULL|NULL|NULL|        y|          x|         v|
+--+----+----+----+---------+-----------+----------+
```

#### Conversion functions
<a name="supported-sql-conversion"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| bigint(expr) | Casts the value `expr` to the target data type `bigint`. | 
| binary(expr) | Casts the value `expr` to the target data type `binary`. | 
| boolean(expr) | Casts the value `expr` to the target data type `boolean`. | 
| cast(expr AS type) | Casts the value `expr` to the target data type `type`. | 
| date(expr) | Casts the value `expr` to the target data type `date`. | 
| decimal(expr) | Casts the value `expr` to the target data type `decimal`. | 
| double(expr) | Casts the value `expr` to the target data type `double`. | 
| float(expr) | Casts the value `expr` to the target data type `float`. | 
| int(expr) | Casts the value `expr` to the target data type `int`. | 
| smallint(expr) | Casts the value `expr` to the target data type `smallint`. | 
| string(expr) | Casts the value `expr` to the target data type `string`. | 
| timestamp(expr) | Casts the value `expr` to the target data type `timestamp`. | 
| tinyint(expr) | Casts the value `expr` to the target data type `tinyint`. | 

**Examples**

```
-- cast
SELECT cast(field as int);
+---------------+
|CAST(field AS INT)|
+---------------+
|             10|
+---------------+
```

#### Predicate functions
<a name="supported-sql-predicate"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| \! expr | Logical not. | 
| expr1 < expr2 | Returns true if `expr1` is less than `expr2`. | 
| expr1 <= expr2 | Returns true if `expr1` is less than or equal to `expr2`. | 
| expr1 <=> expr2 | Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of the them is null. | 
| expr1 = expr2 | Returns true if `expr1` equals `expr2`, or false otherwise. | 
| expr1 == expr2 | Returns true if `expr1` equals `expr2`, or false otherwise. | 
| expr1 > expr2 | Returns true if `expr1` is greater than `expr2`. | 
| expr1 >= expr2 | Returns true if `expr1` is greater than or equal to `expr2`. | 
| expr1 and expr2 | Logical AND. | 
| str ilike pattern[ ESCAPE escape] | Returns true if str matches `pattern` with `escape` case-insensitively, null if any arguments are null, false otherwise. | 
| expr1 in(expr2, expr3, ...) | Returns true if `expr` equals to any valN. | 
| isnan(expr) | Returns true if `expr` is NaN, or false otherwise. | 
| isnotnull(expr) | Returns true if `expr` is not null, or false otherwise. | 
| isnull(expr) | Returns true if `expr` is null, or false otherwise. | 
| str like pattern[ ESCAPE escape] | Returns true if str matches `pattern` with `escape`, null if any arguments are null, false otherwise. | 
| not expr | Logical not. | 
| expr1 or expr2 | Logical OR. | 
| regexp(str, regexp) | Returns true if `str` matches `regexp`, or false otherwise. | 
| regexp\_like(str, regexp) | Returns true if `str` matches `regexp`, or false otherwise. | 
| rlike(str, regexp) | Returns true if `str` matches `regexp`, or false otherwise. | 

**Examples**

```
-- !
SELECT ! true;
+----------+
|(NOT true)|
+----------+
|     false|
+----------+
SELECT ! false;
+-----------+
|(NOT false)|
+-----------+
|       true|
+-----------+
SELECT ! NULL;
+----------+
|(NOT NULL)|
+----------+
|      NULL|
+----------+
-- <
SELECT to_date('2009-07-30 04:17:52') < to_date('2009-07-30 04:17:52');
+-------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) < to_date(2009-07-30 04:17:52))|
+-------------------------------------------------------------+
|                                                        false|
+-------------------------------------------------------------+
SELECT to_date('2009-07-30 04:17:52') < to_date('2009-08-01 04:17:52');
+-------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) < to_date(2009-08-01 04:17:52))|
+-------------------------------------------------------------+
|                                                         true|
+-------------------------------------------------------------+
SELECT 1 < NULL;
+----------+
|(1 < NULL)|
+----------+
|      NULL|
+----------+
-- <=
SELECT 2 <= 2;
+--------+
|(2 <= 2)|
+--------+
|    true|
+--------+
SELECT 1.0 <= '1';
+----------+
|(1.0 <= 1)|
+----------+
|      true|
+----------+
SELECT to_date('2009-07-30 04:17:52') <= to_date('2009-07-30 04:17:52');
+--------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) <= to_date(2009-07-30 04:17:52))|
+--------------------------------------------------------------+
|                                                          true|
+--------------------------------------------------------------+
SELECT to_date('2009-07-30 04:17:52') <= to_date('2009-08-01 04:17:52');
+--------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) <= to_date(2009-08-01 04:17:52))|
+--------------------------------------------------------------+
|                                                          true|
+--------------------------------------------------------------+
SELECT 1 <= NULL;
+-----------+
|(1 <= NULL)|
+-----------+
|       NULL|
+-----------+
-- <=>
SELECT 2 <=> 2;
+---------+
|(2 <=> 2)|
+---------+
|     true|
+---------+
SELECT 1 <=> '1';
+---------+
|(1 <=> 1)|
+---------+
|     true|
+---------+
SELECT true <=> NULL;
+---------------+
|(true <=> NULL)|
+---------------+
|          false|
+---------------+
SELECT NULL <=> NULL;
+---------------+
|(NULL <=> NULL)|
+---------------+
|           true|
+---------------+
-- =
SELECT 2 = 2;
+-------+
|(2 = 2)|
+-------+
|   true|
+-------+
SELECT 1 = '1';
+-------+
|(1 = 1)|
+-------+
|   true|
+-------+
SELECT true = NULL;
+-------------+
|(true = NULL)|
+-------------+
|         NULL|
+-------------+
SELECT NULL = NULL;
+-------------+
|(NULL = NULL)|
+-------------+
|         NULL|
+-------------+
-- ==
SELECT 2 == 2;
+-------+
|(2 = 2)|
+-------+
|   true|
+-------+
SELECT 1 == '1';
+-------+
|(1 = 1)|
+-------+
|   true|
+-------+
SELECT true == NULL;
+-------------+
|(true = NULL)|
+-------------+
|         NULL|
+-------------+
SELECT NULL == NULL;
+-------------+
|(NULL = NULL)|
+-------------+
|         NULL|
+-------------+
-- >
SELECT 2 > 1;
+-------+
|(2 > 1)|
+-------+
|   true|
+-------+
SELECT 2 > 1.1;
+-------+
|(2 > 1)|
+-------+
|   true|
+-------+
SELECT to_date('2009-07-30 04:17:52') > to_date('2009-07-30 04:17:52');
+-------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) > to_date(2009-07-30 04:17:52))|
+-------------------------------------------------------------+
|                                                        false|
+-------------------------------------------------------------+
SELECT to_date('2009-07-30 04:17:52') > to_date('2009-08-01 04:17:52');
+-------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) > to_date(2009-08-01 04:17:52))|
+-------------------------------------------------------------+
|                                                        false|
+-------------------------------------------------------------+
SELECT 1 > NULL;
+----------+
|(1 > NULL)|
+----------+
|      NULL|
+----------+
-- >=
SELECT 2 >= 1;
+--------+
|(2 >= 1)|
+--------+
|    true|
+--------+
SELECT 2.0 >= '2.1';
+------------+
|(2.0 >= 2.1)|
+------------+
|       false|
+------------+
SELECT to_date('2009-07-30 04:17:52') >= to_date('2009-07-30 04:17:52');
+--------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) >= to_date(2009-07-30 04:17:52))|
+--------------------------------------------------------------+
|                                                          true|
+--------------------------------------------------------------+
SELECT to_date('2009-07-30 04:17:52') >= to_date('2009-08-01 04:17:52');
+--------------------------------------------------------------+
|(to_date(2009-07-30 04:17:52) >= to_date(2009-08-01 04:17:52))|
+--------------------------------------------------------------+
|                                                         false|
+--------------------------------------------------------------+
SELECT 1 >= NULL;
+-----------+
|(1 >= NULL)|
+-----------+
|       NULL|
+-----------+
-- and
SELECT true and true;
+---------------+
|(true AND true)|
+---------------+
|           true|
+---------------+
SELECT true and false;
+----------------+
|(true AND false)|
+----------------+
|           false|
+----------------+
SELECT true and NULL;
+---------------+
|(true AND NULL)|
+---------------+
|           NULL|
+---------------+
SELECT false and NULL;
+----------------+
|(false AND NULL)|
+----------------+
|           false|
+----------------+
-- ilike
SELECT ilike('Wagon', '_Agon');
+-------------------+
|ilike(Wagon, _Agon)|
+-------------------+
|               true|
+-------------------+
SELECT '%SystemDrive%\Users\John' ilike '\%SystemDrive\%\\users%';
+--------------------------------------------------------+
|ilike(%SystemDrive%\Users\John, \%SystemDrive\%\\users%)|
+--------------------------------------------------------+
|                                                    true|
+--------------------------------------------------------+
SELECT '%SystemDrive%\\USERS\\John' ilike '\%SystemDrive\%\\\\Users%';
+--------------------------------------------------------+
|ilike(%SystemDrive%\USERS\John, \%SystemDrive\%\\Users%)|
+--------------------------------------------------------+
|                                                    true|
+--------------------------------------------------------+
SELECT '%SystemDrive%/Users/John' ilike '/%SYSTEMDrive/%//Users%' ESCAPE '/';
+--------------------------------------------------------+
|ilike(%SystemDrive%/Users/John, /%SYSTEMDrive/%//Users%)|
+--------------------------------------------------------+
|                                                    true|
+--------------------------------------------------------+
-- in
SELECT 1 in(1, 2, 3);
+----------------+
|(1 IN (1, 2, 3))|
+----------------+
|            true|
+----------------+
SELECT 1 in(2, 3, 4);
+----------------+
|(1 IN (2, 3, 4))|
+----------------+
|           false|
+----------------+
SELECT named_struct('a', 1, 'b', 2) in(named_struct('a', 1, 'b', 1), named_struct('a', 1, 'b', 3));
+----------------------------------------------------------------------------------+
|(named_struct(a, 1, b, 2) IN (named_struct(a, 1, b, 1), named_struct(a, 1, b, 3)))|
+----------------------------------------------------------------------------------+
|                                                                             false|
+----------------------------------------------------------------------------------+
SELECT named_struct('a', 1, 'b', 2) in(named_struct('a', 1, 'b', 2), named_struct('a', 1, 'b', 3));
+----------------------------------------------------------------------------------+
|(named_struct(a, 1, b, 2) IN (named_struct(a, 1, b, 2), named_struct(a, 1, b, 3)))|
+----------------------------------------------------------------------------------+
|                                                                              true|
+----------------------------------------------------------------------------------+
-- isnan
SELECT isnan(cast('NaN' as double));
+--------------------------+
|isnan(CAST(NaN AS DOUBLE))|
+--------------------------+
|                      true|
+--------------------------+
-- isnotnull
SELECT isnotnull(1);
+---------------+
|(1 IS NOT NULL)|
+---------------+
|           true|
+---------------+
-- isnull
SELECT isnull(1);
+-----------+
|(1 IS NULL)|
+-----------+
|      false|
+-----------+
-- like
SELECT like('Wagon', '_Agon');
+----------------+
|Wagon LIKE _Agon|
+----------------+
|            true|
+----------------+
-- not
SELECT not true;
+----------+
|(NOT true)|
+----------+
|     false|
+----------+
SELECT not false;
+-----------+
|(NOT false)|
+-----------+
|       true|
+-----------+
SELECT not NULL;
+----------+
|(NOT NULL)|
+----------+
|      NULL|
+----------+
-- or
SELECT true or false;
+---------------+
|(true OR false)|
+---------------+
|           true|
+---------------+
SELECT false or false;
+----------------+
|(false OR false)|
+----------------+
|           false|
+----------------+
SELECT true or NULL;
+--------------+
|(true OR NULL)|
+--------------+
|          true|
+--------------+
SELECT false or NULL;
+---------------+
|(false OR NULL)|
+---------------+
|           NULL|
+---------------+
```

#### Map functions
<a name="supported-sql-map"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| element\_at(array, index) | Returns element of array at given (1-based) index. | 
| element\_at(map, key) | Returns value for given key. The function returns NULL if the key is not contained in the map. | 
| map(key0, value0, key1, value1, ...) | Creates a map with the given key/value pairs. | 
| map\_concat(map, ...) | Returns the union of all the given maps | 
| map\_contains\_key(map, key) | Returns true if the map contains the key. | 
| map\_entries(map) | Returns an unordered array of all entries in the given map. | 
| map\_from\_arrays(keys, values) | Creates a map with a pair of the given key/value arrays. All elements in keys should not be null | 
| map\_from\_entries(arrayOfEntries) | Returns a map created from the given array of entries. | 
| map\_keys(map) | Returns an unordered array containing the keys of the map. | 
| map\_values(map) | Returns an unordered array containing the values of the map. | 
| str\_to\_map(text[, pairDelim[, keyValueDelim]]) | Creates a map after splitting the text into key/value pairs using delimiters. Default delimiters are ',' for `pairDelim` and ':' for `keyValueDelim`. Both `pairDelim` and `keyValueDelim` are treated as regular expressions. | 
| try\_element\_at(array, index) | Returns element of array at given (1-based) index. If Index is 0, the system will throw an error. If index < 0, accesses elements from the last to the first. The function always returns NULL if the index exceeds the length of the array. | 
| try\_element\_at(map, key) | Returns value for given key. The function always returns NULL if the key is not contained in the map. | 

**Examples**

```
-- element_at
SELECT element_at(array(1, 2, 3), 2);
+-----------------------------+
|element_at(array(1, 2, 3), 2)|
+-----------------------------+
|                            2|
+-----------------------------+
SELECT element_at(map(1, 'a', 2, 'b'), 2);
+------------------------------+
|element_at(map(1, a, 2, b), 2)|
+------------------------------+
|                             b|
+------------------------------+
-- map
SELECT map(1.0, '2', 3.0, '4');
+--------------------+
| map(1.0, 2, 3.0, 4)|
+--------------------+
|{1.0 -> 2, 3.0 -> 4}|
+--------------------+
-- map_concat
SELECT map_concat(map(1, 'a', 2, 'b'), map(3, 'c'));
+--------------------------------------+
|map_concat(map(1, a, 2, b), map(3, c))|
+--------------------------------------+
|                  {1 -> a, 2 -> b, ...|
+--------------------------------------+
-- map_contains_key
SELECT map_contains_key(map(1, 'a', 2, 'b'), 1);
+------------------------------------+
|map_contains_key(map(1, a, 2, b), 1)|
+------------------------------------+
|                                true|
+------------------------------------+
SELECT map_contains_key(map(1, 'a', 2, 'b'), 3);
+------------------------------------+
|map_contains_key(map(1, a, 2, b), 3)|
+------------------------------------+
|                               false|
+------------------------------------+
-- map_entries
SELECT map_entries(map(1, 'a', 2, 'b'));
+----------------------------+
|map_entries(map(1, a, 2, b))|
+----------------------------+
|            [{1, a}, {2, b}]|
+----------------------------+
-- map_from_arrays
SELECT map_from_arrays(array(1.0, 3.0), array('2', '4'));
+---------------------------------------------+
|map_from_arrays(array(1.0, 3.0), array(2, 4))|
+---------------------------------------------+
|                         {1.0 -> 2, 3.0 -> 4}|
+---------------------------------------------+
-- map_from_entries
SELECT map_from_entries(array(struct(1, 'a'), struct(2, 'b')));
+---------------------------------------------------+
|map_from_entries(array(struct(1, a), struct(2, b)))|
+---------------------------------------------------+
|                                   {1 -> a, 2 -> b}|
+---------------------------------------------------+
-- map_keys
SELECT map_keys(map(1, 'a', 2, 'b'));
+-------------------------+
|map_keys(map(1, a, 2, b))|
+-------------------------+
|                   [1, 2]|
+-------------------------+
-- map_values
SELECT map_values(map(1, 'a', 2, 'b'));
+---------------------------+
|map_values(map(1, a, 2, b))|
+---------------------------+
|                     [a, b]|
+---------------------------+
-- str_to_map
SELECT str_to_map('a:1,b:2,c:3', ',', ':');
+-----------------------------+
|str_to_map(a:1,b:2,c:3, ,, :)|
+-----------------------------+
|         {a -> 1, b -> 2, ...|
+-----------------------------+
SELECT str_to_map('a');
+-------------------+
|str_to_map(a, ,, :)|
+-------------------+
|        {a -> NULL}|
+-------------------+
-- try_element_at
SELECT try_element_at(array(1, 2, 3), 2);
+---------------------------------+
|try_element_at(array(1, 2, 3), 2)|
+---------------------------------+
|                                2|
+---------------------------------+
SELECT try_element_at(map(1, 'a', 2, 'b'), 2);
+----------------------------------+
|try_element_at(map(1, a, 2, b), 2)|
+----------------------------------+
|                                 b|
+----------------------------------+
```

#### Mathematical functions
<a name="supported-sql-math"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| expr1 % expr2 | Returns the remainder after `expr1`/`expr2`. | 
| expr1 \* expr2 | Returns `expr1`\*`expr2`. | 
| expr1 \+ expr2 | Returns `expr1`\+`expr2`. | 
| expr1 - expr2 | Returns `expr1`-`expr2`. | 
| expr1 / expr2 | Returns `expr1`/`expr2`. It always performs floating point division. | 
| abs(expr) | Returns the absolute value of the numeric or interval value. | 
| acos(expr) | Returns the inverse cosine (a.k.a. arc cosine) of `expr`, as if computed by `java.lang.Math.acos`. | 
| acosh(expr) | Returns inverse hyperbolic cosine of `expr`. | 
| asin(expr) | Returns the inverse sine (a.k.a. arc sine) the arc sin of `expr`, as if computed by `java.lang.Math.asin`. | 
| asinh(expr) | Returns inverse hyperbolic sine of `expr`. | 
| atan(expr) | Returns the inverse tangent (a.k.a. arc tangent) of `expr`, as if computed by `java.lang.Math.atan` | 
| atan2(exprY, exprX) | Returns the angle in radians between the positive x-axis of a plane and the point given by the coordinates (`exprX`, `exprY`), as if computed by `java.lang.Math.atan2`. | 
| atanh(expr) | Returns inverse hyperbolic tangent of `expr`. | 
| bin(expr) | Returns the string representation of the long value `expr` represented in binary. | 
| bround(expr, d) | Returns `expr` rounded to `d` decimal places using HALF\_EVEN rounding mode. | 
| cbrt(expr) | Returns the cube root of `expr`. | 
| ceil(expr[, scale]) | Returns the smallest number after rounding up that is not smaller than `expr`. An optional `scale` parameter can be specified to control the rounding behavior. | 
| ceiling(expr[, scale]) | Returns the smallest number after rounding up that is not smaller than `expr`. An optional `scale` parameter can be specified to control the rounding behavior. | 
| conv(num, from\_base, to\_base) | Convert `num` from `from\_base` to `to\_base`. | 
| cos(expr) | Returns the cosine of `expr`, as if computed by `java.lang.Math.cos`. | 
| cosh(expr) | Returns the hyperbolic cosine of `expr`, as if computed by `java.lang.Math.cosh`. | 
| cot(expr) | Returns the cotangent of `expr`, as if computed by `1/java.lang.Math.tan`. | 
| csc(expr) | Returns the cosecant of `expr`, as if computed by `1/java.lang.Math.sin`. | 
| degrees(expr) | Converts radians to degrees. | 
| expr1 div expr2 | Divide `expr1` by `expr2`. It returns NULL if an operand is NULL or `expr2` is 0. The result is casted to long. | 
| e() | Returns Euler's number, e. | 
| exp(expr) | Returns e to the power of `expr`. | 
| expm1(expr) - Returns exp(`expr`) | 1 | 
| factorial(expr) | Returns the factorial of `expr`. `expr` is [0..20]. Otherwise, null. | 
| floor(expr[, scale]) | Returns the largest number after rounding down that is not greater than `expr`. An optional `scale` parameter can be specified to control the rounding behavior. | 
| greatest(expr, ...) | Returns the greatest value of all parameters, skipping null values. | 
| hex(expr) | Converts `expr` to hexadecimal. | 
| hypot(expr1, expr2) | Returns sqrt(`expr1`\*\*2 \+ `expr2`\*\*2). | 
| least(expr, ...) | Returns the least value of all parameters, skipping null values. | 
| ln(expr) | Returns the natural logarithm (base e) of `expr`. | 
| log(base, expr) | Returns the logarithm of `expr` with `base`. | 
| log10(expr) | Returns the logarithm of `expr` with base 10. | 
| log1p(expr) | Returns log(1 \+ `expr`). | 
| log2(expr) | Returns the logarithm of `expr` with base 2. | 
| expr1 mod expr2 | Returns the remainder after `expr1`/`expr2`. | 
| negative(expr) | Returns the negated value of `expr`. | 
| pi() | Returns pi. | 
| pmod(expr1, expr2) | Returns the positive value of `expr1` mod `expr2`. | 
| positive(expr) | Returns the value of `expr`. | 
| pow(expr1, expr2) | Raises `expr1` to the power of `expr2`. | 
| power(expr1, expr2) | Raises `expr1` to the power of `expr2`. | 
| radians(expr) | Converts degrees to radians. | 
| rand([seed]) | Returns a random value with independent and identically distributed (i.i.d.) uniformly distributed values in [0, 1). | 
| randn([seed]) | Returns a random value with independent and identically distributed (i.i.d.) values drawn from the standard normal distribution. | 
| random([seed]) | Returns a random value with independent and identically distributed (i.i.d.) uniformly distributed values in [0, 1). | 
| rint(expr) | Returns the double value that is closest in value to the argument and is equal to a mathematical integer. | 
| round(expr, d) | Returns `expr` rounded to `d` decimal places using HALF\_UP rounding mode. | 
| sec(expr) | Returns the secant of `expr`, as if computed by `1/java.lang.Math.cos`. | 
| shiftleft(base, expr) | Bitwise left shift. | 
| sign(expr) | Returns -1.0, 0.0 or 1.0 as `expr` is negative, 0 or positive. | 
| signum(expr) | Returns -1.0, 0.0 or 1.0 as `expr` is negative, 0 or positive. | 
| sin(expr) | Returns the sine of `expr`, as if computed by `java.lang.Math.sin`. | 
| sinh(expr) | Returns hyperbolic sine of `expr`, as if computed by `java.lang.Math.sinh`. | 
| sqrt(expr) | Returns the square root of `expr`. | 
| tan(expr) | Returns the tangent of `expr`, as if computed by `java.lang.Math.tan`. | 
| tanh(expr) | Returns the hyperbolic tangent of `expr`, as if computed by `java.lang.Math.tanh`. | 
| try\_add(expr1, expr2) | Returns the sum of `expr1`and `expr2` and the result is null on overflow. The acceptable input types are the same with the `\+` operator. | 
| try\_divide(dividend, divisor) | Returns `dividend`/`divisor`. It always performs floating point division. Its result is always null if `expr2` is 0. `dividend` must be a numeric or an interval. `divisor` must be a numeric. | 
| try\_multiply(expr1, expr2) | Returns `expr1`\*`expr2` and the result is null on overflow. The acceptable input types are the same with the `\*` operator. | 
| try\_subtract(expr1, expr2) | Returns `expr1`-`expr2` and the result is null on overflow. The acceptable input types are the same with the `-` operator. | 
| unhex(expr) | Converts hexadecimal `expr` to binary. | 
| width\_bucket(value, min\_value, max\_value, num\_bucket) | Returns the bucket number to which `value` would be assigned in an equiwidth histogram with `num\_bucket` buckets, in the range `min\_value` to `max\_value`." | 

**Examples**

```
-- %
SELECT 2 % 1.8;
+---------+
|(2 % 1.8)|
+---------+
|      0.2|
+---------+
SELECT MOD(2, 1.8);
+-----------+
|mod(2, 1.8)|
+-----------+
|        0.2|
+-----------+
-- *
SELECT 2 * 3;
+-------+
|(2 * 3)|
+-------+
|      6|
+-------+
-- +
SELECT 1 + 2;
+-------+
|(1 + 2)|
+-------+
|      3|
+-------+
-- -
SELECT 2 - 1;
+-------+
|(2 - 1)|
+-------+
|      1|
+-------+
-- /
SELECT 3 / 2;
+-------+
|(3 / 2)|
+-------+
|    1.5|
+-------+
SELECT 2L / 2L;
+-------+
|(2 / 2)|
+-------+
|    1.0|
+-------+
-- abs
SELECT abs(-1);
+-------+
|abs(-1)|
+-------+
|      1|
+-------+
SELECT abs(INTERVAL -'1-1' YEAR TO MONTH);
+----------------------------------+
|abs(INTERVAL '-1-1' YEAR TO MONTH)|
+----------------------------------+
|              INTERVAL '1-1' YE...|
+----------------------------------+
-- acos
SELECT acos(1);
+-------+
|ACOS(1)|
+-------+
|    0.0|
+-------+
SELECT acos(2);
+-------+
|ACOS(2)|
+-------+
|    NaN|
+-------+
-- acosh
SELECT acosh(1);
+--------+
|ACOSH(1)|
+--------+
|     0.0|
+--------+
SELECT acosh(0);
+--------+
|ACOSH(0)|
+--------+
|     NaN|
+--------+
-- asin
SELECT asin(0);
+-------+
|ASIN(0)|
+-------+
|    0.0|
+-------+
SELECT asin(2);
+-------+
|ASIN(2)|
+-------+
|    NaN|
+-------+
-- asinh
SELECT asinh(0);
+--------+
|ASINH(0)|
+--------+
|     0.0|
+--------+
-- atan
SELECT atan(0);
+-------+
|ATAN(0)|
+-------+
|    0.0|
+-------+
-- atan2
SELECT atan2(0, 0);
+-----------+
|ATAN2(0, 0)|
+-----------+
|        0.0|
+-----------+
-- atanh
SELECT atanh(0);
+--------+
|ATANH(0)|
+--------+
|     0.0|
+--------+
SELECT atanh(2);
+--------+
|ATANH(2)|
+--------+
|     NaN|
+--------+
-- bin
SELECT bin(13);
+-------+
|bin(13)|
+-------+
|   1101|
+-------+
SELECT bin(-13);
+--------------------+
|            bin(-13)|
+--------------------+
|11111111111111111...|
+--------------------+
SELECT bin(13.3);
+---------+
|bin(13.3)|
+---------+
|     1101|
+---------+
-- bround
SELECT bround(2.5, 0);
+--------------+
|bround(2.5, 0)|
+--------------+
|             2|
+--------------+
SELECT bround(25, -1);
+--------------+
|bround(25, -1)|
+--------------+
|            20|
+--------------+
-- cbrt
SELECT cbrt(27.0);
+----------+
|CBRT(27.0)|
+----------+
|       3.0|
+----------+
-- ceil
SELECT ceil(-0.1);
+----------+
|CEIL(-0.1)|
+----------+
|         0|
+----------+
SELECT ceil(5);
+-------+
|CEIL(5)|
+-------+
|      5|
+-------+
SELECT ceil(3.1411, 3);
+---------------+
|ceil(3.1411, 3)|
+---------------+
|          3.142|
+---------------+
SELECT ceil(3.1411, -3);
+----------------+
|ceil(3.1411, -3)|
+----------------+
|            1000|
+----------------+
-- ceiling
SELECT ceiling(-0.1);
+-------------+
|ceiling(-0.1)|
+-------------+
|            0|
+-------------+
SELECT ceiling(5);
+----------+
|ceiling(5)|
+----------+
|         5|
+----------+
SELECT ceiling(3.1411, 3);
+------------------+
|ceiling(3.1411, 3)|
+------------------+
|             3.142|
+------------------+
SELECT ceiling(3.1411, -3);
+-------------------+
|ceiling(3.1411, -3)|
+-------------------+
|               1000|
+-------------------+
-- conv
SELECT conv('100', 2, 10);
+----------------+
|conv(100, 2, 10)|
+----------------+
|               4|
+----------------+
SELECT conv(-10, 16, -10);
+------------------+
|conv(-10, 16, -10)|
+------------------+
|               -16|
+------------------+
-- cos
SELECT cos(0);
+------+
|COS(0)|
+------+
|   1.0|
+------+
-- cosh
SELECT cosh(0);
+-------+
|COSH(0)|
+-------+
|    1.0|
+-------+
-- cot
SELECT cot(1);
+------------------+
|            COT(1)|
+------------------+
|0.6420926159343306|
+------------------+
-- csc
SELECT csc(1);
+------------------+
|            CSC(1)|
+------------------+
|1.1883951057781212|
+------------------+
-- degrees
SELECT degrees(3.141592653589793);
+--------------------------+
|DEGREES(3.141592653589793)|
+--------------------------+
|                     180.0|
+--------------------------+
-- div
SELECT 3 div 2;
+---------+
|(3 div 2)|
+---------+
|        1|
+---------+
SELECT INTERVAL '1-1' YEAR TO MONTH div INTERVAL '-1' MONTH;
+------------------------------------------------------+
|(INTERVAL '1-1' YEAR TO MONTH div INTERVAL '-1' MONTH)|
+------------------------------------------------------+
|                                                   -13|
+------------------------------------------------------+
-- e
SELECT e();
+-----------------+
|              E()|
+-----------------+
|2.718281828459045|
+-----------------+
-- exp
SELECT exp(0);
+------+
|EXP(0)|
+------+
|   1.0|
+------+
-- expm1
SELECT expm1(0);
+--------+
|EXPM1(0)|
+--------+
|     0.0|
+--------+
-- factorial
SELECT factorial(5);
+------------+
|factorial(5)|
+------------+
|         120|
+------------+
-- floor
SELECT floor(-0.1);
+-----------+
|FLOOR(-0.1)|
+-----------+
|         -1|
+-----------+
SELECT floor(5);
+--------+
|FLOOR(5)|
+--------+
|       5|
+--------+
SELECT floor(3.1411, 3);
+----------------+
|floor(3.1411, 3)|
+----------------+
|           3.141|
+----------------+
SELECT floor(3.1411, -3);
+-----------------+
|floor(3.1411, -3)|
+-----------------+
|                0|
+-----------------+
-- greatest
SELECT greatest(10, 9, 2, 4, 3);
+------------------------+
|greatest(10, 9, 2, 4, 3)|
+------------------------+
|                      10|
+------------------------+
-- hex
SELECT hex(17);
+-------+
|hex(17)|
+-------+
|     11|
+-------+
SELECT hex('SQL');
+------------------+
|    hex(SQL)|
+------------------+
|53514C|
+------------------+
-- hypot
SELECT hypot(3, 4);
+-----------+
|HYPOT(3, 4)|
+-----------+
|        5.0|
+-----------+
-- least
SELECT least(10, 9, 2, 4, 3);
+---------------------+
|least(10, 9, 2, 4, 3)|
+---------------------+
|                    2|
+---------------------+
-- ln
SELECT ln(1);
+-----+
|ln(1)|
+-----+
|  0.0|
+-----+
-- log
SELECT log(10, 100);
+------------+
|LOG(10, 100)|
+------------+
|         2.0|
+------------+
-- log10
SELECT log10(10);
+---------+
|LOG10(10)|
+---------+
|      1.0|
+---------+
-- log1p
SELECT log1p(0);
+--------+
|LOG1P(0)|
+--------+
|     0.0|
+--------+
-- log2
SELECT log2(2);
+-------+
|LOG2(2)|
+-------+
|    1.0|
+-------+
-- mod
SELECT 2 % 1.8;
+---------+
|(2 % 1.8)|
+---------+
|      0.2|
+---------+
SELECT MOD(2, 1.8);
+-----------+
|mod(2, 1.8)|
+-----------+
|        0.2|
+-----------+
-- negative
SELECT negative(1);
+-----------+
|negative(1)|
+-----------+
|         -1|
+-----------+
-- pi
SELECT pi();
+-----------------+
|             PI()|
+-----------------+
|3.141592653589793|
+-----------------+
-- pmod
SELECT pmod(10, 3);
+-----------+
|pmod(10, 3)|
+-----------+
|          1|
+-----------+
SELECT pmod(-10, 3);
+------------+
|pmod(-10, 3)|
+------------+
|           2|
+------------+
-- positive
SELECT positive(1);
+-----+
|(+ 1)|
+-----+
|    1|
+-----+
-- pow
SELECT pow(2, 3);
+---------+
|pow(2, 3)|
+---------+
|      8.0|
+---------+
-- power
SELECT power(2, 3);
+-----------+
|POWER(2, 3)|
+-----------+
|        8.0|
+-----------+
-- radians
SELECT radians(180);
+-----------------+
|     RADIANS(180)|
+-----------------+
|3.141592653589793|
+-----------------+
-- rand
SELECT rand();
+------------------+
|            rand()|
+------------------+
|0.7211420708112387|
+------------------+
SELECT rand(0);
+------------------+
|           rand(0)|
+------------------+
|0.7604953758285915|
+------------------+
SELECT rand(null);
+------------------+
|        rand(NULL)|
+------------------+
|0.7604953758285915|
+------------------+
-- randn
SELECT randn();
+-------------------+
|            randn()|
+-------------------+
|-0.8175603217732732|
+-------------------+
SELECT randn(0);
+------------------+
|          randn(0)|
+------------------+
|1.6034991609278433|
+------------------+
SELECT randn(null);
+------------------+
|       randn(NULL)|
+------------------+
|1.6034991609278433|
+------------------+
-- random
SELECT random();
+-----------------+
|           rand()|
+-----------------+
|0.394205008255365|
+-----------------+
SELECT random(0);
+------------------+
|           rand(0)|
+------------------+
|0.7604953758285915|
+------------------+
SELECT random(null);
+------------------+
|        rand(NULL)|
+------------------+
|0.7604953758285915|
+------------------+
-- rint
SELECT rint(12.3456);
+-------------+
|rint(12.3456)|
+-------------+
|         12.0|
+-------------+
-- round
SELECT round(2.5, 0);
+-------------+
|round(2.5, 0)|
+-------------+
|            3|
+-------------+
-- sec
SELECT sec(0);
+------+
|SEC(0)|
+------+
|   1.0|
+------+
-- shiftleft
SELECT shiftleft(2, 1);
+---------------+
|shiftleft(2, 1)|
+---------------+
|              4|
+---------------+
-- sign
SELECT sign(40);
+--------+
|sign(40)|
+--------+
|     1.0|
+--------+
SELECT sign(INTERVAL -'100' YEAR);
+--------------------------+
|sign(INTERVAL '-100' YEAR)|
+--------------------------+
|                      -1.0|
+--------------------------+
-- signum
SELECT signum(40);
+----------+
|SIGNUM(40)|
+----------+
|       1.0|
+----------+
SELECT signum(INTERVAL -'100' YEAR);
+----------------------------+
|SIGNUM(INTERVAL '-100' YEAR)|
+----------------------------+
|                        -1.0|
+----------------------------+
-- sin
SELECT sin(0);
+------+
|SIN(0)|
+------+
|   0.0|
+------+
-- sinh
SELECT sinh(0);
+-------+
|SINH(0)|
+-------+
|    0.0|
+-------+
-- sqrt
SELECT sqrt(4);
+-------+
|SQRT(4)|
+-------+
|    2.0|
+-------+
-- tan
SELECT tan(0);
+------+
|TAN(0)|
+------+
|   0.0|
+------+
-- tanh
SELECT tanh(0);
+-------+
|TANH(0)|
+-------+
|    0.0|
+-------+
-- try_add
SELECT try_add(1, 2);
+-------------+
|try_add(1, 2)|
+-------------+
|            3|
+-------------+
SELECT try_add(2147483647, 1);
+----------------------+
|try_add(2147483647, 1)|
+----------------------+
|                  NULL|
+----------------------+
SELECT try_add(date'2021-01-01', 1);
+-----------------------------+
|try_add(DATE '2021-01-01', 1)|
+-----------------------------+
|                   2021-01-02|
+-----------------------------+
SELECT try_add(date'2021-01-01', interval 1 year);
+---------------------------------------------+
|try_add(DATE '2021-01-01', INTERVAL '1' YEAR)|
+---------------------------------------------+
|                                   2022-01-01|
+---------------------------------------------+
SELECT try_add(timestamp'2021-01-01 00:00:00', interval 1 day);
+----------------------------------------------------------+
|try_add(TIMESTAMP '2021-01-01 00:00:00', INTERVAL '1' DAY)|
+----------------------------------------------------------+
|                                       2021-01-02 00:00:00|
+----------------------------------------------------------+
SELECT try_add(interval 1 year, interval 2 year);
+---------------------------------------------+
|try_add(INTERVAL '1' YEAR, INTERVAL '2' YEAR)|
+---------------------------------------------+
|                            INTERVAL '3' YEAR|
+---------------------------------------------+
-- try_divide
SELECT try_divide(3, 2);
+----------------+
|try_divide(3, 2)|
+----------------+
|             1.5|
+----------------+
SELECT try_divide(2L, 2L);
+----------------+
|try_divide(2, 2)|
+----------------+
|             1.0|
+----------------+
SELECT try_divide(1, 0);
+----------------+
|try_divide(1, 0)|
+----------------+
|            NULL|
+----------------+
SELECT try_divide(interval 2 month, 2);
+---------------------------------+
|try_divide(INTERVAL '2' MONTH, 2)|
+---------------------------------+
|             INTERVAL '0-1' YE...|
+---------------------------------+
SELECT try_divide(interval 2 month, 0);
+---------------------------------+
|try_divide(INTERVAL '2' MONTH, 0)|
+---------------------------------+
|                             NULL|
+---------------------------------+
-- try_multiply
SELECT try_multiply(2, 3);
+------------------+
|try_multiply(2, 3)|
+------------------+
|                 6|
+------------------+
SELECT try_multiply(-2147483648, 10);
+-----------------------------+
|try_multiply(-2147483648, 10)|
+-----------------------------+
|                         NULL|
+-----------------------------+
SELECT try_multiply(interval 2 year, 3);
+----------------------------------+
|try_multiply(INTERVAL '2' YEAR, 3)|
+----------------------------------+
|              INTERVAL '6-0' YE...|
+----------------------------------+
-- try_subtract
SELECT try_subtract(2, 1);
+------------------+
|try_subtract(2, 1)|
+------------------+
|                 1|
+------------------+
SELECT try_subtract(-2147483648, 1);
+----------------------------+
|try_subtract(-2147483648, 1)|
+----------------------------+
|                        NULL|
+----------------------------+
SELECT try_subtract(date'2021-01-02', 1);
+----------------------------------+
|try_subtract(DATE '2021-01-02', 1)|
+----------------------------------+
|                        2021-01-01|
+----------------------------------+
SELECT try_subtract(date'2021-01-01', interval 1 year);
+--------------------------------------------------+
|try_subtract(DATE '2021-01-01', INTERVAL '1' YEAR)|
+--------------------------------------------------+
|                                        2020-01-01|
+--------------------------------------------------+
SELECT try_subtract(timestamp'2021-01-02 00:00:00', interval 1 day);
+---------------------------------------------------------------+
|try_subtract(TIMESTAMP '2021-01-02 00:00:00', INTERVAL '1' DAY)|
+---------------------------------------------------------------+
|                                            2021-01-01 00:00:00|
+---------------------------------------------------------------+
SELECT try_subtract(interval 2 year, interval 1 year);
+--------------------------------------------------+
|try_subtract(INTERVAL '2' YEAR, INTERVAL '1' YEAR)|
+--------------------------------------------------+
|                                 INTERVAL '1' YEAR|
+--------------------------------------------------+
-- unhex
SELECT decode(unhex('53514C'), 'UTF-8');
+----------------------------------------+
|decode(unhex(53514C), UTF-8)|
+----------------------------------------+
|                               SQL|
+----------------------------------------+
-- width_bucket
SELECT width_bucket(5.3, 0.2, 10.6, 5);
+-------------------------------+
|width_bucket(5.3, 0.2, 10.6, 5)|
+-------------------------------+
|                              3|
+-------------------------------+
SELECT width_bucket(-2.1, 1.3, 3.4, 3);
+-------------------------------+
|width_bucket(-2.1, 1.3, 3.4, 3)|
+-------------------------------+
|                              0|
+-------------------------------+
SELECT width_bucket(8.1, 0.0, 5.7, 4);
+------------------------------+
|width_bucket(8.1, 0.0, 5.7, 4)|
+------------------------------+
|                             5|
+------------------------------+
SELECT width_bucket(-0.9, 5.2, 0.5, 2);
+-------------------------------+
|width_bucket(-0.9, 5.2, 0.5, 2)|
+-------------------------------+
|                              3|
+-------------------------------+
SELECT width_bucket(INTERVAL '0' YEAR, INTERVAL '0' YEAR, INTERVAL '10' YEAR, 10);
+--------------------------------------------------------------------------+
|width_bucket(INTERVAL '0' YEAR, INTERVAL '0' YEAR, INTERVAL '10' YEAR, 10)|
+--------------------------------------------------------------------------+
|                                                                         1|
+--------------------------------------------------------------------------+
SELECT width_bucket(INTERVAL '1' YEAR, INTERVAL '0' YEAR, INTERVAL '10' YEAR, 10);
+--------------------------------------------------------------------------+
|width_bucket(INTERVAL '1' YEAR, INTERVAL '0' YEAR, INTERVAL '10' YEAR, 10)|
+--------------------------------------------------------------------------+
|                                                                         2|
+--------------------------------------------------------------------------+
SELECT width_bucket(INTERVAL '0' DAY, INTERVAL '0' DAY, INTERVAL '10' DAY, 10);
+-----------------------------------------------------------------------+
|width_bucket(INTERVAL '0' DAY, INTERVAL '0' DAY, INTERVAL '10' DAY, 10)|
+-----------------------------------------------------------------------+
|                                                                      1|
+-----------------------------------------------------------------------+
SELECT width_bucket(INTERVAL '1' DAY, INTERVAL '0' DAY, INTERVAL '10' DAY, 10);
+-----------------------------------------------------------------------+
|width_bucket(INTERVAL '1' DAY, INTERVAL '0' DAY, INTERVAL '10' DAY, 10)|
+-----------------------------------------------------------------------+
|                                                                      2|
+-----------------------------------------------------------------------+
```

#### Generator functions
<a name="supported-sql-generator"></a>

**Note**  
To see which AWS data source integrations support these SQL functions, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).


****  

| Function | Description | 
| --- | --- | 
| explode(expr) | Separates the elements of array `expr` into multiple rows, or the elements of map `expr` into multiple rows and columns. Unless specified otherwise, uses the default column name `col` for elements of the array or `key` and `value` for the elements of the map. | 
| explode\_outer(expr) | Separates the elements of array `expr` into multiple rows, or the elements of map `expr` into multiple rows and columns. Unless specified otherwise, uses the default column name `col` for elements of the array or `key` and `value` for the elements of the map. | 
| inline(expr) | Explodes an array of structs into a table. Uses column names col1, col2, etc. by default unless specified otherwise. | 
| inline\_outer(expr) | Explodes an array of structs into a table. Uses column names col1, col2, etc. by default unless specified otherwise. | 
| posexplode(expr) | Separates the elements of array `expr` into multiple rows with positions, or the elements of map `expr` into multiple rows and columns with positions. Unless specified otherwise, uses the column name `pos` for position, `col` for elements of the array or `key` and `value` for elements of the map. | 
| posexplode\_outer(expr) | Separates the elements of array `expr` into multiple rows with positions, or the elements of map `expr` into multiple rows and columns with positions. Unless specified otherwise, uses the column name `pos` for position, `col` for elements of the array or `key` and `value` for elements of the map. | 
| stack(n, expr1, ..., exprk) | Separates `expr1`, ..., `exprk` into `n` rows. Uses column names col0, col1, etc. by default unless specified otherwise. | 

**Examples**

```
-- explode
SELECT explode(array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

SELECT explode(collection => array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

SELECT * FROM explode(collection => array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

-- explode_outer
SELECT explode_outer(array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

SELECT explode_outer(collection => array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

SELECT * FROM explode_outer(collection => array(10, 20));
+---+
|col|
+---+
| 10|
| 20|
+---+

-- inline
SELECT inline(array(struct(1, 'a'), struct(2, 'b')));
+----+----+
|col1|col2|
+----+----+
|   1|   a|
|   2|   b|
+----+----+

-- inline_outer
SELECT inline_outer(array(struct(1, 'a'), struct(2, 'b')));
+----+----+
|col1|col2|
+----+----+
|   1|   a|
|   2|   b|
+----+----+

-- posexplode
SELECT posexplode(array(10,20));
+---+---+
|pos|col|
+---+---+
|  0| 10|
|  1| 20|
+---+---+

SELECT * FROM posexplode(array(10,20));
+---+---+
|pos|col|
+---+---+
|  0| 10|
|  1| 20|
+---+---+

-- posexplode_outer
SELECT posexplode_outer(array(10,20));
+---+---+
|pos|col|
+---+---+
|  0| 10|
|  1| 20|
+---+---+

SELECT * FROM posexplode_outer(array(10,20));
+---+---+
|pos|col|
+---+---+
|  0| 10|
|  1| 20|
+---+---+

-- stack
SELECT stack(2, 1, 2, 3);
+----+----+
|col0|col1|
+----+----+
|   1|   2|
|   3|NULL|
+----+----+
```

#### SELECT clause
<a name="supported-sql-select"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

OpenSearch SQL supports a `SELECT` statement used for retrieving result sets from one or more tables. The following section describes the overall query syntax and the different constructs of a query.

**Syntax** 

```
select_statement 
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select_statement, ... ]
[ ORDER BY 
    { expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] 
    [ , ... ] 
    } 
]
[ SORT BY 
    { expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] 
    [ , ... ] 
    } 
]
[ WINDOW { named_window [ , WINDOW named_window, ... ] } ]
[ LIMIT { ALL | expression } ]
```

While `select_statement` is defined as:

```
SELECT [ ALL | DISTINCT ] { [ [ named_expression ] [ , ... ] ] }
FROM { from_item [ , ... ] }
[ PIVOT clause ]
[ UNPIVOT clause ]
[ LATERAL VIEW clause ] [ ... ]
[ WHERE boolean_expression ]
[ GROUP BY expression [ , ... ] ]
[ HAVING boolean_expression ]
```

 **Parameters** 
+ **ALL** 

  Selects all matching rows from the relation and is enabled by default. 
+ **DISTINCT** 

  Selects all matching rows from the relation after removing duplicates in results. 
+ **named\_expression **

  An expression with an assigned name. In general, it denotes a column expression. 

  Syntax: `expression [[AS] alias]` 
+ **from\_item **

  Table relation

  Join relation

  Pivot relation

  Unpivot relation

  Table-value function

  Inline table

  `[ LATERAL ] ( Subquery )`
+ **PIVOT** 

  The `PIVOT` clause is used for data perspective. You can get the aggregated values based on specific column value. 
+ **UNPIVOT** 

  The `UNPIVOT` clause transforms columns into rows. It is the reverse of `PIVOT`, except for aggregation of values. 
+ **LATERAL VIEW **

  The `LATERAL VIEW` clause is used in conjunction with generator functions such as `EXPLODE`, which will generate a virtual table containing one or more rows.

  `LATERAL VIEW` will apply the rows to each original output row. 
+ **WHERE** 

  Filters the result of the `FROM` clause based on the supplied predicates. 
+ **GROUP BY **

  Specifies the expressions that are used to group the rows. 

  This is used in conjunction with aggregate functions (`MIN`, `MAX`, `COUNT`, `SUM`, `AVG`, and so on) to group rows based on the grouping expressions and aggregate values in each group. 

  When a `FILTER` clause is attached to an aggregate function, only the matching rows are passed to that function. 
+ **HAVING** 

  Specifies the predicates by which the rows produced by `GROUP BY` are filtered. 

  The `HAVING` clause is used to filter rows after the grouping is performed. 

  If `HAVING` is specified without `GROUP BY`, it indicates a `GROUP BY` without grouping expressions (global aggregate). 
+ **ORDER BY **

  Specifies an ordering of the rows of the complete result set of the query. 

  The output rows are ordered across the partitions. 

  This parameter is mutually exclusive with `SORT BY` and `DISTRIBUTE BY` and can not be specified together. 
+ **SORT BY **

  Specifies an ordering by which the rows are ordered within each partition. 

  This parameter is mutually exclusive with `ORDER BY` and can not be specified together. 
+ **LIMIT** 

  Specifies the maximum number of rows that can be returned by a statement or subquery. 

  This clause is mostly used in the conjunction with `ORDER BY` to produce a deterministic result. 
+ **boolean\_expression **

  Specifies any expression that evaluates to a result type boolean. 

  Two or more expressions may be combined together using the logical operators ( `AND`, `OR` ). 
+ **expression** 

  Specifies a combination of one or more values, operators, and SQL functions that evaluates to a value. 
+ **named\_window **

  Specifies aliases for one or more source window specifications. 

  The source window specifications can be referenced in the widow definitions in the query. 

#### WHERE clause
<a name="supported-sql-where"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `WHERE` clause is used to limit the results of the `FROM` clause of a query or a subquery based on the specified condition. 

**Syntax** 

```
WHERE boolean_expression
```

**Parameters**
+ **boolean\_expression** 

  Specifies any expression that evaluates to a result type boolean. 

  Two or more expressions may be combined together using the logical operators ( `AND`, `OR` ). 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT);
INSERT INTO person VALUES
(100, 'John', 30),
(200, 'Mary', NULL),
(300, 'Mike', 80),
(400, 'Dan',  50);

-- Comparison operator in `WHERE` clause.
SELECT * FROM person WHERE id > 200 ORDER BY id;
+---+----+---+
| id|name|age|
+---+----+---+
|300|Mike| 80|
|400| Dan| 50|
+---+----+---+

-- Comparison and logical operators in `WHERE` clause.
SELECT * FROM person WHERE id = 200 OR id = 300 ORDER BY id;
+---+----+----+
| id|name| age|
+---+----+----+
|200|Mary|null|
|300|Mike|  80|
+---+----+----+

-- IS NULL expression in `WHERE` clause.
SELECT * FROM person WHERE id > 300 OR age IS NULL ORDER BY id;
+---+----+----+
| id|name| age|
+---+----+----+
|200|Mary|null|
|400| Dan|  50|
+---+----+----+

-- Function expression in `WHERE` clause.
SELECT * FROM person WHERE length(name) > 3 ORDER BY id;
+---+----+----+
| id|name| age|
+---+----+----+
|100|John|  30|
|200|Mary|null|
|300|Mike|  80|
+---+----+----+

-- `BETWEEN` expression in `WHERE` clause.
SELECT * FROM person WHERE id BETWEEN 200 AND 300 ORDER BY id;
+---+----+----+
| id|name| age|
+---+----+----+
|200|Mary|null|
|300|Mike|  80|
+---+----+----+

-- Scalar Subquery in `WHERE` clause.
SELECT * FROM person WHERE age > (SELECT avg(age) FROM person);
+---+----+---+
| id|name|age|
+---+----+---+
|300|Mike| 80|
+---+----+---+
 
-- Correlated Subquery in `WHERE` clause.
SELECT id FROM person
WHERE exists (SELECT id FROM person where id = 200);
+---+----+----+
|id |name|age |
+---+----+----+
|200|Mary|null|
+---+----+----+
```

#### GROUP BY clause
<a name="supported-sql-group-by"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `GROUP BY` clause is used to group the rows based on a set of specified grouping expressions and compute aggregations on the group of rows based on one or more specified aggregate functions. 

The system also does multiple aggregations for the same input record set via `GROUPING SETS`, `CUBE`, `ROLLUP` clauses. The grouping expressions and advanced aggregations can be mixed in the `GROUP BY` clause and nested in a `GROUPING SETS `clause. See more details in the `Mixed/Nested Grouping Analytics `section. 

When a `FILTER` clause is attached to an aggregate function, only the matching rows are passed to that function. 

**Syntax** 

```
GROUP BY group_expression [ , group_expression [ , ... ] ] [ WITH { ROLLUP | CUBE } ]
GROUP BY { group_expression | { ROLLUP | CUBE | GROUPING SETS } (grouping_set [ , ...]) } [ , ... ]
```

While aggregate functions are defined as: 

```
aggregate_name ( [ DISTINCT ] expression [ , ... ] ) [ FILTER ( WHERE boolean_expression ) ]
```

**Parameters**
+ **group\_expression **

  Specifies the criteria based on which the rows are grouped together. The grouping of rows is performed based on result values of the grouping expressions. 

  A grouping expression may be a column name like `GROUP BY a`, a column position like `GROUP BY 0`, or an expression like `GROUP BY a + b`. 
+ **grouping\_set **

  A grouping set is specified by zero or more comma-separated expressions in parentheses. When the grouping set has only one element, parentheses can be omitted. 

  For example, `GROUPING SETS ((a), (b))` is the same as `GROUPING SETS (a, b)`. 

  Syntax: `{ ( [ expression [ , ... ] ] ) | expression }` 
+ **GROUPING SETS **

  Groups the rows for each grouping set specified after `GROUPING SETS`. 

  For example, `GROUP BY GROUPING SETS ((warehouse), (product))` is semantically equivalent to union of results of `GROUP BY warehouse` and `GROUP BY product`. This clause is a shorthand for a UNION ALL where each leg of the `UNION ALL` operator performs aggregation of each grouping set specified in the `GROUPING SETS` clause. 

  Similarly, `GROUP BY GROUPING SETS ((warehouse, product), (product), ())` is semantically equivalent to the union of results of `GROUP BY warehouse, product, GROUP BY product` and global aggregate. 
+ **ROLLUP** 

  Specifies multiple levels of aggregations in a single statement. This clause is used to compute aggregations based on multiple grouping sets. `ROLLUP` is a shorthand for `GROUPING SETS`. 

  For example, `GROUP BY warehouse, product WITH ROLLUP or GROUP BY ROLLUP(warehouse, product)` is equivalent to `GROUP BY GROUPING SETS((warehouse, product), (warehouse), ())`. 

  `GROUP BY ROLLUP(warehouse, product, (warehouse, location))` is equivalent to `GROUP BY GROUPING SETS((warehouse, product, location), (warehouse, product), (warehouse), ())`.

  The N elements of a ROLLUP specification results in N\+1 GROUPING SETS. 
+ **CUBE** 

  CUBE clause is used to perform aggregations based on combination of grouping columns specified in the GROUP BY clause. CUBE is a shorthand for GROUPING SETS. 

  For example, `GROUP BY warehouse, product WITH CUBE or GROUP BY CUBE(warehouse, product)` is equivalent to `GROUP BY GROUPING SETS((warehouse, product), (warehouse), (product), ())`. 

  `GROUP BY CUBE(warehouse, product, (warehouse, location))` is equivalent to `GROUP BY GROUPING SETS((warehouse, product, location), (warehouse, product), (warehouse, location), (product, warehouse, location), (warehouse), (product), (warehouse, product), ())`. The N elements of a `CUBE` specification results in 2^N `GROUPING SETS`. 
+ **Mixed/Nested Grouping Analytics **

  A `GROUP BY` clause can include multiple group\_expressions and multiple `CUBE|ROLLUP|GROUPING SETS`. `GROUPING SETS` can also have nested `CUBE|ROLLUP|GROUPING SETS` clauses, such as `GROUPING SETS(ROLLUP(warehouse, location)`, `CUBE(warehouse, location))`, `GROUPING SETS(warehouse, GROUPING SETS(location, GROUPING SETS(ROLLUP(warehouse, location),` `CUBE(warehouse, location))))`. 

  `CUBE|ROLLUP` is just a syntax sugar for `GROUPING SETS`. Refer to the sections above for how to translate `CUBE|ROLLUP` to `GROUPING SETS`. `group_expression` can be treated as a single-group `GROUPING SETS` under this context. 

  For multiple `GROUPING SETS` in the `GROUP BY` clause, we generate a single `GROUPING SETS` by doing a cross-product of the original `GROUPING SETS`. For nested `GROUPING SETS` in the `GROUPING SETS` clause, we simply take its grouping sets and strip it. 

  For example, `GROUP BY warehouse, GROUPING SETS((product), ()), GROUPING SETS((location, size), (location), (size), ()) and GROUP BY warehouse, ROLLUP(product), CUBE(location, size)` is equivalent to `GROUP BY GROUPING SETS( (warehouse, product, location, size), (warehouse, product, location), (warehouse, product, size), (warehouse, product), (warehouse, location, size), (warehouse, location), (warehouse, size), (warehouse))`. 

  `GROUP BY GROUPING SETS(GROUPING SETS(warehouse), GROUPING SETS((warehouse, product)))` is equivalent to `GROUP BY GROUPING SETS((warehouse), (warehouse, product))`. 
+ **aggregate\_name **

  Specifies an aggregate function name (`MIN`, `MAX`, `COUNT`, `SUM`, `AVG`, and so on). 
+ **DISTINCT** 

  Removes duplicates in input rows before they are passed to aggregate functions. 
+ **FILTER** 

  Filters the input rows for which the `boolean_expression` in the `WHERE` clause evaluates to true are passed to the aggregate function; other rows are discarded. 

**Examples**

```
CREATE TABLE dealer (id INT, city STRING, car_model STRING, quantity INT);
INSERT INTO dealer VALUES
(100, 'Fremont', 'Honda Civic', 10),
(100, 'Fremont', 'Honda Accord', 15),
(100, 'Fremont', 'Honda CRV', 7),
(200, 'Dublin', 'Honda Civic', 20),
(200, 'Dublin', 'Honda Accord', 10),
(200, 'Dublin', 'Honda CRV', 3),
(300, 'San Jose', 'Honda Civic', 5),
(300, 'San Jose', 'Honda Accord', 8);

-- Sum of quantity per dealership. Group by `id`.
SELECT id, sum(quantity) FROM dealer GROUP BY id ORDER BY id;
+---+-------------+
| id|sum(quantity)|
+---+-------------+
|100|           32|
|200|           33|
|300|           13|
+---+-------------+

-- Use column position in GROUP by clause.
SELECT id, sum(quantity) FROM dealer GROUP BY 1 ORDER BY 1;
+---+-------------+
| id|sum(quantity)|
+---+-------------+
|100|           32|
|200|           33|
|300|           13|
+---+-------------+

-- Multiple aggregations.
-- 1. Sum of quantity per dealership.
-- 2. Max quantity per dealership.
SELECT id, sum(quantity) AS sum, max(quantity) AS max FROM dealer GROUP BY id ORDER BY id;
+---+---+---+
| id|sum|max|
+---+---+---+
|100| 32| 15|
|200| 33| 20|
|300| 13|  8|
+---+---+---+

-- Count the number of distinct dealer cities per car_model.
SELECT car_model, count(DISTINCT city) AS count FROM dealer GROUP BY car_model;
+------------+-----+
|   car_model|count|
+------------+-----+
| Honda Civic|    3|
|   Honda CRV|    2|
|Honda Accord|    3|
+------------+-----+

-- Sum of only 'Honda Civic' and 'Honda CRV' quantities per dealership.
SELECT id, sum(quantity) FILTER (
WHERE car_model IN ('Honda Civic', 'Honda CRV')
) AS `sum(quantity)` FROM dealer
GROUP BY id ORDER BY id;
+---+-------------+
| id|sum(quantity)|
+---+-------------+
|100|           17|
|200|           23|
|300|            5|
+---+-------------+

-- Aggregations using multiple sets of grouping columns in a single statement.
-- Following performs aggregations based on four sets of grouping columns.
-- 1. city, car_model
-- 2. city
-- 3. car_model
-- 4. Empty grouping set. Returns quantities for all city and car models.
SELECT city, car_model, sum(quantity) AS sum FROM dealer
GROUP BY GROUPING SETS ((city, car_model), (city), (car_model), ())
ORDER BY city;
+---------+------------+---+
|     city|   car_model|sum|
+---------+------------+---+
|     null|        null| 78|
|     null| HondaAccord| 33|
|     null|    HondaCRV| 10|
|     null|  HondaCivic| 35|
|   Dublin|        null| 33|
|   Dublin| HondaAccord| 10|
|   Dublin|    HondaCRV|  3|
|   Dublin|  HondaCivic| 20|
|  Fremont|        null| 32|
|  Fremont| HondaAccord| 15|
|  Fremont|    HondaCRV|  7|
|  Fremont|  HondaCivic| 10|
| San Jose|        null| 13|
| San Jose| HondaAccord|  8|
| San Jose|  HondaCivic|  5|
+---------+------------+---+

-- Group by processing with `ROLLUP` clause.
-- Equivalent GROUP BY GROUPING SETS ((city, car_model), (city), ())
SELECT city, car_model, sum(quantity) AS sum FROM dealer
GROUP BY city, car_model WITH ROLLUP
ORDER BY city, car_model;
+---------+------------+---+
|     city|   car_model|sum|
+---------+------------+---+
|     null|        null| 78|
|   Dublin|        null| 33|
|   Dublin| HondaAccord| 10|
|   Dublin|    HondaCRV|  3|
|   Dublin|  HondaCivic| 20|
|  Fremont|        null| 32|
|  Fremont| HondaAccord| 15|
|  Fremont|    HondaCRV|  7|
|  Fremont|  HondaCivic| 10|
| San Jose|        null| 13|
| San Jose| HondaAccord|  8|
| San Jose|  HondaCivic|  5|
+---------+------------+---+

-- Group by processing with `CUBE` clause.
-- Equivalent GROUP BY GROUPING SETS ((city, car_model), (city), (car_model), ())
SELECT city, car_model, sum(quantity) AS sum FROM dealer
GROUP BY city, car_model WITH CUBE
ORDER BY city, car_model;
+---------+------------+---+
|     city|   car_model|sum|
+---------+------------+---+
|     null|        null| 78|
|     null| HondaAccord| 33|
|     null|    HondaCRV| 10|
|     null|  HondaCivic| 35|
|   Dublin|        null| 33|
|   Dublin| HondaAccord| 10|
|   Dublin|    HondaCRV|  3|
|   Dublin|  HondaCivic| 20|
|  Fremont|        null| 32|
|  Fremont| HondaAccord| 15|
|  Fremont|    HondaCRV|  7|
|  Fremont|  HondaCivic| 10|
| San Jose|        null| 13|
| San Jose| HondaAccord|  8|
| San Jose|  HondaCivic|  5|
+---------+------------+---+

--Prepare data for ignore nulls example
CREATE TABLE person (id INT, name STRING, age INT);
INSERT INTO person VALUES
(100, 'Mary', NULL),
(200, 'John', 30),
(300, 'Mike', 80),
(400, 'Dan', 50);

--Select the first row in column age
SELECT FIRST(age) FROM person;
+--------------------+
| first(age, false)  |
+--------------------+
| NULL               |
+--------------------+

--Get the first row in column `age` ignore nulls,last row in column `id` and sum of column `id`.
SELECT FIRST(age IGNORE NULLS), LAST(id), SUM(id) FROM person;
+-------------------+------------------+----------+
| first(age, true)  | last(id, false)  | sum(id)  |
+-------------------+------------------+----------+
| 30                | 400              | 1000     |
+-------------------+------------------+----------+
```

#### HAVING clause
<a name="supported-sql-having"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `HAVING` clause is used to filter the results produced by `GROUP BY` based on the specified condition. It is often used in conjunction with a `GROUP BY` clause. 

**Syntax** 

```
HAVING boolean_expression
```

**Parameters**
+ **boolean\_expression **

  Specifies any expression that evaluates to a result type boolean. Two or more expressions may be combined together using the logical operators ( `AND`, `OR` ). 

  **Note** The expressions specified in the `HAVING` clause can only refer to: 

  1. Constants 

  1. Expressions that appear in `GROUP BY` 

  1. Aggregate functions 

**Examples**

```
CREATE TABLE dealer (id INT, city STRING, car_model STRING, quantity INT);
INSERT INTO dealer VALUES
(100, 'Fremont', 'Honda Civic', 10),
(100, 'Fremont', 'Honda Accord', 15),
(100, 'Fremont', 'Honda CRV', 7),
(200, 'Dublin', 'Honda Civic', 20),
(200, 'Dublin', 'Honda Accord', 10),
(200, 'Dublin', 'Honda CRV', 3),
(300, 'San Jose', 'Honda Civic', 5),
(300, 'San Jose', 'Honda Accord', 8);

-- `HAVING` clause referring to column in `GROUP BY`.
SELECT city, sum(quantity) AS sum FROM dealer GROUP BY city HAVING city = 'Fremont';
+-------+---+
|   city|sum|
+-------+---+
|Fremont| 32|
+-------+---+

-- `HAVING` clause referring to aggregate function.
SELECT city, sum(quantity) AS sum FROM dealer GROUP BY city HAVING sum(quantity) > 15;
+-------+---+
|   city|sum|
+-------+---+
| Dublin| 33|
|Fremont| 32|
+-------+---+

-- `HAVING` clause referring to aggregate function by its alias.
SELECT city, sum(quantity) AS sum FROM dealer GROUP BY city HAVING sum > 15;
+-------+---+
|   city|sum|
+-------+---+
| Dublin| 33|
|Fremont| 32|
+-------+---+

-- `HAVING` clause referring to a different aggregate function than what is present in
-- `SELECT` list.
SELECT city, sum(quantity) AS sum FROM dealer GROUP BY city HAVING max(quantity) > 15;
+------+---+
|  city|sum|
+------+---+
|Dublin| 33|
+------+---+

-- `HAVING` clause referring to constant expression.
SELECT city, sum(quantity) AS sum FROM dealer GROUP BY city HAVING 1 > 0 ORDER BY city;
+--------+---+
|    city|sum|
+--------+---+
|  Dublin| 33|
| Fremont| 32|
|San Jose| 13|
+--------+---+

-- `HAVING` clause without a `GROUP BY` clause.
SELECT sum(quantity) AS sum FROM dealer HAVING sum(quantity) > 10;
+---+
|sum|
+---+
| 78|
+---+
```

#### ORDER BY clause
<a name="supported-sql-order-by"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `ORDER BY` clause is used to return the result rows in a sorted manner in the user specified order. Unlike the SORT BY clause, this clause guarantees a total order in the output. 

**Syntax** 

```
ORDER BY { expression [ sort_direction | nulls_sort_order ] [ , ... ] }
```

**Parameters**
+ **ORDER BY **

  Specifies a comma-separated list of expressions along with optional parameters `sort_direction` and `nulls_sort_order` which are used to sort the rows. 
+ **sort\_direction **

  Optionally specifies whether to sort the rows in ascending or descending order. 

  The valid values for the sort direction are `ASC` for ascending and `DESC` for descending. 

  If sort direction is not explicitly specified, then by default rows are sorted ascending. 

  Syntax: `[ ASC | DESC ] `
+ **nulls\_sort\_order **

  Optionally specifies whether `NULL` values are returned before/after non-NULL values. 

  If null\_sort\_order is not specified, then `NULLs` sort first if sort order is `ASC` and NULLS sort last if sort order is `DESC`. 

  1. If `NULLS FIRST` is specified, then NULL values are returned first regardless of the sort order. 

  2. If `NULLS LAST` is specified, then NULL values are returned last regardless of the sort order. 

  Syntax: `[ NULLS { FIRST | LAST } ]` 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT);
INSERT INTO person VALUES
(100, 'John', 30),
(200, 'Mary', NULL),
(300, 'Mike', 80),
(400, 'Jerry', NULL),
(500, 'Dan',  50);

-- Sort rows by age. By default rows are sorted in ascending manner with NULL FIRST.
SELECT name, age FROM person ORDER BY age;
+-----+----+
| name| age|
+-----+----+
|Jerry|null|
| Mary|null|
| John|  30|
|  Dan|  50|
| Mike|  80|
+-----+----+

-- Sort rows in ascending manner keeping null values to be last.
SELECT name, age FROM person ORDER BY age NULLS LAST;
+-----+----+
| name| age|
+-----+----+
| John|  30|
|  Dan|  50|
| Mike|  80|
| Mary|null|
|Jerry|null|
+-----+----+

-- Sort rows by age in descending manner, which defaults to NULL LAST.
SELECT name, age FROM person ORDER BY age DESC;
+-----+----+
| name| age|
+-----+----+
| Mike|  80|
|  Dan|  50|
| John|  30|
|Jerry|null|
| Mary|null|
+-----+----+

-- Sort rows in ascending manner keeping null values to be first.
SELECT name, age FROM person ORDER BY age DESC NULLS FIRST;
+-----+----+
| name| age|
+-----+----+
|Jerry|null|
| Mary|null|
| Mike|  80|
|  Dan|  50|
| John|  30|
+-----+----+

-- Sort rows based on more than one column with each column having different
-- sort direction.
SELECT * FROM person ORDER BY name ASC, age DESC;
+---+-----+----+
| id| name| age|
+---+-----+----+
|500|  Dan|  50|
|400|Jerry|null|
|100| John|  30|
|200| Mary|null|
|300| Mike|  80|
+---+-----+----+
```

#### JOIN clause
<a name="supported-sql-join"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

A SQL join is used to combine rows from two relations based on join criteria. The following section describes the overall join syntax and the different types of joins along with examples. 

**Syntax** 

```
relation INNER JOIN relation [ join_criteria ]
```

**Parameters**
+ **relation **

  Specifies the relation to be joined. 
+ **join\_type **

  Specifies the join type. 

  Syntax: `INNER | CROSS | LEFT OUTER`
+ **join\_criteria **

  Specifies how the rows from one relation will be combined with the rows of another relation. 

  Syntax: `ON boolean_expression | USING ( column_name [ , ... ] ) `
+ **boolean\_expression **

  Specifies an expression with a return type of boolean. 

**Join types**
+ **Inner Join**

  The inner join needs to be explicitly specified. It selects rows that have matching values in both relations.

  Syntax: `relation INNER JOIN relation [ join_criteria ] `
+ **Left Join **

  A left join returns all values from the left relation and the matched values from the right relation, or appends NULL if there is no match. It is also referred to as a left outer join. 

  Syntax: `relation LEFT OUTER JOIN relation [ join_criteria ]` 
+ **Cross Join **

  A cross join returns the Cartesian product of two relations. 

  Syntax: `relation CROSS JOIN relation [ join_criteria ]` 

**Examples**

```
-- Use employee and department tables to demonstrate different type of joins.
SELECT * FROM employee;
+---+-----+------+
| id| name|deptno|
+---+-----+------+
|105|Chloe|     5|
|103| Paul|     3|
|101| John|     1|
|102| Lisa|     2|
|104| Evan|     4|
|106|  Amy|     6|
+---+-----+------+
SELECT * FROM department;
+------+-----------+
|deptno|   deptname|
+------+-----------+
|     3|Engineering|
|     2|      Sales|
|     1|  Marketing|
+------+-----------+

-- Use employee and department tables to demonstrate inner join.
SELECT id, name, employee.deptno, deptname
FROM employee INNER JOIN department ON employee.deptno = department.deptno;
+---+-----+------+-----------|
| id| name|deptno|   deptname|
+---+-----+------+-----------|
|103| Paul|     3|Engineering|
|101| John|     1|  Marketing|
|102| Lisa|     2|      Sales|
+---+-----+------+-----------|

-- Use employee and department tables to demonstrate left join.
SELECT id, name, employee.deptno, deptname
FROM employee LEFT JOIN department ON employee.deptno = department.deptno;
+---+-----+------+-----------|
| id| name|deptno|   deptname|
+---+-----+------+-----------|
|105|Chloe|     5|       NULL|
|103| Paul|     3|Engineering|
|101| John|     1|  Marketing|
|102| Lisa|     2|      Sales|
|104| Evan|     4|       NULL|
|106|  Amy|     6|       NULL|
+---+-----+------+-----------|

-- Use employee and department tables to demonstrate cross join.
SELECT id, name, employee.deptno, deptname FROM employee CROSS JOIN department;
+---+-----+------+-----------|
| id| name|deptno|   deptname|
+---+-----+------+-----------|
|105|Chloe|     5|Engineering|
|105|Chloe|     5|  Marketing|
|105|Chloe|     5|      Sales|
|103| Paul|     3|Engineering|
|103| Paul|     3|  Marketing|
|103| Paul|     3|      Sales|
|101| John|     1|Engineering|
|101| John|     1|  Marketing|
|101| John|     1|      Sales|
|102| Lisa|     2|Engineering|
|102| Lisa|     2|  Marketing|
|102| Lisa|     2|      Sales|
|104| Evan|     4|Engineering|
|104| Evan|     4|  Marketing|
|104| Evan|     4|      Sales|
|106|  Amy|     4|Engineering|
|106|  Amy|     4|  Marketing|
|106|  Amy|     4|      Sales|
+---+-----+------+-----------|
```

#### LIMIT clause
<a name="supported-sql-limit"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `LIMIT` clause is used to constrain the number of rows returned by the `SELECT` statement. In general, this clause is used in conjunction with `ORDER BY` to ensure that the results are deterministic. 

**Syntax** 

```
LIMIT { ALL | integer_expression }
```

**Parameters**
+ **ALL**

  If specified, the query returns all the rows. In other words, no limit is applied if this option is specified. 
+ **integer\_expression **

  Specifies a foldable expression that returns an integer. 

**Examples**

```
CREATE TABLE person (name STRING, age INT);
INSERT INTO person VALUES
('Jane Doe', 25),
('Pat C', 18),
('Nikki W', 16),
('John D', 25),
('Juan L', 18),
('Jorge S', 16);

-- Select the first two rows.
SELECT name, age FROM person ORDER BY name LIMIT 2;
+-------+---+
|   name|age|
+-------+---+
|  Pat C| 18|
|Jorge S| 16|
+------+---+

-- Specifying ALL option on LIMIT returns all the rows.
SELECT name, age FROM person ORDER BY name LIMIT ALL;
+--------+---+
|    name|age|
+--------+---+
|   Pat C| 18|
| Jorge S| 16|
|  Juan L| 18|
|  John D| 25|
| Nikki W| 16|
|Jane Doe| 25|
+--------+---+

-- A function expression as an input to LIMIT.
SELECT name, age FROM person ORDER BY name LIMIT length('OPENSEARCH');
+-------+---+
|   name|age|
+-------+---+
|  Pat C| 18|
|Jorge S| 16|
| Juan L| 18|
| John D| 25|
|Nikki W| 16|
+-------+---+
```

#### CASE clause
<a name="supported-sql-case"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `CASE` clause uses a rule to return a specific result based on the specified condition, similar to if/else statements in other programming languages. 

**Syntax** 

```
CASE [ expression ] { WHEN boolean_expression THEN then_expression } [ ... ]
[ ELSE else_expression ]
END
```

**Parameters**
+ **boolean\_expression **

  Specifies any expression that evaluates to a result type boolean. 

  Two or more expressions may be combined together using the logical operators ( `AND`, `OR` ). 
+ **then\_expression **

  Specifies the then expression based on the boolean\_expression condition.

  `then_expression` and `else_expression` should all be same type or coercible to a common type. 
+ **else\_expression **

  Specifies the default expression.

  `then_expression` and` else_expression` should all be same type or coercible to a common type. 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT);
INSERT INTO person VALUES
(100, 'John', 30),
(200, 'Mary', NULL),
(300, 'Mike', 80),
(400, 'Dan', 50);
SELECT id, CASE WHEN id > 200 THEN 'bigger' ELSE 'small' END FROM person;
+------+--------------------------------------------------+
|  id  | CASE WHEN (id > 200) THEN bigger ELSE small END  |
+------+--------------------------------------------------+
| 100  | small                                            |
| 200  | small                                            |
| 300  | bigger                                           |
| 400  | bigger                                           |
+------+--------------------------------------------------+
SELECT id, CASE id WHEN 100 then 'bigger' WHEN  id > 300 THEN '300' ELSE 'small' END FROM person;
+------+-----------------------------------------------------------------------------------------------+
|  id  | CASE WHEN (id = 100) THEN bigger WHEN (id = CAST((id > 300) AS INT)) THEN 300 ELSE small END  |
+------+-----------------------------------------------------------------------------------------------+
| 100  | bigger                                                                                        |
| 200  | small                                                                                         |
| 300  | small                                                                                         |
| 400  | small                                                                                         |
+------+-----------------------------------------------------------------------------------------------+
```

#### Common table expression
<a name="supported-sql-cte"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

A common table expression (CTE) defines a temporary result set that a user can reference possibly multiple times within the scope of a SQL statement. A CTE is used mainly in a `SELECT` statement. 

**Syntax** 

```
WITH common_table_expression [ , ... ]
```

While `common_table_expression` is defined as:

```
Syntexpression_name [ ( column_name [ , ... ] ) ] [ AS ] ( query )
```

**Parameters** 
+ **expression\_name **

  Specifies a name for the common table expression. 
+ **query** 

  A `SELECT` statement. 

**Examples**

```
-- CTE with multiple column aliases
WITH t(x, y) AS (SELECT 1, 2)
SELECT * FROM t WHERE x = 1 AND y = 2;
+---+---+
|  x|  y|
+---+---+
|  1|  2|
+---+---+

-- CTE in CTE definition
WITH t AS (
WITH t2 AS (SELECT 1)
SELECT * FROM t2
)
SELECT * FROM t;
+---+
|  1|
+---+
|  1|
+---+

-- CTE in subquery
SELECT max(c) FROM (
WITH t(c) AS (SELECT 1)
SELECT * FROM t
);
+------+
|max(c)|
+------+
|     1|
+------+

-- CTE in subquery expression
SELECT (
WITH t AS (SELECT 1)
SELECT * FROM t
);
+----------------+
|scalarsubquery()|
+----------------+
|               1|
+----------------+

-- CTE in CREATE VIEW statement
CREATE VIEW v AS
WITH t(a, b, c, d) AS (SELECT 1, 2, 3, 4)
SELECT * FROM t;
SELECT * FROM v;
+---+---+---+---+
|  a|  b|  c|  d|
+---+---+---+---+
|  1|  2|  3|  4|
+---+---+---+---+
```

#### EXPLAIN
<a name="supported-sql-explain"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `EXPLAIN` statement is used to provide logical/physical plans for an input statement. By default, this clause provides information about a physical plan only. 

**Syntax** 

```
EXPLAIN [ EXTENDED | CODEGEN | COST | FORMATTED ] statement
```

**Parameters**
+ **EXTENDED** 

  Generates parsed logical plan, analyzed logical plan, optimized logical plan and physical plan. 

  Parsed Logical plan is a unresolved plan that extracted from the query. 

  Analyzed logical plans transforms which translates `unresolvedAttribute` and `unresolvedRelation` into fully typed objects. 

  The optimized logical plan transforms through a set of optimization rules, resulting in the physical plan. 
+ **CODEGEN** 

  Generates code for the statement, if any and a physical plan. 
+ **COST** 

  If plan node statistics are available, generates a logical plan and the statistics. 
+ **FORMATTED** 

  Generates two sections: a physical plan outline and node details. 
+ **statement** 

  Specifies a SQL statement to be explained. 

**Examples**

```
-- Default Output
EXPLAIN select k, sum(v) from values (1, 2), (1, 3) t(k, v) group by k;
+----------------------------------------------------+
|                                                plan|
+----------------------------------------------------+
| == Physical Plan ==
*(2) HashAggregate(keys=[k#33], functions=[sum(cast(v#34 as bigint))])
+- Exchange hashpartitioning(k#33, 200), true, [id=#59]
+- *(1) HashAggregate(keys=[k#33], functions=[partial_sum(cast(v#34 as bigint))])
+- *(1) LocalTableScan [k#33, v#34]
|
+----------------------------------------------------

-- Using Extended
EXPLAIN EXTENDED select k, sum(v) from values (1, 2), (1, 3) t(k, v) group by k;
+----------------------------------------------------+
|                                                plan|
+----------------------------------------------------+
| == Parsed Logical Plan ==
'Aggregate ['k], ['k, unresolvedalias('sum('v), None)]
 +- 'SubqueryAlias `t`
+- 'UnresolvedInlineTable [k, v], [List(1, 2), List(1, 3)]
   
 == Analyzed Logical Plan ==
 k: int, sum(v): bigint
 Aggregate [k#47], [k#47, sum(cast(v#48 as bigint)) AS sum(v)#50L]
 +- SubqueryAlias `t`
    +- LocalRelation [k#47, v#48]
   
 == Optimized Logical Plan ==
 Aggregate [k#47], [k#47, sum(cast(v#48 as bigint)) AS sum(v)#50L]
 +- LocalRelation [k#47, v#48]
   
 == Physical Plan ==
 *(2) HashAggregate(keys=[k#47], functions=[sum(cast(v#48 as bigint))], output=[k#47, sum(v)#50L])
+- Exchange hashpartitioning(k#47, 200), true, [id=#79]
   +- *(1) HashAggregate(keys=[k#47], functions=[partial_sum(cast(v#48 as bigint))], output=[k#47, sum#52L])
    +- *(1) LocalTableScan [k#47, v#48]
|
+----------------------------------------------------+

-- Using Formatted
EXPLAIN FORMATTED select k, sum(v) from values (1, 2), (1, 3) t(k, v) group by k;
+----------------------------------------------------+
|                                                plan|
+----------------------------------------------------+
| == Physical Plan ==
 * HashAggregate (4)
 +- Exchange (3)
    +- * HashAggregate (2)
       +- * LocalTableScan (1)
   
   
 (1) LocalTableScan [codegen id : 1]
 Output: [k#19, v#20]
        
 (2) HashAggregate [codegen id : 1]
 Input: [k#19, v#20]
        
 (3) Exchange
 Input: [k#19, sum#24L]
        
 (4) HashAggregate [codegen id : 2]
 Input: [k#19, sum#24L]
|
+----------------------------------------------------+
```

#### LATERAL SUBQUERY clause
<a name="supported-sql-lateral-subquery"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

`LATERAL SUBQUERY` is a subquery that is preceded by the keyword `LATERAL`. It provides a way to reference columns in the preceding `FROM` clause. Without the `LATERAL` keyword, subqueries can only refer to columns in the outer query, but not in the `FROM` clause. `LATERAL SUBQUERY` makes the complicated queries simpler and more efficient. 

**Syntax** 

```
[ LATERAL ] primary_relation [ join_relation ]
```

**Parameters**
+ **primary\_relation **

  Specifies the primary relation. It can be one of the following: 

  1. Table relation 

  1. Aliased query 

     Syntax: `( query ) [ [ AS ] alias ] `

  1. Aliased relation 

     `Syntax: ( relation ) [ [ AS ] alias ]` 

**Examples**

```
CREATE TABLE t1 (c1 INT, c2 INT);
INSERT INTO t1 VALUES (0, 1), (1, 2);
CREATE TABLE t2 (c1 INT, c2 INT);
INSERT INTO t2 VALUES (0, 2), (0, 3);
SELECT * FROM t1,
LATERAL (SELECT * FROM t2 WHERE t1.c1 = t2.c1);
+--------+-------+--------+-------+
|  t1.c1 | t1.c2 |  t2.c1 | t2.c2 |
+-------+--------+--------+-------+
|    0   |   1   |    0   |   3   |
|    0   |   1   |    0   |   2   |
+-------+--------+--------+-------+
SELECT a, b, c FROM t1,
LATERAL (SELECT c1 + c2 AS a),
LATERAL (SELECT c1 - c2 AS b),
LATERAL (SELECT a * b AS c);
+--------+-------+--------+
|    a   |   b   |    c   |
+-------+--------+--------+
|    3   |  -1   |   -3   |
|    1   |  -1   |   -1   |
+-------+--------+--------+
```

#### LATERAL VIEW clause
<a name="supported-sql-lateral-view"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `LATERAL VIEW` clause is used in conjunction with generator functions such as `EXPLODE`, which will generate a virtual table containing one or more rows. `LATERAL VIEW` will apply the rows to each original output row. 

**Syntax** 

```
LATERAL VIEW [ OUTER ] generator_function ( expression [ , ... ] ) [ table_alias ] AS column_alias [ , ... ]
```

**Parameters**
+ **OUTER**

  If `OUTER` specified, returns null if an input array/map is empty or null. 
+ **generator\_function **

  Specifies a generator function (`EXPLODE`, `INLINE`, and so on.). 
+ **table\_alias **

  The alias for `generator_function`, which is optional. 
+ **column\_alias **

  Lists the column aliases of `generator_function`, which may be used in output rows. 

  You can have multiple aliases if `generator_function` has multiple output columns. 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT, class INT, address STRING);
INSERT INTO person VALUES
(100, 'John', 30, 1, 'Street 1'),
(200, 'Mary', NULL, 1, 'Street 2'),
(300, 'Mike', 80, 3, 'Street 3'),
(400, 'Dan', 50, 4, 'Street 4');
SELECT * FROM person
LATERAL VIEW EXPLODE(ARRAY(30, 60)) tableName AS c_age
LATERAL VIEW EXPLODE(ARRAY(40, 80)) AS d_age;
+------+-------+-------+--------+-----------+--------+--------+
|  id  | name  |  age  | class  |  address  | c_age  | d_age  |
+------+-------+-------+--------+-----------+--------+--------+
| 100  | John  | 30    | 1      | Street 1  | 30     | 40     |
| 100  | John  | 30    | 1      | Street 1  | 30     | 80     |
| 100  | John  | 30    | 1      | Street 1  | 60     | 40     |
| 100  | John  | 30    | 1      | Street 1  | 60     | 80     |
| 200  | Mary  | NULL  | 1      | Street 2  | 30     | 40     |
| 200  | Mary  | NULL  | 1      | Street 2  | 30     | 80     |
| 200  | Mary  | NULL  | 1      | Street 2  | 60     | 40     |
| 200  | Mary  | NULL  | 1      | Street 2  | 60     | 80     |
| 300  | Mike  | 80    | 3      | Street 3  | 30     | 40     |
| 300  | Mike  | 80    | 3      | Street 3  | 30     | 80     |
| 300  | Mike  | 80    | 3      | Street 3  | 60     | 40     |
| 300  | Mike  | 80    | 3      | Street 3  | 60     | 80     |
| 400  | Dan   | 50    | 4      | Street 4  | 30     | 40     |
| 400  | Dan   | 50    | 4      | Street 4  | 30     | 80     |
| 400  | Dan   | 50    | 4      | Street 4  | 60     | 40     |
| 400  | Dan   | 50    | 4      | Street 4  | 60     | 80     |
+------+-------+-------+--------+-----------+--------+--------+
SELECT c_age, COUNT(1) FROM person
LATERAL VIEW EXPLODE(ARRAY(30, 60)) AS c_age
LATERAL VIEW EXPLODE(ARRAY(40, 80)) AS d_age
GROUP BY c_age;
+--------+-----------+
| c_age  | count(1)  |
+--------+-----------+
| 60     | 8         |
| 30     | 8         |
+--------+-----------+
SELECT * FROM person
LATERAL VIEW EXPLODE(ARRAY()) tableName AS c_age;
+-----+-------+------+--------+----------+--------+
| id  | name  | age  | class  | address  | c_age  |
+-----+-------+------+--------+----------+--------+
+-----+-------+------+--------+----------+--------+
SELECT * FROM person
LATERAL VIEW OUTER EXPLODE(ARRAY()) tableName AS c_age;
+------+-------+-------+--------+-----------+--------+
|  id  | name  |  age  | class  |  address  | c_age  |
+------+-------+-------+--------+-----------+--------+
| 100  | John  | 30    | 1      | Street 1  | NULL   |
| 200  | Mary  | NULL  | 1      | Street 2  | NULL   |
| 300  | Mike  | 80    | 3      | Street 3  | NULL   |
| 400  | Dan   | 50    | 4      | Street 4  | NULL   |
+------+-------+-------+--------+-----------+--------+
```

#### LIKE predicate
<a name="supported-sql-like-predicate"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

A `LIKE` predicate is used to search for a specific pattern. This predicate also supports multiple patterns with quantifiers include `ANY`, `SOME`, and `ALL`. 

**Syntax** 

```
[ NOT ] { LIKE search_pattern [ ESCAPE esc_char ] | [ RLIKE | REGEXP ] regex_pattern }
[ NOT ] { LIKE quantifiers ( search_pattern [ , ... ]) }
```

**Parameters**
+ **search\_pattern **

  Specifies a string pattern to be searched by the LIKE clause. It can contain special pattern-matching characters: 
  + `%` matches zero or more characters. 
  + `_` matches exactly one character. 
+ **esc\_char **

  Specifies the escape character. The default escape character is `\`. 
+ **regex\_pattern **

  Specifies a regular expression search pattern to be searched by the `RLIKE` or `REGEXP` clause. 
+ **quantifiers** 

  Specifies the predicate quantifiers include `ANY`, `SOME` and `ALL`. 

  `ANY` or `SOME` means if one of the patterns matches the input, then return true.

  `ALL` means if all the patterns matches the input, then return true. 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT);
INSERT INTO person VALUES
(100, 'John', 30),
(200, 'Mary', NULL),
(300, 'Mike', 80),
(400, 'Dan',  50),
(500, 'Evan_w', 16);
SELECT * FROM person WHERE name LIKE 'M%';
+---+----+----+
| id|name| age|
+---+----+----+
|300|Mike|  80|
|200|Mary|null|
+---+----+----+
SELECT * FROM person WHERE name LIKE 'M_ry';
+---+----+----+
| id|name| age|
+---+----+----+
|200|Mary|null|
+---+----+----+
SELECT * FROM person WHERE name NOT LIKE 'M_ry';
+---+------+---+
| id|  name|age|
+---+------+---+
|500|Evan_W| 16|
|300|  Mike| 80|
|100|  John| 30|
|400|   Dan| 50|
+---+------+---+
SELECT * FROM person WHERE name RLIKE 'M+';
+---+----+----+
| id|name| age|
+---+----+----+
|300|Mike|  80|
|200|Mary|null|
+---+----+----+
SELECT * FROM person WHERE name REGEXP 'M+';
+---+----+----+
| id|name| age|
+---+----+----+
|300|Mike|  80|
|200|Mary|null|
+---+----+----+
SELECT * FROM person WHERE name LIKE '%\_%';
+---+------+---+
| id|  name|age|
+---+------+---+
|500|Evan_W| 16|
+---+------+---+
SELECT * FROM person WHERE name LIKE '%$_%' ESCAPE '$';
+---+------+---+
| id|  name|age|
+---+------+---+
|500|Evan_W| 16|
+---+------+---+
SELECT * FROM person WHERE name LIKE ALL ('%an%', '%an');
+---+----+----+
| id|name| age|
+---+----+----+
|400| Dan|  50|
+---+----+----+
SELECT * FROM person WHERE name LIKE ANY ('%an%', '%an');
+---+------+---+
| id|  name|age|
+---+------+---+
|400|   Dan| 50|
|500|Evan_W| 16|
+---+------+---+
SELECT * FROM person WHERE name LIKE SOME ('%an%', '%an');
+---+------+---+
| id|  name|age|
+---+------+---+
|400|   Dan| 50|
|500|Evan_W| 16|
+---+------+---+
SELECT * FROM person WHERE name NOT LIKE ALL ('%an%', '%an');
+---+----+----+
| id|name| age|
+---+----+----+
|100|John|  30|
|200|Mary|null|
|300|Mike|  80|
+---+----+----+
SELECT * FROM person WHERE name NOT LIKE ANY ('%an%', '%an');
+---+------+----+
| id|  name| age|
+---+------+----+
|100|  John|  30|
|200|  Mary|null|
|300|  Mike|  80|
|500|Evan_W|  16|
+---+------+----+
SELECT * FROM person WHERE name NOT LIKE SOME ('%an%', '%an');
+---+------+----+
| id|  name| age|
+---+------+----+
|100|  John|  30|
|200|  Mary|null|
|300|  Mike|  80|
|500|Evan_W|  16|
+---+------+----+
```

#### OFFSET
<a name="supported-sql-offset"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `OFFSET` clause is used to specify the number of rows to skip before beginning to return rows returned by the `SELECT` statement. In general, this clause is used in conjunction with `ORDER BY` to ensure that the results are deterministic. 

**Syntax** 

```
OFFSET integer_expression
```

**Parameters**
+ **integer\_expression **

  Specifies a foldable expression that returns an integer. 

**Examples**

```
CREATE TABLE person (name STRING, age INT);
INSERT INTO person VALUES
('Jane Doe', 25),
('Pat C', 18),
('Nikki W', 16),
('Juan L', 25),
('John D', 18),
('Jorge S', 16);

-- Skip the first two rows.
SELECT name, age FROM person ORDER BY name OFFSET 2;
+-------+---+
|   name|age|
+-------+---+
| John D| 18|
| Juan L| 25|
|Nikki W| 16|
|Jane Doe| 25|
+-------+---+

-- Skip the first two rows and returns the next three rows.
SELECT name, age FROM person ORDER BY name LIMIT 3 OFFSET 2;
+-------+---+
|   name|age|
+-------+---+
| John D| 18|
| Juan L| 25|
|Nikki W| 16|
+-------+---+

-- A function expression as an input to OFFSET.
SELECT name, age FROM person ORDER BY name OFFSET length('WAGON');
+-------+---+
|   name|age|
+-------+---+
|Jane Doe| 25|
+-------+---+
```

#### PIVOT clause
<a name="supported-sql-pivot"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `PIVOT` clause is used for data perspective. We can get the aggregated values based on specific column values, which will be turned to multiple columns used in `SELECT` clause. The `PIVOT` clause can be specified after the table name or subquery. 

**Syntax** 

```
PIVOT ( { aggregate_expression [ AS aggregate_expression_alias ] } [ , ... ] FOR column_list IN ( expression_list ) ) 
```

**Parameters** 
+ **aggregate\_expression**

  Specifies an aggregate expression `(SUM(a)`, `COUNT(DISTINCT b)`, and so on.). 
+ **aggregate\_expression\_alias**

  Specifies an alias for the aggregate expression. 
+ **column\_list**

  Contains columns in the `FROM` clause, which specifies the columns you want to replace with new columns. You can use brackets to surround the columns, such as `(c1, c2)`. 
+ **expression\_list**

  Specifies new columns, which are used to match values in `column_list` as the aggregating condition. You can also add aliases for them. 

**Examples**

```
CREATE TABLE person (id INT, name STRING, age INT, class INT, address STRING);
INSERT INTO person VALUES
(100, 'John', 30, 1, 'Street 1'),
(200, 'Mary', NULL, 1, 'Street 2'),
(300, 'Mike', 80, 3, 'Street 3'),
(400, 'Dan', 50, 4, 'Street 4');
SELECT * FROM person
PIVOT (
SUM(age) AS a, AVG(class) AS c
FOR name IN ('John' AS john, 'Mike' AS mike)
);
+------+-----------+---------+---------+---------+---------+
|  id  |  address  | john_a  | john_c  | mike_a  | mike_c  |
+------+-----------+---------+---------+---------+---------+
| 200  | Street 2  | NULL    | NULL    | NULL    | NULL    |
| 100  | Street 1  | 30      | 1.0     | NULL    | NULL    |
| 300  | Street 3  | NULL    | NULL    | 80      | 3.0     |
| 400  | Street 4  | NULL    | NULL    | NULL    | NULL    |
+------+-----------+---------+---------+---------+---------+
SELECT * FROM person
PIVOT (
SUM(age) AS a, AVG(class) AS c
FOR (name, age) IN (('John', 30) AS c1, ('Mike', 40) AS c2)
);
+------+-----------+-------+-------+-------+-------+
|  id  |  address  | c1_a  | c1_c  | c2_a  | c2_c  |
+------+-----------+-------+-------+-------+-------+
| 200  | Street 2  | NULL  | NULL  | NULL  | NULL  |
| 100  | Street 1  | 30    | 1.0   | NULL  | NULL  |
| 300  | Street 3  | NULL  | NULL  | NULL  | NULL  |
| 400  | Street 4  | NULL  | NULL  | NULL  | NULL  |
+------+-----------+-------+-------+-------+-------+
```

#### Set operators
<a name="supported-sql-set"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

Set operators are used to combine two input relations into a single one. OpenSearch SQL supports three types of set operators: 
+ `EXCEPT` or `MINUS`
+ `INTERSECT` 
+ `UNION` 

Input relations must have the same number of columns and compatible data types for the respective columns. 

**EXCEPT** 

`EXCEPT` and `EXCEPT ALL` return the rows that are found in one relation but not the other. `EXCEPT` (alternatively, `EXCEPT DISTINCT`) takes only distinct rows while `EXCEPT ALL` does not remove duplicates from the result rows. Note that `MINUS` is an alias for `EXCEPT`. 

**Syntax** 

```
 [ ( ] relation [ ) ] EXCEPT | MINUS [ ALL | DISTINCT ] [ ( ] relation [ ) ] 
```

**Examples**

```
-- Use table1 and table2 tables to demonstrate set operators in this page.
SELECT * FROM table1;
+---+
|  c|
+---+
|  3|
|  1|
|  2|
|  2|
|  3|
|  4|
+---+
SELECT * FROM table2;
+---+
|  c|
+---+
|  5|
|  1|
|  2|
|  2|
+---+
SELECT c FROM table1 EXCEPT SELECT c FROM table2;
+---+
|  c|
+---+
|  3|
|  4|
+---+
SELECT c FROM table1 MINUS SELECT c FROM table2;
+---+
|  c|
+---+
|  3|
|  4|
+---+
SELECT c FROM table1 EXCEPT ALL (SELECT c FROM table2);
+---+
|  c|
+---+
|  3|
|  3|
|  4|
+---+
SELECT c FROM table1 MINUS ALL (SELECT c FROM table2);
+---+
|  c|
+---+
|  3|
|  3|
|  4|
+---+
```

**INTERSECT** 

`INTERSECT` and `INTERSECT ALL` return the rows that are found in both relations. `INTERSECT` (alternatively, `INTERSECT DISTINCT`) takes only distinct rows while `INTERSECT ALL` does not remove duplicates from the result rows.

**Syntax** 

```
 [ ( ] relation [ ) ] INTERSECT [ ALL | DISTINCT ] [ ( ] relation [ ) ]
```

**Examples**

```
(SELECT c FROM table1) INTERSECT (SELECT c FROM table2);
+---+
|  c|
+---+
|  1|
|  2|
+---+
(SELECT c FROM table1) INTERSECT DISTINCT (SELECT c FROM table2);
+---+
|  c|
+---+
|  1|
|  2|
+---+
(SELECT c FROM table1) INTERSECT ALL (SELECT c FROM table2);
+---+
|  c|
+---+
|  1|
|  2|
|  2|
+---+
```

**UNION** 

`UNION` and `UNION ALL` return the rows that are found in either relation. `UNION` (alternatively, `UNION DISTINCT`) takes only distinct rows while `UNION ALL` does not remove duplicates from the result rows.

**Syntax** 

```
 [ ( ] relation [ ) ] UNION [ ALL | DISTINCT ] [ ( ] relation [ ) ]
```

**Examples**

```
(SELECT c FROM table1) UNION (SELECT c FROM table2);
+---+
|  c|
+---+
|  1|
|  3|
|  5|
|  4|
|  2|
+---+
(SELECT c FROM table1) UNION DISTINCT (SELECT c FROM table2);
+---+
|  c|
+---+
|  1|
|  3|
|  5|
|  4|
|  2|
+---+
SELECT c FROM table1 UNION ALL (SELECT c FROM table2);
+---+
|  c|
+---+
|  3|
|  1|
|  2|
|  2|
|  3|
|  4|
|  5|
|  1|
|  2|
|  2|
+---+
```

#### SORT BY clause
<a name="supported-sql-sort-by"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `SORT BY` clause is used to return the result rows sorted within each partition in the user specified order. When there is more than one partition `SORT BY` may return result that is partially ordered. This is different than `ORDER BY` clause which guarantees a total order of the output. 

**Syntax** 

```
SORT BY { expression [ sort_direction | nulls_sort_order ] [ , ... ] }
```

**Parameters**
+ **SORT BY **

  Specifies a comma-separated list of expressions along with optional parameters sort\_direction and nulls\_sort\_order which are used to sort the rows within each partition. 
+ **sort\_direction **

  Optionally specifies whether to sort the rows in ascending or descending order. 

  The valid values for the sort direction are `ASC` for ascending and `DESC` for descending. 

  If sort direction is not explicitly specified, then by default rows are sorted ascending. 

  Syntax: `[ ASC | DESC ]` 
+ **nulls\_sort\_order **

  Optionally specifies whether NULL values are returned before/after non-NULL values. 

  If `null_sort_order` is not specified, then NULLs sort first if the sort order is `ASC` and NULLS sort last if the sort order is `DESC`. 

  1. If `NULLS FIRST` is specified, then NULL values are returned first regardless of the sort order. 

  2. If `NULLS LAST` is specified, then NULL values are returned last regardless of the sort order. 

  Syntax: `[ NULLS { FIRST | LAST } ] `

**Examples**

```
CREATE TABLE person (zip_code INT, name STRING, age INT);
INSERT INTO person VALUES
(94588, 'Shirley Rodriguez', 50),
(94588, 'Juan Li', 18),
(94588, 'Anil K', 27),
(94588, 'John D', NULL),
(94511, 'David K', 42),
(94511, 'Aryan B.', 18),
(94511, 'Lalit B.', NULL);
-- Sort rows by `name` within each partition in ascending manner
SELECT name, age, zip_code FROM person SORT BY name;
+------------------+----+--------+
|              name| age|zip_code|
+------------------+----+--------+
|            Anil K|  27|   94588|
|           Juan Li|  18|   94588|
|            John D|null|   94588|
| Shirley Rodriguez|  50|   94588|
|          Aryan B.|  18|   94511|
|           David K|  42|   94511|
|          Lalit B.|null|   94511|
+------------------+----+--------+
-- Sort rows within each partition using column position.
SELECT name, age, zip_code FROM person SORT BY 1;
+----------------+----+----------+
|              name| age|zip_code|
+------------------+----+--------+
|            Anil K|  27|   94588|
|           Juan Li|  18|   94588|
|            John D|null|   94588|
| Shirley Rodriguez|  50|   94588|
|          Aryan B.|  18|   94511|
|           David K|  42|   94511|
|          Lalit B.|null|   94511|
+------------------+----+--------+

-- Sort rows within partition in ascending manner keeping null values to be last.
SELECT age, name, zip_code FROM person SORT BY age NULLS LAST;
+----+------------------+--------+
| age|              name|zip_code|
+----+------------------+--------+
|  18|           Juan Li|   94588|
|  27|            Anil K|   94588|
|  50| Shirley Rodriguez|   94588|
|null|            John D|   94588|
|  18|          Aryan B.|   94511|
|  42|           David K|   94511|
|null|          Lalit B.|   94511|
+--------------+--------+--------+

-- Sort rows by age within each partition in descending manner, which defaults to NULL LAST.
SELECT age, name, zip_code FROM person SORT BY age DESC;
+----+------------------+--------+
| age|              name|zip_code|
+----+------------------+--------+
|  50|          Shirley Rodriguez|   94588|
|  27|            Anil K|   94588|
|  18|           Juan Li|   94588|
|null|            John D|   94588|
|  42|           David K|   94511|
|  18|          Aryan B.|   94511|
|null|          Lalit B.|   94511|
+----+------------------+--------+

-- Sort rows by age within each partition in descending manner keeping null values to be first.
SELECT age, name, zip_code FROM person SORT BY age DESC NULLS FIRST;
+----+------------------+--------+
| age|              name|zip_code|
+----+------------------+--------+
|null|            John D|   94588|
|  50| Shirley Rodriguez|   94588|
|  27|            Anil K|   94588|
|  18|           Juan Li|   94588|
|null|          Lalit B.|   94511|
|  42|           David K|   94511|
|  18|          Aryan B.|   94511|
+--------------+--------+--------+

-- Sort rows within each partition based on more than one column with each column having
-- different sort direction.
SELECT name, age, zip_code FROM person
SORT BY name ASC, age DESC;
+------------------+----+--------+
|              name| age|zip_code|
+------------------+----+--------+
|            Anil K|  27|   94588|
|           Juan Li|  18|   94588|
|            John D|null|   94588|
| Shirley Rodriguez|  50|   94588|
|          Aryan B.|  18|   94511|
|           David K|  42|   94511|
|          Lalit B.|null|   94511|
+------------------+----+--------+
```

#### UNPIVOT
<a name="supported-sql-unpivot"></a>

**Note**  
To see which AWS data source integrations support this SQL command, see [Supported OpenSearch SQL commands and functions](#supported-directquery-sql).

The `UNPIVOT` clause transforms multiple columns into multiple rows used in `SELECT` clause. The `UNPIVOT` clause can be specified after the table name or subquery. 

**Syntax** 

```
UNPIVOT [ { INCLUDE | EXCLUDE } NULLS ] (
    { single_value_column_unpivot | multi_value_column_unpivot }
) [[AS] alias]

single_value_column_unpivot:
    values_column
    FOR name_column
    IN (unpivot_column [[AS] alias] [, ...])

multi_value_column_unpivot:
    (values_column [, ...])
    FOR name_column
    IN ((unpivot_column [, ...]) [[AS] alias] [, ...])
```

**Parameters**
+ **unpivot\_column **

  Contains columns in the `FROM` clause, which specifies the columns we want to unpivot. 
+ **name\_column **

  The name for the column that holds the names of the unpivoted columns. 
+ **values\_column **

  The name for the column that holds the values of the unpivoted columns. 

**Examples**

```
CREATE TABLE sales_quarterly (year INT, q1 INT, q2 INT, q3 INT, q4 INT);
INSERT INTO sales_quarterly VALUES
(2020, null, 1000, 2000, 2500),
(2021, 2250, 3200, 4200, 5900),
(2022, 4200, 3100, null, null);
-- column names are used as unpivot columns
SELECT * FROM sales_quarterly
UNPIVOT (
sales FOR quarter IN (q1, q2, q3, q4)
);
+------+---------+-------+
| year | quarter | sales |
+------+---------+-------+
| 2020 | q2      | 1000  |
| 2020 | q3      | 2000  |
| 2020 | q4      | 2500  |
| 2021 | q1      | 2250  |
| 2021 | q2      | 3200  |
| 2021 | q3      | 4200  |
| 2021 | q4      | 5900  |
| 2022 | q1      | 4200  |
| 2022 | q2      | 3100  |
+------+---------+-------+
-- NULL values are excluded by default, they can be included
-- unpivot columns can be alias
-- unpivot result can be referenced via its alias
SELECT up.* FROM sales_quarterly
UNPIVOT INCLUDE NULLS (
sales FOR quarter IN (q1 AS Q1, q2 AS Q2, q3 AS Q3, q4 AS Q4)
) AS up;
+------+---------+-------+
| year | quarter | sales |
+------+---------+-------+
| 2020 | Q1      | NULL  |
| 2020 | Q2      | 1000  |
| 2020 | Q3      | 2000  |
| 2020 | Q4      | 2500  |
| 2021 | Q1      | 2250  |
| 2021 | Q2      | 3200  |
| 2021 | Q3      | 4200  |
| 2021 | Q4      | 5900  |
| 2022 | Q1      | 4200  |
| 2022 | Q2      | 3100  |
| 2022 | Q3      | NULL  |
| 2022 | Q4      | NULL  |
+------+---------+-------+
-- multiple value columns can be unpivoted per row
SELECT * FROM sales_quarterly
UNPIVOT EXCLUDE NULLS (
(first_quarter, second_quarter)
FOR half_of_the_year IN (
(q1, q2) AS H1,
(q3, q4) AS H2
)
);
+------+------------------+---------------+----------------+
|  id  | half_of_the_year | first_quarter | second_quarter |
+------+------------------+---------------+----------------+
| 2020 | H1               | NULL          | 1000           |
| 2020 | H2               | 2000          | 2500           |
| 2021 | H1               | 2250          | 3200           |
| 2021 | H2               | 4200          | 5900           |
| 2022 | H1               | 4200          | 3100           |
+------+------------------+---------------+----------------+
```