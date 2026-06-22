---
id: "@specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.prereqs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Prerequisites"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Prerequisites

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.prereqs
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Prerequisites
<a name="JDBC.withAzureAD.prereqs"></a>

Ensure that you have met the following prerequisites before using the Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD:
+ [Admin permissions in AWS to create the identity provider and the roles](security-iam.md).
+ An Azure Active Directory account (Go to [ https://azure.microsoft.com/en-ca/services/active-directory/](https://azure.microsoft.com/en-ca/services/active-directory/) to create an account)
+ [Access to Amazon Timestream for LiveAnalytics](accessing.md).