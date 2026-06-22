---
id: "@specs/aws/timestream-influxdb/docs/Using-API.endpoint-discovery.how-it-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How it works"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# How it works

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Using-API.endpoint-discovery.how-it-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# How the endpoint discovery pattern works
<a name="Using-API.endpoint-discovery.how-it-works"></a>

 Timestream is built using a [cellular architecture ](architecture.md#cells) to ensure better scaling and traffic isolation properties. Because each customer account is mapped to a specific cell in a region, your application must use the correct cell-specific endpoints that your account has been mapped to. When using the SDKs, this mapping is transparently handled for you and you do not need to manage the cell-specific endpoints. However, when directly accessing the REST API, you will need to manage and map the correct endpoints yourself. This process, the *endpoint discovery pattern*, is described below: 

1.  The endpoint discovery pattern starts with a call to the `DescribeEndpoints` action (described in the [https://docs.aws.amazon.com/timestream/latest/developerguide/API_Reference.html](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Reference.html) section). 

1.  The endpoint should be cached and reused for the amount of time specified by the returned time-to-live (TTL) value (the [https://docs.aws.amazon.com/timestream/latest/developerguide/API_Endpoint.html#timestream-Type-Endpoint-CachePeriodInMinutes.html](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Endpoint.html#timestream-Type-Endpoint-CachePeriodInMinutes.html)). Calls to the Timestream Live Analytics API can then be made for the duration of the TTL. 

1.  After the TTL expires, a new call to DescribeEndpoints should be made to refresh the endpoint (in other words, start over at Step 1). 

**Note**  
 Syntax, parameters and other usage information for the `DescribeEndpoints` action are described in the [API Reference](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeEndpoints.html). Note that the `DescribeEndpoints` action is available via both SDKs, and is identical for each. 

For implementation of the endpoint discovery pattern, see [Implementing the endpoint discovery pattern](Using-API.endpoint-discovery.describe-endpoints.implementation.md).