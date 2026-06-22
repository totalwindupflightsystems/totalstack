---
id: "@specs/aws/timestream-influxdb/docs/bitwise-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bitwise functions"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Bitwise functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/bitwise-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Bitwise functions
<a name="bitwise-functions"></a>

Timestream for LiveAnalytics supports the following bitwise functions.


| Function | Output data type | Description | 
| --- | --- | --- | 
| bit\_count(bigint, bigint) | bigint (two's complement) | Returns the count of bits in the first bigint parameter where the second parameter is a bit signed integer such as 8 or 64.<pre>SELECT bit_count(19, 8)</pre><br />Example result: `3`<pre>SELECT bit_count(19, 2)</pre><br />Example result: `Number must be representable with the bits specified. 19 can not be represented with 2 bits`  | 
| bitwise\_and(bigint, bigint) | bigint (two's complement) | Returns the bitwise AND of the bigint parameters.<pre>SELECT bitwise_and(12, 7)</pre><br />Example result: `4` | 
| bitwise\_not(bigint) | bigint (two's complement) | Returns the bitwise NOT of the bigint parameter.<pre>SELECT bitwise_not(12)</pre><br />Example result: `-13` | 
| bitwise\_or(bigint, bigint) | bigint (two's complement) | Returns the bitwise OR of the bigint parameters.<pre>SELECT bitwise_or(12, 7)</pre><br />Example result: `15` | 
| bitwise\_xor(bigint, bigint) | bigint (two's complement) | Returns the bitwise XOR of the bigint parameters.<pre>SELECT bitwise_xor(12, 7)</pre><br />Example result: `11` | 