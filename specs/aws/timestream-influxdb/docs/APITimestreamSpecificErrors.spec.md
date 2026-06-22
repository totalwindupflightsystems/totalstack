---
id: "@specs/aws/timestream-influxdb/docs/APITimestreamSpecificErrors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Timestream for LiveAnalytics specific error codes"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Timestream for LiveAnalytics specific error codes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/APITimestreamSpecificErrors
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Timestream for LiveAnalytics specific error codes
<a name="APITimestreamSpecificErrors"></a>

This section contains the specific error codes for Timestream for LiveAnalytics. 

## Timestream for LiveAnalytics write API errors
<a name="APITimestreamSpecificErrors.write"></a>

****InternalServerException****  
 HTTP Status Code: 500

**ThrottlingException**  
 HTTP Status Code: 429

**ValidationException**  
 HTTP Status Code: 400

**ConflictException**  
 HTTP Status Code: 409

**AccessDeniedException**  
You do not have sufficient access to perform this action.  
 HTTP Status Code: 403

**ServiceQuotaExceededException**  
 HTTP Status Code: 402

**ResourceNotFoundException**  
 HTTP Status Code: 404

**RejectedRecordsException**  
 HTTP Status Code: 419

**InvalidEndpointException**  
 HTTP Status Code: 421

## Timestream for LiveAnalytics query API errors
<a name="APITimestreamSpecificErrors.query"></a>

**ValidationException**  
 HTTP Status Code: 400

**QueryExecutionException**  
 HTTP Status Code: 400

**ConflictException**  
 HTTP Status Code: 409

**ThrottlingException**  
 HTTP Status Code: 429

**InternalServerException**  
 HTTP Status Code: 500

**InvalidEndpointException**  
 HTTP Status Code: 421