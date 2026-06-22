---
id: "@specs/aws/timestream-influxdb/docs/getting-started.dot-net"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS .NET"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# .NET

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/getting-started.dot-net
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# .NET
<a name="getting-started.dot-net"></a>

To get started with the [.NET SDK](https://aws.amazon.com/sdk-for-net/) and Amazon Timestream, complete the prerequisites, described below.

Once you've completed the necessary prerequisites for the .NET SDK, you can get started with the [Code samples](code-samples.md).

## Prerequisites
<a name="getting-started.dot-net.prereqs"></a>

Before you get started with .NET, install the required NuGet packages and ensure that AWSSDK.Core version is 3.3.107 or newer by running the following commands: 

```
dotnet add package AWSSDK.Core
dotnet add package AWSSDK.TimestreamWrite
dotnet add package AWSSDK.TimestreamQuery
```