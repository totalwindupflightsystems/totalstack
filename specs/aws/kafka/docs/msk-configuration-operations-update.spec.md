---
id: "@specs/aws/kafka/docs/msk-configuration-operations-update"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Update configuration"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Update configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-update
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Update configuration
<a name="msk-configuration-operations-update"></a>

This process describes how to update a custom Amazon MSK configuration.

1. Create a file where you specify the configuration properties that you want to update and the values that you want to assign to them. The following are the contents of an example configuration file.

   ```
   auto.create.topics.enable = true
   
   min.insync.replicas = 2
   ```

1. Run the following AWS CLI command, and replace {{config-file-path}} with the path to the file where you saved your configuration in the previous step.

   Replace {{configuration-arn}} with the ARN that you obtained when you created the configuration. If you didn't save the ARN when you created the configuration, you can use the `list-configurations` command to list all configuration in your account. The configuration that you want in the list appears in the response. The ARN of the configuration also appears in that list.

   ```
   aws kafka update-configuration --arn {{configuration-arn}} --description "Example configuration revision description." --server-properties {{fileb://config-file-path}}
   ```

1. The following is an example of a successful response after you run this command.

   ```
   {
       "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-1234-abcd-1234-abcd123e8e8e-1",
       "LatestRevision": {
           "CreationTime": "2020-08-27T19:37:40.626Z",
           "Description": "Example configuration revision description.",
           "Revision": 2
       }
   }
   ```