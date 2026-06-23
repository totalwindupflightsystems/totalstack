---
id: "@specs/aws/comprehend/docs/API_DetectDominantLanguage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetectDominantLanguage"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DetectDominantLanguage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DetectDominantLanguage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetectDominantLanguage
<a name="API_DetectDominantLanguage"></a>

Determines the dominant language of the input text. For a list of languages that Amazon Comprehend can detect, see [Amazon Comprehend Supported Languages](https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html). 

## Request Syntax
<a name="API_DetectDominantLanguage_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectDominantLanguage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_DetectDominantLanguage_RequestSyntax) **   <a name="comprehend-DetectDominantLanguage-request-Text"></a>
A UTF-8 text string. The string must contain at least 20 characters. The maximum string size is 100 KB.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_DetectDominantLanguage_ResponseSyntax"></a>

```
{
   "Languages": [ 
      { 
         "LanguageCode": "string",
         "Score": number
      }
   ]
}
```

## Response Elements
<a name="API_DetectDominantLanguage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Languages](#API_DetectDominantLanguage_ResponseSyntax) **   <a name="comprehend-DetectDominantLanguage-response-Languages"></a>
Array of languages that Amazon Comprehend detected in the input text. The array is sorted in descending order of the score (the dominant language is always the first element in the array).  
For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see [Tags for Identifying Languages](https://tools.ietf.org/html/rfc5646) on the *IETF Tools* web site.  
Type: Array of [DominantLanguage](API_DominantLanguage.md) objects

## Errors
<a name="API_DetectDominantLanguage_Errors"></a>

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

## Examples
<a name="API_DetectDominantLanguage_Examples"></a>

### Detect dominant language
<a name="API_DetectDominantLanguage_Example_1"></a>

If the input text is "Bob lives in Seattle. He is a software engineer at Amazon.", the operation returns the following:

```
{
    "Languages": [
        {
            "LanguageCode": "en",
            "Score": 0.9774383902549744
        },
        {
            "LanguageCode": "de",
            "Score": 0.010717987082898617
        }
    ]
}
```

## See Also
<a name="API_DetectDominantLanguage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DetectDominantLanguage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DetectDominantLanguage) 