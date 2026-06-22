---
id: "@specs/aws/kafka/docs/create-cluster-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a provisioned Amazon MSK cluster using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a provisioned Amazon MSK cluster using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-cluster-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a provisioned Amazon MSK cluster using the AWS CLI
<a name="create-cluster-cli"></a>

****

1. Copy the following JSON and save it to a file. Name the file `brokernodegroupinfo.json`. Replace the subnet IDs in the JSON with the values that correspond to your subnets. These subnets must be in different Availability Zones. Replace {{"Security-Group-ID"}} with the ID of one or more security groups of the client VPC. Clients associated with these security groups get access to the cluster. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the `ec2:DescribeSecurityGroups` permission. For an example, see [Amazon EC2: Allows Managing Amazon EC2 Security Groups Associated With a Specific VPC, Programmatically and in the Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_securitygroups-vpc.html). Finally, save the updated JSON file on the computer where you have the AWS CLI installed.

   ```
   {
     "InstanceType": "kafka.m5.large",
     "ClientSubnets": [
       "{{Subnet-1-ID}}",
       "{{Subnet-2-ID}}"
     ],
     "SecurityGroups": [
       {{"Security-Group-ID"}}
     ]
   }
   ```
**Important**  
For Express brokers, you need three subnets in three different Availability Zones. You also do not need to define any storage-related properties.  
For Standard brokers in the US West (N. California) Region, you need two subnets in two different Availability Zones. In all other Regions where Amazon MSK is available, you can specify either two or three subnets. Your subnets must all be in different Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly over the subnets that you specify.

1. Run the following AWS CLI command in the directory where you saved the `brokernodegroupinfo.json` file, replacing {{"Your-Cluster-Name"}} with a name of your choice. For {{"Monitoring-Level"}}, you can specify one of the following three values: `DEFAULT`, `PER_BROKER`, or `PER_TOPIC_PER_BROKER`. For information about these three different levels of monitoring, see [Monitor an Amazon MSK Provisioned cluster](monitoring.md). The `enhanced-monitoring` parameter is optional. If you don't specify it in the `create-cluster` command, you get the `DEFAULT` level of monitoring.

   ```
   aws kafka create-cluster --cluster-name {{"Your-Cluster-Name"}} --broker-node-group-info file://brokernodegroupinfo.json --kafka-version "2.8.1" --number-of-broker-nodes 3 --enhanced-monitoring {{"Monitoring-Level"}}
   ```

   The output of the command looks like the following JSON:

   ```
   {
       "ClusterArn": "...",
       "ClusterName": "AWSKafkaTutorialCluster",
       "State": "CREATING"
   }
   ```
**Note**  
The `create-cluster` command might return an error stating that one or more subnets belong to unsupported Availability Zones. When this happens, the error indicates which Availability Zones are unsupported. Create subnets that don't use the unsupported Availability Zones and try the `create-cluster` command again.

1. Save the value of the `ClusterArn` key because you need it to perform other actions on your cluster.

1. Run the following command to check your cluster `STATE`. The `STATE` value changes from `CREATING` to `ACTIVE` as Amazon MSK provisions the cluster. When the state is `ACTIVE`, you can connect to the cluster. For more information about cluster status, see [Understand MSK Provisioned cluster states](msk-cluster-states.md).

   ```
   aws kafka describe-cluster --cluster-arn {{<your-cluster-ARN>}}
   ```