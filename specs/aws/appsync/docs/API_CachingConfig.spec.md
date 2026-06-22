---
id: "@specs/aws/appsync/docs/API_CachingConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CachingConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CachingConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CachingConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CachingConfig
<a name="API_CachingConfig"></a>

The caching configuration for a resolver that has caching activated.

## Contents
<a name="API_CachingConfig_Contents"></a>

 ** ttl **   <a name="appsync-Type-CachingConfig-ttl"></a>
The TTL in seconds for a resolver that has caching activated.  
Valid values are 1–3,600 seconds.  
Type: Long  
Required: Yes

 ** cachingKeys **   <a name="appsync-Type-CachingConfig-cachingKeys"></a>
The caching keys for a resolver that has caching activated.  
Valid values are entries from the `$context.arguments`, `$context.source`, and `$context.identity` maps.  
Type: Array of strings  
Required: No

## See Also
<a name="API_CachingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CachingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CachingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CachingConfig) 