---
id: "@specs/aws/emr/docs/API_ErrorDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ErrorDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ErrorDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ErrorDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ErrorDetail
<a name="API_ErrorDetail"></a>

A tuple that provides information about an error that caused a cluster to terminate.

## Contents
<a name="API_ErrorDetail_Contents"></a>

 ** ErrorCode **   <a name="EMR-Type-ErrorDetail-ErrorCode"></a>
The name or code associated with the error.  
Type: String  
Required: No

 ** ErrorData **   <a name="EMR-Type-ErrorDetail-ErrorData"></a>
A list of key value pairs that provides contextual information about why an error occured.  
Type: Array of string to string maps  
Required: No

 ** ErrorMessage **   <a name="EMR-Type-ErrorDetail-ErrorMessage"></a>
A message that describes the error.  
Type: String  
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ErrorDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ErrorDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ErrorDetail) 