---
id: "@specs/aws/bedrock-agent/docs/API_CreateGuardrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateGuardrail"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateGuardrail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateGuardrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateGuardrail
<a name="API_CreateGuardrail"></a>

Creates a guardrail to detect and filter harmful content in your generative AI application.

Amazon Bedrock Guardrails provides the following safeguards (also known as policies) to detect and filter harmful content:
+  **Content filters** - Detect and filter harmful text or image content in input prompts or model responses. Filtering is done based on detection of certain predefined harmful content categories: Hate, Insults, Sexual, Violence, Misconduct and Prompt Attack. You also can adjust the filter strength for each of these categories.
+  **Denied topics** - Define a set of topics that are undesirable in the context of your application. The filter will help block them if detected in user queries or model responses.
+  **Word filters** - Configure filters to help block undesirable words, phrases, and profanity (exact match). Such words can include offensive terms, competitor names, etc.
+  **Sensitive information filters** - Configure filters to help block or mask sensitive information, such as personally identifiable information (PII), or custom regex in user inputs and model responses. Blocking or masking is done based on probabilistic detection of sensitive information in standard formats in entities such as SSN number, Date of Birth, address, etc. This also allows configuring regular expression based detection of patterns for identifiers.
+  **Contextual grounding check** - Help detect and filter hallucinations in model responses based on grounding in a source and relevance to the user query.

For more information, see [How Amazon Bedrock Guardrails works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html).

## Request Syntax
<a name="API_CreateGuardrail_RequestSyntax"></a>

```
POST /guardrails HTTP/1.1
Content-type: application/json

{
   "automatedReasoningPolicyConfig": { 
      "confidenceThreshold": {{number}},
      "policies": [ "{{string}}" ]
   },
   "blockedInputMessaging": "{{string}}",
   "blockedOutputsMessaging": "{{string}}",
   "clientRequestToken": "{{string}}",
   "contentPolicyConfig": { 
      "filtersConfig": [ 
         { 
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "inputModalities": [ "{{string}}" ],
            "inputStrength": "{{string}}",
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "outputModalities": [ "{{string}}" ],
            "outputStrength": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "tierConfig": { 
         "tierName": "{{string}}"
      }
   },
   "contextualGroundingPolicyConfig": { 
      "filtersConfig": [ 
         { 
            "action": "{{string}}",
            "enabled": {{boolean}},
            "threshold": {{number}},
            "type": "{{string}}"
         }
      ]
   },
   "crossRegionConfig": { 
      "guardrailProfileIdentifier": "{{string}}"
   },
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "sensitiveInformationPolicyConfig": { 
      "piiEntitiesConfig": [ 
         { 
            "action": "{{string}}",
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "type": "{{string}}"
         }
      ],
      "regexesConfig": [ 
         { 
            "action": "{{string}}",
            "description": "{{string}}",
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "name": "{{string}}",
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "pattern": "{{string}}"
         }
      ]
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "topicPolicyConfig": { 
      "tierConfig": { 
         "tierName": "{{string}}"
      },
      "topicsConfig": [ 
         { 
            "definition": "{{string}}",
            "examples": [ "{{string}}" ],
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "name": "{{string}}",
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "type": "{{string}}"
         }
      ]
   },
   "wordPolicyConfig": { 
      "managedWordListsConfig": [ 
         { 
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "type": "{{string}}"
         }
      ],
      "wordsConfig": [ 
         { 
            "inputAction": "{{string}}",
            "inputEnabled": {{boolean}},
            "outputAction": "{{string}}",
            "outputEnabled": {{boolean}},
            "text": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_CreateGuardrail_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGuardrail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [automatedReasoningPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-automatedReasoningPolicyConfig"></a>
Optional configuration for integrating Automated Reasoning policies with the new guardrail.  
Type: [GuardrailAutomatedReasoningPolicyConfig](API_GuardrailAutomatedReasoningPolicyConfig.md) object  
Required: No

 ** [blockedInputMessaging](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-blockedInputMessaging"></a>
The message to return when the guardrail blocks a prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** [blockedOutputsMessaging](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-blockedOutputsMessaging"></a>
The message to return when the guardrail blocks a model response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** [clientRequestToken](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon S3 User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [contentPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-contentPolicyConfig"></a>
The content filter policies to configure for the guardrail.  
Type: [GuardrailContentPolicyConfig](API_GuardrailContentPolicyConfig.md) object  
Required: No

 ** [contextualGroundingPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-contextualGroundingPolicyConfig"></a>
The contextual grounding policy configuration used to create a guardrail.  
Type: [GuardrailContextualGroundingPolicyConfig](API_GuardrailContextualGroundingPolicyConfig.md) object  
Required: No

 ** [crossRegionConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-crossRegionConfig"></a>
The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination AWS Regions where guardrail inference requests can be automatically routed.  
For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).  
Type: [GuardrailCrossRegionConfig](API_GuardrailCrossRegionConfig.md) object  
Required: No

 ** [description](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-description"></a>
A description of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [kmsKeyId](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-kmsKeyId"></a>
The ARN of the AWS KMS key that you use to encrypt the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [name](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-name"></a>
The name to give the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[0-9a-zA-Z-_]+`   
Required: Yes

 ** [sensitiveInformationPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-sensitiveInformationPolicyConfig"></a>
The sensitive information policy to configure for the guardrail.  
Type: [GuardrailSensitiveInformationPolicyConfig](API_GuardrailSensitiveInformationPolicyConfig.md) object  
Required: No

 ** [tags](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-tags"></a>
The tags that you want to attach to the guardrail.   
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [topicPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-topicPolicyConfig"></a>
The topic policies to configure for the guardrail.  
Type: [GuardrailTopicPolicyConfig](API_GuardrailTopicPolicyConfig.md) object  
Required: No

 ** [wordPolicyConfig](#API_CreateGuardrail_RequestSyntax) **   <a name="bedrock-CreateGuardrail-request-wordPolicyConfig"></a>
The word policy you configure for the guardrail.  
Type: [GuardrailWordPolicyConfig](API_GuardrailWordPolicyConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateGuardrail_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "guardrailArn": "string",
   "guardrailId": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateGuardrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateGuardrail_ResponseSyntax) **   <a name="bedrock-CreateGuardrail-response-createdAt"></a>
The time at which the guardrail was created.  
Type: Timestamp

 ** [guardrailArn](#API_CreateGuardrail_ResponseSyntax) **   <a name="bedrock-CreateGuardrail-response-guardrailArn"></a>
The ARN of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+` 

 ** [guardrailId](#API_CreateGuardrail_ResponseSyntax) **   <a name="bedrock-CreateGuardrail-response-guardrailId"></a>
The unique identifier of the guardrail that was created.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+` 

 ** [version](#API_CreateGuardrail_ResponseSyntax) **   <a name="bedrock-CreateGuardrail-response-version"></a>
The version of the guardrail that was created. This value will always be `DRAFT`.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT` 

## Errors
<a name="API_CreateGuardrail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateGuardrail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateGuardrail) 