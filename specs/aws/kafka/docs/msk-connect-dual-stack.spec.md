---
id: "@specs/aws/kafka/docs/msk-connect-dual-stack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure dual-stack network type"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Configure dual-stack network type

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-dual-stack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure dual-stack network type
<a name="msk-connect-dual-stack"></a>

Amazon MSK Connect supports dual-stack network type for new connectors. With dual-stack networking, your connectors can connect to destinations over both IPv4 and IPv6. Note that IPv6 connectivity is only available in dual-stack mode (IPv4 \+ IPv6) - IPv6-only networking is not supported.

By default, new connectors use IPv4 network type. To create a connector with dual-stack network type, make sure you've fulfilled the prerequisites described in the following section. Note that, once you create a connector using dual-stack network type, you cannot modify its network type. To change network types, you must delete and recreate the connector.

Amazon MSK Connect also supports service API endpoint connectivity over both IPv6 and IPv4. To use IPv6 connectivity for API calls, you need to use the dual-stack endpoints. For more information about MSK Connect service endpoints, see [Amazon MSK Connect endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/msk-connect.html).

## Prerequisites for using dual-stack network type
<a name="dual-stack-prerequisites"></a>

Before you configure dual-stack network type for your connectors, make sure that all subnets you provide during connector creation have both IPv6 and IPv4 CIDR blocks assigned.

## Considerations for using dual-stack network type
<a name="dual-stack-considerations"></a>
+ IPv6 support is currently available only in dual-stack mode (IPv4 \+ IPv6), not as IPv6-only
+ Connectors with dual-stack enabled can connect over both IPv4 and IPv6 to both MSK and Sink or Source data systems
+ Network type cannot be modified after connector creation - you must delete and recreate the connector to change network types
+ All subnets specified during the connector creation must support dual-stack for the connector creation to succeed with dual-stack network type
+ If using dual-stack subnets but no network type is specified, the connector will default to IPv4-only for backwards compatibility
+ For existing connectors, you cannot update network type - you must delete and recreate the connector to change network types
+ Using dual-stack networking doesn't incur additional costs