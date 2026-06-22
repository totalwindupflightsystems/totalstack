---
id: "@specs/aws/kafka/docs/zookeeper-security-group"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS To place your Apache ZooKeeper nodes in a separate security group"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# To place your Apache ZooKeeper nodes in a separate security group

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/zookeeper-security-group
> **target_lang:** meta — documentation tier. ALL sections preserved.



# To place your Apache ZooKeeper nodes in a separate security group
<a name="zookeeper-security-group"></a>

To limit access to Apache ZooKeeper nodes, you can assign a separate security group to them. You can choose who has access to this new security group by setting security group rules.

1. Get the Apache ZooKeeper connection string for your cluster. To learn how, see [ZooKeeper mode](metadata-management.md#msk-get-connection-string). The connection string contains the DNS names of your Apache ZooKeeper nodes.

1. Use a tool like `host` or `ping` to convert the DNS names you obtained in the previous step to IP addresses. Save these IP addresses because you need them later in this procedure.

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left pane, under **NETWORK & SECURITY**, choose **Network Interfaces**.

1. In the search field above the table of network interfaces, type the name of your cluster, then type return. This limits the number of network interfaces that appear in the table to those interfaces that are associated with your cluster.

1. Select the check box at the beginning of the row that corresponds to the first network interface in the list.

1. In the details pane at the bottom of the page, look for the **Primary private IPv4 IP**. If this IP address matches one of the IP addresses you obtained in the first step of this procedure, this means that this network interface is assigned to an Apache ZooKeeper node that is part of your cluster. Otherwise, deselect the check box next to this network interface, and select the next network interface in the list. The order in which you select the network interfaces doesn't matter. In the next steps, you will perform the same operations on all network interfaces that are assigned to Apache ZooKeeper nodes, one by one.

1. When you select a network interface that corresponds to an Apache ZooKeeper node, choose the **Actions** menu at the top of the page, then choose **Change Security Groups**. Assign a new security group to this network interface. For information about creating security groups, see [Creating a Security Group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html?shortFooter=true#CreatingSecurityGroups) in the Amazon VPC documentation.

1. Repeat the previous step to assign the same new security group to all the network interfaces that are associated with the Apache ZooKeeper nodes of your cluster.

1. You can now choose who has access to this new security group. For information about setting security group rules, see [Adding, Removing, and Updating Rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html?shortFooter=true#AddRemoveRules) in the Amazon VPC documentation.