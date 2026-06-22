---
id: "@specs/aws/bedrock/docs/API_UpdateGuardrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateGuardrail"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateGuardrail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateGuardrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateGuardrail
<a name="API_UpdateGuardrail"></a>

Updates a guardrail with the values you specify.
+ Specify a `name` and optional `description`.
+ Specify messages for when the guardrail successfully blocks a prompt or a model response in the `blockedInputMessaging` and `blockedOutputsMessaging` fields.
+ Specify topics for the guardrail to deny in the `topicPolicyConfig` object. Each [GuardrailTopicConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html) object in the `topicsConfig` list pertains to one topic.
  + Give a `name` and `description` so that the guardrail can properly identify the topic.
  + Specify `DENY` in the `type` field.
  + (Optional) Provide up to five prompts that you would categorize as belonging to the topic in the `examples` list.
+ Specify filter strengths for the harmful categories defined in Amazon Bedrock in the `contentPolicyConfig` object. Each [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html) object in the `filtersConfig` list pertains to a harmful category. For more information, see [Content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters). For more information about the fields in a content filter, see [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html).
  + Specify the category in the `type` field.
  + Specify the strength of the filter for prompts in the `inputStrength` field and for model responses in the `strength` field of the [GuardrailContentFilterConfig](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html).
+ (Optional) For security, include the ARN of a AWS KMS key in the `kmsKeyId` field.

## Request Syntax
<a name="API_UpdateGuardrail_RequestSyntax"></a>

```
PUT /guardrails/{{guardrailIdentifier}} HTTP/1.1
Content-type: application/json

{
   "automatedReasoningPolicyConfig": { 
      "confidenceThreshold": {{number}},
      "policies": [ "{{string}}" ]
   },
   "blockedInputMessaging": "{{string}}",
   "blockedOutputsMessaging": "{{string}}",
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
<a name="API_UpdateGuardrail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [guardrailIdentifier](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-uri-guardrailIdentifier"></a>
The unique identifier of the guardrail. This can be an ID or the ARN.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

## Request Body
<a name="API_UpdateGuardrail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [automatedReasoningPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-automatedReasoningPolicyConfig"></a>
Updated configuration for Automated Reasoning policies associated with the guardrail.  
Type: [GuardrailAutomatedReasoningPolicyConfig](API_GuardrailAutomatedReasoningPolicyConfig.md) object  
Required: No

 ** [blockedInputMessaging](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-blockedInputMessaging"></a>
The message to return when the guardrail blocks a prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** [blockedOutputsMessaging](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-blockedOutputsMessaging"></a>
The message to return when the guardrail blocks a model response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: Yes

 ** [contentPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-contentPolicyConfig"></a>
The content policy to configure for the guardrail.  
Type: [GuardrailContentPolicyConfig](API_GuardrailContentPolicyConfig.md) object  
Required: No

 ** [contextualGroundingPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-contextualGroundingPolicyConfig"></a>
The contextual grounding policy configuration used to update a guardrail.  
Type: [GuardrailContextualGroundingPolicyConfig](API_GuardrailContextualGroundingPolicyConfig.md) object  
Required: No

 ** [crossRegionConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-crossRegionConfig"></a>
The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination AWS Regions where guardrail inference requests can be automatically routed.  
For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).  
Type: [GuardrailCrossRegionConfig](API_GuardrailCrossRegionConfig.md) object  
Required: No

 ** [description](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-description"></a>
A description of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [kmsKeyId](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-kmsKeyId"></a>
The ARN of the AWS KMS key with which to encrypt the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [name](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-name"></a>
A name for the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[0-9a-zA-Z-_]+`   
Required: Yes

 ** [sensitiveInformationPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-sensitiveInformationPolicyConfig"></a>
The sensitive information policy to configure for the guardrail.  
Type: [GuardrailSensitiveInformationPolicyConfig](API_GuardrailSensitiveInformationPolicyConfig.md) object  
Required: No

 ** [topicPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-topicPolicyConfig"></a>
The topic policy to configure for the guardrail.  
Type: [GuardrailTopicPolicyConfig](API_GuardrailTopicPolicyConfig.md) object  
Required: No

 ** [wordPolicyConfig](#API_UpdateGuardrail_RequestSyntax) **   <a name="bedrock-UpdateGuardrail-request-wordPolicyConfig"></a>
The word policy to configure for the guardrail.  
Type: [GuardrailWordPolicyConfig](API_GuardrailWordPolicyConfig.md) object  
Required: No

## Response Syntax
<a name="API_UpdateGuardrail_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "guardrailArn": "string",
   "guardrailId": "string",
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_UpdateGuardrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [guardrailArn](#API_UpdateGuardrail_ResponseSyntax) **   <a name="bedrock-UpdateGuardrail-response-guardrailArn"></a>
The ARN of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+` 

 ** [guardrailId](#API_UpdateGuardrail_ResponseSyntax) **   <a name="bedrock-UpdateGuardrail-response-guardrailId"></a>
The unique identifier of the guardrail  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+` 

 ** [updatedAt](#API_UpdateGuardrail_ResponseSyntax) **   <a name="bedrock-UpdateGuardrail-response-updatedAt"></a>
The date and time at which the guardrail was updated.  
Type: Timestamp

 ** [version](#API_UpdateGuardrail_ResponseSyntax) **   <a name="bedrock-UpdateGuardrail-response-version"></a>
The version of the guardrail.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT` 

## Errors
<a name="API_UpdateGuardrail_Errors"></a>

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

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateGuardrail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateGuardrail) 