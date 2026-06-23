---
id: "@specs/aws/comprehend/docs/API_DetectTargetedSentiment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetectTargetedSentiment"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DetectTargetedSentiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DetectTargetedSentiment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetectTargetedSentiment
<a name="API_DetectTargetedSentiment"></a>

Inspects the input text and returns a sentiment analysis for each entity identified in the text.

For more information about targeted sentiment, see [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_DetectTargetedSentiment_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectTargetedSentiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_DetectTargetedSentiment_RequestSyntax) **   <a name="comprehend-DetectTargetedSentiment-request-LanguageCode"></a>
The language of the input documents. Currently, English is the only supported language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** [Text](#API_DetectTargetedSentiment_RequestSyntax) **   <a name="comprehend-DetectTargetedSentiment-request-Text"></a>
A UTF-8 text string. The maximum string length is 5 KB.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_DetectTargetedSentiment_ResponseSyntax"></a>

```
{
   "Entities": [ 
      { 
         "DescriptiveMentionIndex": [ number ],
         "Mentions": [ 
            { 
               "BeginOffset": number,
               "EndOffset": number,
               "GroupScore": number,
               "MentionSentiment": { 
                  "Sentiment": "string",
                  "SentimentScore": { 
                     "Mixed": number,
                     "Negative": number,
                     "Neutral": number,
                     "Positive": number
                  }
               },
               "Score": number,
               "Text": "string",
               "Type": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DetectTargetedSentiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_DetectTargetedSentiment_ResponseSyntax) **   <a name="comprehend-DetectTargetedSentiment-response-Entities"></a>
Targeted sentiment analysis for each of the entities identified in the input text.  
Type: Array of [TargetedSentimentEntity](API_TargetedSentimentEntity.md) objects

## Errors
<a name="API_DetectTargetedSentiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** TextSizeLimitExceededException **   
The size of the input text exceeds the limit. Use a smaller document.  
HTTP Status Code: 400

 ** UnsupportedLanguageException **   
Amazon Comprehend can't process the language of the input text. For a list of supported languages, [Supported languages](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html) in the Comprehend Developer Guide.   
HTTP Status Code: 400

## See Also
<a name="API_DetectTargetedSentiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DetectTargetedSentiment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DetectTargetedSentiment) 