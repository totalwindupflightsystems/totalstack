---
id: "@specs/aws/timestream-influxdb/docs/Telegraf.installing-output-plugin"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Installing Telegraf with the Timestream for LiveAnalytics output plugin"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Installing Telegraf with the Timestream for LiveAnalytics output plugin

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Telegraf.installing-output-plugin
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Installing Telegraf with the Timestream for LiveAnalytics output plugin
<a name="Telegraf.installing-output-plugin"></a>

As of version 1.16, the Timestream for LiveAnalytics output plugin is available in the official Telegraf release. To install the output plugin on most major operating systems, follow the steps outlined in the [InfluxData Telegraf Documentation](https://docs.influxdata.com/telegraf/v1.16/introduction/installation/). To install on the Amazon Linux 2 OS, follow the instructions below.

## Installing Telegraf with the Timestream for LiveAnalytics output plugin on Amazon Linux 2
<a name="w2aab7c44c35b9b5"></a>

 To install Telegraf with the Timestream Output Plugin on Amazon Linux 2, perform the following steps. 

1. Install Telegraf using the `yum` package manager.

   ```
   cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
   [influxdb]
   name = InfluxDB Repository - RHEL \$releasever
   baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
   enabled = 1
   gpgcheck = 1
   gpgkey = https://repos.influxdata.com/influxdb.key
   EOF
   ```

1. Run the following command.

   ```
   sudo sed -i "s/\$releasever/$(rpm -E %{rhel})/g" /etc/yum.repos.d/influxdb.repo
   ```

1. Install and start Telegraf.

   ```
   sudo yum install telegraf
   sudo service telegraf start
   ```