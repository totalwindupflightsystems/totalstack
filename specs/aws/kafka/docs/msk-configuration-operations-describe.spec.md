---
id: "@specs/aws/kafka/docs/msk-configuration-operations-describe"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get configuration metadata"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Get configuration metadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-describe
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Get configuration metadata
<a name="msk-configuration-operations-describe"></a>

The following procedure shows how to describe an Amazon MSK configuration to get metadata about the configuration.

1. The following command returns metadata about the configuration. To get a detailed description of the configuration, run the `describe-configuration-revision`.

   To run this example, replace {{configuration-arn}} with the ARN that you obtained when you created the configuration. If you didn't save the ARN when you created the configuration, you can use the `list-configurations` command to list all configuration in your account. The configuration that you want in the list appears in the response. The ARN of the configuration also appears in that list.

   ```
   aws kafka describe-configuration --arn {{configuration-arn}}
   ```

1. The following is an example of a successful response after you run this command.

   ```
   {
       "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-abcd-1234-abcd-abcd123e8e8e-1",
       "CreationTime": "2019-05-21T00:54:23.591Z",
       "Description": "Example configuration description.",
       "KafkaVersions": [
           "1.1.1"
       ],
       "LatestRevision": {
           "CreationTime": "2019-05-21T00:54:23.591Z",
           "Description": "Example configuration description.",
           "Revision": 1
       },
       "Name": "SomeTest"
   }
   ```