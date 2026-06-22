---
id: "@specs/aws/kafka/docs/cruise-control"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Use Cruise Control"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Use Cruise Control

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/cruise-control
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Use LinkedIn's Cruise Control for Apache Kafka with Amazon MSK
<a name="cruise-control"></a>

You can use LinkedIn's Cruise Control to rebalance your Amazon MSK cluster, detect and fix anomalies, and monitor the state and health of the cluster.

**Note**  
If [intelligent rebalancing](intelligent-rebalancing.md) is turned on for your newly created Express-based clusters, you won’t be able to use third-party tools, such as Cruise Control, for partition rebalancing. You must first pause intelligent rebalancing to use the partition reassignment API provided by these third-party tools.

**To download and build Cruise Control**

1. Create an Amazon EC2 instance in the same Amazon VPC as the Amazon MSK cluster.

1. Install Prometheus on the Amazon EC2 instance that you created in the previous step. Note the private IP and the port. The default port number is 9090. For information on how to configure Prometheus to aggregate metrics for your cluster, see [Monitor an MSK Provisioned cluster with Prometheus](open-monitoring.md).

1. Download [Cruise Control](https://github.com/linkedin/cruise-control/releases) on the Amazon EC2 instance. (Alternatively, you can use a separate Amazon EC2 instance for Cruise Control if you prefer.) For a cluster that has Apache Kafka version 2.4.\*, use the latest 2.4.\* Cruise Control release. If your cluster has an Apache Kafka version that is older than 2.4.\*, use the latest 2.0.\* Cruise Control release.

1. Decompress the Cruise Control file, then go to the decompressed folder.

1. Run the following command to install git.

   ```
   sudo yum -y install git
   ```

1. Run the following command to initialize the local repo. Replace {{Your-Cruise-Control-Folder}} with the name of your current folder (the folder that you obtained when you decompressed the Cruise Control download).

   ```
   git init && git add . && git commit -m "Init local repo." && git tag -a {{Your-Cruise-Control-Folder}} -m "Init local version."
   ```

1. Run the following command to build the source code.

   ```
   ./gradlew jar copyDependantLibs
   ```

**To configure and run Cruise Control**

1. Make the following updates to the `config/cruisecontrol.properties` file. Replace the example bootstrap servers and bootstrap-brokers string with the values for your cluster. To get these strings for your cluster, you can see the cluster details in the console. Alternatively, you can use the [GetBootstrapBrokers](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html#GetBootstrapBrokers) and [DescribeCluster](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API operations or their CLI equivalents.

   ```
   # If using TLS encryption, use 9094; use 9092 if using plaintext
   bootstrap.servers=b-1.test-cluster.2skv42.c1.kafka.us-east-1.amazonaws.com:9094,b-2.test-cluster.2skv42.c1.kafka.us-east-1.amazonaws.com:9094,b-3.test-cluster.2skv42.c1.kafka.us-east-1.amazonaws.com:9094
       
   # SSL properties, needed if cluster is using TLS encryption
   security.protocol=SSL
   ssl.truststore.location=/home/ec2-user/kafka.client.truststore.jks
       
   # Use the Prometheus Metric Sampler
   metric.sampler.class=com.linkedin.kafka.cruisecontrol.monitor.sampling.prometheus.PrometheusMetricSampler
       
   # Prometheus Metric Sampler specific configuration
   prometheus.server.endpoint=1.2.3.4:9090 # Replace with your Prometheus IP and port
       
   # Change the capacity config file and specify its path; details below
   capacity.config.file=config/capacityCores.json
   ```

   For express brokers, we recommend that you do not use the `DiskCapacityGoal` in any of the goals configured in your [analyzer configurations](https://github.com/linkedin/cruise-control/wiki/Configurations#analyzer-configurations).

1. Edit the `config/capacityCores.json` file to specify the right disk size and CPU cores and network in/out limits. For Express brokers, the `DISK` capacity entry is only needed for setting up Cruise Control. Since MSK manages all the storage for Express brokers, you should set this value to an extremely high number, such as `Integer.MAX_VALUE (2147483647)`. For Standard brokers, you can use the [DescribeCluster](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn.html#DescribeCluster) API operation (or [describe-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html) CLI) to obtain the disk size. For CPU cores and network in/out limits, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/).

------
#### [ Standard broker config/capacityCores.json ]

   ```
   {
     "brokerCapacities": [
       {
         "brokerId": "-1",
         "capacity": {
           "DISK": "10000",
           "CPU": {
             "num.cores": "2"
           },
           "NW_IN": "5000000",
           "NW_OUT": "5000000"
         },
         "doc": "This is the default capacity. Capacity unit used for disk is in MB, cpu is in number of cores, network throughput is in KB."
       }
     ]
   }
   ```

------
#### [ Express broker config/capacityCores.json ]

   ```
   {
     "brokerCapacities":[
       {
         "brokerId": "-1",
         "capacity": {
           "DISK": "2147483647",
           "CPU": {"num.cores": "16"},
           "NW_IN": "1073741824",
           "NW_OUT": "1073741824"
         },
         "doc": "This is the default capacity. Capacity unit used for disk is in MB, cpu is in number of cores, network throughput is in KB."
       }
     ]
   }
   ```

------

1. You can optionally install the Cruise Control UI. To download it, go to [Setting Up Cruise Control Frontend](https://github.com/linkedin/cruise-control-ui/wiki/Single-Kafka-Cluster#setting-up-cruise-control-frontend).

1. Run the following command to start Cruise Control. Consider using a tool like `screen` or `tmux` to keep a long-running session open.

   ```
   {{<path-to-your-CRUISE-CONTROL-installation>}}/bin/kafka-cruise-control-start.sh config/cruisecontrol.properties 9091
   ```

1. Use the Cruise Control APIs or the UI to make sure that Cruise Control has the cluster load data and that it's making rebalancing suggestions. It might take several minutes to get a valid window of metrics.
**Important**  
Only Cruise Control versions 2.5.60 and above are compatible with Express brokers as Express brokers do not expose Zookeeper endpoints.

## Use automated deployment template of Cruise Control for Amazon MSK
<a name="cruise-control-cfn-template"></a>

You can also use this [CloudFormation template](https://github.com/aws-samples/cruise-control-for-msk), to easily deploy Cruise Control and Prometheus to gain deeper insights into your Amazon MSK cluster's performance and optimize resource utilization.

**Key features:**
+ Automated provisioning of an Amazon EC2 instance with Cruise Control and Prometheus pre-configured.
+ Support for Amazon MSK provisioned cluster.
+ Flexible authentication with [PlainText and IAM](kafka_apis_iam.md).
+ No Zookeeper dependency for Cruise Control.
+ Easily customize Prometheus targets, Cruise Control capacity settings, and other configurations by providing your own configuration files stored in an Amazon S3 bucket.

## Partition rebalancing guideline
<a name="cruise-control-partition-rebalancing"></a>

### Guidelines for Kafka partition reassignment
<a name="cruise-control-partition-reassignment"></a>

Partition reassignment in Kafka can be resource-intensive, as it involves transferring significant data across brokers, potentially causing network congestion and affecting client operations. The following best practices help you manage partition reassignment effectively by tuning throttle rates, leveraging concurrency controls, and understanding reassignment types to minimize disruption to cluster operations.

**Note**  
If you have a newly created Express-based cluster, use [intelligent rebalancing](intelligent-rebalancing.md) for automatic partition distribution as you scale your clusters up or down.

#### Managing concurrency in Cruise Control
<a name="cruise-control-managing-concurrency"></a>

Cruise Control provides auto-adjustment parameters to control the concurrency of partition and leadership movements. The following parameters help maintain an acceptable load during reassignments:
+ **Maximum concurrent partition movements**: Define the `num.concurrent.partition.movements.per.broker` to cap concurrent inter-broker partition movements, avoiding excessive network utilization.  
**Example**  

  ```
  num.concurrent.partition.movements.per.broker = 5
  ```

  This setting limits each broker to move no more than 10 partitions at any given time, balancing the load across brokers.

#### Use throttling to control bandwidth
<a name="cruise-control-control-bandwidth"></a>
+ **Throttle Parameter**: When performing partition reassignment with `kafka-reassign-partitions.sh`, use the `--throttle parameter` to set a maximum transfer rate (in bytes per second) for data movement between brokers.  
**Example**  

  ```
  --throttle 5000000
  ```

  This sets a maximum bandwidth of 5 MB/s.
+ **Balance Throttle Settings**: Choosing an appropriate throttle rate is crucial:

  If set too low, the reassignment may take significantly longer.

  If set too high, clients may experience latency increases.
+ Start with a conservative throttle rate and adjust based on cluster performance monitoring. Test your chosen throttle before applying to a production environment to find the optimal balance.

#### Test and validate in a staging environment
<a name="cruise-control-partition-rebalancing-test"></a>

Prior to implementing reassignments in production, perform load tests in a staging environment with similar configurations. This allows you to fine-tune parameters and minimize unexpected impacts in live production.