---
id: "@specs/aws/kafka/docs/msk-configuration-operations-describe-revision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Get configuration revision details"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Get configuration revision details

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-describe-revision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Get details about configuration revision
<a name="msk-configuration-operations-describe-revision"></a>

This process gets you a detailed description of the Amazon MSK configuration revision.

If you use the `describe-configuration` command to describe an MSK configuration, you see the metadata of the configuration. To get a description of the configuration, use the command, `describe-configuration-revision`.
+ Run the following command and replace {{configuration-arn}} with the ARN that you obtained when you created the configuration. If you didn't save the ARN when you created the configuration, you can use the `list-configurations` command to list all configuration in your account. The configuration that you want in the list that appears in the response. The ARN of the configuration also appears in that list.

  ```
  aws kafka describe-configuration-revision --arn {{configuration-arn}} --revision 1
  ```

  The following is an example of a successful response after you run this command.

  ```
  {
      "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-abcd-1234-abcd-abcd123e8e8e-1",
      "CreationTime": "2019-05-21T00:54:23.591Z",
      "Description": "Example configuration description.",
      "Revision": 1,
      "ServerProperties": "YXV0by5jcmVhdGUudG9waWNzLmVuYWJsZSA9IHRydWUKCgp6b29rZWVwZXIuY29ubmVjdGlvbi50aW1lb3V0Lm1zID0gMTAwMAoKCmxvZy5yb2xsLm1zID0gNjA0ODAwMDAw"
  }
  ```

  The value of `ServerProperties` is encoded with base64. If you use a base64 decoder (for example, https://www.base64decode.org/) to decode it manually, you get the contents of the original configuration file that you used to create the custom configuration. In this case, you get the following:

  ```
  auto.create.topics.enable = true
  
  log.roll.ms = 604800000
  ```