---
id: "@specs/aws/kafka/docs/msk-tiered-storage-retention-rules"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tiered storage scenario"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Tiered storage scenario

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-tiered-storage-retention-rules
> **target_lang:** meta — documentation tier. ALL sections preserved.



# How log segments are copied to tiered storage for a Amazon MSK topic
<a name="msk-tiered-storage-retention-rules"></a>

When you enable tiered storage for a new or existing topic, Apache Kafka copies closed log segments from primary storage to tiered storage.
+ Apache Kafka only copies closed log segments. It copies all messages within the log segment to tiered storage.
+ Active segments are not eligible for tiering. The log segment size (segment.bytes) or the segment roll time (segment.ms) controls the rate of segment closure, and the rate Apache Kafka then copies them to tiered storage.

Retention settings for a topic with tiered storage enabled are different from settings for a topic without tiered storage enabled. The following rules control the retention of messages in topics with tiered storage enabled:
+ You define retention in Apache Kafka with two settings: log.retention.ms (time) and log.retention.bytes (size). These settings determine the total duration and size of the data that Apache Kafka retains in the cluster. Whether or not you enable tiered storage mode, you set these configurations at the cluster level. You can override the settings at the topic level with topic configurations.
+ When you enable tiered storage, you can additionally specify how long the primary high-performance storage tier stores data. For example, if a topic has overall retention (log.retention.ms) setting of 7 days and local retention (local.retention.ms) of 12 hours, then the cluster primary storage retains data for only the first 12 hours. The low-cost storage tier retains the data for the full 7 days.
+ The usual retention settings apply to the full log. This includes its tiered and primary parts.
+ The local.retention.ms or local.retention.bytes settings control the retention of messages in primary storage. Apache Kafka copies closed log segments to tiered storage as soon as they close (based on segment.bytes or segment.ms), independent of local retention settings. After segments are copied to tiered storage, they remain in primary storage until the local.retention.ms or local.retention.bytes thresholds are reached. At that point, the data is deleted from primary storage but remains available in tiered storage. This allows you to keep recent data on high-performance primary storage for fast access while older data is served from the low-cost tiered storage.
+ When Apache Kafka copies a message in a log segment to tiered storage, it removes the message from the cluster based on retention.ms or retention.bytes settings.

## Example Amazon MSK tiered storage scenario
<a name="msk-tiered-storage-retention-scenario"></a>

This scenario illustrates how an existing topic that has messages in primary storage behaves when tiered storage is enabled. You enable tiered storage on this topic by when you set remote.storage.enable to `true`. In this example, retention.ms is set to 5 days and local.retention.ms is set to 2 days. The following is the sequence of events when a segment expires.

**Time T0 - Before you enable tiered storage.**  
Before you enable tiered storage for this topic, there are two log segments. One of the segments is active for an existing topic partition 0.

![Time T0 - Before you enable tiered storage.](http://docs.aws.amazon.com/msk/latest/developerguide/images/tiered-storage-segments-1.png)


**Time T1 (< 2 days) - Tiered storage enabled. Segment 0 copied to tiered storage.**  
After you enable tiered storage for this topic, Apache Kafka copies closed log segment 0 to tiered storage as soon as it closes. The segment closes based on segment.bytes or segment.ms settings, not based on retention settings. Apache Kafka retains a copy in primary storage as well. The active segment 1 is not eligible to copy to tiered storage yet because it is still active and hasn't closed. In this timeline, Amazon MSK doesn't apply any of the retention settings yet for any of the messages in segment 0 and segment 1. (local.retention.bytes/ms, retention.ms/bytes)

![Time T1 (< 2 days) - Tiered storage enabled. Segment 0 copied to tiered storage.](http://docs.aws.amazon.com/msk/latest/developerguide/images/tiered-storage-segments-2.png)


**Time T2 - Local retention in effect.**  
After 2 days, the local retention threshold is reached for segment 0. The setting of local.retention.ms as 2 days determines this. Segment 0 is now deleted from primary storage, but it remains available in tiered storage. Note that segment 0 was already copied to tiered storage at Time T1 when it closed, not at Time T2 when local retention expired. Active segment 1 is neither eligible for deletion nor eligible to copy to tiered storage yet because it is still active.

![Time T2 - Local retention in effect.](http://docs.aws.amazon.com/msk/latest/developerguide/images/tiered-storage-segments-3.png)


**Time T3 - Overall retention in effect.**  
 After 5 days, retention settings take effect, and Kafka clears log segment 0 and associated messages from tiered storage. Segment 1 is neither eligible for expiration nor eligible to copy over to tiered storage yet because it is active. Segment 1 is not yet closed, so it is ineligible for segment roll.

![Time T3 - Overall retention in effect.](http://docs.aws.amazon.com/msk/latest/developerguide/images/tiered-storage-segments-4.png)
