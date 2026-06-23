---
id: "@specs/aws/amplify/docs/API_CacheConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheConfig"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CacheConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CacheConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheConfig
<a name="API_CacheConfig"></a>

Describes the cache configuration for an Amplify app.

For more information about how Amplify applies an optimal cache configuration for your app based on the type of content that is being served, see [Managing cache configuration](https://docs.aws.amazon.com/amplify/latest/userguide/managing-cache-configuration) in the *Amplify User guide*.

## Contents
<a name="API_CacheConfig_Contents"></a>

 ** type **   <a name="amplify-Type-CacheConfig-type"></a>
The type of cache configuration to use for an Amplify app.  
The `AMPLIFY_MANAGED` cache configuration automatically applies an optimized cache configuration for your app based on its platform, routing rules, and rewrite rules.  
The `AMPLIFY_MANAGED_NO_COOKIES` cache configuration type is the same as `AMPLIFY_MANAGED`, except that it excludes all cookies from the cache key. This is the default setting.  
Type: String  
Valid Values: `AMPLIFY_MANAGED | AMPLIFY_MANAGED_NO_COOKIES`   
Required: Yes

## See Also
<a name="API_CacheConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CacheConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CacheConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CacheConfig) 