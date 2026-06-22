---
id: "@specs/aws/timestream-influxdb/docs/supported-sql-constructs.UNLOAD"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UNLOAD"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# UNLOAD

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/supported-sql-constructs.UNLOAD
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# UNLOAD
<a name="supported-sql-constructs.UNLOAD"></a>

Timestream for LiveAnalytics supports an `UNLOAD` command as an extension to its SQL support. Data types supported by `UNLOAD` are described in [Supported data types](supported-data-types.md). The `time` and `unknown` types do not apply to `UNLOAD`.

```
UNLOAD (SELECT statement)
 TO 's3://bucket-name/folder'
 WITH ( option = expression [, ...] )
```

where option is

```
{ partitioned_by = ARRAY[ col_name[,…] ] 
 | format = [ '{ CSV | PARQUET }' ] 
 | compression = [ '{ GZIP | NONE }' ]
 | encryption = [ '{ SSE_KMS | SSE_S3 }' ]
 | kms_key = '<string>'
 | field_delimiter ='<character>'
 | escaped_by = '<character>'
 | include_header = ['{true, false}']
 | max_file_size = '<value>'
}
```

SELECT statement  
The query statement used to select and retrieve data from one or more Timestream for LiveAnalytics tables.   

```
(SELECT column 1, column 2, column 3 from database.table
      where measure_name = "ABC" and timestamp between ago (1d) and now() )
```

TO clause  

```
TO 's3://bucket-name/folder'
```
or  

```
TO 's3://access-point-alias/folder'
```
The `TO` clause in the `UNLOAD` statement specifies the destination for the output of the query results. You need to provide the full path, including either Amazon S3 bucket-name or Amazon S3 access-point-alias with folder location on Amazon S3 where Timestream for LiveAnalytics writes the output file objects. The S3 bucket should be owned by the same account and in the same region. In addition to the query result set, Timestream for LiveAnalytics writes the manifest and metadata files to specified destination folder. 

PARTITIONED\_BY clause  

```
partitioned_by = ARRAY [col_name[,…] , (default: none)
```
The `partitioned_by` clause is used in queries to group and analyze data at a granular level. When you export your query results to the S3 bucket, you can choose to partition the data based on one or more columns in the select query. When partitioning the data, the exported data is divided into subsets based on the partition column and each subset is stored in a separate folder. Within the results folder that contains your exported data, a sub-folder `folder/results/partition column = partition value/` is automatically created. However, note that partitioned columns are not included in the output file.   
`partitioned_by` is not a mandatory clause in the syntax. If you choose to export the data without any partitioning, you can exclude the clause in the syntax.   

**Example**  
Assuming you are monitoring clickstream data of your website and have 5 channels of traffic namely `direct`, `Social Media`, `Organic Search`, `Other`, and `Referral`. When exporting the data, you can choose to partition the data using the column `Channel`. Within your data folder, `s3://bucketname/results`, you will have five folders each with their respective channel name, for instance, `s3://bucketname/results/channel=Social Media/.` Within this folder you will find the data of all the customers that landed on your website through the `Social Media` channel. Similarly, you will have other folders for the remaining channels.
Exported data partitioned by Channel column  

![S3 bucket showing five folders organized by channel: Direct, Organic search, Other, Referral, and Social media.](http://docs.aws.amazon.com/timestream/latest/developerguide/images/unload-results.png)


FORMAT  

```
format = [ '{ CSV | PARQUET }' , default: CSV
```
The keywords to specify the format of the query results written to your S3 bucket. You can export the data either as a comma separated value (CSV) using a comma (,) as the default delimiter or in the Apache Parquet format, an efficient open columnar storage format for analytics. 

COMPRESSION  

```
compression = [ '{ GZIP | NONE }' ], default: GZIP
```
You can compress the exported data using compression algorithm GZIP or have it uncompressed by specifying the `NONE` option.

ENCRYPTION  

```
encryption = [ '{ SSE_KMS | SSE_S3 }' ], default: SSE_S3
```
The output files on Amazon S3 are encrypted using your selected encryption option. In addition to your data, the manifest and metadata files are also encrypted based on your selected encryption option. We currently support SSE\_S3 and SSE\_KMS encryption. SSE\_S3 is a server-side encryption with Amazon S3 encrypting the data using 256-bit advanced encryption standard (AES) encryption. SSE\_KMS is a server-side encryption to encrypt data using customer-managed keys.

KMS\_KEY  

```
kms_key = '<string>'
```
KMS Key is a customer-defined key to encrypt exported query results. KMS Key is securely managed by AWS Key Management Service (AWS KMS) and used to encrypt data files on Amazon S3.

FIELD\_DELIMITER  

```
field_delimiter ='<character>' , default: (,)
```
When exporting the data in CSV format, this field specifies a single ASCII character that is used to separate fields in the output file, such as pipe character (\|), a comma (,), or tab (/t). The default delimiter for CSV files is a comma character. If a value in your data contains the chosen delimiter, the delimiter will be quoted with a quote character. For instance, if the value in your data contains `Time,stream`, then this value will be quoted as `"Time,stream"` in the exported data. The quote character used by Timestream for LiveAnalytics is double quotes (").  
Avoid specifying the carriage return character (ASCII 13, hex `0D`, text '\\r') or the line break character (ASCII 10, hex 0A, text '\\n') as the `FIELD_DELIMITER` if you want to include headers in the CSV, since that will prevent many parsers from being able to parse the headers correctly in the resulting CSV output.

ESCAPED\_BY  

```
escaped_by = '<character>', default: (\)
```
When exporting the data in CSV format, this field specifies the character that should be treated as an escape character in the data file written to S3 bucket. Escaping happens in the following scenarios:  

1. If the value itself contains the quote character (") then it will be escaped using an escape character. For example, if the value is `Time"stream`, where (\\) is the configured escape character, then it will be escaped as `Time\"stream`. 

1. If the value contains the configured escape character, it will be escaped. For example, if the value is `Time\stream`, then it will be escaped as `Time\\stream`. 
If the exported output contains complex data type in the like Arrays, Rows or Timeseries, it will be serialized as a JSON string. Following is an example.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/supported-sql-constructs.UNLOAD.html)

INCLUDE\_HEADER  

```
include_header = 'true' , default: 'false'
```
When exporting the data in CSV format, this field lets you include column names as the first row of the exported CSV data files.  
The accepted values are 'true' and 'false' and the default value is 'false'. Text transformation options such as `escaped_by` and `field_delimiter` apply to headers as well.  
When including headers, it is important that you not select a carriage return character (ASCII 13, hex 0D, text '\\r') or a line break character (ASCII 10, hex 0A, text '\\n') as the `FIELD_DELIMITER`, since that will prevent many parsers from being able to parse the headers correctly in the resulting CSV output.

MAX\_FILE\_SIZE  

```
max_file_size = 'X[MB|GB]' , default: '78GB'
```
This field specifies the maximum size of the files that the `UNLOAD` statement creates in Amazon S3. The `UNLOAD` statement can create multiple files but the maximum size of each file written to Amazon S3 will be approximately what is specified in this field.  
The value of the field must be between 16 MB and 78 GB, inclusive. You can specify it in integer such as `12GB`, or in decimals such as `0.5GB` or `24.7MB`. The default value is 78 GB.  
The actual file size is approximated when the file is being written, so the actual maximum size may not be exactly equal to the number you specify.