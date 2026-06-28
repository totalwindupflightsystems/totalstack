---
id: "@specs/aws/storagegateway/docs/API_CacheReportFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CacheReportFilter"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CacheReportFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CacheReportFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CacheReportFilter
<a name="API_CacheReportFilter"></a>

A list of filter parameters and associated values that determine which files are included or excluded from a cache report created by a `StartCacheReport` request. Multiple instances of the same filter parameter are combined with an OR operation, while different parameters are combined with an AND operation.

## Contents
<a name="API_CacheReportFilter_Contents"></a>

 ** Name **   <a name="StorageGateway-Type-CacheReportFilter-Name"></a>
The parameter name for a filter that determines which files are included or excluded from a cache report.  
 **Valid Names:**   
UploadFailureReason \| UploadState  
Type: String  
Valid Values: `UploadState | UploadFailureReason`   
Required: Yes

 ** Values **   <a name="StorageGateway-Type-CacheReportFilter-Values"></a>
The parameter value for a filter that determines which files are included or excluded from a cache report.  
 **Valid `UploadFailureReason` Values:**   
 `InaccessibleStorageClass` \| `InvalidObjectState` \| `ObjectMissing` \| `S3AccessDenied`   
 **Valid `UploadState` Values:**   
 `FailingUpload`   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: Yes

## See Also
<a name="API_CacheReportFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CacheReportFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CacheReportFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CacheReportFilter) 