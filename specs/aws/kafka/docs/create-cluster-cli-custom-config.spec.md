---
id: "@specs/aws/kafka/docs/create-cluster-cli-custom-config"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/create-cluster-cli-custom-config
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI
<a name="create-cluster-cli-custom-config"></a>

****

For information about custom Amazon MSK configurations and how to create them, see [Amazon MSK Provisioned configuration](msk-configuration.md).

1. Save the following JSON to a file, replacing {{configuration-arn}} with the ARN of the configuration that you want to use to create the cluster.

   ```
   {
       "Arn": {{configuration-arn}},
       "Revision": 1
   }
   ```

1. Run the `create-cluster` command and use the `configuration-info` option to point to the JSON file you saved in the previous step. The following is an example.

   ```
   aws kafka create-cluster --cluster-name ExampleClusterName --broker-node-group-info file://brokernodegroupinfo.json --kafka-version "2.8.1" --number-of-broker-nodes 3 --enhanced-monitoring PER_TOPIC_PER_BROKER --configuration-info file://configuration.json
   ```

   The following is an example of a successful response after running this command.

   ```
   {
       "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/CustomConfigExampleCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2",
       "ClusterName": "CustomConfigExampleCluster",
       "State": "CREATING"
   }
   ```