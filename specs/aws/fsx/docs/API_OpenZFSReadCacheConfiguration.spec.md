---
id: "@specs/aws/fsx/docs/API_OpenZFSReadCacheConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSReadCacheConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSReadCacheConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSReadCacheConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSReadCacheConfiguration
<a name="API_OpenZFSReadCacheConfiguration"></a>

 The configuration for the optional provisioned SSD read cache on Amazon FSx for OpenZFS file systems that use the Intelligent-Tiering storage class. 

## Contents
<a name="API_OpenZFSReadCacheConfiguration_Contents"></a>

 ** SizeGiB **   <a name="FSx-Type-OpenZFSReadCacheConfiguration-SizeGiB"></a>
 Required if `SizingMode` is set to `USER_PROVISIONED`. Specifies the size of the file system's SSD read cache, in gibibytes (GiB).   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** SizingMode **   <a name="FSx-Type-OpenZFSReadCacheConfiguration-SizingMode"></a>
 Specifies how the provisioned SSD read cache is sized, as follows:   
+ Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
+ Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
+ Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.
Type: String  
Valid Values: `NO_CACHE | USER_PROVISIONED | PROPORTIONAL_TO_THROUGHPUT_CAPACITY`   
Required: No

## See Also
<a name="API_OpenZFSReadCacheConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSReadCacheConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSReadCacheConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSReadCacheConfiguration) 