---
id: "@specs/aws/comprehend/docs/API_DetectEntities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetectEntities"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DetectEntities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DetectEntities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetectEntities
<a name="API_DetectEntities"></a>

Detects named entities in input text when you use the pre-trained model. Detects custom entities if you have a custom entity recognition model. 

 When detecting named entities using the pre-trained model, use plain text as the input. For more information about named entities, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html) in the Comprehend Developer Guide.

When you use a custom entity recognition model, you can input plain text or you can upload a single-page input document (text, PDF, Word, or image). 

If the system detects errors while processing a page in the input document, the API response includes an entry in `Errors` for each error. 

If the system detects a document-level error in your input document, the API returns an `InvalidRequestException` error response. For details about this exception, see [ Errors in semi-structured documents](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html) in the Comprehend Developer Guide. 

## Request Syntax
<a name="API_DetectEntities_RequestSyntax"></a>

```
{
   "Bytes": {{blob}},
   "DocumentReaderConfig": { 
      "DocumentReadAction": "{{string}}",
      "DocumentReadMode": "{{string}}",
      "FeatureTypes": [ "{{string}}" ]
   },
   "EndpointArn": "{{string}}",
   "LanguageCode": "{{string}}",
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectEntities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Bytes](#API_DetectEntities_RequestSyntax) **   <a name="comprehend-DetectEntities-request-Bytes"></a>
This field applies only when you use a custom entity recognition model that was trained with PDF annotations. For other cases, enter your text input in the `Text` field.  
 Use the `Bytes` parameter to input a text, PDF, Word or image file. Using a plain-text file in the `Bytes` parameter is equivelent to using the `Text` parameter (the `Entities` field in the response is identical).  
You can also use the `Bytes` parameter to input an Amazon Textract `DetectDocumentText` or `AnalyzeDocument` output file.  
Provide the input document as a sequence of base64-encoded bytes. If your code uses an AWS SDK to detect entities, the SDK may encode the document file bytes for you.   
The maximum length of this field depends on the input document type. For details, see [ Inputs for real-time custom analysis](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html) in the Comprehend Developer Guide.   
If you use the `Bytes` parameter, do not use the `Text` parameter.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1.  
Required: No

 ** [DocumentReaderConfig](#API_DetectEntities_RequestSyntax) **   <a name="comprehend-DetectEntities-request-DocumentReaderConfig"></a>
Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.  
Type: [DocumentReaderConfig](API_DocumentReaderConfig.md) object  
Required: No

 ** [EndpointArn](#API_DetectEntities_RequestSyntax) **   <a name="comprehend-DetectEntities-request-EndpointArn"></a>
The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model. Provide an endpoint if you want to detect entities by using your own custom model instead of the default model that is used by Amazon Comprehend.  
If you specify an endpoint, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you provide in your request.  
For information about endpoints, see [Managing endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html).  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer-endpoint/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** [LanguageCode](#API_DetectEntities_RequestSyntax) **   <a name="comprehend-DetectEntities-request-LanguageCode"></a>
The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. If your request includes the endpoint for a custom entity recognition model, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you specify here.  
All input documents must be in the same language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: No

 ** [Text](#API_DetectEntities_RequestSyntax) **   <a name="comprehend-DetectEntities-request-Text"></a>
A UTF-8 text string. The maximum string size is 100 KB. If you enter text using this parameter, do not use the `Bytes` parameter.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_DetectEntities_ResponseSyntax"></a>

```
{
   "Blocks": [ 
      { 
         "BlockType": "string",
         "Geometry": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Polygon": [ 
               { 
                  "X": number,
                  "Y": number
               }
            ]
         },
         "Id": "string",
         "Page": number,
         "Relationships": [ 
            { 
               "Ids": [ "string" ],
               "Type": "string"
            }
         ],
         "Text": "string"
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
   "Entities": [ 
      { 
         "BeginOffset": number,
         "BlockReferences": [ 
            { 
               "BeginOffset": number,
               "BlockId": "string",
               "ChildBlocks": [ 
                  { 
                     "BeginOffset": number,
                     "ChildBlockId": "string",
                     "EndOffset": number
                  }
               ],
               "EndOffset": number
            }
         ],
         "EndOffset": number,
         "Score": number,
         "Text": "string",
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
   ]
}
```

## Response Elements
<a name="API_DetectEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blocks](#API_DetectEntities_ResponseSyntax) **   <a name="comprehend-DetectEntities-response-Blocks"></a>
Information about each block of text in the input document. Blocks are nested. A page block contains a block for each line of text, which contains a block for each word.   
The `Block` content for a Word input document does not include a `Geometry` field.  
The `Block` field is not present in the response for plain-text inputs.  
Type: Array of [Block](API_Block.md) objects

 ** [DocumentMetadata](#API_DetectEntities_ResponseSyntax) **   <a name="comprehend-DetectEntities-response-DocumentMetadata"></a>
Information about the document, discovered during text extraction. This field is present in the response only if your request used the `Byte` parameter.   
Type: [DocumentMetadata](API_DocumentMetadata.md) object

 ** [DocumentType](#API_DetectEntities_ResponseSyntax) **   <a name="comprehend-DetectEntities-response-DocumentType"></a>
The document type for each page in the input document. This field is present in the response only if your request used the `Byte` parameter.   
Type: Array of [DocumentTypeListItem](API_DocumentTypeListItem.md) objects

 ** [Entities](#API_DetectEntities_ResponseSyntax) **   <a name="comprehend-DetectEntities-response-Entities"></a>
A collection of entities identified in the input text. For each entity, the response provides the entity text, entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection.   
If your request uses a custom entity recognition model, Amazon Comprehend detects the entities that the model is trained to recognize. Otherwise, it detects the default entity types. For a list of default entity types, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html) in the Comprehend Developer Guide.   
Type: Array of [Entity](API_Entity.md) objects

 ** [Errors](#API_DetectEntities_ResponseSyntax) **   <a name="comprehend-DetectEntities-response-Errors"></a>
Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.  
Type: Array of [ErrorsListItem](API_ErrorsListItem.md) objects

## Errors
<a name="API_DetectEntities_Errors"></a>

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

 ** UnsupportedLanguageException **   
Amazon Comprehend can't process the language of the input text. For a list of supported languages, [Supported languages](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html) in the Comprehend Developer Guide.   
HTTP Status Code: 400

## Examples
<a name="API_DetectEntities_Examples"></a>

### Detect entities
<a name="API_DetectEntities_Example_1"></a>

If the input text is "Bob ordered two sandwiches and three ice cream cones today from a store in Seattle.", the operation returns the following:

```
    {
    "Entities": [
        {
            "Text": "Bob",
            "Score": 1.0,
            "Type": "PERSON",
            "BeginOffset": 0,
            "EndOffset": 3
        },
        {
            "Text": "two",
            "Score": 1.0,
            "Type": "QUANTITY",
            "BeginOffset": 12,
            "EndOffset": 15
        },
        {
            "Text": "three",
            "Score": 1.0,
            "Type": "QUANTITY",
            "BeginOffset": 32,
            "EndOffset": 37
        },
        {
            "Text": "Today",
            "Score": 1.0,
            "Type": "DATE",
            "BeginOffset": 54,
            "EndOffset": 59
        },
        {
            "Text": "Seattle",
            "Score": 1.0,
            "Type": "LOCATION",
            "BeginOffset": 76,
            "EndOffset": 83
        }
    ],
}
```

## See Also
<a name="API_DetectEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DetectEntities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DetectEntities) 