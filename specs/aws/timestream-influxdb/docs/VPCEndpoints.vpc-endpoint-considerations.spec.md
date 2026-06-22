---
id: "@specs/aws/timestream-influxdb/docs/VPCEndpoints.vpc-endpoint-considerations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How VPC endpoints work with Timestream"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# How VPC endpoints work with Timestream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/VPCEndpoints.vpc-endpoint-considerations
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# How VPC endpoints work with Timestream
<a name="VPCEndpoints.vpc-endpoint-considerations"></a>

 When you create a VPC endpoint to access either the Timestream Write or Timestream Query SDK, all requests are routed to endpoints within the Amazon network and do not access the public internet. More specifically, your requests are routed to the write and query endpoints of the cell that your account has been mapped to for a given region. To learn more about Timestream's cellular architecture and cell-specific endpoints, you can refer to [Cellular architecture](architecture.md#cells). For example, suppose that your account has been mapped to `cell1` in `us-west-2`, and you've set up VPC interface endpoints for writes (`ingest-cell1.timestream.us-west-2.amazonaws.com`) and queries (`query-cell1.timestream.us-west-2.amazonaws.com`). In this case, any write requests sent using these endpoints will stay entirely within the Amazon network and will not access the public internet. 

## Considerations for Timestream VPC endpoints
<a name="VPCEndpoints.vpc-endpoint-considerations.how-it-works"></a>

Consider the following when creating a VPC endpoint for Timestream:
+ Before you set up an interface VPC endpoint for Timestream for LiveAnalytics, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 
+ Timestream for LiveAnalytics supports making calls to [all of its API actions](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Reference.html) from your VPC. 
+ VPC endpoint policies are supported for Timestream for LiveAnalytics. By default, full access to Timestream for LiveAnalytics is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.
+ Because of Timestream's architecture, access to both Write and Query actions requires the creation of two VPC interface endpoints, one for each SDK. Additionally, you must specify a cell endpoint (you will only be able to create an endpoint for the Timestream cell that you are mapped to). Detailed information can be found in the [create an interface VPC endpoint for Timestream for LiveAnalytics](VPCEndpoints.vpc-endpoint-create.md) section of this guide. 

Now that you understand how Timestream for LiveAnalytics works with VPC endpoints, [create an interface VPC endpoint for Timestream for LiveAnalytics](VPCEndpoints.vpc-endpoint-create.md).