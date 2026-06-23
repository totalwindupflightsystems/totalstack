---
id: "@specs/aws/comprehend/docs/API_BatchDetectSentimentItemResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDetectSentimentItemResult"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# BatchDetectSentimentItemResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_BatchDetectSentimentItemResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDetectSentimentItemResult
<a name="API_BatchDetectSentimentItemResult"></a>

The result of calling the [BatchDetectSentiment](API_BatchDetectSentiment.md) operation. The operation returns one object for each document that is successfully processed by the operation.

## Contents
<a name="API_BatchDetectSentimentItemResult_Contents"></a>

 ** Index **   <a name="comprehend-Type-BatchDetectSentimentItemResult-Index"></a>
The zero-based index of the document in the input list.  
Type: Integer  
Required: No

 ** Sentiment **   <a name="comprehend-Type-BatchDetectSentimentItemResult-Sentiment"></a>
The sentiment detected in the document.  
Type: String  
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL | MIXED`   
Required: No

 ** SentimentScore **   <a name="comprehend-Type-BatchDetectSentimentItemResult-SentimentScore"></a>
The level of confidence that Amazon Comprehend has in the accuracy of its sentiment detection.  
Type: [SentimentScore](API_SentimentScore.md) object  
Required: No

## See Also
<a name="API_BatchDetectSentimentItemResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchDetectSentimentItemResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchDetectSentimentItemResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchDetectSentimentItemResult) 