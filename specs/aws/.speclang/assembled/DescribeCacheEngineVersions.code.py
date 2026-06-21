// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/DescribeCacheEngineVersions.spec.py.md#input-shape-describecacheengineversionsmessage
// spec:generated DO NOT EDIT — edit the spec instead

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