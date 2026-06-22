---
id: "@specs/aws/kafka/docs/msk-configuration-operations-create"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create configuration"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Create configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-create
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create a configuration
<a name="msk-configuration-operations-create"></a>

This process describes how to create a custom Amazon MSK configuration and how to perform operations on it.

1. Create a file where you specify the configuration properties that you want to set and the values that you want to assign to them. The following are the contents of an example configuration file.

   ```
   auto.create.topics.enable = true
   
   log.roll.ms = 604800000
   ```

1. Run the following AWS CLI command, and replace {{config-file-path}} with the path to the file where you saved your configuration in the previous step.
**Note**  
The name that you choose for your configuration must match the following regex: "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".

   ```
   aws kafka create-configuration --name "ExampleConfigurationName" --description "Example configuration description." --kafka-versions "1.1.1" --server-properties fileb://{{config-file-path}}
   ```

   The following is an example of a successful response after you run this command.

   ```
   {
       "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-1234-abcd-1234-abcd123e8e8e-1",
       "CreationTime": "2019-05-21T19:37:40.626Z",
       "LatestRevision": {
           "CreationTime": "2019-05-21T19:37:40.626Z",
           "Description": "Example configuration description.",
           "Revision": 1
       },
       "Name": "ExampleConfigurationName"
   }
   ```

1. The previous command returns an Amazon Resource Name (ARN) for your new configuration. Save this ARN because you need it to refer to this configuration in other commands. If you lose your configuration ARN, you can list all the configurations in your account to find it again.