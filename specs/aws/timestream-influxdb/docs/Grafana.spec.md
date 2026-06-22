---
id: "@specs/aws/timestream-influxdb/docs/Grafana"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Grafana"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Grafana

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Grafana
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Grafana
<a name="Grafana"></a>

 You can visualize your time series data and create alerts using Grafana. To help you get started with data visualization, we have created a sample dashboard in Grafana that visualizes data sent to Timestream from a Python application and a [video tutorial ](https://youtu.be/pilkz645cs4) that describes the setup. 

**Topics**
+ [Sample application](#Grafana.sample-app)
+ [Video tutorial](#Grafana.video-tutorial)

## Sample application
<a name="Grafana.sample-app"></a>

1.  Create a database and a table in Timestream following the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console) for more information. 
**Note**  
 The default database name and table name for the Grafana dashboard are set to grafanaDB and grafanaTable respectively. Use these names to minimize setup. 

1. Install [Python 3.7 ](https://www.python.org/downloads/)or higher.

1.  [Install and configure the Timestream Python SDK](getting-started.python.md).s

1.  Clone the GitHub repository for the [multi-thread Python application](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor) continuously ingesting data into Timestream following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

1. Run the application for continuously ingesting data into Timestream following the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md). 

1. Complete [Learn how to create and use Amazon Managed Grafana resources](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html) or complete [Install Grafana](https://grafana.com/docs/grafana/latest/installation/).

1. If installing Grafana instead of using Amazon Managed Grafana, complete [Installing Amazon Timestream on Grafana Cloud](https://grafana.com/grafana/plugins/grafana-timestream-datasource/?tab=installation/).

1. Open the Grafana dashboard using a browser of your choice. If you've locally installed Grafana, you can follow the instructions described in the Grafana documentation to [log in](https://grafana.com/docs/grafana/latest/getting-started/getting-started/#log-in-for-the-first-time).

1. After launching Grafana, go to Datasources, click on Add Datasource, search for Timestream, and select the Timestream datasource.

1. Configure the Auth Provider and the region and click Save and Test.

1. Set the default macros.

   1. Set $\_\_database to the name of your Timestream database (e.g. grafanaDB).

   1. Set $\_\_table to the name of your Timestream table (e.g. grafanaTable).

   1. Set $\_\_measure to the most commonly used measure from the table.

1. Click Save and Test.

1. Click on the Dashboards tab.

1. Click on Import to import the dashboard.

1. Double click the Sample Application Dashboard.

1. Click on the dashboard settings.

1. Select Variables.

1. Change dbName and tableName to match the names of the Timestream database and table.

1. Click Save.

1. Refresh the dashboard.

1. To create alerts, follow the instructions described in the Grafana documentation to [Configure Grafana-managed alert rules](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/).

1. To troubleshoot alerts, follow the instructions described in the Grafana documentation for [Troubleshooting](https://grafana.com/docs/grafana/latest/troubleshooting/).

1. For additional information, see the [Grafana documentation](https://grafana.com/docs/).

## Video tutorial
<a name="Grafana.video-tutorial"></a>

This [video](https://youtu.be/pilkz645cs4) explains how Grafana works with Timestream.