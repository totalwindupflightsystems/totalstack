---
id: "@specs/aws/kafka/docs/get-bootstrap-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get the bootstrap brokers using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Get the bootstrap brokers using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/get-bootstrap-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Get the bootstrap brokers using the AWS CLI
<a name="get-bootstrap-cli"></a>

Run the following command, replacing {{ClusterArn}} with the Amazon Resource Name (ARN) that you obtained when you created your cluster. If you don't have the ARN for your cluster, you can find it by listing all clusters. For more information, see [List Amazon MSK clusters](msk-list-clusters.md).

```
aws kafka get-bootstrap-brokers --cluster-arn {{ClusterArn}}
```

For an MSK cluster that uses [IAM access control](iam-access-control.md), the output of this command looks like the following JSON example.

```
{
    "BootstrapBrokerStringSaslIam": "b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9098,b-2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9098"
}
```

The following example shows the bootstrap brokers for a cluster that has public access turned on. Use the `BootstrapBrokerStringPublicSaslIam` for public access, and the `BootstrapBrokerStringSaslIam` string for access from within AWS.

```
{
    "BootstrapBrokerStringPublicSaslIam": "b-2-public.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9198,b-1-public.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9198,b-3-public.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9198",
    "BootstrapBrokerStringSaslIam": "b-2.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9098,b-1.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9098,b-3.myTestCluster.v4ni96.c2.kafka-beta.us-east-1.amazonaws.com:9098"
}
```

The bootstrap brokers string should contain three brokers from across the Availability Zones in which your MSK cluster is deployed (unless only two brokers are available). 