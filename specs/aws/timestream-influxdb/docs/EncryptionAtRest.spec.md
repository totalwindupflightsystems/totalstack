---
id: "@specs/aws/timestream-influxdb/docs/EncryptionAtRest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Encryption at rest"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Encryption at rest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/EncryptionAtRest
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Encryption at rest
<a name="EncryptionAtRest"></a>

Timestream for LiveAnalytics encryption at rest provides enhanced security by encrypting all your data at rest using encryption keys stored in [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/). This functionality helps reduce the operational burden and complexity involved in protecting sensitive data. With encryption at rest, you can build security-sensitive applications that meet strict encryption compliance and regulatory requirements. 
+ Encryption is turned on by default on your Timestream for LiveAnalytics database, and cannot be turned off. The industry standard AES-256 encryption algorithm is the default encryption algorithm used.
+ AWS KMS is required for encryption at rest in Timestream for LiveAnalytics.
+ You cannot encrypt only a subset of items in a table.
+  You don't need to modify your database client applications to use encryption. 

 If you do not provide a key, Timestream for LiveAnalytics creates and uses an AWS KMS key named `alias/aws/timestream` in your account. 

You may use your own customer managed key in KMS to encrypt your Timestream for LiveAnalytics data. For more information on keys in Timestream for LiveAnalytics, see [Key management](KeyManagement.md). 

 Timestream for LiveAnalytics stores your data in two storage tiers, memory store and magnetic store. Memory store data is encrypted using a Timestream for LiveAnalytics service key. Magnetic store data is encrypted using your AWS KMS key. 

The Timestream Query service requires credentials to access your data. These credentials are encrypted using your KMS key.

**Note**  
Timestream for LiveAnalytics doesn't call AWS KMS for every Decrypt operation. Instead, it maintains a local cache of keys for 5 minutes with active traffic. Any permission changes are propagated through the Timestream for LiveAnalytics system with eventual consistency within at most 5 minutes.