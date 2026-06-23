---
id: "@specs/aws/comprehend/docs/API_DetectKeyPhrases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetectKeyPhrases"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DetectKeyPhrases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DetectKeyPhrases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetectKeyPhrases
<a name="API_DetectKeyPhrases"></a>

Detects the key noun phrases found in the text. 

## Request Syntax
<a name="API_DetectKeyPhrases_RequestSyntax"></a>

```
{
   "LanguageCode": "{{string}}",
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectKeyPhrases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LanguageCode](#API_DetectKeyPhrases_RequestSyntax) **   <a name="comprehend-DetectKeyPhrases-request-LanguageCode"></a>
The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** [Text](#API_DetectKeyPhrases_RequestSyntax) **   <a name="comprehend-DetectKeyPhrases-request-Text"></a>
A UTF-8 text string. The string must contain less than 100 KB of UTF-8 encoded characters.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_DetectKeyPhrases_ResponseSyntax"></a>

```
{
   "KeyPhrases": [ 
      { 
         "BeginOffset": number,
         "EndOffset": number,
         "Score": number,
         "Text": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DetectKeyPhrases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyPhrases](#API_DetectKeyPhrases_ResponseSyntax) **   <a name="comprehend-DetectKeyPhrases-response-KeyPhrases"></a>
A collection of key phrases that Amazon Comprehend identified in the input text. For each key phrase, the response provides the text of the key phrase, where the key phrase begins and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection.   
Type: Array of [KeyPhrase](API_KeyPhrase.md) objects

## Errors
<a name="API_DetectKeyPhrases_Errors"></a>

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

## Examples
<a name="API_DetectKeyPhrases_Examples"></a>

### Detect phrases
<a name="API_DetectKeyPhrases_Example_1"></a>

If the input text is "Bob lives in Seattle. He is a software engineer at Amazon.", the API returns the following:

```
          {
    "KeyPhrases": [
        {
            "Text": "Bob",
            "Score": 1.0,
            "BeginOffset": 0,
            "EndOffset": 3
        },
        {
            "Text": "Seattle",
            "Score": 1.0,
            "BeginOffset": 13,
            "EndOffset": 20
        },
        {
            "Text": "a software engineer",
            "Score": 1.0,
            "BeginOffset": 28,
            "EndOffset": 39
        },
        {
            "Text": "Amazon",
            "Score": 1.0,
            "BeginOffset": 43,
            "EndOffset": 49
        }
    ]
}}
```

## See Also
<a name="API_DetectKeyPhrases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DetectKeyPhrases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DetectKeyPhrases) 