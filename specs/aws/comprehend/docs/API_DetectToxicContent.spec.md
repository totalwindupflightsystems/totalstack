---
id: "@specs/aws/comprehend/docs/API_DetectToxicContent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetectToxicContent"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DetectToxicContent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DetectToxicContent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetectToxicContent
<a name="API_DetectToxicContent"></a>

**Important**  
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html). 

Performs toxicity analysis on the list of text strings that you provide as input. The API response contains a results list that matches the size of the input list. For more information about toxicity detection, see [Toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/toxicity-detection.html) in the *Amazon Comprehend Developer Guide*. 

## Request Syntax
<a name="API_DetectToxicContent_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "TextSegments": [ 
      { 
         "Text": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DetectToxicContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_DetectToxicContent_RequestSyntax) **   <a name="comprehend-DetectToxicContent-request-LanguageCode"></a>
The language of the input text. Currently, English is the only supported language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** [TextSegments](#API_DetectToxicContent_RequestSyntax) **   <a name="comprehend-DetectToxicContent-request-TextSegments"></a>
A list of up to 10 text strings. Each string has a maximum size of 1 KB, and the maximum size of the list is 10 KB.  
Type: Array of [TextSegment](API_TextSegment.md) objects  
Array Members: Minimum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_DetectToxicContent_ResponseSyntax"></a>

```
{
   "ResultList": [ 
      { 
         "Labels": [ 
            { 
               "Name": "string",
               "Score": number
            }
         ],
         "Toxicity": number
      }
   ]
}
```

## Response Elements
<a name="API_DetectToxicContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResultList](#API_DetectToxicContent_ResponseSyntax) **   <a name="comprehend-DetectToxicContent-response-ResultList"></a>
Results of the content moderation analysis. Each entry in the results list contains a list of toxic content types identified in the text, along with a confidence score for each content type. The results list also includes a toxicity score for each entry in the results list.   
Type: Array of [ToxicLabels](API_ToxicLabels.md) objects

## Errors
<a name="API_DetectToxicContent_Errors"></a>

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
<a name="API_DetectToxicContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DetectToxicContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DetectToxicContent) 