---
id: "@specs/aws/timestream-influxdb/docs/ODBC-setup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Driver setup"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Driver setup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/ODBC-setup
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Setting up the Timestream for LiveAnalytics ODBC driver
<a name="ODBC-setup"></a>

## Set up access to Timestream for LiveAnalytics in your AWS account
<a name="ODBC-setup-access"></a>

If you haven't already set up your AWS account to work with Timestream for LiveAnalytics, follow the insructions in [Accessing Timestream for LiveAnalytics](accessing.md).

## Install the ODBC driver on your system
<a name="ODBC-setup-download"></a>

Download the appropriate Timestream ODBC driver installer for your system from the [ODBC GitHub repository](https://github.com/awslabs/amazon-timestream-odbc-driver/releases), and follow the installation instructions that apply to your system:.
+ [Windows installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-installation-guide.md)
+ [MacOS installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-installation-guide.md)
+ [Linux installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-installation-guide.md)

## Set up a data source name (DSN) for the ODBC driver
<a name="ODBC-setup-dsn"></a>

Follow the instructions in the DSN configuration guide for your system:
+ [Windows DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-dsn-configuration.md)
+ [MacOS DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-dsn-configuration.md)
+ [Linux DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-dsn-configuration.md)

## Set up your business intelligence (BI) application to work with the ODBC driver
<a name="ODBC-setup-bi-apps"></a>

Here are instructions for setting several common BI applications to work with the ODBC driver:
+ [Setting up Microsoft Power BI.](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-power-bi.md)
+ [Setting up Microsoft Excel](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-excel.md)
+ [Setting up Tableau](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/tableau.md)

For other applications