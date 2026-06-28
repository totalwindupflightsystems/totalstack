---
id: "@specs/aws/storagegateway/docs/API_CacheAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheAttributes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CacheAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CacheAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheAttributes
<a name="API_CacheAttributes"></a>

The refresh cache information for the file share or FSx file systems.

## Contents
<a name="API_CacheAttributes_Contents"></a>

 ** CacheStaleTimeoutInSeconds **   <a name="StorageGateway-Type-CacheAttributes-CacheStaleTimeoutInSeconds"></a>
Refreshes a file share's cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directory's contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.  
Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)  
Type: Integer  
Required: No

## See Also
<a name="API_CacheAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CacheAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CacheAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CacheAttributes) 