---
id: "@specs/aws/comprehend/docs/API_BatchDetectTargetedSentimentItemResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDetectTargetedSentimentItemResult"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# BatchDetectTargetedSentimentItemResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_BatchDetectTargetedSentimentItemResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDetectTargetedSentimentItemResult
<a name="API_BatchDetectTargetedSentimentItemResult"></a>

Analysis results for one of the documents in the batch.

## Contents
<a name="API_BatchDetectTargetedSentimentItemResult_Contents"></a>

 ** Entities **   <a name="comprehend-Type-BatchDetectTargetedSentimentItemResult-Entities"></a>
An array of targeted sentiment entities.  
Type: Array of [TargetedSentimentEntity](API_TargetedSentimentEntity.md) objects  
Required: No

 ** Index **   <a name="comprehend-Type-BatchDetectTargetedSentimentItemResult-Index"></a>
The zero-based index of this result in the input list.  
Type: Integer  
Required: No

## See Also
<a name="API_BatchDetectTargetedSentimentItemResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchDetectTargetedSentimentItemResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchDetectTargetedSentimentItemResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchDetectTargetedSentimentItemResult) 