---
id: "@specs/aws/kafka/docs/msk-connect-dns-failure-handling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Handle connector creation failures"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Handle connector creation failures

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-dns-failure-handling
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Handle connector creation failures
<a name="msk-connect-dns-failure-handling"></a>

This section describes possible connector creation failures associated with DNS resolution and suggested actions to resolve the issues.


| Failure | Suggested action | 
| --- | --- | 
| Connector creation fails if a DNS resolution query fails, or if DNS servers are unreachable from the connector. | You can see connector creation failures due to unsuccessful DNS resolution queries in your CloudWatch logs, if you've configured these logs for your connector.<br />Check the DNS server configurations and ensure network connectivity to the DNS servers from the connector. | 
| If you change the DNS servers configuration in your VPC DHCP option set while a connector is running, DNS resolution queries from the connector can fail. If the DNS resolution fails, some of the connector tasks can enter a failed state. | You can see connector creation failures due to unsuccessful DNS resolution queries in your CloudWatch logs, if you've configured these logs for your connector.<br />The failed tasks should automatically restart to bring the connector back up. If that does not happen, you can contact support to restart the failed tasks for their connector or you can recreate the connector. | 