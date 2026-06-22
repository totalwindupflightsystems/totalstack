---
id: "@specs/aws/opensearchserverless/docs/sm-pause-snapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Pausing automated snapshots"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Pausing automated snapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/sm-pause-snapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Pausing automated snapshots
<a name="sm-pause-snapshots"></a>

OpenSearch Service lets you temporarily pause automated snapshots on your domain. This is useful when you need to perform data migrations, run maintenance operations, or avoid snapshot overhead during peak traffic periods.

You configure the pause using `AutomatedSnapshotPauseOptions` in your domain configuration. The options include an `enabled` flag, a `StartTime`, and an `EndTime`. Times are Unix epoch timestamps in seconds, and the maximum duration of a single pause cannot exceed 72 hours. The `EndTime` cannot be set more than 90 days in the future.

If you omit `StartTime`, OpenSearch Service begins the pause immediately. If a pause is currently active and you omit `StartTime`, the existing start time is preserved.

A pause window has the following states:
+ `DISABLED` — No pause is configured.
+ `SCHEDULED` — A pause is configured with a start time in the future.
+ `ACTIVE` — A pause is currently in effect.
+ `COMPLETED` — The pause window has elapsed.

**Important**  
While automated snapshots are paused, your domain has reduced data protection. You cannot restore to any point in time during the pause window. Use this feature only for short-term operational needs.

To pause automated snapshots, include the following parameters when you update your domain configuration:

```
POST https://es.{{us-east-1}}.amazonaws.com/2021-01-01/opensearch/domain/{{my-domain}}/config
{
  "AutomatedSnapshotPauseOptions": {
    "Enabled": true,
    "StartTime": 1737100800,
    "EndTime": 1737360000
  }
}
```

`StartTime` is optional. If you omit it, the pause begins immediately. `EndTime` is required when `Enabled` is `true` and specifies when OpenSearch Service resumes taking automated snapshots.

To cancel a pause before it ends, set `Enabled` to `false` with no `StartTime` or `EndTime`. Providing start or end times when disabling is not allowed and results in a validation error.

After a pause completes, the new pause's `StartTime` must be at least 1 hour after the previous pause's `EndTime`. This ensures that OpenSearch Service takes at least one snapshot between consecutive pause windows.

While a pause is `ACTIVE`, you can update only the `EndTime` to shorten or extend the window. The `StartTime` cannot be modified once a pause is in progress. The total duration of the updated window must still not exceed 72 hours.

When snapshots are paused, the OpenSearch Service console displays a warning banner on the domain details page indicating the pause end time and reduced data protection status.