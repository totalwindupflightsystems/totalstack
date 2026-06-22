---
id: "@specs/aws/kafka/docs/mvpc-cluster-owner-action-turn-on"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster owner turns on multi-VPC"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Cluster owner turns on multi-VPC

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mvpc-cluster-owner-action-turn-on
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Step 1: On the MSK cluster in Account A, turn on multi-VPC connectivity for IAM auth scheme on the cluster
<a name="mvpc-cluster-owner-action-turn-on"></a>

The MSK cluster owner needs to make configuration settings on the MSK cluster after the cluster is created and in an ACTIVE state.

The cluster owner turns on multi-VPC private connectivity on the ACTIVE cluster for any auth schemes that will be active on the cluster. This can be done using the [UpdateSecurity API](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-security.html) or MSK console. The IAM, SASL/SCRAM, and TLS auth schemes support multi-VPC private connectivity. Multi-VPC private connectivity can’t be enabled for unauthenticated clusters.

For this use case, you’ll configure the cluster to use the IAM auth scheme.

**Note**  
If you are configuring your MSK cluster to use SASL/SCRAM auth scheme, the Apache Kafka ACLs property "`allow.everyone.if.no.acl.found=false`" is mandatory. See [Apache Kafka ACLs](https://docs.aws.amazon.com/msk/latest/developerguide/msk-acls.html).

When you update multi-VPC private connectivity settings, Amazon MSK starts a rolling reboot of broker nodes that updates the broker configurations. This can take up to 30 minutes or more to complete. You can’t make other updates to the cluster while connectivity is being updated.

**Turn on multi-VPC for selected auth schemes on the cluster in Account A using the console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://docs.aws.amazon.com/msk/latest/developerguide/msk-acls.html) for the account where the cluster is located.

1. In the navigation pane, under **MSK Clusters**, choose **Clusters** to display the list of clusters in the account.

1. Select the cluster to configure for multi-VPC private connectivity. The cluster must be in an ACTIVE state.

1. Select the cluster **Properties** tab, and then go to **Network** settings.

1. Select the **Edit** drop down menu and select **Turn on multi-VPC connectivity**.

1. Select one or more authentication types you want turned on for this cluster. For this use case, select **IAM role-based authentication**.

1. Select **Save changes**.

**Example - UpdateConnectivity API that turns on Multi-VPC private connectivity auth schemes on a cluster**  
As an alternative to the MSK console, you can use the [UpdateConnectivity API](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-connectivity.html) to turn on multi-VPC private connectivity and configure auth schemes on an ACTIVE cluster. The following example shows the IAM auth scheme turned on for the cluster.  

```
{
  "currentVersion": "K3T4TT2Z381HKD",
  "connectivityInfo": {
    "vpcConnectivity": {
      "clientAuthentication": {
        "sasl": {
          "iam": {
            "enabled": TRUE
            }
        }
      }
    }
  }
}
```

Amazon MSK creates the networking infrastructure required for private connectivity. Amazon MSK also creates a new set of bootstrap broker endpoints for each auth type that requires private connectivity. Note that the plaintext auth scheme does not support multi-VPC private connectivity.