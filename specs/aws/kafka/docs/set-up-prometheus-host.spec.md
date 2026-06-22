---
id: "@specs/aws/kafka/docs/set-up-prometheus-host"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Set up a Prometheus host"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Set up a Prometheus host

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/set-up-prometheus-host
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Set up a Prometheus host on an Amazon EC2 instance
<a name="set-up-prometheus-host"></a>

This procedure describes how to set up a Prometheus host using a prometheus.yml file.

1. Download the Prometheus server from [https://prometheus.io/download/#prometheus](https://prometheus.io/download/#prometheus) to your Amazon EC2 instance.

1. Extract the downloaded file to a directory and go to that directory.

1. Create a file with the following contents and name it `prometheus.yml`.

   ```
   # file: prometheus.yml
   # my global config
   global:
     scrape_interval:     60s
   
   # A scrape configuration containing exactly one endpoint to scrape:
   # Here it's Prometheus itself.
   scrape_configs:
     # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
     - job_name: 'prometheus'
       static_configs:
       # 9090 is the prometheus server port
       - targets: ['localhost:9090']
     - job_name: 'broker'
       file_sd_configs:
       - files:
         - 'targets.json'
   ```

1. Use the [ListNodes](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-nodes.html#ListNodes) operation to get a list of your cluster's brokers.

1. Create a file named `targets.json` with the following JSON. Replace {{broker\_dns\_1}}, {{broker\_dns\_2}}, and the rest of the broker DNS names with the DNS names you obtained for your brokers in the previous step. Include all of the brokers you obtained in the previous step. Amazon MSK uses port 11001 for the JMX Exporter and port 11002 for the Node Exporter.

------
#### [ ZooKeeper mode targets.json ]

   ```
   [
     {
       "labels": {
         "job": "jmx"
       },
       "targets": [
         "{{broker_dns_1}}:11001",
         "{{broker_dns_2}}:11001",
         .
         .
         .
         "{{broker_dns_N}}:11001"
       ]
     },
     {
       "labels": {
         "job": "node"
       },
       "targets": [
         "{{broker_dns_1}}:11002",
         "{{broker_dns_2}}:11002",
         .
         .
         .
         "{{broker_dns_N}}:11002"
       ]
     }
   ]
   ```

------
#### [ KRaft mode targets.json ]

   ```
   [
     {
       "labels": {
         "job": "jmx"
       },
       "targets": [
         "{{broker_dns_1}}:11001",
         "{{broker_dns_2}}:11001",
         .
         .
         .
         "{{broker_dns_N}}:11001",
         "{{controller_dns_1}}:11001",
         "{{controller_dns_2}}:11001",
         "{{controller_dns_3}}:11001"
       ]
     },
     {
       "labels": {
         "job": "node"
       },
       "targets": [
         "{{broker_dns_1}}:11002",
         "{{broker_dns_2}}:11002",
         .
         .
         .
         "{{broker_dns_N}}:11002"
       ]
     }
   ]
   ```

------
**Note**  
To scrape JMX metrics from KRaft controllers, add controller DNS names as targets in the JSON file. For example: `controller_dns_1:11001`, replacing `controller_dns_1` with the actual controller DNS name.

1. To start the Prometheus server on your Amazon EC2 instance, run the following command in the directory where you extracted the Prometheus files and saved `prometheus.yml` and `targets.json`.

   ```
   ./prometheus
   ```

1. Find the IPv4 public IP address of the Amazon EC2 instance where you ran Prometheus in the previous step. You need this public IP address in the following step.

1. To access the Prometheus web UI, open a browser that can access your Amazon EC2 instance, and go to `{{Prometheus-Instance-Public-IP}}:9090`, where {{Prometheus-Instance-Public-IP}} is the public IP address you got in the previous step.