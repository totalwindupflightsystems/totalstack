---
id: "@specs/aws/elasticache/DescribeEvents"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeEvents

Returns events related to clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cluster, cache security group, or cache parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.

## Input Shape: DescribeEventsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| SourceIdentifier | String |  |
| SourceType | SourceType |  |
| StartTime | TStamp |  |
| EndTime | TStamp |  |
| Duration | IntegerOptional |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: EventsMessage
- Marker: String
- Events: EventList

## Errors
InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def describe_events(store, request):
    """Handle DescribeEvents — describe resources."""
    items = list(store.events)
    return {Events: items}
```
