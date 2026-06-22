---
id: "@specs/aws/kafka/docs/msk-configuration-express-read-only"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Read-only configurations"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Read-only configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-express-read-only
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Express brokers read-only configurations
<a name="msk-configuration-express-read-only"></a>

Amazon MSK sets the values for these configurations and protects them from change that may affect the availability of your cluster. These values may change depending on the Apache Kafka version running on the cluster, so remember to check the values from your specific cluster.

The following table lists the read-only configurations for Express brokers.


| Property | Description | Express Broker Value | 
| --- | --- | --- | 
| broker.id | The broker id for this server. | 1,2,3... | 
| broker.rack | Rack of the broker. This will be used in rack aware replication assignment for fault tolerance. Examples: `RACK1`, `us-east-1d` | AZ ID or Subnet ID | 
| default.replication.factor | Default replication factors for all topics. | 3 | 
| fetch.max.bytes | The maximum number of bytes we will return for a fetch request. | Apache Kafka Default | 
| group.max.size | The maximum number of consumers that a single consumer group can accommodate. | Apache Kafka Default | 
| inter.broker.listener.name | Name of listener used for communication between brokers. | REPLICATION\_SECURE or REPLICATION | 
| inter.broker.protocol.version | Specifies which version of the inter-broker protocol is used. | Apache Kafka Default | 
| listeners | Listener List - Comma-separated list of URIs we will listen on and the listener names. You can set the advertised.listeners property, but not the listeners property. | MSK-generated | 
| log.message.format.version | Specify the message format version the broker will use to append messages to the logs. | Apache Kafka Default | 
| min.insync.replicas | When a producer sets acks to `all` (or `-1`), the value in `min.insync.replicas` specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. If this minimum cannot be met, the producer raises an exception (either `NotEnoughReplicas` or `NotEnoughReplicasAfterAppend`).<br />You can use value of acks from your producer to enforce greater durability guarantees. By setting acks to "all". This ensures that the producer raises an exception if a majority of replicas don't receive a write. | 2 | 
| num.io.threads | Number of threads that the server uses to produce requests, which may include disk I/O. (m7g.large, 8), (m7g.xlarge, 8), (m7g.2xlarge, 16), (m7g.4xlarge, 32), (m7g.8xlarge, 64), (m7g.12xlarge, 96), (m7g.16xlarge, 128) | Based on instance type. =Math.max(8, 2 \* vCPUs) | 
| num.network.threads | Number of threads that the server uses to receive requests from the network and send responses to the network. (m7g.large, 8), (m7g.xlarge, 8), (m7g.2xlarge, 8), (m7g.4xlarge, 16), (m7g.8xlarge, 32), (m7g.12xlarge, 48), (m7g.16xlarge, 64) | Based on instance type. =Math.max(8, vCPUs) | 
| replica.fetch.response.max.bytes | The maximum number of bytes expected for the entire fetch response. Records are fetched in batches, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure progress. This isn't an absolute maximum. The message.max.bytes (broker config) or max.message.bytes (topic config) properties specify the maximum record batch size that the broker accepts. | Apache Kafka Default | 
| request.timeout.ms | The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses, the client will resend the request if necessary or fail the request if retries are exhausted. | Apache Kafka Default | 
| transaction.state.log.min.isr | Overridden min.insync.replicas configuration for the transaction topic. | 2 | 
| transaction.state.log.replication.factor | The replication factor for the transaction topic. | Apache Kafka Default | 
| unclean.leader.election.enable | Allows replicas not in the ISR set to serve as leader as a last resort, even though this might result in data loss. | FALSE | 