---
id: "@specs/aws/datasync/docs/direct-connect-architecture"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Architecture and routing examples with Direct Connect"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Architecture and routing examples with Direct Connect

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/direct-connect-architecture
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSync architecture and routing examples with Direct Connect
<a name="direct-connect-architecture"></a>

Consider the following network architectures when using [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) with your AWS DataSync transfers.

**Tip**  
If your network uses a transit gateway, we recommend separating your DataSync transfer's logical path to optimize costs (particularly if you're migrating a large amount of data).  
For example, if you use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) for normal traffic between your on-premises networks and virtual private clouds (VPCs), you can configure your network so that DataSync traffic bypasses the transit gateway and its data processing charges.

## Using Direct Connect with a DataSync VPC service endpoint
<a name="using-direct-connect-vpc-endpoint"></a>

If your DataSync agent uses a [VPC service endpoint](choose-service-endpoint.md#datasync-in-vpc), you need a [Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) to connect to your VPC.

**Contents**
+ [Direct Connect architecture with VPC endpoint and S3 destination](#direct-connect-example-vpc-s3)
+ [Direct Connect architecture with VPC endpoint and file system destination in same subnet](#direct-connect-example-vpc-file-same-subnet)
+ [Direct Connect architecture with VPC endpoint and file system destination in different subnets](#direct-connect-example-vpc-file-different-subnet)

### Direct Connect architecture with VPC endpoint and S3 destination
<a name="direct-connect-example-vpc-s3"></a>

The following Direct Connect architecture shows a DataSync transfer from an on-premises storage system to an S3 bucket.

![A diagram that shows DataSync transfer traffic routed through Direct Connect to an S3 bucket.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-direct-connect-diagram-vpc-s3.png)


1. The DataSync agent routes DataSync traffic from the on-premises storage system (source location) to the Direct Connect connection.

1. DataSync traffic routes to a Direct Connect gateway that’s used for your transfer. To set this up, you must:

   1. Associate the Direct Connect gateway with a [virtual private gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html) for the VPC. This is the VPC where the DataSync VPC endpoint is located and where the DataSync task creates [network interfaces](required-network-interfaces.md).

   1. Create a [private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-private-vif) that connects this VPC to the Direct Connect gateway.

1. DataSync traffic (control plane) routes through the DataSync VPC endpoint.

1. DataSync traffic (data plane) routes through the DataSync network interfaces in the subnet that you specify when [creating the DataSync agent](choose-service-endpoint.md#datasync-in-vpc).

1. DataSync traffic routes through the DataSync service to the S3 bucket (destination location).

### Direct Connect architecture with VPC endpoint and file system destination in same subnet
<a name="direct-connect-example-vpc-file-same-subnet"></a>

When transferring to or from an Amazon EFS or Amazon FSx file system, your file system and DataSync VPC endpoint can be in the same subnet.

The following Direct Connect architecture shows a DataSync transfer from an on-premises storage system to an Amazon EFS or Amazon FSx file system.

![A diagram that shows DataSync transfer traffic routed through Direct Connect to an AWS storage file system.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-direct-connect-diagram-vpc-file-1subnet.png)


1. The DataSync agent routes DataSync traffic from the on-premises storage system (source location) to the Direct Connect connection.

1. DataSync traffic routes to a Direct Connect gateway that's used for your transfer. To set this up, you must:

   1. Associate the Direct Connect gateway with a [virtual private gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html) for the VPC. This is the VPC where the DataSync VPC endpoint is located and where the DataSync task creates [network interfaces](required-network-interfaces.md) for the file system (destination location).

   1. Create a [private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-private-vif) that connects this VPC to the Direct Connect gateway.

1. DataSync traffic (control plane) routes through the DataSync VPC endpoint.

1. DataSync traffic (data plane) routes through the DataSync network interfaces in the file system's subnet. This is the same subnet where the DataSync VPC endpoint is located.

1. DataSync traffic routes through the DataSync service to the file system (destination location).

### Direct Connect architecture with VPC endpoint and file system destination in different subnets
<a name="direct-connect-example-vpc-file-different-subnet"></a>

When transferring to or from an Amazon EFS or Amazon FSx file system, your file system and DataSync VPC endpoint can be in different subnets.

The following Direct Connect architecture shows a DataSync transfer from an on-premises storage system to an Amazon EFS or Amazon FSx file system.

![A diagram that shows DataSync transfer traffic routed through Direct Connect and two subnets to an AWS storage file system.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-direct-connect-diagram-vpc-file-2subnet.png)


1. The DataSync agent routes DataSync traffic from the on-premises storage system (source location) to the Direct Connect connection.

1. DataSync traffic routes to a Direct Connect gateway that's used for your transfer. To set this up, you must:

   1. Associate the Direct Connect gateway with a [virtual private gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html) for the VPC. This is the VPC where the DataSync VPC endpoint is located and where the DataSync task creates [network interfaces](required-network-interfaces.md) for the file system (destination location).

   1. Create a [private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-private-vif) that connects these VPCs to the Direct Connect gateway.

1. DataSync traffic (control plane) routes through the DataSync VPC endpoint.

1. DataSync traffic (data plane) routes through the DataSync network interfaces in the file system's subnet. This is a different subnet than where the DataSync VPC endpoint is located.

1. DataSync traffic routes through the DataSync service to the file system (destination location).

## Using Direct Connect with a DataSync public or FIPS service endpoint
<a name="direct-connect-example-public-fips"></a>

If your DataSync agent uses a [public](choose-service-endpoint.md#choose-service-endpoint-public) or [Federal Information Processing Standard (FIPS)](choose-service-endpoint.md#choose-service-endpoint-fips) service endpoint, you can route your data transfer traffic through a Direct Connect connection by using a [public virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-public-vif).

While Direct Connect advertises all local and remote AWS Region prefixes by default, you can use [BGP community tags](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#bgp-communities) to control the scope (Regional or global) and route preference of traffic on the public virtual interface. You must advertise at least one public prefix to create your DataSync agent.

The following Direct Connect architecture shows a DataSync transfer from an on-premises storage system through a public or FIPS endpoint to an S3 bucket.

![A diagram that shows DataSync transfer traffic routed through Direct Connect using a public virtual interface to an S3 bucket.](http://docs.aws.amazon.com/datasync/latest/userguide/images/datasync-direct-connect-diagram-public-endpoint.png)


1. The DataSync agent routes DataSync traffic from the on-premises storage system (source location) to the Direct Connect connection.

1. DataSync traffic routes to the DataSync service through a public virtual interface.

1. DataSync traffic to the S3 bucket (destination location).

## Next steps
<a name="direct-connect-next-steps"></a>

If [you need a DataSync agent](do-i-need-datasync-agent.md) and haven't created one yet, [deploy](deploy-agents.md) the agent, [choose a service endpoint](choose-service-endpoint.md) for the agent, and then [activate](activate-agent.md) the agent. 

Once you create the agent, you can [configure your network](datasync-network.md) for DataSync.