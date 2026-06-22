---
id: "@specs/aws/timestream-influxdb/docs/KeyManagement"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Key management"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Key management

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/KeyManagement
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Key management
<a name="KeyManagement"></a>

 You can manage keys for Amazon Timestream Live Analytics using the [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/). **Timestream Live Analytics requires the use of KMS to encrypt your data.** You have the following options for key management, depending on how much control you require over your keys: 

**Database and table resources**
+  *Timestream Live Analytics-managed key: * If you do not provide a key, Timestream Live Analytics will create a `alias/aws/timestream` key using KMS. 
+  *Customer managed key: * KMS customer managed keys are supported. Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.

**Scheduled query resource**
+  *Timestream Live Analytics-owned key: * If you do not provide a key, Timestream Live Analytics will use its own a KMS key to encrypt the Query resource, this key is present in timestream account. See [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the KMS developer guide for more details.
+  *Customer managed key: * KMS customer managed keys are supported. Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.

KMS keys in an external key store (XKS) are not supported.