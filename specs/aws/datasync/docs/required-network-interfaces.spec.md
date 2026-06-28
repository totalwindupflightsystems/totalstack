---
id: "@specs/aws/datasync/docs/required-network-interfaces"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Network interfaces for data transfers"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Network interfaces for data transfers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/required-network-interfaces
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Network interfaces for AWS DataSync transfers
<a name="required-network-interfaces"></a>

For every task you create, AWS DataSync automatically generates and manages [network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) for data transfer traffic. How many network interfaces DataSync creates and where they’re created depends on the following details about your transfer task:
+ Whether your task [requires a DataSync agent](do-i-need-datasync-agent.md).
+ Your source and destination locations (where you’re copying data from and to).
+ The type of service endpoint that your agent uses.

Each network interface uses a single IP address in your subnet (the more network interfaces there are, the more IP addresses you need). Use the following tables to make sure your subnet has enough IP addresses for your task.

## Network interfaces for transfers with agents
<a name="transfers-with-agents-enis"></a>

In general, you need a DataSync agent when copying data between an AWS storage service and storage system that isn't AWS.


<table>
<thead>
  <tr><th>Location</th><th>Network interfaces created by default</th><th>Where network interfaces are created when using a public or FIPS endpoint</th><th>Where network interfaces are created when using a private (VPC) endpoint </th></tr>
</thead>
<tbody>
  <tr><td>Amazon S3</td><td>4</td><td>N/A1</td><td>The subnet you specify when activating your DataSync agent.</td></tr>
  <tr><td>Amazon EFS</td><td>4</td><td colspan="2">The subnet you specify when creating the Amazon EFS location.</td></tr>
  <tr><td>Amazon FSx for Windows File Server</td><td>4</td><td colspan="2">The same subnet as the file system's preferred file server.</td></tr>
  <tr><td>Amazon FSx for Lustre</td><td>4</td><td colspan="2">The same subnet as the file system.</td></tr>
  <tr><td>Amazon FSx for OpenZFS</td><td>4</td><td colspan="2">The same subnet as the file system.</td></tr>
  <tr><td>Amazon FSx for NetApp ONTAP</td><td>4</td><td colspan="2">The same subnet as the file system.</td></tr>
</tbody>
</table>


1 Network interfaces aren't needed because the DataSync service communicates directly with the S3 bucket.

## Network interfaces for transfers without agents
<a name="transfers-without-agents-enis"></a>

You don’t need a DataSync agent when copying data between AWS services.

The total number of network interfaces depends on the DataSync locations in your transfer. For example, transferring between Amazon EFS and FSx for Lustre file systems requires four network interfaces. Meanwhile, transferring between FSx for Windows File Server and an S3 bucket requires two network interfaces.


| Location | Network interfaces created by default | Where network interfaces are created | 
| --- | --- | --- | 
| Amazon S3 | N/A1 | N/A1 | 
| Amazon EFS | 2 | The subnet you specify when creating the Amazon EFS location. | 
| FSx for Windows File Server | 2 | The same subnet as the preferred file server for the file system. | 
| FSx for Lustre | 2 | The same subnet as the file system. | 
| FSx for OpenZFS | 2 | The same subnet as the file system. | 
| FSx for ONTAP | 2 | The same subnet as the file system. | 

1 Network interfaces aren't needed because the DataSync service communicates directly with the S3 bucket.

## Viewing your network interfaces
<a name="view-network-interfaces"></a>

To see the network interfaces allocated to your DataSync transfer task, do one of the following:
+ Use the [DescribeTask](https://docs.aws.amazon.com//datasync/latest/userguide/API_DescribeTask.html) operation. The operation returns `SourceNetworkInterfaceArns` and `DestinationNetworkInterfaceArns` with responses that look like this:

  ```
  arn:aws:ec2:{{your-region}}:{{your-account-id}}:network-interface/eni-f012345678abcdef0
  ```

  In this example, the network interface ID is `eni-f012345678abcdef0`.
+ In the Amazon EC2 console, search for your task ID (such as `task-f012345678abcdef0`) to find its network interfaces.