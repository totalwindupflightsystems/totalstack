
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
