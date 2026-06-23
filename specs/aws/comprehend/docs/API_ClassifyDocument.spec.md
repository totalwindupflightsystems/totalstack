---
id: "@specs/aws/comprehend/docs/API_ClassifyDocument"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClassifyDocument"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ClassifyDocument

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ClassifyDocument
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClassifyDocument
<a name="API_ClassifyDocument"></a>

Creates a classification request to analyze a single document in real-time. `ClassifyDocument` supports the following model types:
+ Custom classifier - a custom model that you have created and trained. For input, you can provide plain text, a single-page document (PDF, Word, or image), or Amazon Textract API output. For more information, see [Custom classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html) in the *Amazon Comprehend Developer Guide*.
+ Prompt safety classifier - Amazon Comprehend provides a pre-trained model for classifying input prompts for generative AI applications. For input, you provide English plain text input. For prompt safety classification, the response includes only the `Classes` field. For more information about prompt safety classifiers, see [Prompt safety classification](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification) in the *Amazon Comprehend Developer Guide*.

If the system detects errors while processing a page in the input document, the API response includes an `Errors` field that describes the errors.

If the system detects a document-level error in your input document, the API returns an `InvalidRequestException` error response. For details about this exception, see [ Errors in semi-structured documents](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html) in the Comprehend Developer Guide. 

## Request Syntax
<a name="API_ClassifyDocument_RequestSyntax"></a>

```
{
   "Bytes": {{blob}},
   "DocumentReaderConfig": { 
      "DocumentReadAction": "{{string}}",
      "DocumentReadMode": "{{string}}",
      "FeatureTypes": [ "{{string}}" ]
   },
   "EndpointArn": "{{string}}",
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_ClassifyDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Bytes](#API_ClassifyDocument_RequestSyntax) **   <a name="comprehend-ClassifyDocument-request-Bytes"></a>
Use the `Bytes` parameter to input a text, PDF, Word or image file.  
When you classify a document using a custom model, you can also use the `Bytes` parameter to input an Amazon Textract `DetectDocumentText` or `AnalyzeDocument` output file.  
To classify a document using the prompt safety classifier, use the `Text` parameter for input.  
Provide the input document as a sequence of base64-encoded bytes. If your code uses an AWS SDK to classify documents, the SDK may encode the document file bytes for you.   
The maximum length of this field depends on the input document type. For details, see [ Inputs for real-time custom analysis](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html) in the Comprehend Developer Guide.   
If you use the `Bytes` parameter, do not use the `Text` parameter.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1.  
Required: No

 ** [DocumentReaderConfig](#API_ClassifyDocument_RequestSyntax) **   <a name="comprehend-ClassifyDocument-request-DocumentReaderConfig"></a>
Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.  
Type: [DocumentReaderConfig](API_DocumentReaderConfig.md) object  
Required: No

 ** [EndpointArn](#API_ClassifyDocument_RequestSyntax) **   <a name="comprehend-ClassifyDocument-request-EndpointArn"></a>
The Amazon Resource Number (ARN) of the endpoint.   
For prompt safety classification, Amazon Comprehend provides the endpoint ARN. For more information about prompt safety classifiers, see [Prompt safety classification](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification) in the *Amazon Comprehend Developer Guide*   
For custom classification, you create an endpoint for your custom model. For more information, see [Using Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/using-endpoints.html).  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:([0-9]{12}|aws):document-classifier-endpoint/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

 ** [Text](#API_ClassifyDocument_RequestSyntax) **   <a name="comprehend-ClassifyDocument-request-Text"></a>
The document text to be analyzed. If you enter text using this parameter, do not use the `Bytes` parameter.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ClassifyDocument_ResponseSyntax"></a>

```
{
   "Classes": [ 
      { 
         "Name": "string",
         "Page": number,
         "Score": number
      }
   ],
   "DocumentMetadata": { 
      "ExtractedCharacters": [ 
         { 
            "Count": number,
            "Page": number
         }
      ],
      "Pages": number
   },
   "DocumentType": [ 
      { 
         "Page": number,
         "Type": "string"
      }
   ],
   "Errors": [ 
      { 
         "ErrorCode": "string",
         "ErrorDocumentType": "string",
         "ErrorMessage": "string",
         "Page": number
      }
   ],
   "Labels": [ 
      { 
         "Name": "string",
         "Page": number,
         "Score": number
      }
   ],
   "Warnings": [ 
      { 
         "Page": number,
         "WarnCode": "string",
         "WarnMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ClassifyDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Classes](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-Classes"></a>
The classes used by the document being analyzed. These are used for models trained in multi-class mode. Individual classes are mutually exclusive and each document is expected to have only a single class assigned to it. For example, an animal can be a dog or a cat, but not both at the same time.   
For prompt safety classification, the response includes only two classes (SAFE\_PROMPT and UNSAFE\_PROMPT), along with a confidence score for each class. The value range of the score is zero to one, where one is the highest confidence.  
Type: Array of [DocumentClass](API_DocumentClass.md) objects

 ** [DocumentMetadata](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-DocumentMetadata"></a>
Extraction information about the document. This field is present in the response only if your request includes the `Byte` parameter.   
Type: [DocumentMetadata](API_DocumentMetadata.md) object

 ** [DocumentType](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-DocumentType"></a>
The document type for each page in the input document. This field is present in the response only if your request includes the `Byte` parameter.   
Type: Array of [DocumentTypeListItem](API_DocumentTypeListItem.md) objects

 ** [Errors](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-Errors"></a>
Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.  
Type: Array of [ErrorsListItem](API_ErrorsListItem.md) objects

 ** [Labels](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-Labels"></a>
The labels used in the document being analyzed. These are used for multi-label trained models. Individual labels represent different categories that are related in some manner and are not mutually exclusive. For example, a movie can be just an action movie, or it can be an action movie, a science fiction movie, and a comedy, all at the same time.   
Type: Array of [DocumentLabel](API_DocumentLabel.md) objects

 ** [Warnings](#API_ClassifyDocument_ResponseSyntax) **   <a name="comprehend-ClassifyDocument-response-Warnings"></a>
Warnings detected while processing the input document. The response includes a warning if there is a mismatch between the input document type and the model type associated with the endpoint that you specified. The response can also include warnings for individual pages that have a mismatch.   
The field is empty if the system generated no warnings.  
Type: Array of [WarningsListItem](API_WarningsListItem.md) objects

## Errors
<a name="API_ClassifyDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceUnavailableException **   
The specified resource is not available. Check the resource and try your request again.  
HTTP Status Code: 400

 ** TextSizeLimitExceededException **   
The size of the input text exceeds the limit. Use a smaller document.  
HTTP Status Code: 400

## See Also
<a name="API_ClassifyDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ClassifyDocument) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ClassifyDocument) 