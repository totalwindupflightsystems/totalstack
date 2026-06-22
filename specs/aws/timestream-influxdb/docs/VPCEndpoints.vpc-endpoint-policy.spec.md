---
id: "@specs/aws/timestream-influxdb/docs/VPCEndpoints.vpc-endpoint-policy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a VPC endpoint policy for Timestream for LiveAnalytics"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Creating a VPC endpoint policy for Timestream for LiveAnalytics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/VPCEndpoints.vpc-endpoint-policy
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Creating a VPC endpoint policy for Timestream for LiveAnalytics
<a name="VPCEndpoints.vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Timestream for LiveAnalytics. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Timestream for LiveAnalytics actions**  
The following is an example of an endpoint policy for Timestream for LiveAnalytics. When attached to an endpoint, this policy grants access to the listed Timestream for LiveAnalytics actions (in this case, [https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListDatabases.html](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListDatabases.html)) for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "timestream:ListDatabases"
         ],
         "Resource":"*"
      }
   ]
}
```