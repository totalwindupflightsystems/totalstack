---
id: "@specs/aws/timestream-influxdb/docs/aws-sso-with-okta-prerequisites"
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
> **spec:id:** @specs/aws/timestream-influxdb/docs/aws-sso-with-okta-prerequisites
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Prerequisites
<a name="aws-sso-with-okta-prerequisites"></a>

Ensure that you have met the following prerequisites before using the Timestream for LiveAnalytics JDBC single sign-on authentication with Okta:
+ [Admin permissions in AWS to create the identity provider and the roles](security-iam.md).
+  An Okta account (Go to [https://www.okta.com/login/](https://www.okta.com/login/) to create an account).
+ [Access to Amazon Timestream for LiveAnalytics](accessing.md).

Now that you have completed the Prerequisites, you may proceed to [AWS account federation in Okta](aws-account-federation-in-okta.md).