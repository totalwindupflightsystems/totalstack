---
id: "@specs/aws/kafka/docs/msk-connect-debeziumsource-connector-example-steps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create a Debezium source connector"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create a Debezium source connector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-debeziumsource-connector-example-steps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a Debezium source connector
<a name="msk-connect-debeziumsource-connector-example-steps"></a>

This procedure describes how to create a Debezium source connector.

1. 

**Create a custom plugin**

   1. Download the MySQL connector plugin for the latest stable release from the [Debezium](https://debezium.io/releases/) site. Make a note of the Debezium release version you download (version 2.x, or the older series 1.x). Later in this procedure, you'll create a connector based on your Debezium version.

   1. Download and extract the [AWS Secrets Manager Config Provider](https://www.confluent.io/hub/jcustenborder/kafka-config-provider-aws).

   1. Place the following archives into the same directory:
      + The `debezium-connector-mysql` folder
      + The `jcusten-border-kafka-config-provider-aws-0.1.1` folder

   1. Compress the directory that you created in the previous step into a ZIP file and then upload the ZIP file to an S3 bucket. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the *Amazon S3 User Guide.*

   1. Copy the following JSON and paste it in a file. For example, `debezium-source-custom-plugin.json`. Replace {{<example-custom-plugin-name>}} with the name that you want the plugin to have, {{<amzn-s3-demo-bucket-arn>}} with the ARN of the Amazon S3 bucket where you uploaded the ZIP file, and `{{<file-key-of-ZIP-object>}}` with the file key of the ZIP object that you uploaded to S3.

      ```
      {
          "name": "{{<example-custom-plugin-name>}}",
          "contentType": "ZIP",
          "location": {
              "s3Location": {
                  "bucketArn": "{{<amzn-s3-demo-bucket-arn>}}",
                  "fileKey": "{{<file-key-of-ZIP-object>}}"
              }
          }
      }
      ```

   1. Run the following AWS CLI command from the folder where you saved the JSON file to create a plugin.

      ```
      aws kafkaconnect create-custom-plugin --cli-input-json file://{{<debezium-source-custom-plugin.json>}}
      ```

      You should see output similar to the following example.

      ```
      {
          "CustomPluginArn": "arn:aws:kafkaconnect:us-east-1:012345678901:custom-plugin/example-custom-plugin-name/abcd1234-a0b0-1234-c1-12345678abcd-1",
          "CustomPluginState": "CREATING",
          "Name": "example-custom-plugin-name",
          "Revision": 1
      }
      ```

   1. Run the following command to check the plugin state. The state should change from `CREATING` to `ACTIVE`. Replace the ARN placeholder with the ARN that you got in the output of the previous command.

      ```
      aws kafkaconnect describe-custom-plugin --custom-plugin-arn "{{<arn-of-your-custom-plugin>}}"
      ```

1. 

**Configure AWS Secrets Manager and create a secret for your database credentials**

   1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

   1. Create a new secret to store your database sign-in credentials. For instructions, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in the *AWS Secrets Manager* User Guide.

   1. Copy your secret's ARN.

   1. Add the Secrets Manager permissions from the following example policy to your [Understand service execution role](msk-connect-service-execution-role.md). Replace {{<arn:aws:secretsmanager:us-east-1:123456789000:secret:MySecret-1234>}} with the ARN of your secret.

------
#### [ JSON ]

****  

      ```
      {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "secretsmanager:GetResourcePolicy",
              "secretsmanager:GetSecretValue",
              "secretsmanager:DescribeSecret",
              "secretsmanager:ListSecretVersionIds"
            ],
            "Resource": [
            "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{MySecret-1234}}"
            ]
          }
        ]
      }
      ```

------

      For instructions on how to add IAM permissions, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

1. 

**Create a custom worker configuration with information about your configuration provider**

   1. Copy the following worker configuration properties into a file, replacing the placeholder strings with values that correspond to your scenario. To learn more about the configuration properties for the AWS Secrets Manager Config Provider, see [SecretsManagerConfigProvider](https://jcustenborder.github.io/kafka-connect-documentation/projects/kafka-config-provider-aws/configProviders/SecretsManagerConfigProvider.html) in the plugin's documentation.

      ```
      key.converter={{<org.apache.kafka.connect.storage.StringConverter>}}
      value.converter={{<org.apache.kafka.connect.storage.StringConverter>}}
      config.providers.secretManager.class=com.github.jcustenborder.kafka.config.aws.SecretsManagerConfigProvider
      config.providers=secretManager
      config.providers.secretManager.param.aws.region={{<us-east-1>}}
      ```

   1. Run the following AWS CLI command to create your custom worker configuration. 

      Replace the following values:
      + {{<my-worker-config-name>}} - a descriptive name for your custom worker configuration
      + {{<encoded-properties-file-content-string>}} - a base64-encoded version of the plaintext properties that you copied in the previous step

      ```
      aws kafkaconnect create-worker-configuration --name {{<my-worker-config-name>}} --properties-file-content {{<encoded-properties-file-content-string>}}
      ```

1. 

**Create a connector**

   1. Copy the following JSON that corresponds to your Debezium version (2.x or 1.x) and paste it in a new file. Replace the `{{<placeholder>}}` strings with values that correspond to your scenario. For information about how to set up a service execution role, see [IAM roles and policies for MSK Connect](msk-connect-iam.md).

      Note that the configuration uses variables like `${secretManager:MySecret-1234:dbusername}` instead of plaintext to specify database credentials. Replace `{{MySecret-1234}}` with the name of your secret and then include the name of the key that you want to retrieve. You must also replace `{{<arn-of-config-provider-worker-configuration>}}` with the ARN of your custom worker configuration.

------
#### [ Debezium 2.x ]

      For Debezium 2.x versions, copy the following JSON and paste it in a new file. Replace the {{<placeholder>}} strings with values that correspond to your scenario.

      ```
      {
      	"connectorConfiguration": {
      		"connector.class": "io.debezium.connector.mysql.MySqlConnector",
      		"tasks.max": "1",
      		"database.hostname": "{{<aurora-database-writer-instance-endpoint>}}",
      		"database.port": "3306",
      		"database.user": "{{<${secretManager:MySecret-1234:dbusername}>}}",
      		"database.password": "{{<${secretManager:MySecret-1234:dbpassword}>}}",
      		"database.server.id": "123456",
      		"database.include.list": "{{<list-of-databases-hosted-by-specified-server>}}",
      		"topic.prefix": "{{<logical-name-of-database-server>}}",
      		"schema.history.internal.kafka.topic": "{{<kafka-topic-used-by-debezium-to-track-schema-changes>}}",
      		"schema.history.internal.kafka.bootstrap.servers": "{{<cluster-bootstrap-servers-string>}}",
      		"schema.history.internal.consumer.security.protocol": "SASL_SSL",
      		"schema.history.internal.consumer.sasl.mechanism": "AWS_MSK_IAM",
      		"schema.history.internal.consumer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
      		"schema.history.internal.consumer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
      		"schema.history.internal.producer.security.protocol": "SASL_SSL",
      		"schema.history.internal.producer.sasl.mechanism": "AWS_MSK_IAM",
      		"schema.history.internal.producer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
      		"schema.history.internal.producer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
      		"include.schema.changes": "true"
      	},
      	"connectorName": "example-Debezium-source-connector",
      	"kafkaCluster": {
      		"apacheKafkaCluster": {
      			"bootstrapServers": "{{<cluster-bootstrap-servers-string>}}",
      			"vpc": {
      				"subnets": [
      					"{{<cluster-subnet-1>}}",
      					"{{<cluster-subnet-2>}}",
      					"{{<cluster-subnet-3>}}"
      				],
      				"securityGroups": ["{{<id-of-cluster-security-group>}}"]
      			}
      		}
      	},
      	"capacity": {
      		"provisionedCapacity": {
      			"mcuCount": 2,
      			"workerCount": 1
      		}
      	},
      	"kafkaConnectVersion": "2.7.1",
      	"serviceExecutionRoleArn": "{{<arn-of-service-execution-role-that-msk-connect-can-assume>}}",
      	"plugins": [{
      		"customPlugin": {
      			"customPluginArn": "{{<arn-of-msk-connect-plugin-that-contains-connector-code>}}",
      			"revision": 1
      		}
      	}],
      	"kafkaClusterEncryptionInTransit": {
      		"encryptionType": "TLS"
      	},
      	"kafkaClusterClientAuthentication": {
      		"authenticationType": "IAM"
      	},
      	"workerConfiguration": {
      		"workerConfigurationArn": "{{<arn-of-config-provider-worker-configuration>}}",
      		"revision": 1
      	}
      }
      ```

------
#### [ Debezium 1.x ]

      For Debezium 1.x versions, copy the following JSON and paste it in a new file. Replace the {{<placeholder>}} strings with values that correspond to your scenario.

      ```
      {
      	"connectorConfiguration": {
      		"connector.class": "io.debezium.connector.mysql.MySqlConnector",
      		"tasks.max": "1",
      		"database.hostname": "{{<aurora-database-writer-instance-endpoint>}}",
      		"database.port": "3306",
      		"database.user": "{{<${secretManager:MySecret-1234:dbusername}>}}",
      		"database.password": "{{<${secretManager:MySecret-1234:dbpassword}>}}",
      		"database.server.id": "123456",
      		"database.server.name": "{{<logical-name-of-database-server>}}",
      		"database.include.list": "{{<list-of-databases-hosted-by-specified-server>}}",
      		"database.history.kafka.topic": "{{<kafka-topic-used-by-debezium-to-track-schema-changes>}}",
      		"database.history.kafka.bootstrap.servers": "{{<cluster-bootstrap-servers-string>}}",
      		"database.history.consumer.security.protocol": "SASL_SSL",
      		"database.history.consumer.sasl.mechanism": "AWS_MSK_IAM",
      		"database.history.consumer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
      		"database.history.consumer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
      		"database.history.producer.security.protocol": "SASL_SSL",
      		"database.history.producer.sasl.mechanism": "AWS_MSK_IAM",
      		"database.history.producer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
      		"database.history.producer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
      		"include.schema.changes": "true"
      	},
      	"connectorName": "example-Debezium-source-connector",
      	"kafkaCluster": {
      		"apacheKafkaCluster": {
      			"bootstrapServers": "{{<cluster-bootstrap-servers-string>}}",
      			"vpc": {
      				"subnets": [
      					"{{<cluster-subnet-1>}}",
      					"{{<cluster-subnet-2>}}",
      					"{{<cluster-subnet-3>}}"
      				],
      				"securityGroups": ["{{<id-of-cluster-security-group>}}"]
      			}
      		}
      	},
      	"capacity": {
      		"provisionedCapacity": {
      			"mcuCount": 2,
      			"workerCount": 1
      		}
      	},
      	"kafkaConnectVersion": "2.7.1",
      	"serviceExecutionRoleArn": "<arn-of-service-execution-role-that-msk-connect-can-assume>",
      	"plugins": [{
      		"customPlugin": {
      			"customPluginArn": "<arn-of-msk-connect-plugin-that-contains-connector-code>",
      			"revision": 1
      		}
      	}],
      	"kafkaClusterEncryptionInTransit": {
      		"encryptionType": "TLS"
      	},
      	"kafkaClusterClientAuthentication": {
      		"authenticationType": "IAM"
      	},
      	"workerConfiguration": {
      		"workerConfigurationArn": "{{<arn-of-config-provider-worker-configuration>}}",
      		"revision": 1
      	}
      }
      ```

------

   1. Run the following AWS CLI command in the folder where you saved the JSON file in the previous step.

      ```
      aws kafkaconnect create-connector --cli-input-json file://connector-info.json
      ```

      The following is an example of the output that you get when you run the command successfully.

      ```
      {
          "ConnectorArn": "arn:aws:kafkaconnect:us-east-1:123450006789:connector/example-Debezium-source-connector/abc12345-abcd-4444-a8b9-123456f513ed-2", 
          "ConnectorState": "CREATING", 
          "ConnectorName": "example-Debezium-source-connector"
      }
      ```