---
id: "@specs/aws/timestream-influxdb/docs/ODBC-connecting-examples"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Connection string examples"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Connection string examples

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/ODBC-connecting-examples
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Connection string examples for the Timestream for LiveAnalytics ODBC driver
<a name="ODBC-connecting-examples"></a>

## Example of connecting to the ODBC driver with IAM credentials
<a name="ODBC-connecting-examples-iam"></a>

```
Driver={Amazon Timestream ODBC Driver};Auth=IAM;AccessKeyId={{{{(your access key ID)}}}};secretKey={{(your secret key)}};SessionToken=(your session token);Region={{us-east-2}};
```

## Example of connecting to the ODBC driver with a profile
<a name="ODBC-connecting-examples-profile"></a>

```
Driver={Amazon Timestream ODBC Driver};ProfileName={{(the profile name)}};region=us-west-2;
```

The driver will attempt to connect using the credentials provided in `~/.aws/credentials`, or if a file is specified in the environment variable `AWS_SHARED_CREDENTIALS_FILE`, using the credentials in that file.

## Example of connecting to the ODBC driver with Okta
<a name="ODBC-connecting-examples-okta"></a>

```
driver={Amazon Timestream ODBC Driver};auth=okta;region=us-west-2;idPHost={{(your host at Okta)}};idPUsername={{(your user name)}};idPPassword={{(your password)}};OktaApplicationID={{(your Okta AppId)}};roleARN={{(your role ARN)}};idPARN={{(your Idp ARN)}};
```

## Example of connecting to the ODBC driver with Azure Active Directory (AAD)
<a name="ODBC-connecting-examples-aad"></a>

```
driver={Amazon Timestream ODBC Driver};auth=aad;region=us-west-2;idPUsername={{(your user name)}};idPPassword={{(your password)}};aadApplicationID={{(your AAD AppId)}};aadClientSecret={{(your AAD client secret)}};aadTenant={{(your AAD tenant)}};roleARN={{(your role ARN)}};idPARN={{(your idP ARN)}};
```

## Example of connecting to the ODBC driver with a specified endpoint and a log level of 2 (WARNING)
<a name="ODBC-connecting-examples-okta"></a>

```
Driver={Amazon Timestream ODBC Driver};Auth=IAM;AccessKeyId={{(your access key ID)}};secretKey={{(your secret key)}};EndpointOverride=ingest.timestream.us-west-2.amazonaws.com;Region=us-east-2;LogLevel=2;
```