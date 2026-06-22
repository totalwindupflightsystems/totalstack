---
id: "@specs/aws/emr/docs/API_S3LoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3LoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# S3LoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_S3LoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3LoggingConfiguration
<a name="API_S3LoggingConfiguration"></a>

Configuration for S3 logging behavior in EMR clusters. Defines how different types of logs are uploaded to S3 based on the specified upload policies for each log type.

## Contents
<a name="API_S3LoggingConfiguration_Contents"></a>

 ** LogTypeUploadPolicy **   <a name="EMR-Type-S3LoggingConfiguration-LogTypeUploadPolicy"></a>
A map that specifies the upload policy for each log type. The key is the log type, and the value is the upload policy.  
Valid log types:  
+  `system-logs`: EMR Daemon logs.
+  `application-logs`: Framework logs from Hadoop, Spark, Hive and other applications running on the cluster.
+  `persistent-ui-logs`: Logs required for persistent application UIs such as Spark History Server and Tez UI.
Valid upload policies:  
+  `emr-managed`: Standard behavior. Logs are uploaded to S3 bucket as configured in your LogUri, with certain logs retained by the service for operational support and troubleshooting purposes.
+  `on-customer-s3only`: Logs are uploaded only to the customer-specified S3 bucket. This requires you to specify a LogUri when creating the cluster. Persistent-ui-logs cannot have on-customer-s3only policy. Allowed policies for persistent-ui-logs are emr-managed and disabled.
+  `disabled`: No S3 upload for this log type.
Type: String to string map  
Valid Keys: `system-logs | application-logs | persistent-ui-logs`   
Valid Values: `emr-managed | on-customer-s3only | disabled`   
Required: No

## See Also
<a name="API_S3LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/S3LoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/S3LoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/S3LoggingConfiguration) 