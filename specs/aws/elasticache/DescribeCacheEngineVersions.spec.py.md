---
id: "@specs/aws/elasticache/DescribeCacheEngineVersions"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeCacheEngineVersions

Returns a list of the available cache engines and their versions.

## Input Shape: DescribeCacheEngineVersionsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| Engine | String |  |
| EngineVersion | String |  |
| CacheParameterGroupFamily | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |
| DefaultOnly | Boolean |  |

## Output Shape: CacheEngineVersionMessage
- Marker: String
- CacheEngineVersions: CacheEngineVersionList

## Errors
none

## Implementation

```speclang
def describe_cache_engine_versions(store, request):
    """Handle DescribeCacheEngineVersions — describe resources."""
    # Return static list of supported engine versions
    return {
        "CacheEngineVersions": [
            {"Engine": "redis", "EngineVersion": "7.0.7"},
            {"Engine": "redis", "EngineVersion": "6.2.6"},
            {"Engine": "memcached", "EngineVersion": "1.6.12"},
            {"Engine": "valkey", "EngineVersion": "7.2.0"},
        ]
    }
```
