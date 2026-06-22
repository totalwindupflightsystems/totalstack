---
id: "@specs/aws/timestream-influxdb/docs/ODBC-connecting-troubleshooting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Troubleshooting

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/ODBC-connecting-troubleshooting
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Troubleshooting connection with the ODBC driver
<a name="ODBC-connecting-troubleshooting"></a>

**Note**  
When the username and password are already specified in the DSN, there is no need to specify them again when the ODBC driver manager asks for them.

An error code of `01S02` with a message, `Re-writing {{(connection string option)}} (have you specified it several times?` occurs when a connection string option is passed more than once in the connection string. Specifying an option more than once raises an error. When making a connection with a DSN and a connection string, if a connection option is already specified in the DSN, do not specify it again in the connection string.