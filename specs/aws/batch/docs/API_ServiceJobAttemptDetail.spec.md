---
id: "@specs/aws/batch/docs/API_ServiceJobAttemptDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceJobAttemptDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceJobAttemptDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceJobAttemptDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceJobAttemptDetail
<a name="API_ServiceJobAttemptDetail"></a>

Detailed information about an attempt to run a service job.

## Contents
<a name="API_ServiceJobAttemptDetail_Contents"></a>

 ** serviceResourceId **   <a name="Batch-Type-ServiceJobAttemptDetail-serviceResourceId"></a>
The service resource identifier associated with the service job attempt.  
Type: [ServiceResourceId](API_ServiceResourceId.md) object  
Required: No

 ** startedAt **   <a name="Batch-Type-ServiceJobAttemptDetail-startedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt was started.  
Type: Long  
Required: No

 ** statusReason **   <a name="Batch-Type-ServiceJobAttemptDetail-statusReason"></a>
A string that provides additional details for the current status of the service job attempt.  
Type: String  
Required: No

 ** stoppedAt **   <a name="Batch-Type-ServiceJobAttemptDetail-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the service job attempt stopped running.  
Type: Long  
Required: No

## See Also
<a name="API_ServiceJobAttemptDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobAttemptDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobAttemptDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobAttemptDetail) 