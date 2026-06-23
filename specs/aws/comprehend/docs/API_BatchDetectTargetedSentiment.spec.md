---
id: "@specs/aws/comprehend/docs/API_BatchDetectTargetedSentiment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDetectTargetedSentiment"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# BatchDetectTargetedSentiment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_BatchDetectTargetedSentiment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDetectTargetedSentiment
<a name="API_BatchDetectTargetedSentiment"></a>

Inspects a batch of documents and returns a sentiment analysis for each entity identified in the documents.

For more information about targeted sentiment, see [Targeted sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_BatchDetectTargetedSentiment_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "TextList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDetectTargetedSentiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_BatchDetectTargetedSentiment_RequestSyntax) **   <a name="comprehend-BatchDetectTargetedSentiment-request-LanguageCode"></a>
The language of the input documents. Currently, English is the only supported language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** [TextList](#API_BatchDetectTargetedSentiment_RequestSyntax) **   <a name="comprehend-BatchDetectTargetedSentiment-request-TextList"></a>
A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_BatchDetectTargetedSentiment_ResponseSyntax"></a>

```
{
   "ErrorList": [ 
      { 
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "Index": number
      }
   ],
   "ResultList": [ 
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
         ],
         "Index": number
      }
   ]
}
```

## Response Elements
<a name="API_BatchDetectTargetedSentiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorList](#API_BatchDetectTargetedSentiment_ResponseSyntax) **   <a name="comprehend-BatchDetectTargetedSentiment-response-ErrorList"></a>
List of errors that the operation can return.  
Type: Array of [BatchItemError](API_BatchItemError.md) objects

 ** [ResultList](#API_BatchDetectTargetedSentiment_ResponseSyntax) **   <a name="comprehend-BatchDetectTargetedSentiment-response-ResultList"></a>
A list of objects containing the results of the operation. The results are sorted in ascending order by the `Index` field and match the order of the documents in the input list. If all of the documents contain an error, the `ResultList` is empty.  
Type: Array of [BatchDetectTargetedSentimentItemResult](API_BatchDetectTargetedSentimentItemResult.md) objects

## Errors
<a name="API_BatchDetectTargetedSentiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchSizeLimitExceededException **   
The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.  
HTTP Status Code: 400

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
<a name="API_BatchDetectTargetedSentiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/BatchDetectTargetedSentiment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/BatchDetectTargetedSentiment) 