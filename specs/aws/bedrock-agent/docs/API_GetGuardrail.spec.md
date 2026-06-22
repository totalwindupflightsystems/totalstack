---
id: "@specs/aws/bedrock-agent/docs/API_GetGuardrail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetGuardrail"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetGuardrail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetGuardrail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetGuardrail
<a name="API_GetGuardrail"></a>

Gets details about a guardrail. If you don't specify a version, the response returns details for the `DRAFT` version.

## Request Syntax
<a name="API_GetGuardrail_RequestSyntax"></a>

```
GET /guardrails/{{guardrailIdentifier}}?guardrailVersion={{guardrailVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGuardrail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [guardrailIdentifier](#API_GetGuardrail_RequestSyntax) **   <a name="bedrock-GetGuardrail-request-uri-guardrailIdentifier"></a>
The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: Yes

 ** [guardrailVersion](#API_GetGuardrail_RequestSyntax) **   <a name="bedrock-GetGuardrail-request-uri-guardrailVersion"></a>
The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the `DRAFT` version.  
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))` 

## Request Body
<a name="API_GetGuardrail_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGuardrail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "automatedReasoningPolicy": { 
      "confidenceThreshold": number,
      "policies": [ "string" ]
   },
   "blockedInputMessaging": "string",
   "blockedOutputsMessaging": "string",
   "contentPolicy": { 
      "filters": [ 
         { 
            "inputAction": "string",
            "inputEnabled": boolean,
            "inputModalities": [ "string" ],
            "inputStrength": "string",
            "outputAction": "string",
            "outputEnabled": boolean,
            "outputModalities": [ "string" ],
            "outputStrength": "string",
            "type": "string"
         }
      ],
      "tier": { 
         "tierName": "string"
      }
   },
   "contextualGroundingPolicy": { 
      "filters": [ 
         { 
            "action": "string",
            "enabled": boolean,
            "threshold": number,
            "type": "string"
         }
      ]
   },
   "createdAt": "string",
   "crossRegionDetails": { 
      "guardrailProfileArn": "string",
      "guardrailProfileId": "string"
   },
   "description": "string",
   "failureRecommendations": [ "string" ],
   "guardrailArn": "string",
   "guardrailId": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "sensitiveInformationPolicy": { 
      "piiEntities": [ 
         { 
            "action": "string",
            "inputAction": "string",
            "inputEnabled": boolean,
            "outputAction": "string",
            "outputEnabled": boolean,
            "type": "string"
         }
      ],
      "regexes": [ 
         { 
            "action": "string",
            "description": "string",
            "inputAction": "string",
            "inputEnabled": boolean,
            "name": "string",
            "outputAction": "string",
            "outputEnabled": boolean,
            "pattern": "string"
         }
      ]
   },
   "status": "string",
   "statusReasons": [ "string" ],
   "topicPolicy": { 
      "tier": { 
         "tierName": "string"
      },
      "topics": [ 
         { 
            "definition": "string",
            "examples": [ "string" ],
            "inputAction": "string",
            "inputEnabled": boolean,
            "name": "string",
            "outputAction": "string",
            "outputEnabled": boolean,
            "type": "string"
         }
      ]
   },
   "updatedAt": "string",
   "version": "string",
   "wordPolicy": { 
      "managedWordLists": [ 
         { 
            "inputAction": "string",
            "inputEnabled": boolean,
            "outputAction": "string",
            "outputEnabled": boolean,
            "type": "string"
         }
      ],
      "words": [ 
         { 
            "inputAction": "string",
            "inputEnabled": boolean,
            "outputAction": "string",
            "outputEnabled": boolean,
            "text": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetGuardrail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [automatedReasoningPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-automatedReasoningPolicy"></a>
The current Automated Reasoning policy configuration for the guardrail, if any is configured.  
Type: [GuardrailAutomatedReasoningPolicy](API_GuardrailAutomatedReasoningPolicy.md) object

 ** [blockedInputMessaging](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-blockedInputMessaging"></a>
The message that the guardrail returns when it blocks a prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [blockedOutputsMessaging](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-blockedOutputsMessaging"></a>
The message that the guardrail returns when it blocks a model response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [contentPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-contentPolicy"></a>
The content policy that was configured for the guardrail.  
Type: [GuardrailContentPolicy](API_GuardrailContentPolicy.md) object

 ** [contextualGroundingPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-contextualGroundingPolicy"></a>
The contextual grounding policy used in the guardrail.  
Type: [GuardrailContextualGroundingPolicy](API_GuardrailContextualGroundingPolicy.md) object

 ** [createdAt](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-createdAt"></a>
The date and time at which the guardrail was created.  
Type: Timestamp

 ** [crossRegionDetails](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-crossRegionDetails"></a>
Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).  
Type: [GuardrailCrossRegionDetails](API_GuardrailCrossRegionDetails.md) object

 ** [description](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-description"></a>
The description of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [failureRecommendations](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-failureRecommendations"></a>
Appears if the `status` of the guardrail is `FAILED`. A list of recommendations to carry out before retrying the request.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [guardrailArn](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-guardrailArn"></a>
The ARN of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+` 

 ** [guardrailId](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-guardrailId"></a>
The unique identifier of the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 64.  
Pattern: `[a-z0-9]+` 

 ** [kmsKeyArn](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-kmsKeyArn"></a>
The ARN of the AWS KMS key that encrypts the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-name"></a>
The name of the guardrail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[0-9a-zA-Z-_]+` 

 ** [sensitiveInformationPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-sensitiveInformationPolicy"></a>
The sensitive information policy that was configured for the guardrail.  
Type: [GuardrailSensitiveInformationPolicy](API_GuardrailSensitiveInformationPolicy.md) object

 ** [status](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-status"></a>
The status of the guardrail.  
Type: String  
Valid Values: `CREATING | UPDATING | VERSIONING | READY | FAILED | DELETING` 

 ** [statusReasons](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-statusReasons"></a>
Appears if the `status` is `FAILED`. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [topicPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-topicPolicy"></a>
The topic policy that was configured for the guardrail.  
Type: [GuardrailTopicPolicy](API_GuardrailTopicPolicy.md) object

 ** [updatedAt](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-updatedAt"></a>
The date and time at which the guardrail was updated.  
Type: Timestamp

 ** [version](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-version"></a>
The version of the guardrail.  
Type: String  
Pattern: `(([1-9][0-9]{0,7})|(DRAFT))` 

 ** [wordPolicy](#API_GetGuardrail_ResponseSyntax) **   <a name="bedrock-GetGuardrail-response-wordPolicy"></a>
The word policy that was configured for the guardrail.  
Type: [GuardrailWordPolicy](API_GuardrailWordPolicy.md) object

## Errors
<a name="API_GetGuardrail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_GetGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetGuardrail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetGuardrail) 