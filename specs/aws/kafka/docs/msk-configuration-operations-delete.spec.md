---
id: "@specs/aws/kafka/docs/msk-configuration-operations-delete"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Delete configuration"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Delete configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-delete
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Delete configuration
<a name="msk-configuration-operations-delete"></a>

The following procedure shows how to delete a configuration that isn't attached to a cluster. You can't delete a configuration that's attached to a cluster.

1. To run this example, replace {{configuration-arn}} with the ARN that you obtained when you created the configuration. If you didn't save the ARN when you created the configuration, you can use the `list-configurations` command to list all configuration in your account. The configuration that you want in the list appears in the response. The ARN of the configuration also appears in that list.

   ```
   aws kafka delete-configuration --arn {{configuration-arn}}
   ```

1. The following is an example of a successful response after you run this command.

   ```
   {
       "arn": " arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-1234-abcd-1234-abcd123e8e8e-1",
       "state": "DELETING"
   }
   ```