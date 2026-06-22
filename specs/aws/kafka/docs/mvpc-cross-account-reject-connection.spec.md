---
id: "@specs/aws/kafka/docs/mvpc-cross-account-reject-connection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Reject managed VPC connection"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Reject managed VPC connection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/mvpc-cross-account-reject-connection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Reject a managed VPC connection to an Amazon MSK cluster
<a name="mvpc-cross-account-reject-connection"></a>

From the Amazon MSK console on the cluster admin account, you can reject a client VPC connection. The client VPC connection must be in the AVAILABLE state to be rejected. You might want to reject a managed VPC connection from a client that is no longer authorized to connect to your cluster. To prevent new managed VPC connections from a connecting to a client, deny access to the client in the cluster policy. A rejected connection still incurs cost until its deleted by the connection owner. See [Delete a managed VPC connection to an Amazon MSK cluster ](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-delete-connection.html).

**To reject a client VPC connection using the MSK console**

1. Open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk).

1. In the navigation pane, select **Clusters** and scroll to the **Network settings > Client VPC connections** list.

1. Select the connection that you want to reject and select **Reject client VPC connection**.

1. Confirm that you want to reject the selected client VPC connection.

To reject a managed VPC connection using the API, use the `RejectClientVpcConnection` API.