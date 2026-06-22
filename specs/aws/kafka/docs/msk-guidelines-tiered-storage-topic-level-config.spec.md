---
id: "@specs/aws/kafka/docs/msk-guidelines-tiered-storage-topic-level-config"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Guidelines for tiered storage topic-level configurations"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Guidelines for tiered storage topic-level configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-guidelines-tiered-storage-topic-level-config
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Guidelines for Amazon MSK tiered storage topic-level configuration
<a name="msk-guidelines-tiered-storage-topic-level-config"></a>

The following are default settings and limitations when you configure tiered storage at the topic level.
+ Amazon MSK doesn't support smaller log segment sizes for topics with tiered storage activated. If you want to create a segment, there is a minimum log segment size of 48 MiB, or a minimum segment roll time of 10 minutes. These values map to the segment.bytes and segment.ms properties.
+ The value of local.retention.ms/bytes can't equal or exceed the retention.ms/bytes. This is the tiered storage retention setting.
+ The default value for for local.retention.ms/bytes is -2. This means that the retention.ms value is used for local.retention.ms/bytes. In this case, data remains in both local storage and tiered storage (one copy in each), and they expire together. For this option, a copy of the local data is persisted to the remote storage. In this case, the data read from consume traffic comes from the local storage.
+ The default value for retention.ms is 7 days. There is no default size limit for retention.bytes.
+ The minimum value for retention.ms/bytes is -1. This means infinite retention.
+ The minimum value for local.retention.ms/bytes is -2. This means infinite retention for local storage. It matches with the retention.ms/bytes setting as -1.
+ The topic-level configuration retention.ms is mandatory for topics with tiered storage activated. The minimum retention.ms is 3 days.

For more information about tiered storage contraints, see [Tiered storage constraints and limitations for Amazon MSK clusters](msk-tiered-storage.md#msk-tiered-storage-constraints).