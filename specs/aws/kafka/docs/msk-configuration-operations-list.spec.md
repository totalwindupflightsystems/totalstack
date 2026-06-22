---
id: "@specs/aws/kafka/docs/msk-configuration-operations-list"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS List configurations"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# List configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-operations-list
> **target_lang:** meta — documentation tier. ALL sections preserved.



# List configurations in your account for the current Region
<a name="msk-configuration-operations-list"></a>

This process describes how to list all Amazon MSK configurations in your account for the current AWS Region.
+ Run the following command.

  ```
  aws kafka list-configurations
  ```

  The following is an example of a successful response after you run this command.

  ```
  {
      "Configurations": [
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
          },
          {
              "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-1234-abcd-1234-abcd123e8e8e-1",
              "CreationTime": "2019-05-03T23:08:29.446Z",
              "Description": "Example configuration description.",
              "KafkaVersions": [
                  "1.1.1"
              ],
              "LatestRevision": {
                  "CreationTime": "2019-05-03T23:08:29.446Z",
                  "Description": "Example configuration description.",
                  "Revision": 1
              },
              "Name": "ExampleConfigurationName"
          }
      ]
  }
  ```