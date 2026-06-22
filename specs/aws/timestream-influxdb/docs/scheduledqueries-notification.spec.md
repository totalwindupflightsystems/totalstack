---
id: "@specs/aws/timestream-influxdb/docs/scheduledqueries-notification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Notification messages"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Notification messages

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/scheduledqueries-notification
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Scheduled query notification messages
<a name="scheduledqueries-notification"></a>

This section describes the messages sent by Timestream for LiveAnalytics when creating, deleting, running, or updating the state of a scheduled query. 


| Notification message name | Structure | Description | 
| --- | --- | --- | 
| CreatingNotificationMessage |  <pre>CreatingNotificationMessage {<br />    String arn;<br />    NotificationType type;<br />}</pre>  | This notification message is sent before sending the response for `CreateScheduledQuery`. The scheduled query is enabled after sending this notification. <br />*arn* - The ARN of the scheduled query that is being created.<br />*type* - SCHEDULED\_QUERY\_CREATING | 
| UpdateNotificationMessage |  <pre> UpdateNotificationMessage {<br />    String arn;<br />    NotificationType type;<br />    QueryState state;<br />}</pre>  | This notification message is sent when a scheduled query is updated. Timestream for LiveAnalytics can disable the scheduled query, automatically, in case non-recoverable error is encountered, such as:[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/scheduledqueries-notification.html)<br />*arn* - The ARN of the scheduled query that is being updated.<br />*type* - SCHEDULED\_QUERY\_UPDATE<br />*state* - ENABLED or DISABLED | 
| DeleteNotificationMessage |  <pre>DeletionNotificationMessage {<br />    String arn;<br />    NotificationType type;<br />}</pre>  | This notification message is sent when a scheduled query has been deleted. <br />*arn* - The ARN of the scheduled query that is being created.<br />*type* - SCHEDULED\_QUERY\_DELETED | 
| SuccessNotificationMessage |  <pre>SuccessNotificationMessage {<br />    NotificationType type;<br />    String arn;<br />    Date nextInvocationEpochSecond;<br />    ScheduledQueryRunSummary runSummary;<br />}<br /><br />ScheduledQueryRunSummary {<br />    Date invocationTime;<br />    Date triggerTime;<br />    String runStatus;<br />    ExecutionStats executionstats;<br />    ErrorReportLocation errorReportLocation;<br />    String failureReason;<br />}<br /><br /><br />ExecutionStats {<br />    Long bytesMetered;<br />    Long dataWrites;<br />    Long queryResultRows;<br />    Long recordsIngested;<br />    Long executionTimeInMillis;<br />}<br /><br /><br />ErrorReportLocation {<br />    S3ReportLocation s3ReportLocation;<br />}<br /><br /><br />S3ReportLocation {<br />    String bucketName;<br />    String objectKey;<br />}</pre>  | This notification message is sent after the scheduled query is run and the results are successfully ingested. <br />*ARN* - The ARN of the scheduled query that is being deleted.<br />*NotificationType* - AUTO\_TRIGGER\_SUCCESS or MANUAL\_TRIGGER\_SUCCESS.<br />*nextInvocationEpochSecond* - The next time Timestream for LiveAnalytics will run the scheduled query.<br />*runSummary* - Information about the scheduled query run. | 
| FailureNotificationMessage |  <pre>FailureNotificationMessage {<br />    NotificationType type;<br />    String arn;<br />    ScheduledQueryRunSummary runSummary;<br />}<br /><br />ScheduledQueryRunSummary {<br />    Date invocationTime;<br />    Date triggerTime;<br />    String runStatus;<br />    ExecutionStats executionstats;<br />    ErrorReportLocation errorReportLocation;<br />    String failureReason;<br />}<br /><br /><br />ExecutionStats {<br />    Long bytesMetered;<br />    Long dataWrites;<br />    Long queryResultRows;<br />    Long recordsIngested;<br />    Long executionTimeInMillis;<br />}<br /><br /><br />ErrorReportLocation {<br />    S3ReportLocation s3ReportLocation;<br />}<br /><br /><br />S3ReportLocation {<br />    String bucketName;<br />    String objectKey;<br />}</pre>  | This notification message is sent when a failure is encountered during a scheduled query run or when ingesting the query results. <br />*arn* - The ARN of the scheduled query that is being run.<br />*type* - AUTO\_TRIGGER\_FAILURE or MANUAL\_TRIGGER\_FAILURE.<br />*runSummary* - Information about the scheduled query run. | 